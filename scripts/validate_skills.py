#!/usr/bin/env python3
"""Lint the plugin's skills and language agents. Standard library only; exit 1 on any error.

Skills (skills/<name>/SKILL.md): frontmatter with name and description, name
matches the folder and is kebab-case, description at most 1024 characters,
every relative Markdown link resolves.

Agents (agents/*.md, or any folder given with --agents): frontmatter with name
matching the file name, a description, preloaded skills that exist, every
section required by skills/setup/AGENT-TEMPLATE.md, and at least 8 numbered
style rules.

Docs (*.md at the repository root, docs/ and evals/): every relative link resolves.

Usage:
  validate_skills.py                  skills + the plugin's agents + doc links
  validate_skills.py --agents DIR     also agents in DIR (e.g. ones /setup generated)
  validate_skills.py --test           self-test
"""
import argparse
import pathlib
import re
import sys
import tempfile

ROOT = pathlib.Path(__file__).resolve().parent.parent
KEBAB = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")
FRONTMATTER = re.compile(r"\A---\n(.*?)\n---\n", re.S)
LINK = re.compile(r"\]\(([^)\s]+)\)")
AGENT_SECTIONS = ["## Role", "## Modes", "## Course units", "## Style rules", "## Common mistakes",
                  "## Feedback", "## Feedback loop", "## Teaching moves", "## Done when"]
MIN_STYLE_RULES = 8
MIN_MISTAKES = 8


def parse_frontmatter(text):
    """Return a dict of top-level keys; list values (`- item` lines) become lists."""
    m = FRONTMATTER.match(text)
    if not m:
        return None
    meta, key = {}, None
    for line in m.group(1).splitlines():
        item = re.match(r"^\s+-\s+(.*)$", line)
        if item and key:
            if not isinstance(meta[key], list):
                meta[key] = []
            meta[key].append(item.group(1).strip())
            continue
        k, sep, value = line.partition(":")
        if sep and not line.startswith((" ", "\t")):
            key = k.strip()
            meta[key] = value.split(" #")[0].strip().strip('"')
    return meta


def check_description(label, meta):
    description = meta.get("description", "")
    if not description:
        return [f"{label}: missing description"]
    if len(description) > 1024:
        return [f"{label}: description has {len(description)} characters (max 1024)"]
    return []


def validate_skill(folder):
    skill = folder / "SKILL.md"
    if not skill.is_file():
        return [f"{folder.name}: missing SKILL.md"]
    meta = parse_frontmatter(skill.read_text(encoding="utf-8"))
    if meta is None:
        return [f"{folder.name}: missing YAML frontmatter"]
    errors = check_description(folder.name, meta)
    if meta.get("name") != folder.name:
        errors.append(f"{folder.name}: name '{meta.get('name', '')}' does not match the folder")
    if not KEBAB.match(folder.name):
        errors.append(f"{folder.name}: folder name is not kebab-case")
    for md in folder.rglob("*.md"):
        for target in LINK.findall(md.read_text(encoding="utf-8")):
            if target.startswith(("http://", "https://", "#", "mailto:")):
                continue
            if not (md.parent / target.split("#")[0]).exists():
                errors.append(f"{md.relative_to(folder.parent)}: broken link -> {target}")
    return errors


def validate_agent(path, skills_dir):
    label = f"agents/{path.name}"
    text = path.read_text(encoding="utf-8")
    meta = parse_frontmatter(text)
    if meta is None:
        return [f"{label}: missing YAML frontmatter"]
    errors = check_description(label, meta)
    if meta.get("name") != path.stem:
        errors.append(f"{label}: name '{meta.get('name', '')}' does not match the file name")
    if not KEBAB.match(path.stem):
        errors.append(f"{label}: file name is not kebab-case")
    preload = meta.get("skills", [])
    for skill in preload if isinstance(preload, list) else [preload]:
        if skill and not (skills_dir / skill / "SKILL.md").is_file():
            errors.append(f"{label}: preloaded skill '{skill}' does not exist")
    headings = {line.strip() for line in text.splitlines() if line.startswith("## ")}
    for section in AGENT_SECTIONS:
        if section not in headings:
            errors.append(f"{label}: missing section '{section}'")
    style = re.search(r"^## Style rules\n(.*?)(?=^## |\Z)", text, re.S | re.M)
    rules = re.findall(r"^\d+\. ", style.group(1), re.M) if style else []
    if style and len(rules) < MIN_STYLE_RULES:
        errors.append(f"{label}: {len(rules)} numbered style rules (min {MIN_STYLE_RULES})")
    mistakes = re.search(r"^## Common mistakes\n(.*?)(?=^## |\Z)", text, re.S | re.M)
    items = re.findall(r"^\d+\. .*\bask: ", mistakes.group(1), re.M) if mistakes else []
    if mistakes and len(items) < MIN_MISTAKES:
        errors.append(f"{label}: {len(items)} common mistakes with an 'ask:' question (min {MIN_MISTAKES})")
    return errors


