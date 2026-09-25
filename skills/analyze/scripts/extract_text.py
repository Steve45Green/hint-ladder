#!/usr/bin/env python3
"""Extract the text of office documents for study notes. Standard library only.

Handles .pptx (slides and speaker notes, in slide order), .docx, .odt/.odp,
.html and plain text. PDFs go through `pdftotext -layout` when it is
installed; otherwise the caller reads the PDF pages directly.

Usage:
  extract_text.py FILE [--out FILE]
  extract_text.py --test
"""
import argparse
import html
import pathlib
import re
import shutil
import subprocess
import sys
import tempfile
import zipfile

W_P = re.compile(r"<w:p[ >].*?</w:p>", re.S)
W_T = re.compile(r"<w:t(?: [^>]*)?>(.*?)</w:t>", re.S)
A_P = re.compile(r"<a:p>.*?</a:p>|<a:p .*?</a:p>", re.S)
A_T = re.compile(r"<a:t>(.*?)</a:t>", re.S)
ODF_P = re.compile(r"<text:(?:p|h)[^>]*>(.*?)</text:(?:p|h)>", re.S)
TAG = re.compile(r"<[^>]+>")


def paragraphs(xml, para, run):
    out = []
    for p in para.findall(xml):
        text = "".join(html.unescape(t) for t in run.findall(p)).strip()
        if text:
            out.append(text)
    return out


def number(name):
    m = re.search(r"(\d+)\.xml$", name)
    return int(m.group(1)) if m else 0


def pptx(path):
    with zipfile.ZipFile(path) as z:
        names = z.namelist()
        slides = sorted((n for n in names if re.match(r"ppt/slides/slide\d+\.xml$", n)), key=number)
        notes = {number(n): n for n in names if re.match(r"ppt/notesSlides/notesSlide\d+\.xml$", n)}
        out = []
        for s in slides:
            i = number(s)
            out.append(f"## Slide {i}")
            out.extend(paragraphs(z.read(s).decode("utf-8", "replace"), A_P, A_T) or ["(no text)"])
            if i in notes:
                note = [t for t in paragraphs(z.read(notes[i]).decode("utf-8", "replace"), A_P, A_T) if not t.isdigit()]
                if note:
                    out.append("Notes: " + " ".join(note))
            out.append("")
        return "\n".join(out)


def docx(path):
    with zipfile.ZipFile(path) as z:
        return "\n\n".join(paragraphs(z.read("word/document.xml").decode("utf-8", "replace"), W_P, W_T))


def odf(path):
    with zipfile.ZipFile(path) as z:
        xml = z.read("content.xml").decode("utf-8", "replace")
    return "\n\n".join(t for t in (html.unescape(TAG.sub("", p)).strip() for p in ODF_P.findall(xml)) if t)


def pdf(path):
    if not shutil.which("pdftotext"):
        sys.exit("pdftotext is not installed: read the PDF pages directly instead.")
    result = subprocess.run(["pdftotext", "-layout", str(path), "-"], capture_output=True, text=True)
    if result.returncode != 0:
        sys.exit(result.stderr.strip() or "pdftotext failed")
    pages = result.stdout.split("\f")
    return "\n".join(f"## Page {i}\n{p.strip()}\n" for i, p in enumerate(pages, 1) if p.strip())


def extract(path):
    path = pathlib.Path(path)
    ext = path.suffix.lower()
    if ext == ".pptx":
        return pptx(path)
    if ext == ".docx":
        return docx(path)
    if ext in (".odt", ".odp"):
        return odf(path)
    if ext == ".pdf":
        return pdf(path)
    if ext in (".html", ".htm"):
        raw = path.read_text(encoding="utf-8", errors="replace")
        raw = re.sub(r"<(script|style)[^>]*>.*?</\1>", "", raw, flags=re.S | re.I)
        return re.sub(r"\n\s*\n+", "\n\n", html.unescape(TAG.sub("", raw))).strip()
    if ext in (".txt", ".md", ".csv"):
        return path.read_text(encoding="utf-8", errors="replace")
    sys.exit(f"Unsupported file type: {ext} (read it directly instead)")


def self_test():
    with tempfile.TemporaryDirectory() as d:
        base = pathlib.Path(d)
        with zipfile.ZipFile(base / "deck.pptx", "w") as z:
            z.writestr("ppt/slides/slide2.xml", "<p:sld><a:p><a:r><a:t>Second &amp; last</a:t></a:r></a:p></p:sld>")
            z.writestr("ppt/slides/slide10.xml", "<p:sld><a:p><a:r><a:t>Tenth</a:t></a:r></a:p></p:sld>")
            z.writestr("ppt/slides/slide1.xml", "<p:sld><a:p><a:r><a:t>Normal</a:t></a:r><a:r><a:t> forms</a:t></a:r></a:p></p:sld>")
            z.writestr("ppt/notesSlides/notesSlide1.xml", "<p:notes><a:p><a:r><a:t>Say 3NF here</a:t></a:r></a:p><a:p><a:r><a:t>1</a:t></a:r></a:p></p:notes>")
        text = pptx(base / "deck.pptx")
        assert text.index("## Slide 1") < text.index("## Slide 2") < text.index("## Slide 10"), text
        assert "Normal forms" in text and "Second & last" in text and "Notes: Say 3NF here" in text, text
        with zipfile.ZipFile(base / "notes.docx", "w") as z:
            z.writestr("word/document.xml", '<w:document><w:body><w:p><w:r><w:t>Big-O</w:t></w:r><w:r><w:t xml:space="preserve"> notation</w:t></w:r></w:p><w:p><w:r><w:t>Second paragraph</w:t></w:r></w:p></w:body></w:document>')
        assert docx(base / "notes.docx") == "Big-O notation\n\nSecond paragraph"
        with zipfile.ZipFile(base / "sheet.odt", "w") as z:
            z.writestr("content.xml", '<office:text><text:h text:outline-level="1">Programa</text:h><text:p>1. Processos</text:p></office:text>')
        assert odf(base / "sheet.odt") == "Programa\n\n1. Processos"
        (base / "page.html").write_text("<html><style>x{}</style><body><h1>Tema</h1><p>A &lt; B</p></body></html>")
        assert "Tema" in extract(base / "page.html") and "A < B" in extract(base / "page.html")
    print("self-test ok")


def main():
    ap = argparse.ArgumentParser(description="Extract text from course material.")
    ap.add_argument("file", nargs="?")
    ap.add_argument("--out", help="write the text here instead of stdout")
    ap.add_argument("--test", action="store_true", help="run the self-test")
    args = ap.parse_args()
    if args.test:
        return self_test()
    if not args.file:
        ap.error("give a file")
    text = extract(args.file)
    if args.out:
        pathlib.Path(args.out).write_text(text, encoding="utf-8")
        print(f"Wrote {args.out} ({len(text.splitlines())} lines).")
    else:
        print(text)


if __name__ == "__main__":
    main()
