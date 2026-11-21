#!/usr/bin/env python3
"""Generate README.md and models/ from the EmpirioLabs AI examples feed.

The feed (https://catalog.empiriolabs.ai/examples.json) carries, for every model with a page on
empiriolabs.ai, the code that page shows: cURL and Python. This script turns each model into a folder
of runnable files that read the API key from the EMPIRIOLABS_API_KEY environment variable, plus an
index. .github/workflows/refresh.yml runs it every hour and commits what changed.

Usage:
  python scripts/build_examples.py                      # write README.md and models/ from the live feed
  python scripts/build_examples.py --feed feed.json     # from a saved feed
  python scripts/build_examples.py --check              # exit 1 if the tree differs from a fresh build

The feed is validated before anything is written: an unexpected host, path, file kind or size stops
the build, so a malformed feed can never reach the repository.

Exit codes: 0 written or in sync, 1 out of date or the feed was refused, 2 could not run.
Python 3.9+, standard library only.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
import urllib.request

FEED_URL = "https://catalog.empiriolabs.ai/examples.json"
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
KEY_URL = "https://platform.empiriolabs.ai/dashboard/api-keys"
# The official logo files (github.com/EmpirioLabs-AI/assets), as the organization profile shows them.
LOGO_DARK = "https://raw.githubusercontent.com/EmpirioLabs-AI/assets/main/logo-dark.png"
LOGO_LIGHT = "https://raw.githubusercontent.com/EmpirioLabs-AI/assets/main/logo-white.png"
SLUG_RE = re.compile(r"^[a-z0-9][a-z0-9.-]{0,79}$")
PATH_RE = re.compile(r"^/v1/[A-Za-z0-9/_{}.:-]+$")
METHODS = {"GET", "POST", "WEBSOCKET"}
CODE_HOSTS = re.compile(r"^(https://(api\.empiriolabs\.ai|example\.com|arxiv\.org)|wss://api\.empiriolabs\.ai)$")
# kind: (file name, language)
KINDS = {
    "curl": ("request.sh", "bash"),
    "curl-submit": ("submit.sh", "bash"),
    "curl-poll": ("poll.sh", "bash"),
    "python": ("example.py", "python"),
    "python-openai": ("example.py", "python"),
    "python-websocket": ("realtime.py", "python"),
}
MODEL_FILES = {"README.md", "request.sh", "submit.sh", "poll.sh", "example.py", "example_openai.py", "realtime.py"}
MAX_MODELS = 2000
EM_DASH = "\u2014"


class FeedError(Exception):
    pass


# --- reading and validating the feed -----------------------------------------------------------------

def load_feed(source):
    if re.match(r"^https?://", source):
        request = urllib.request.Request(source, headers={"User-Agent": "EmpirioLabs-AI-examples/1.0 (+https://github.com/EmpirioLabs-AI/examples)"})
        with urllib.request.urlopen(request, timeout=60) as response:
            raw = response.read(20_000_000)
    else:
        with open(source, "rb") as handle:
            raw = handle.read()
    try:
        return json.loads(raw.decode("utf-8"))
    except ValueError as exc:
        raise FeedError("the feed is not JSON: " + str(exc))


def text(value, field, limit, required=True):
    if value is None and not required:
        return ""
    if not isinstance(value, str) or (required and not value.strip()):
        raise FeedError(field + " must be a non-empty string")
    if len(value) > limit:
        raise FeedError(field + " is longer than " + str(limit) + " characters")
    if EM_DASH in value:
        raise FeedError(field + " contains an em dash")
    if any(ord(ch) < 32 and ch not in "\n\t" for ch in value):
        raise FeedError(field + " contains a control character")
    return value


def validate(feed):
    """The models, checked field by field; FeedError on anything unexpected."""
    if not isinstance(feed, dict) or feed.get("object") != "model.examples.list":
        raise FeedError("not an examples feed (object is not model.examples.list)")
    models = feed.get("models")
    if not isinstance(models, list) or not models or len(models) > MAX_MODELS:
        raise FeedError("models must be a list of 1 to " + str(MAX_MODELS) + " entries")
    seen = set()
    out = []
    for entry in models:
        if not isinstance(entry, dict):
            raise FeedError("a model entry is not an object")
        slug = entry.get("slug")
        if not isinstance(slug, str) or not SLUG_RE.match(slug) or ".." in slug or slug in seen:
            raise FeedError("bad or repeated slug: " + repr(slug))
        seen.add(slug)
        where = "model " + slug
        endpoint = entry.get("endpoint") or {}
        method, path = endpoint.get("method"), endpoint.get("path")
        if method not in METHODS or not isinstance(path, str) or not PATH_RE.match(path):
            raise FeedError(where + ": bad endpoint " + repr(endpoint))
        links = entry.get("links") or {}
        page, docs, playground = links.get("page"), links.get("docs"), links.get("playground")
        if page != "https://empiriolabs.ai/models/" + slug:
            raise FeedError(where + ": unexpected page link " + repr(page))
        if not isinstance(docs, str) or not docs.startswith("https://docs.empiriolabs.ai/"):
            raise FeedError(where + ": unexpected docs link " + repr(docs))
        if playground is not None and playground != "https://platform.empiriolabs.ai/dashboard/playground?model=" + slug:
            raise FeedError(where + ": unexpected playground link " + repr(playground))
        blocks = entry.get("blocks")
        if not isinstance(blocks, list) or not blocks or len(blocks) > 6:
            raise FeedError(where + ": blocks must be a list of 1 to 6 entries")
        kinds = set()
        checked = []
        for block in blocks:
            kind = block.get("kind") if isinstance(block, dict) else None
            if kind not in KINDS or kind in kinds:
                raise FeedError(where + ": unknown or repeated block kind " + repr(kind))
            kinds.add(kind)
            if block.get("language") != KINDS[kind][1]:
                raise FeedError(where + ": " + kind + " is not " + KINDS[kind][1])
            code = text(block.get("code"), where + " " + kind + " code", 20000)
            for host in re.findall(r"\b(?:https?|wss?)://[A-Za-z0-9.-]+", code):
                if not CODE_HOSTS.match(host):
                    raise FeedError(where + ": " + kind + " code reaches " + host)
            checked.append({"kind": kind, "title": text(block.get("title"), where + " block title", 120), "code": code})
        out.append({
            "slug": slug,
            "name": text(entry.get("name"), where + " name", 120),
            "provider": text(entry.get("provider"), where + " provider", 120, required=False),
            "category": text(entry.get("category"), where + " category", 120, required=False) or "Other",
            "description": text(entry.get("description"), where + " description", 2000, required=False),
            "method": method,
            "path": path,
            "intro": text(entry.get("intro"), where + " intro", 4000, required=False),
            "blocks": checked,
            "page": page,
            "docs": docs,
            "playground": playground,
        })
    return out


# --- rendering ---------------------------------------------------------------------------------------

def cell(value):
    """Plain text safe in a Markdown table cell or line: no HTML, no pipe, one line."""
    return " ".join(str(value).replace("|", "\\|").replace("<", "&lt;").replace(">", "&gt;").split())


def plain(value):
    return str(value).replace("<", "&lt;").replace(">", "&gt;").strip()


def anchor(heading):
    """The id GitHub gives a heading: lowercase, punctuation dropped, spaces to hyphens."""
    return re.sub(r"[^a-z0-9 -]", "", heading.lower()).strip().replace(" ", "-")


def file_names(blocks):
    names = {}
    has_python = any(b["kind"] == "python" for b in blocks)
    for block in blocks:
        name = KINDS[block["kind"]][0]
        if block["kind"] == "python-openai" and has_python:
            name = "example_openai.py"
        names[block["kind"]] = name
    return names


def python_requirements(code):
    needs = []
    if re.search(r"^\s*import requests\b|^\s*from requests\b", code, re.M):
        needs.append("requests")
    if re.search(r"^\s*from openai import|^\s*import openai\b", code, re.M):
        needs.append("openai")
    if re.search(r"\bwebsockets\b", code):
        needs.append("websockets")
    return needs


def python_code(code):
    """The page's Python with the key read from EMPIRIOLABS_API_KEY instead of a placeholder."""
    out = code.replace('"Bearer YOUR_EMPIRIOLABS_API_KEY"', "f\"Bearer {os.environ['EMPIRIOLABS_API_KEY']}\"")
    out = out.replace('"YOUR_EMPIRIOLABS_API_KEY"', 'os.environ["EMPIRIOLABS_API_KEY"]')
    if "YOUR_EMPIRIOLABS_API_KEY" in out:
        raise FeedError("a Python example keeps a key placeholder this script cannot replace")
    if not re.search(r"^\s*import (?:[\w, ]+, )?os\b|^\s*import os\b", out, re.M):
        out = "import os\n" + out
    return out