def validate_doc_links(root):
    errors = []
    docs = list(root.glob("*.md")) + list((root / "docs").rglob("*.md")) + list((root / "evals").rglob("*.md"))
    for md in docs:
        text = re.sub(r"```.*?```", "", md.read_text(encoding="utf-8"), flags=re.S)
        for target in LINK.findall(text):
            if target.startswith(("http://", "https://", "#", "mailto:")):
                continue
            if not (md.parent / target.split("#")[0]).exists():
                errors.append(f"{md.relative_to(root)}: broken link -> {target}")
    return errors


def run(extra_agent_dirs=()):
    skills_dir = ROOT / "skills"
    folders = sorted(p for p in skills_dir.iterdir() if p.is_dir())
    errors = [e for f in folders for e in validate_skill(f)]
    agent_files = sorted((ROOT / "agents").glob("*.md"))
    for d in extra_agent_dirs:
        agent_files += sorted(pathlib.Path(d).glob("*.md"))
    errors += [e for a in agent_files for e in validate_agent(a, skills_dir)]
    errors += validate_doc_links(ROOT)
    return len(folders), len(agent_files), errors


def self_test():
    good_agent = "---\nname: x-expert\ndescription: d\nskills:\n  - tutor\n---\n" + "\n".join(
        s + "\n" + ("\n".join(f"{i}. rule" for i in range(1, 9)) if s == "## Style rules"
                    else "\n".join(f'{i}. **m{i}**: s · ask: "q" · drill: d' for i in range(1, 9)) if s == "## Common mistakes"
                    else "text")
        for s in AGENT_SECTIONS) + "\n"
    with tempfile.TemporaryDirectory() as d:
        base = pathlib.Path(d)
        (base / "skills" / "tutor").mkdir(parents=True)
        (base / "skills" / "tutor" / "SKILL.md").write_text("---\nname: tutor\ndescription: d\n---\n")
        (base / "x-expert.md").write_text(good_agent)
        assert validate_agent(base / "x-expert.md", base / "skills") == []
        bad = good_agent.replace("name: x-expert", "name: y").replace("  - tutor", "  - ghost")
        bad = bad.replace("## Teaching moves", "## Other").replace("8. rule", "").replace('8. **m8**: s · ask: "q" · drill: d', "")
        (base / "bad-expert.md").write_text(bad)
        errors = validate_agent(base / "bad-expert.md", base / "skills")
        for fragment in ["does not match the file name", "'ghost' does not exist",
                         "missing section '## Teaching moves'", "7 numbered style rules", "7 common mistakes"]:
            assert any(fragment in e for e in errors), (fragment, errors)
        (base / "skills" / "Bad_Skill").mkdir()
        (base / "skills" / "Bad_Skill" / "SKILL.md").write_text("---\nname: other\ndescription: d\n---\n[a](missing.md)\n")
        errors = validate_skill(base / "skills" / "Bad_Skill")
        assert len(errors) == 3, errors
        (base / "README.md").write_text("[ok](x-expert.md) [bad](nowhere.md) ```[ignored](in-code.md)```")
        errors = validate_doc_links(base)
        assert len(errors) == 1 and "nowhere.md" in errors[0], errors
    print("self-test ok")


def main():
    ap = argparse.ArgumentParser(description="Lint skills and language agents.")
    ap.add_argument("--agents", action="append", default=[], metavar="DIR", help="extra folder of agents to lint")
    ap.add_argument("--test", action="store_true", help="run the self-test")
    args = ap.parse_args()
    if args.test:
        return self_test()
    n_skills, n_agents, errors = run(args.agents)
    for e in errors:
        print(f"ERROR {e}")
    print(f"{n_skills} skills, {n_agents} agents, {len(errors)} errors.")
    sys.exit(1 if errors else 0)


if __name__ == "__main__":
    main()
