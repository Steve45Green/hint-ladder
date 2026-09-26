#!/usr/bin/env python3
"""Every dated assessment of the student's active units, the clashes between them, and a calendar file.

Reads the study root: CURRICULUM.md (active units and their folders), each unit's MISSION.md
(the assessment table and the resit line) and, when present, .moodle.json (assignment due dates
seen on Moodle). Standard library only.

Usage:
  plan.py [ROOT] [--clash-days 3]             JSON: units, events, clashes, weeks, to confirm
  plan.py [ROOT] --ics plan/calendar.ics      also write an iCalendar file (RFC 5545)
  plan.py --test                              self-test
"""
import argparse
import datetime as dt
import hashlib
import json
import os
import re
import sys
import tempfile

DATE = re.compile(r"\b(\d{4})-(\d{2})-(\d{2})\b")
DATE_HEADERS = ("date", "data", "fecha")
WEIGHT_HEADERS = ("weight", "peso")
RESIT = re.compile(r"^\s*(?:resit(?: exam)?|exame de recurso|época de recurso|epoca de recurso|recurso)\b[^:\n]*:\s*(.+)$", re.I | re.M)


def find_root(start):
    here = os.path.abspath(start)
    while True:
        if os.path.isfile(os.path.join(here, "CURRICULUM.md")):
            return here
        parent = os.path.dirname(here)
        if parent == here:
            return None
        here = parent


def read(path):
    try:
        with open(path, encoding="utf-8") as f:
            return f.read()
    except OSError:
        return ""


def tables(text):
    """Markdown tables as lists of rows (lists of cell strings), header first, separator dropped."""
    out, rows = [], []
    for line in text.splitlines() + [""]:
        if line.strip().startswith("|"):
            cells = [c.strip() for c in line.strip().strip("|").split("|")]
            if not all(re.fullmatch(r":?-{2,}:?", c) for c in cells if c):
                rows.append(cells)
        elif rows:
            out.append(rows)
            rows = []
    return out


def column(header, names):
    for i, cell in enumerate(header):
        if cell.strip().lower() in names:
            return i
    return None


def active_units(root):
    """[(unit name, folder)] for rows whose Status is active and that have a folder."""
    units = []
    for table in tables(read(os.path.join(root, "CURRICULUM.md"))):
        header = [c.lower() for c in table[0]]
        unit, status, folder = (column(header, n) for n in (("unit", "unidade curricular", "cadeira"), ("status", "estado"), ("folder", "pasta")))
        if None in (unit, status, folder):
            continue
        for row in table[1:]:
            if len(row) <= max(unit, status, folder):
                continue
            name, state, path = row[unit], row[status].lower(), row[folder].strip("` /")
            if state.startswith(("active", "ativa", "activa")) and path and path not in ("—", "-"):
                units.append((name, path))
    return units


def parse_date(text):
    m = DATE.search(text)
    if not m:
        return None
    try:
        return dt.date(int(m.group(1)), int(m.group(2)), int(m.group(3)))
    except ValueError:
        return None


def mission_events(unit, folder, text):
    events, unconfirmed = [], []
    for table in tables(text):
        header = [c.lower() for c in table[0]]
        when, weight = column(header, DATE_HEADERS), column(header, WEIGHT_HEADERS)
        if when is None:
            continue
        for row in table[1:]:
            if len(row) <= when or not row[0]:
                continue
            item = {"unit": unit, "folder": folder, "what": row[0],
                    "weight": row[weight] if weight is not None and len(row) > weight else "", "source": "MISSION.md"}
            day = parse_date(row[when])
            if day:
                events.append(dict(item, date=day.isoformat()))
            else:
                unconfirmed.append(dict(item, date=row[when] or "?"))
    for m in RESIT.finditer(text):
        day = parse_date(m.group(1))
        item = {"unit": unit, "folder": folder, "what": "Resit exam", "weight": "", "source": "MISSION.md"}
        if day:
            events.append(dict(item, date=day.isoformat()))
        else:
            unconfirmed.append(dict(item, date=m.group(1).split(". ")[0].strip(" .")))
    return events, unconfirmed


def moodle_events(root, units, known):
    """Assignment due dates from .moodle.json that MISSION.md does not already hold on the same day."""
    try:
        with open(os.path.join(root, ".moodle.json"), encoding="utf-8") as f:
            state = json.load(f)
    except (OSError, ValueError):
        return []
    names = dict((folder, unit) for unit, folder in units)
    events = []
    for course, folder in (state.get("courses") or {}).items():
        folder = folder.strip("/")
        if folder not in names:
            continue
        for what, stamp in ((state.get("seen") or {}).get(course, {}).get("assign") or {}).items():
            if not stamp:
                continue
            day = dt.datetime.fromtimestamp(int(stamp), dt.timezone.utc).date().isoformat()
            if (folder, day) in known:
                continue
            events.append({"unit": names[folder], "folder": folder, "what": what, "weight": "", "source": "Moodle", "date": day})
    return events


