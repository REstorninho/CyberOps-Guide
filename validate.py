#!/usr/bin/env python3
"""
validate.py — integrity gate for CyberOps.html

Runs the checks documented in CLAUDE.md §3/§6 in one pass:
  1. Each data array extracts cleanly (bracket-matching) and parses.
  2. JS syntax is valid (node --check on the extracted <script> block).
  3. Cross-references hold: (cat, name) unique, cat exists, tags exist,
     {VARS} used exist in VAR_DEFS, install field is well-formed.

Exit code 0 = all good, 1 = at least one error. Warnings never fail the
build but are printed for review.

Usage:
    python3 validate.py            # validate ./CyberOps.html
    python3 validate.py path.html  # validate a specific file
"""

import json
import os
import re
import subprocess
import sys
import tempfile

HTML_DEFAULT = os.path.join(os.path.dirname(__file__), "CyberOps.html")

# install values that are accepted verbatim (besides https:// URLs and
# literal install commands such as "pip3 install x").
NATIVE_INSTALLS = {
    "native://windows",
    "native://linux",
    "native://cisco",
    "native://manual",
}

errors = []
warnings = []


def err(msg):
    errors.append(msg)


def warn(msg):
    warnings.append(msg)


def find_array(html, varname):
    """Return (start, end) byte offsets of the [...] literal after `varname`.

    Walks characters tracking string/escape/bracket-depth so embedded
    brackets and quotes inside string values do not throw the parser off.
    """
    i = html.index(varname)
    start = html.index("[", i)
    depth = 0
    in_str = False
    esc = False
    for j in range(start, len(html)):
        c = html[j]
        if in_str:
            if esc:
                esc = False
            elif c == "\\":
                esc = True
            elif c == '"':
                in_str = False
        else:
            if c == '"':
                in_str = True
            elif c == "[":
                depth += 1
            elif c == "]":
                depth -= 1
                if depth == 0:
                    return start, j + 1
    raise ValueError(f"unterminated array literal for {varname!r}")


def load_json_array(html, varname):
    start, end = find_array(html, varname)
    return json.loads(html[start:end])


def extract_var_def_keys(html):
    """VAR_DEFS uses JS literals ({k:'X',...}); pull keys via regex."""
    start, end = find_array(html, "var VAR_DEFS=")
    body = html[start:end]
    return set(re.findall(r"k:\s*'([A-Z0-9_]+)'", body))


def extract_tag_map_keys(html):
    """TAG_MAP uses unquoted keys + // comments; each entry is `key:{l:...}`."""
    i = html.index("var TAG_MAP=")
    start = html.index("{", i)
    depth = 0
    end = None
    for j in range(start, len(html)):
        c = html[j]
        if c == "{":
            depth += 1
        elif c == "}":
            depth -= 1
            if depth == 0:
                end = j + 1
                break
    body = html[start:end]
    return set(re.findall(r"(\w+)\s*:\s*\{l:", body))


def check_js_syntax(html):
    m = re.search(r"<script>(.*)</script>", html, re.S)
    if not m:
        err("could not locate a <script>...</script> block")
        return
    with tempfile.NamedTemporaryFile(
        "w", suffix=".js", delete=False, encoding="utf-8"
    ) as f:
        f.write(m.group(1))
        path = f.name
    try:
        r = subprocess.run(
            ["node", "--check", path], capture_output=True, text=True
        )
        if r.returncode != 0:
            err("node --check failed:\n" + (r.stderr or r.stdout).strip())
        else:
            print("  node --check: SYNTAX_OK")
    except FileNotFoundError:
        warn("node not found — skipping JS syntax check")
    finally:
        os.unlink(path)


