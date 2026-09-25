#!/usr/bin/env python3
"""Read the student's Moodle for /setup: their courses, the files in each, and the assignments.

Uses Moodle's web service API (the one the Moodle app uses) with the student's own key.
Standard library only.

    python3 moodle.py login --url https://moodle.school.pt   # the student runs this in their own terminal
    python3 moodle.py courses                                # JSON: id, fullname, shortname
    python3 moodle.py files --course 42                      # JSON: section, module, filename, size, modified
    python3 moodle.py fetch --course 42 --dest bases-de-dados-1/material/moodle
    python3 moodle.py assignments --course 42                # JSON: name, due date, statement as text
    python3 moodle.py --test

The key is stored in ~/.config/hint-ladder/moodle.json (mode 0600), outside every course folder,
and is never printed. A password, when the student signs in with one, is used once and never stored.
"""
import argparse
import getpass
import html.parser
import json
import os
import re
import sys
import urllib.error
import urllib.parse
import urllib.request
from datetime import datetime, timezone

CONFIG = os.environ.get("HINT_LADDER_MOODLE_CONFIG",
                        os.path.join(os.path.expanduser("~"), ".config", "hint-ladder", "moodle.json"))
DEFAULT_TYPES = {"pdf", "pptx", "ppt", "docx", "doc", "odt", "odp", "txt", "md"}
HINTS = {
    "invalidtoken": "The Moodle key is not valid any more: run `moodle.py login` again.",
    "invalidlogin": "Wrong username or password. If the school signs in through its own page (SSO), use the key from Preferences > Security keys instead.",
    "enablewsdescription": "The school has not enabled the Moodle app web services; ask them, or download the files by hand and use /analyze.",
    "servicenotavailable": "The school has not enabled the Moodle app web services; ask them, or download the files by hand and use /analyze.",
    "accessexception": "Moodle refused access to this course or function.",
}


class MoodleError(Exception):
    pass


def check_url(url):
    url = url.strip().rstrip("/")
    parts = urllib.parse.urlparse(url)
    local = parts.hostname in ("localhost", "127.0.0.1")
    if parts.scheme != "https" and not (parts.scheme == "http" and local):
        raise MoodleError("Use the school's https:// Moodle address; the key must not travel unencrypted.")
    return url


def post(url, data):
    body = urllib.parse.urlencode(data).encode()
    try:
        with urllib.request.urlopen(urllib.request.Request(url, data=body), timeout=60) as r:
            text = r.read().decode("utf-8", "replace")
    except urllib.error.URLError as e:
        raise MoodleError(f"Could not reach Moodle: {getattr(e, 'reason', e)}") from None
    try:
        return json.loads(text)
    except json.JSONDecodeError:
        raise MoodleError("This does not look like Moodle's web service: check the address, or ask the school "
                          "whether the Moodle app is enabled.") from None


def flatten(params, prefix=""):
    """{'courseids': [42]} -> {'courseids[0]': 42}, the form encoding Moodle expects."""
    out = {}
    for key, value in params.items():
        name = f"{prefix}[{key}]" if prefix else str(key)
        if isinstance(value, dict):
            out.update(flatten(value, name))
        elif isinstance(value, (list, tuple)):
            out.update(flatten(dict(enumerate(value)), name))
        else:
            out[name] = value
    return out


class Moodle:
    def __init__(self, url, token):
        self.url, self.token = check_url(url), token

    def call(self, function, **params):
        data = {"wstoken": self.token, "wsfunction": function, "moodlewsrestformat": "json", **flatten(params)}
        result = post(self.url + "/webservice/rest/server.php", data)
        if isinstance(result, dict) and "exception" in result:
            code = result.get("errorcode", "")
            raise MoodleError(HINTS.get(code, f"Moodle said: {result.get('message', 'error')} ({code})"))
        return result

    def site(self):
        return self.call("core_webservice_get_site_info")

    def courses(self):
        user = self.site()["userid"]
        return [{"id": c["id"], "fullname": c.get("fullname", ""), "shortname": c.get("shortname", "")}
                for c in self.call("core_enrol_get_users_courses", userid=user)]

    def files(self, course):
        out = []
        for section in self.call("core_course_get_contents", courseid=course):
            for module in section.get("modules", []):
                for f in module.get("contents") or []:
                    if f.get("type") == "file" and f.get("fileurl"):
                        out.append({"section": section.get("name", ""), "module": module.get("name", ""),
                                    "filename": f.get("filename", ""), "size": f.get("filesize", 0),
                                    "modified": f.get("timemodified", 0), "fileurl": f["fileurl"]})
        return out

    def download(self, fileurl, path):
        sep = "&" if "?" in fileurl else "?"
        url = fileurl + sep + urllib.parse.urlencode({"token": self.token})
        tmp = path + ".part"
        try:
            with urllib.request.urlopen(url, timeout=120) as r, open(tmp, "wb") as out:
                while chunk := r.read(1 << 16):
                    out.write(chunk)
        except urllib.error.URLError as e:
            if os.path.exists(tmp):
                os.remove(tmp)
            raise MoodleError(f"Download failed: {getattr(e, 'reason', e)}") from None
        os.replace(tmp, path)

    def assignments(self, course):
        result = self.call("mod_assign_get_assignments", courseids=[course])
        out = []
        for c in result.get("courses", []):
            for a in c.get("assignments", []):
                due = a.get("duedate") or 0
                out.append({"name": a.get("name", ""),
                            "due": datetime.fromtimestamp(due, timezone.utc).strftime("%Y-%m-%d %H:%M UTC") if due else None,
                            "statement": html_to_text(a.get("intro", "")),
                            "attachments": [f.get("filename", "") for f in a.get("introattachments", [])]})
        return out