def clashes(events, days):
    """Groups of assessments from at least two units whose dates all fall within `days` consecutive days."""
    ordered = sorted(events, key=lambda e: e["date"])
    groups, current = [], []
    for e in ordered:
        day = dt.date.fromisoformat(e["date"])
        if current and (day - dt.date.fromisoformat(current[0]["date"])).days >= days:
            if len({x["folder"] for x in current}) >= 2:
                groups.append(current)
            while current and (day - dt.date.fromisoformat(current[0]["date"])).days >= days:
                current = current[1:]
        current = current + [e]
    if len({x["folder"] for x in current}) >= 2:
        groups.append(current)
    merged = []
    for g in groups:
        if merged and set(map(id, g)) & set(map(id, merged[-1])):
            merged[-1] = merged[-1] + [e for e in g if e not in merged[-1]]
        else:
            merged.append(g)
    return [{"from": g[0]["date"], "to": g[-1]["date"], "events": g} for g in merged]


def weeks(events, today):
    """Monday-to-Sunday weeks from this week to the last event, with the events of each."""
    if not events:
        return []
    start = today - dt.timedelta(days=today.weekday())
    last = max(dt.date.fromisoformat(e["date"]) for e in events)
    out = []
    while start <= last:
        end = start + dt.timedelta(days=6)
        inside = [e for e in events if start.isoformat() <= e["date"] <= end.isoformat()]
        out.append({"monday": start.isoformat(), "sunday": end.isoformat(), "events": inside})
        start += dt.timedelta(days=7)
    return out


def collect(root, clash_days=3, today=None):
    today = today or dt.date.today()
    units = active_units(root)
    events, unconfirmed = [], []
    for unit, folder in units:
        e, u = mission_events(unit, folder, read(os.path.join(root, folder, "MISSION.md")))
        events += e
        unconfirmed += u
    events += moodle_events(root, units, {(e["folder"], e["date"]) for e in events})
    events.sort(key=lambda e: (e["date"], e["unit"]))
    upcoming = [e for e in events if e["date"] >= today.isoformat()]
    return {"root": root, "today": today.isoformat(), "units": [{"unit": u, "folder": f} for u, f in units],
            "events": events, "past": len(events) - len(upcoming), "to_confirm": unconfirmed,
            "clashes": clashes(upcoming, clash_days), "weeks": weeks(upcoming, today)}


# --- iCalendar ---

def ics_text(value):
    return value.replace("\\", "\\\\").replace(";", "\\;").replace(",", "\\,").replace("\n", "\\n")


def fold(line):
    """Fold a content line at 75 octets, without splitting a UTF-8 character (RFC 5545, 3.1)."""
    out, current = [], b""
    for ch in line:
        b = ch.encode("utf-8")
        if len(current) + len(b) > (75 if not out else 74):
            out.append(current.decode("utf-8"))
            current = b""
        current += b
    out.append(current.decode("utf-8"))
    return "\r\n ".join(out)