def main():
    path = sys.argv[1] if len(sys.argv) > 1 else HTML_DEFAULT
    if not os.path.isfile(path):
        print(f"error: file not found: {path}", file=sys.stderr)
        return 2

    html = open(path, encoding="utf-8").read()
    print(f"Validating {path}\n")

    if "\r\n" in html:
        err("file contains CRLF line endings (must be LF only)")

    # --- parse the JSON arrays ---
    try:
        commands = load_json_array(html, "var COMMANDS=")
        print(f"  COMMANDS:     {len(commands)} entries")
    except Exception as e:
        err(f"COMMANDS failed to parse: {e}")
        commands = []

    try:
        categories = load_json_array(html, "var CATEGORIES=")
        print(f"  CATEGORIES:   {len(categories)} entries")
    except Exception as e:
        err(f"CATEGORIES failed to parse: {e}")
        categories = []

    try:
        tools = load_json_array(html, "var ONLINE_TOOLS=")
        print(f"  ONLINE_TOOLS: {len(tools)} entries")
    except Exception as e:
        err(f"ONLINE_TOOLS failed to parse: {e}")
        tools = []

    var_keys = extract_var_def_keys(html)
    tag_keys = extract_tag_map_keys(html)
    print(f"  VAR_DEFS:     {len(var_keys)} variables")
    print(f"  TAG_MAP:      {len(tag_keys)} tags")

    cat_ids = {c["id"] for c in categories}

    print("\nJS syntax:")
    check_js_syntax(html)

    # --- cross-reference checks on COMMANDS ---
    print("\nCross-reference checks:")
    seen = {}
    var_re = re.compile(r"\{([A-Z][A-Z0-9_]*)\}")
    for n, c in enumerate(commands):
        label = f"COMMANDS[{n}] {c.get('cat','?')}::{c.get('name','?')!r}"

        for field in ("cat", "name", "cmd", "install", "tags"):
            if field not in c:
                err(f"{label}: missing field {field!r}")

        key = (c.get("cat"), c.get("name"))
        if key in seen:
            err(f"{label}: duplicate (cat, name) — also at index {seen[key]}")
        else:
            seen[key] = n

        if c.get("cat") and c["cat"] not in cat_ids:
            err(f"{label}: cat {c['cat']!r} not in CATEGORIES")

        for t in c.get("tags", []):
            if t not in tag_keys:
                err(f"{label}: tag {t!r} not in TAG_MAP")

        # exactly one severity
        sev = [t for t in c.get("tags", []) if t in
               ("critical", "high", "medium", "low")]
        if len(sev) != 1:
            warn(f"{label}: expected exactly one severity tag, found {sev}")

        # OS sanity: PowerShell/CMD content tagged lin but not win
        cmd = c.get("cmd", "")
        tags = c.get("tags", [])
        looks_windows = bool(re.search(
            r"\b(Get-|Set-|New-|Resolve-DnsName|powershell|Connect-Exchange"
            r"|Format-Table|Where-Object|Select-Object)\b", cmd))
        if looks_windows and "lin" in tags and "win" not in tags:
            warn(f"{label}: looks like Windows/PowerShell but tagged 'lin'")

        # placeholders must exist in VAR_DEFS
        for v in set(var_re.findall(cmd)):
            if v not in var_keys:
                warn(f"{label}: uses {{{v}}} not defined in VAR_DEFS")

        # install well-formed
        inst = c.get("install", "")
        if inst and not (
            inst in NATIVE_INSTALLS
            or inst.startswith("http")
            or " " in inst  # literal install command, e.g. "pip3 install x"
        ):
            warn(f"{label}: unusual install value {inst!r}")

    # --- ONLINE_TOOLS basic shape ---
    tool_seen = {}
    for n, t in enumerate(tools):
        for field in ("cat", "name", "url", "desc", "tags"):
            if field not in t:
                err(f"ONLINE_TOOLS[{n}]: missing field {field!r}")
        key = (t.get("cat"), t.get("name"))
        if key in tool_seen:
            err(f"ONLINE_TOOLS[{n}] {t.get('name')!r}: duplicate (cat, name)")
        else:
            tool_seen[key] = n
        if t.get("url") and not t["url"].startswith("http"):
            warn(f"ONLINE_TOOLS[{n}] {t.get('name')!r}: url not http(s)")

    if not errors:
        print("  no cross-reference errors")

    # --- report ---
    print()
    if warnings:
        print(f"{len(warnings)} warning(s):")
        for w in warnings:
            print(f"  ! {w}")
        print()
    if errors:
        print(f"FAILED — {len(errors)} error(s):")
        for e in errors:
            print(f"  ✗ {e}")
        return 1

    print("PASSED — all checks green.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