class _Text(html.parser.HTMLParser):
    BLOCKS = {"p", "br", "li", "div", "tr", "h1", "h2", "h3", "h4"}

    def __init__(self):
        super().__init__()
        self.parts = []

    def handle_starttag(self, tag, attrs):
        if tag in self.BLOCKS:
            self.parts.append("\n")

    def handle_data(self, data):
        self.parts.append(data)


def html_to_text(markup):
    parser = _Text()
    parser.feed(markup or "")
    lines = [re.sub(r"\s+", " ", line).strip() for line in "".join(parser.parts).splitlines()]
    return "\n".join(line for line in lines if line)


def safe_name(name, basename=False):
    """A file or folder name that cannot leave the destination: no separators, no control characters."""
    if basename:
        name = name.replace("\\", "/").rsplit("/", 1)[-1]
    name = re.sub(r'[\x00-\x1f<>:"/\\|?*]', "_", name).strip(" .")
    return name[:120] or "_"


def fetch(moodle, course, dest, types=DEFAULT_TYPES, max_mb=50):
    """Download a course's files into dest/<section>/; returns (downloaded, unchanged, ignored) path lists."""
    root = os.path.realpath(dest)
    downloaded, unchanged, ignored = [], [], []
    for f in moodle.files(course):
        ext = f["filename"].rsplit(".", 1)[-1].lower() if "." in f["filename"] else ""
        if (types and ext not in types) or f["size"] > max_mb * 1024 * 1024:
            ignored.append(f["filename"])
            continue
        folder = os.path.join(root, safe_name(f["section"]))
        path = os.path.realpath(os.path.join(folder, safe_name(f["filename"], basename=True)))
        if not path.startswith(root + os.sep):
            ignored.append(f["filename"])
            continue
        if os.path.exists(path) and os.path.getsize(path) == f["size"] and os.path.getmtime(path) >= f["modified"]:
            unchanged.append(os.path.relpath(path, root))
            continue
        os.makedirs(folder, exist_ok=True)
        moodle.download(f["fileurl"], path)
        if f["modified"]:
            os.utime(path, (f["modified"], f["modified"]))
        downloaded.append(os.path.relpath(path, root))
    return downloaded, unchanged, ignored


def save_config(url, token, site, config=None):
    config = config or CONFIG
    os.makedirs(os.path.dirname(config), mode=0o700, exist_ok=True)
    fd = os.open(config, os.O_WRONLY | os.O_CREAT | os.O_TRUNC, 0o600)
    with os.fdopen(fd, "w") as out:
        json.dump({"url": url, "token": token, "sitename": site.get("sitename", "")}, out)
    os.chmod(config, 0o600)


def load(config=None):
    config = config or CONFIG
    try:
        with open(config) as f:
            data = json.load(f)
    except FileNotFoundError:
        raise MoodleError("Not signed in: run `python3 moodle.py login --url <your school's Moodle>` "
                          "in your own terminal first.") from None
    return Moodle(data["url"], data["token"])


def login(url, key=None, username=None, password=None, config=None):
    """Store a working key; with a username and password, trade them for a key first (the password is not kept)."""
    url = check_url(url)
    if not key:
        result = post(url + "/login/token.php",
                      {"username": username, "password": password, "service": "moodle_mobile_app"})
        if "token" not in result:
            code = result.get("errorcode", "")
            raise MoodleError(HINTS.get(code, f"Moodle said: {result.get('error', 'sign-in failed')} ({code})"))
        key = result["token"]
    site = Moodle(url, key).site()
    save_config(url, key, site, config)
    return site