def ics(events, stamp=None):
    stamp = stamp or dt.datetime.now(dt.timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    lines = ["BEGIN:VCALENDAR", "VERSION:2.0", "PRODID:-//Hint Ladder//plan//EN", "CALSCALE:GREGORIAN"]
    for e in events:
        day = dt.date.fromisoformat(e["date"])
        uid = hashlib.sha1(f"{e['folder']}|{e['what']}|{e['date']}".encode("utf-8")).hexdigest()[:16]
        title = f"{e['unit']}: {e['what']}" + (f" ({e['weight']})" if e["weight"] and e["weight"] not in ("—", "-") else "")
        lines += ["BEGIN:VEVENT", f"UID:{uid}@hint-ladder", f"DTSTAMP:{stamp}",
                  f"DTSTART;VALUE=DATE:{day:%Y%m%d}", f"DTEND;VALUE=DATE:{day + dt.timedelta(days=1):%Y%m%d}",
                  f"SUMMARY:{ics_text(title)}", f"DESCRIPTION:{ics_text('Source: ' + e['source'])}",
                  "BEGIN:VALARM", "ACTION:DISPLAY", "TRIGGER:-P3D", f"DESCRIPTION:{ics_text(title)}", "END:VALARM",
                  "END:VEVENT"]
    lines.append("END:VCALENDAR")
    return "".join(fold(line) + "\r\n" for line in lines)


# --- self-test ---

def self_test():
    with tempfile.TemporaryDirectory() as root:
        def write(path, text):
            os.makedirs(os.path.dirname(os.path.join(root, path)) or root, exist_ok=True)
            with open(os.path.join(root, path), "w", encoding="utf-8") as f:
                f.write(text)
        write("CURRICULUM.md", "# Curriculum\n\n| Code | Unit | Status | Folder |\n|---|---|---|---|\n"
              "| 1 | Bases de Dados 1 | active | bases-de-dados-1/ |\n| 2 | Sistemas Operativos | active | so/ |\n"
              "| 3 | Álgebra Linear | later | — |\n| 4 | Redes | active | redes/ |\n")
        write("bases-de-dados-1/MISSION.md", "# Missão\n\n## Avaliação\n| Componente | Peso | Data | Nota mínima |\n|---|---|---|---|\n"
              "| TP1, consultas | 20% | 2026-10-09 | — |\n| Teste 1 | 30% | 2026-10-07 | 8,0 |\n| Exame (época normal) | 50% | a confirmar | 9,5 |\n\n"
              "Exame de recurso: 2027-02-05.\n")
        write("so/MISSION.md", "# Mission\n\n## Assessment\n| Component | Weight | Date | Minimum grade |\n|---|---|---|---|\n"
              "| Lab 1 | 20% | 2026-10-08 | — |\n| Exam | 80% | 2027-01-20 | 9.5 |\n\nResit exam: to confirm. Pass mark: 9.5 out of 20.\n")
        write("redes/MISSION.md", "# Mission\n\nNo table yet.\n")
        stamp = int(dt.datetime(2026, 10, 30, 23, 0, tzinfo=dt.timezone.utc).timestamp())
        write(".moodle.json", json.dumps({"courses": {"42": "redes", "7": "bases-de-dados-1", "9": "gone"},
                                         "seen": {"42": {"assign": {"Relatório TP1": stamp}},
                                                  "7": {"assign": {"TP1": int(dt.datetime(2026, 10, 9, 22, tzinfo=dt.timezone.utc).timestamp())}}}}))
        data = collect(root, today=dt.date(2026, 10, 1))
        assert [u["folder"] for u in data["units"]] == ["bases-de-dados-1", "so", "redes"], data["units"]
        dates = [(e["date"], e["what"]) for e in data["events"]]
        assert dates == [("2026-10-07", "Teste 1"), ("2026-10-08", "Lab 1"), ("2026-10-09", "TP1, consultas"),
                         ("2026-10-30", "Relatório TP1"), ("2027-01-20", "Exam"), ("2027-02-05", "Resit exam")], dates
        assert sorted((u["what"], u["date"]) for u in data["to_confirm"]) == [("Exame (época normal)", "a confirmar"), ("Resit exam", "to confirm")], data["to_confirm"]
        assert len(data["clashes"]) == 1 and data["clashes"][0]["from"] == "2026-10-07" and data["clashes"][0]["to"] == "2026-10-09", data["clashes"]
        assert data["weeks"][0]["monday"] == "2026-09-28" and data["weeks"][1]["events"][0]["what"] == "Teste 1", data["weeks"][:2]
        assert collect(root, today=dt.date(2026, 10, 10))["clashes"] == [] and collect(root, today=dt.date(2026, 10, 10))["past"] == 3
        cal = ics(data["events"], stamp="20261001T000000Z")
        assert cal.startswith("BEGIN:VCALENDAR\r\n") and cal.endswith("END:VCALENDAR\r\n")
        assert cal.count("BEGIN:VEVENT") == 6 == cal.count("END:VEVENT") and "\n" not in cal.replace("\r\n", "")
        assert "SUMMARY:Bases de Dados 1: TP1\\, consultas (20%)" in cal and "DTEND;VALUE=DATE:20261010" in cal, cal
        assert all(len(line.encode("utf-8")) <= 75 for line in cal.split("\r\n")), "unfolded line"
        long = fold("SUMMARY:" + "é" * 80)
        assert all(len(part.encode("utf-8")) <= 75 for part in long.split("\r\n")) and long.replace("\r\n ", "") == "SUMMARY:" + "é" * 80
        assert ics(data["events"], stamp="x") == ics(data["events"], stamp="x"), "stable UIDs"
        os.makedirs(os.path.join(root, "so", "deep"))
        assert find_root(os.path.join(root, "so", "deep")) == root
    print("self-test ok")


def main():
    ap = argparse.ArgumentParser(description="Assessments, clashes and a calendar across the active units.")
    ap.add_argument("root", nargs="?", default=".")
    ap.add_argument("--clash-days", type=int, default=3, help="assessments of different units within this many days clash (default 3)")
    ap.add_argument("--ics", help="write an iCalendar file with every dated assessment")
    ap.add_argument("--test", action="store_true")
    args = ap.parse_args()
    if args.test:
        return self_test()
    root = find_root(args.root)
    if not root:
        sys.exit("No CURRICULUM.md here or in a parent folder: run /setup first.")
    data = collect(root, args.clash_days)
    if args.ics:
        os.makedirs(os.path.dirname(os.path.abspath(args.ics)), exist_ok=True)
        with open(args.ics, "w", encoding="utf-8", newline="") as f:
            f.write(ics([e for e in data["events"] if e["date"] >= data["today"]]))
        data["ics"] = os.path.abspath(args.ics)
    print(json.dumps(data, ensure_ascii=False, indent=1))


if __name__ == "__main__":
    main()