def shell_code(code, kind):
    out = code
    if kind == "curl-poll":
        out = out.replace("/v1/jobs/JOB_ID", "/v1/jobs/${JOB_ID:?Set JOB_ID to the job_id that submit.sh returned}")
    return out


def render_file(model, block, name):
    title = model["name"] + ", " + block["title"]
    if name.endswith(".sh"):
        body = shell_code(block["code"], block["kind"])
        return "\n".join([
            "#!/usr/bin/env bash",
            "# " + title,
            "# " + model["page"],
            "set -euo pipefail",
            ": \"${EMPIRIOLABS_API_KEY:?Sign in first with login.py at the repository root, or set an API key from "
            + KEY_URL + "}\"",
            "",
            body,
            "",
        ])
    body = python_code(block["code"])
    needs = python_requirements(body)
    doc = [
        '"""' + title + ".",
        "",
        "Sign in first with login.py at the repository root, or set EMPIRIOLABS_API_KEY to an API key from",
        KEY_URL + ".",
    ]
    if needs:
        doc.append("Requires: pip install " + " ".join(needs))
    doc += [model["page"], '"""']
    return "\n".join(doc) + "\n\n" + body.rstrip("\n") + "\n"


def run_lines(model, names):
    lines = ['eval "$(python ../../login.py)"   # sign in, or: export EMPIRIOLABS_API_KEY="sk-empiriolabs-..."']
    for block in model["blocks"]:
        name = names[block["kind"]]
        if block["kind"] == "curl-poll":
            lines.append("JOB_ID=<the job_id submit.sh returned> bash " + name)
        elif name.endswith(".sh"):
            lines.append("bash " + name)
        else:
            needs = python_requirements(python_code(block["code"]))
            lines.append(("pip install " + " ".join(needs) + " && " if needs else "") + "python " + name)
    return lines