def main(argv=None):
    ap = argparse.ArgumentParser(description="Read the student's Moodle for /setup.")
    ap.add_argument("--test", action="store_true", help="run the self-test")
    sub = ap.add_subparsers(dest="cmd")
    p = sub.add_parser("login", help="sign in once (run it yourself, in a terminal)")
    p.add_argument("--url", required=True)
    sub.add_parser("courses", help="the courses you are enrolled in")
    for name in ("files", "assignments"):
        sub.add_parser(name).add_argument("--course", type=int, required=True)
    p = sub.add_parser("fetch", help="download a course's files")
    p.add_argument("--course", type=int, required=True)
    p.add_argument("--dest", required=True)
    p.add_argument("--types", default=",".join(sorted(DEFAULT_TYPES)), help="extensions, or 'all'")
    p.add_argument("--max-mb", type=float, default=50)
    args = ap.parse_args(argv)
    if args.test:
        return self_test()
    try:
        if args.cmd == "login":
            print("Your Moodle key: Moodle > Preferences > Security keys > 'Moodle mobile web service'.")
            key = getpass.getpass("Paste the key (or press Enter to sign in with username and password): ").strip()
            username = password = None
            if not key:
                username = input("Username: ").strip()
                password = getpass.getpass("Password (used once, not stored): ")
            site = login(args.url, key, username, password)
            print(f"Signed in to {site.get('sitename', 'Moodle')} as {site.get('fullname', '?')}. "
                  f"Key saved in {CONFIG} (only you can read it).")
        elif args.cmd == "courses":
            print(json.dumps(load().courses(), ensure_ascii=False, indent=1))
        elif args.cmd == "files":
            files = [{k: v for k, v in f.items() if k != "fileurl"} for f in load().files(args.course)]
            print(json.dumps(files, ensure_ascii=False, indent=1))
        elif args.cmd == "assignments":
            print(json.dumps(load().assignments(args.course), ensure_ascii=False, indent=1))
        elif args.cmd == "fetch":
            types = None if args.types == "all" else {t.strip().lower().lstrip(".") for t in args.types.split(",")}
            got, same, skipped = fetch(load(), args.course, args.dest, types, args.max_mb)
            print(json.dumps({"downloaded": got, "unchanged": same, "ignored (type or size)": skipped},
                             ensure_ascii=False, indent=1))
        else:
            ap.print_help()
    except MoodleError as e:
        print(f"error: {e}", file=sys.stderr)
        return 1
    return 0


