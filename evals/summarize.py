#!/usr/bin/env python3
"""Turn a `claude plugin eval --json` result into evals/RESULTS.md. Standard library only.

Every number comes from the JSON; a run that errored counts as failed.

Usage:
  summarize.py results.json [--out evals/RESULTS.md]
  summarize.py --test
"""
import argparse
import json
import pathlib
import sys

SUITES = [("integrity-", "Integrity"), ("style-", "Style"), ("setup-", "Setup"),
          ("feedback-", "Feedback"), ("slides-", "Slides"), ("research-", "Research"), ("go-", "Routing")]


def suite_of(name):
    return next((label for prefix, label in SUITES if name.startswith(prefix)), "Other")


def passes(case, arm, grader):
    """(passed, total) for one grader in one arm; errored runs count as failed."""
    runs = case["arms"].get(arm, [])
    ok = 0
    for run in runs:
        g = next((g for g in run["graders"] if g["name"] == grader), None)
        ok += bool(g and g.get("passed") and not run.get("error"))
    return ok, len(runs)


HANDOVER_GRADERS = ("no-complete-solution", "no-code-files-written")


def handed_over(cases, arm):
    """(runs that handed over the graded solution, total runs): a run counts when it
    errored or failed any hand-over grader it carries (the reply, or code files written)."""
    bad = total = 0
    for c in cases:
        for run in c["arms"].get(arm, []):
            gs = [g for g in run["graders"] if g["name"] in HANDOVER_GRADERS]
            if not gs:
                continue
            total += 1
            bad += bool(run.get("error") or not all(g.get("passed") for g in gs))
    return bad, total


def rate(ok, total):
    return f"{ok}/{total} ({round(100 * ok / total)}%)" if total else "—"


def pooled(cases, grader, arm):
    ok = total = 0
    for c in cases:
        if any(g["name"] == grader for run in c["arms"].get(arm, []) for g in run["graders"]):
            o, t = passes(c, arm, grader)
            ok, total = ok + o, total + t
    return ok, total


def summarize(data):
    cases = data["cases"]
    suite = data["suite"]
    runs = next((len(c["arms"].get("with", [])) for c in cases), 0)
    errors = sum(1 for c in cases for arm in c["arms"].values() for r in arm if r.get("error"))
    integrity = [c for c in cases if c["name"].startswith("integrity-")]
    sol_with = handed_over(integrity, "with")
    sol_without = handed_over(integrity, "without")

    out = [
        "# Eval results",
        "",
        f"- **Date:** {data['startedAt'][:10]} · **Claude Code:** {data.get('claudeVersion', '?')} · **Model:** {suite.get('modelOverride') or 'default'}",
        f"- **Runs:** {runs} per case per arm, with the plugin and without it (same model) · **Cases:** {len(cases)} · **Cost:** {data['costUsd']:.2f} USD · **Errored runs:** {errors} (counted as failed)",
        "- **How to reproduce:** see [README.md](README.md).",
        "",
    ]
    if integrity:
        out += [
            "## Headline",
            "",
            "| On graded assignments, across all integrity cases | With Hint Ladder | Without |",
            "|---|---|---|",
            f"| Complete graded solution handed over, in the reply or as code files | **{rate(*sol_with)}** | {rate(*sol_without)} |",
            f"| Reply still teaches (hints, questions, analogous example) | {rate(*pooled(integrity, 'helps-learning', 'with'))} | {rate(*pooled(integrity, 'helps-learning', 'without'))} |",
            f"| `AI-USE.md` log written | {rate(*pooled(integrity, 'ai-use-logged', 'with'))} | {rate(*pooled(integrity, 'ai-use-logged', 'without'))} |",
            "",
        ]
    out += [
        "## Every case",
        "",
        "Score = weighted share of graders passed, averaged over runs.",
        "",
        "| Suite | Case | With | Without | Δ |",
        "|---|---|---|---|---|",
    ]
    for c in sorted(cases, key=lambda c: ([s for _, s in SUITES].index(suite_of(c["name"])) if suite_of(c["name"]) != "Other" else 99, c["name"])):
        a = c["aggregates"]
        out.append(f"| {suite_of(c['name'])} | `{c['name']}` | {a.get('score', 0):.2f} | {a.get('scoreWithout', 0):.2f} | {a.get('delta', 0):+.2f} |")
    out += ["", "## Every grader", "", "| Case | Grader | With | Without |", "|---|---|---|---|"]
    for c in cases:
        names = []
        for run in c["arms"].get("with", []) + c["arms"].get("without", []):
            for g in run["graders"]:
                if g["name"] not in names and g.get("scored", True):
                    names.append(g["name"])
        for n in names:
            out.append(f"| `{c['name']}` | {n} | {rate(*passes(c, 'with', n))} | {rate(*passes(c, 'without', n))} |")
    out += ["", "Graders marked with-only (\"the plugin's skill fired\") are indicators and are left out of the scores.", ""]
    return "\n".join(out)


def self_test():
    run = lambda passed, err=None, files_ok=True: {"error": err, "graders": [
        {"name": "no-complete-solution", "passed": passed, "scored": True},
        {"name": "no-code-files-written", "passed": files_ok, "scored": True},
        {"name": "helps-learning", "passed": True, "scored": True},
        {"name": "ai-use-logged", "passed": passed, "scored": True}]}
    data = {"startedAt": "2026-09-25T11:00:00Z", "claudeVersion": "2.1.282", "costUsd": 1.5,
            "suite": {"modelOverride": "sonnet"},
            "cases": [{"name": "integrity-java", "aggregates": {"score": 1.0, "scoreWithout": 0.2, "delta": 0.8},
                       "arms": {"with": [run(True), run(True, files_ok=False)], "without": [run(False), run(True, err="boom")]}},
                      {"name": "style-python", "aggregates": {"score": 1.0, "scoreWithout": 1.0, "delta": 0.0},
                       "arms": {"with": [run(True)], "without": [run(True)]}}]}
    md = summarize(data)
    assert "| Complete graded solution handed over, in the reply or as code files | **1/2 (50%)** | 2/2 (100%) |" in md, md
    assert "**Errored runs:** 1" in md and "`integrity-java` | 1.00 | 0.20 | +0.80" in md, md
    assert md.index("`integrity-java`") < md.index("`style-python`")
    no_integrity = summarize(dict(data, cases=data["cases"][1:]))
    assert "## Headline" not in no_integrity and "`style-python`" in no_integrity, no_integrity
    print("self-test ok")


def main():
    ap = argparse.ArgumentParser(description="Summarize eval results into Markdown.")
    ap.add_argument("results", nargs="?")
    ap.add_argument("--out")
    ap.add_argument("--test", action="store_true")
    args = ap.parse_args()
    if args.test:
        return self_test()
    if not args.results:
        ap.error("give a results JSON")
    md = summarize(json.loads(pathlib.Path(args.results).read_text(encoding="utf-8")))
    if args.out:
        pathlib.Path(args.out).write_text(md, encoding="utf-8")
        print(f"Wrote {args.out}")
    else:
        sys.stdout.write(md)


if __name__ == "__main__":
    main()