def render_model_readme(model, names, files):
    lines = ["# " + plain(model["name"]) + " API examples", ""]
    if model["description"]:
        lines += [plain(model["description"]), ""]
    if model["intro"]:
        lines += [plain(model["intro"]), ""]
    lines += [
        "| | |",
        "| --- | --- |",
        "| Model id | `" + model["slug"] + "` |",
    ]
    if model["provider"]:
        lines.append("| Provider | " + cell(model["provider"]) + " |")
    lines += [
        "| Category | " + cell(model["category"]) + " |",
        "| Endpoint | `" + model["method"] + " " + model["path"] + "` |",
        "",
        "## Run",
        "",
        "```bash",
    ] + run_lines(model, names) + ["```", ""]
    for block in model["blocks"]:
        name = names[block["kind"]]
        language = "bash" if name.endswith(".sh") else "python"
        lines += ["## " + plain(block["title"]), "", "[`" + name + "`](" + name + ")", "", "```" + language,
                  files[name].rstrip("\n"), "```", ""]
    lines += ["## Links", "", "- [" + cell(model["name"]) + " pricing and specs](" + model["page"] + ")",
              "- [" + cell(model["name"]) + " API reference](" + model["docs"] + ")"]
    if model["playground"]:
        lines.append("- [Try " + cell(model["name"]) + " in the Playground](" + model["playground"] + ")")
    lines += ["", "[All EmpirioLabs AI examples](../../README.md)"]
    return "\n".join(lines) + "\n"