def self_test():
    import contextlib
    import http.server
    import io
    import tempfile
    import threading

    token = "a1b2c3d4e5f60718293a4b5c6d7e8f90"
    files = {"slides.pdf": b"%PDF-1.4 slides", "notas.docx": b"PK docx", "video.mp4": b"mp4"}

    class Fake(http.server.BaseHTTPRequestHandler):
        def log_message(self, *a):
            pass

        def reply(self, obj, raw=None):
            body = raw if raw is not None else json.dumps(obj).encode()
            self.send_response(200)
            self.send_header("Content-Length", str(len(body)))
            self.end_headers()
            self.wfile.write(body)

        def do_POST(self):
            form = dict(urllib.parse.parse_qsl(self.rfile.read(int(self.headers["Content-Length"])).decode()))
            if self.path == "/login/token.php":
                ok = form.get("username") == "ana" and form.get("password") == "pw"
                return self.reply({"token": token} if ok else {"error": "Invalid login", "errorcode": "invalidlogin"})
            if form.get("wstoken") != token:
                return self.reply({"exception": "moodle_exception", "errorcode": "invalidtoken", "message": "Invalid token"})
            fn, base = form["wsfunction"], f"http://127.0.0.1:{port}/webservice/pluginfile.php/1/"
            if fn == "core_webservice_get_site_info":
                return self.reply({"sitename": "Moodle Teste", "userid": 7, "fullname": "Ana"})
            if fn == "core_enrol_get_users_courses":
                assert form["userid"] == "7"
                return self.reply([{"id": 42, "fullname": "Bases de Dados 1", "shortname": "BD1"}])
            if fn == "core_course_get_contents":
                entry = lambda name, size=None: {"type": "file", "filename": name, "filesize": size or len(files.get(name, b"")),
                                                 "timemodified": 1760000000, "fileurl": base + urllib.parse.quote(name.split("/")[-1])}
                return self.reply([
                    {"name": "Semana 1", "modules": [{"name": "Slides", "contents": [entry("slides.pdf"), entry("video.mp4")]},
                                                     {"name": "Fórum", "contents": None}]},
                    {"name": "Avaliação/TP1", "modules": [{"name": "Notas", "contents": [entry("notas.docx"), entry("big.pdf", 60 << 20),
                                                                                         entry("../../evil.pdf", 4)]}]}])
            if fn == "mod_assign_get_assignments":
                assert form["courseids[0]"] == "42"
                return self.reply({"courses": [{"id": 42, "assignments": [
                    {"name": "TP1", "duedate": 1760011200, "intro": "<p>Escreve <b>três</b> consultas.</p><ul><li>Uma com LEFT JOIN</li></ul>",
                     "introattachments": [{"filename": "esquema.pdf"}]}]}]})
            return self.reply({"exception": "x", "errorcode": "invalidfunction", "message": "?"})

        def do_GET(self):
            path, _, query = self.path.partition("?")
            if dict(urllib.parse.parse_qsl(query)).get("token") != token:
                self.send_response(403)
                self.end_headers()
                return
            name = urllib.parse.unquote(path.rsplit("/", 1)[-1])
            self.reply(None, raw=files.get(name, b"evil"))

    os.environ["no_proxy"] = os.environ["NO_PROXY"] = "127.0.0.1,localhost"
    server = http.server.ThreadingHTTPServer(("127.0.0.1", 0), Fake)
    port = server.server_address[1]
    threading.Thread(target=server.serve_forever, daemon=True).start()
    url = f"http://127.0.0.1:{port}"
    with tempfile.TemporaryDirectory() as tmp:
        global CONFIG
        CONFIG = os.path.join(tmp, "cfg", "moodle.json")
        # https is required except on localhost
        try:
            check_url("http://moodle.school.pt")
            raise AssertionError("plain http accepted")
        except MoodleError:
            pass
        # a wrong password and a wrong key both give a clear message
        for kwargs, words in (({"username": "ana", "password": "no"}, "Wrong username"), ({"key": "bad"}, "not valid")):
            try:
                login(url, **kwargs)
                raise AssertionError("bad sign-in accepted")
            except MoodleError as e:
                assert words in str(e), e
        # sign in with a password: the key is stored 0600, the password nowhere
        site = login(url, username="ana", password="pw")
        assert site["sitename"] == "Moodle Teste"
        assert oct(os.stat(CONFIG).st_mode & 0o777) == "0o600"
        stored = open(CONFIG).read()
        assert token in stored and '"pw"' not in stored and "password" not in stored
        # every command prints JSON and never the key
        dest = os.path.join(tmp, "unit", "material", "moodle")
        outputs = {}
        for cmd in (["courses"], ["files", "--course", "42"], ["assignments", "--course", "42"],
                    ["fetch", "--course", "42", "--dest", dest]):
            buf = io.StringIO()
            with contextlib.redirect_stdout(buf):
                assert main(cmd) == 0
            outputs[cmd[0]] = buf.getvalue()
            assert token not in buf.getvalue(), cmd
        assert json.loads(outputs["courses"]) == [{"id": 42, "fullname": "Bases de Dados 1", "shortname": "BD1"}]
        assert "fileurl" not in outputs["files"] and len(json.loads(outputs["files"])) == 5
        a = json.loads(outputs["assignments"])[0]
        assert a["due"] == "2025-10-09 12:00 UTC" and a["statement"] == "Escreve três consultas.\nUma com LEFT JOIN", a
        got = json.loads(outputs["fetch"])
        assert sorted(got["downloaded"]) == ["Avaliação_TP1/evil.pdf", "Avaliação_TP1/notas.docx", "Semana 1/slides.pdf"], got
        assert sorted(got["ignored (type or size)"]) == ["big.pdf", "video.mp4"], got
        assert open(os.path.join(dest, "Semana 1", "slides.pdf"), "rb").read() == files["slides.pdf"]
        assert not any(n.endswith(".part") for _, _, ns in os.walk(dest) for n in ns)
        # a second fetch leaves unchanged files alone
        again = fetch(load(), 42, dest)
        assert again[0] == [] and len(again[1]) == 3, again
        # not signed in: a clear next step
        os.remove(CONFIG)
        try:
            load()
            raise AssertionError("loaded without a key")
        except MoodleError as e:
            assert "login" in str(e)
    server.shutdown()
    print("self-test ok")
    return 0


if __name__ == "__main__":
    sys.exit(main())