def render_index(models):
    by_category = {}
    for model in models:
        by_category.setdefault(model["category"], []).append(model)
    categories = sorted(by_category, key=lambda c: c.lower())
    headings = [cell(c) + " (" + str(len(by_category[c])) + ")" for c in categories]
    lines = [
        '<div align="center">',
        "",
        '<a href="https://empiriolabs.ai">',
        "  <picture>",
        '    <source media="(prefers-color-scheme: dark)" srcset="' + LOGO_LIGHT + '" />',
        '    <img src="' + LOGO_DARK + '" alt="EmpirioLabs AI" width="280" />',
        "  </picture>",
        "</a>",
        "",
        "# EmpirioLabs AI API examples",
        "",
        "Runnable cURL and Python for every model in the EmpirioLabs AI catalog.",
        "",
        "<p>",
        '  <a href="https://empiriolabs.ai/models"><img alt="' + str(len(models)) + ' models" src="https://img.shields.io/badge/Models-'
        + str(len(models)) + '-1f6feb?style=flat-square"></a>',
        '  <a href="https://docs.empiriolabs.ai/welcome"><img alt="Documentation" src="https://img.shields.io/badge/Docs-docs.empiriolabs.ai-0a66c2?style=flat-square"></a>',
        '  <a href="' + KEY_URL + '"><img alt="Get an API key" src="https://img.shields.io/badge/API%20key-Get%20one-0b8a5a?style=flat-square"></a>',
        '  <a href="LICENSE"><img alt="License: MIT-0" src="https://img.shields.io/badge/License-MIT--0-555555?style=flat-square"></a>',
        "</p>",
        "",
        "</div>",
        "",
        "One folder per model on [EmpirioLabs AI](https://empiriolabs.ai), with the same code as the model's page on "
        "empiriolabs.ai. The repository is generated from the live model catalog and kept in sync automatically, so new "
        "models are added without manual updates.",
        "",
        "## Get started",
        "",
        "1. Sign in with your browser, no key to copy: `eval \"$(python login.py)\"` (PowerShell: "
        "`python login.py --powershell | iex`). The connection appears in Settings > Connected applications, where "
        "Disconnect revokes it.",
        "2. Or create an API key at " + KEY_URL + " and set it: `export EMPIRIOLABS_API_KEY=\"sk-empiriolabs-...\"`.",
        "3. Open a model's folder and run a file, for example `bash models/kimi-k3/request.sh`, or follow the folder's README.",
        "",
        "Requests are billed to your EmpirioLabs AI account at each model's listed price (https://empiriolabs.ai/pricing).",
        "",
        "## Models",
        "",
        str(len(models)) + " models in " + str(len(by_category)) + " categories: "
        + ", ".join("[" + cell(c) + "](#" + anchor(h) + ")" for c, h in zip(categories, headings)) + ".",
        "",
    ]
    for category, heading in zip(categories, headings):
        rows = sorted(by_category[category], key=lambda m: (m["name"].lower(), m["slug"]))
        lines += [
            "### " + heading,
            "",
            "| Model | Provider | Endpoint | Examples |",
            "| --- | --- | --- | --- |",
        ]
        for model in rows:
            lines.append("| [" + cell(model["name"]) + "](" + model["page"] + ") | " + cell(model["provider"]) + " | `"
                         + model["method"] + " " + model["path"] + "` | [models/" + model["slug"] + "](models/" + model["slug"] + ") |")
        lines.append("")
    lines += [
        "## How this repository is generated",
        "",
        "A scheduled workflow reads the public examples feed (" + FEED_URL + ") every hour, regenerates `README.md` "
        "and `models/` with `scripts/build_examples.py`, and commits any change. Edits to those files are overwritten; "
        "to report a problem with an example, open an issue.",
        "",
        "## More from EmpirioLabs AI",
        "",
        "- [Documentation](https://docs.empiriolabs.ai)",
        "- [Model catalog and pricing](https://empiriolabs.ai/models)",
        "- [Playground](https://platform.empiriolabs.ai/dashboard/playground)",
        "- [Agent skills](https://github.com/EmpirioLabs-AI/skills)",
        "- [Remote MCP server](https://github.com/EmpirioLabs-AI/mcp)",
        "",
        "## License",
        "",
        "MIT No Attribution (MIT-0): copy the code into your own projects without attribution. See [LICENSE](LICENSE).",
        "",
    ]
    return "\n".join(lines)


def build(models):
    """{relative path: text} for README.md and every model folder."""
    files = {"README.md": render_index(models)}
    for model in models:
        names = file_names(model["blocks"])
        own = {}
        for block in model["blocks"]:
            own[names[block["kind"]]] = render_file(model, block, names[block["kind"]])
        own["README.md"] = render_model_readme(model, names, own)
        for name, content in own.items():
            files["models/" + model["slug"] + "/" + name] = content
    for path, content in files.items():
        if EM_DASH in content:
            raise FeedError(path + " would contain an em dash")
    return files


# --- writing -----------------------------------------------------------------------------------------

def existing(out):
    found = set()
    if os.path.isfile(os.path.join(out, "README.md")):
        found.add("README.md")
    models_dir = os.path.join(out, "models")
    if os.path.isdir(models_dir):
        for current, _dirs, names in os.walk(models_dir):
            for name in names:
                found.add(os.path.relpath(os.path.join(current, name), out).replace(os.sep, "/"))
    return found


def read(path):
    with open(path, "rb") as handle:
        return handle.read()


def check(out, files):
    problems = [p for p, c in sorted(files.items())
                if not os.path.isfile(os.path.join(out, *p.split("/"))) or read(os.path.join(out, *p.split("/"))) != c.encode("utf-8")]
    problems += sorted(p + " (not in the build)" for p in existing(out) - set(files))
    return problems


def write(out, files):
    for path in sorted(existing(out) - set(files)):
        os.remove(os.path.join(out, *path.split("/")))
    models_dir = os.path.join(out, "models")
    if os.path.isdir(models_dir):
        for current, dirs, _names in os.walk(models_dir, topdown=False):
            for d in dirs:
                if not os.listdir(os.path.join(current, d)):
                    os.rmdir(os.path.join(current, d))
    for path, content in sorted(files.items()):
        target = os.path.join(out, *path.split("/"))
        os.makedirs(os.path.dirname(target) or out, exist_ok=True)
        with open(target, "wb") as handle:
            handle.write(content.encode("utf-8"))


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--feed", default=FEED_URL, help="feed URL or file (default: the live feed)")
    parser.add_argument("--out", default=ROOT, help="repository root to write (default: this repository)")
    parser.add_argument("--check", action="store_true", help="compare instead of writing")
    args = parser.parse_args(argv)
    try:
        models = validate(load_feed(args.feed))
        files = build(models)
    except FeedError as exc:
        print("build_examples: refused the feed: " + str(exc), file=sys.stderr)
        return 1
    except OSError as exc:
        print("build_examples: " + str(exc), file=sys.stderr)
        return 2
    out = os.path.abspath(args.out)
    if args.check:
        problems = check(out, files)
        if problems:
            print("build_examples: out of date: " + ", ".join(problems[:20]) + (" and more" if len(problems) > 20 else ""), file=sys.stderr)
            return 1
        print("build_examples: " + str(len(models)) + " models, " + str(len(files)) + " files in sync")
        return 0
    write(out, files)
    print("build_examples: wrote " + str(len(models)) + " models, " + str(len(files)) + " files")
    return 0


if __name__ == "__main__":
    sys.exit(main())
