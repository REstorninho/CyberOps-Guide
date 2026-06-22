# CLAUDE.md

Guidance for AI agents (and humans) working in this repository. Read this **before** editing any file — the data-editing workflow has non-obvious failure modes documented below.

---

## 1. What this project is

**CYBER_OPS Terminal** is a single-file, offline, zero-dependency security cheat-sheet web app. The entire application — markup, CSS, ~1400 command entries, ~100 online tools, and all runtime JavaScript — lives in **one file**: `CyberOps.html` (~780 KB, ~1300 lines).

- **No build step.** No `npm install`, no bundler, no transpiler, no framework.
- **No runtime dependencies.** Open `CyberOps.html` in any browser; it works offline.
- **No backend.** All state is in-memory + browser `localStorage`.
- **Language of the project:** UI strings, command descriptions, and commit/PR prose are in **Portuguese (pt-PT)**. Match this when adding content.

```
CyberOps-Guide/
├── CyberOps.html              ← the entire application (data + UI + logic)
├── validate.py               ← integrity gate (run before every commit)
├── README.md                 ← user-facing docs + live statistics (keep in sync)
├── CLAUDE.md                 ← this file
└── .github/workflows/
    └── validate.yml          ← CI: runs validate.py on push/PR
```

---

## 2. Architecture of `CyberOps.html`

The file is, in order: `<head>` (inline `<style>`), `<body>` (static markup for panels/modals), then **two `<script>` tags**. The data arrays and all logic are in the script block(s) as plain `var` declarations.

### Global data arrays (the "database")
These are large JS array/object literals. **Each is stored as a single, extremely long line** — this matters (see §3).

| Symbol | Shape | Purpose |
|---|---|---|
| `COMMANDS` | `[{cat, name, tags[], cmd, install}]` | The cheat sheets (~1436 entries). |
| `CATEGORIES` | `[{id, label, team, glyph}]` | 42 categories (41 real + `id:"all"` "All Ops"). |
| `ONLINE_TOOLS` | `[{cat, name, url, desc, tags[]}]` | Web tools (~102 entries). |
| `VAR_DEFS` | `[{k, ph, grp}]` | 29 session variables (`{KEY}` placeholders). |
| `TAG_MAP` | `{tag: {l, c}}` | Tag → display label + CSS class. |
| `TEAM_CATS` / `TEAM_MAP` | mappings | Team filter → category membership. |
| `TOOL_TAGS` / `TOOL_CATS` | mappings | Online-tools domain tags + category labels. |
| `CAT_COUNTS` | `{}` | Computed at runtime; do not hand-edit. |

### Key runtime functions
| Function | Role |
|---|---|
| `sub(cmd)` | Substitutes `{VAR}` placeholders with session values before copy. |
| `hlCmd(cmd)` | Syntax-highlights a command; renders filled/unfilled placeholders. |
| `_renderGrid()` / `renderGrid()` | Builds command cards (debounced). Each card carries `data-key="cat::name"`. |
| `getFiltered()` | Applies active category/OS/search filters to `COMMANDS`. |
| `buildVars()` | Renders the SESSION_VARIABLES panel (free-text search + click-to-filter). |
| `filterVarsByCommand(entry)` | Extracts `{VAR}`s from a command and filters the vars panel to just those. |
| `doCopy(entry)` | Copies with CRLF normalization + trailing newline (PowerShell paste-safe). |
| `buildNav` / `renderTools` / `buildHistList` / `showInstall` | Navigation, online-tools view, history, install modal. |

### Card identity
A command's canonical key is **`cat + '::' + name`**. This is used for favourites, the copy/fav/install dispatch, and click-to-filter. The combination `(cat, name)` must therefore be **unique**.

---

## 3. ⚠️ Editing the data arrays — read this carefully

The data arrays are minified onto single lines containing embedded brackets, quotes, and escaped characters inside string values (e.g. PowerShell `{...}` blocks live inside `cmd` strings). **Naive regex extraction and naive string insertion both break.** Use the established Python workflow.

### Reliable extraction (bracket-matching, then `json.loads`)
Walk characters tracking string/escape/bracket-depth to find the exact array bounds:

```python
def find_array(html, varname):           # e.g. 'var COMMANDS='
    i = html.index(varname)
    start = html.index('[', i)
    depth = 0; in_str = False; esc = False; end = None
    for j in range(start, len(html)):
        c = html[j]
        if in_str:
            if esc: esc = False
            elif c == '\\': esc = True
            elif c == '"': in_str = False
        else:
            if c == '"': in_str = True
            elif c == '[': depth += 1
            elif c == ']':
                depth -= 1
                if depth == 0:
                    end = j + 1; break
    return start, end
```

Then `json.loads(html[start:end])` gives you a real Python list to inspect/count.

### Reliable insertion
Build new entries as a JSON array, then splice them in **before the closing `]`**:

```python
new = json.load(open('/tmp/new_entries.json'))
start, end = find_array(html, 'var COMMANDS=')
inner = json.dumps(new, ensure_ascii=False)
assert inner[0] == '[' and inner[-1] == ']'        # guard against stray brackets
html = html[:end-1] + ',' + inner[1:-1] + html[end-1:]
```

> **Past bug:** writing entries to a temp file and slicing `[1:-1]` on the raw read left a trailing newline, so `[1:-1]` stripped `[` and `\n` instead of `[` and `]`, producing a stray `]` and a `]];` double-close. **Always `.strip()` and assert the first/last chars are `[`/`]` before slicing.**

### Mandatory validation gate (run BEFORE every commit)
**Run `python3 validate.py` — it performs the whole gate in one pass** and exits non-zero on any error:
- Bracket-matches and parses every data array (`COMMANDS`, `CATEGORIES`, `ONLINE_TOOLS`) and prints counts.
- `node --check` on the extracted `<script>` block (JS syntax).
- Cross-references: `(cat, name)` uniqueness, `cat` exists in `CATEGORIES`, every tag exists in `TAG_MAP`, install field well-formed, CRLF rejection.
- Warnings (non-failing): missing/duplicate severity, `{VARS}` not in `VAR_DEFS`, Windows-looking commands tagged `lin`.

The same script runs in CI on every push/PR (`.github/workflows/validate.yml`). Errors **fail the build**; warnings are advisory. New unknown tags must be added to `TAG_MAP` (+ a `.tag-x` CSS class) or they render as invisible badges — the validator will flag them as errors.

The two underlying manual checks (if you ever need them standalone):
1. **JSON validity** — re-extract each touched array with the bracket matcher and `json.loads()` it; confirm the new count.
2. **JS syntax** — extract the `<script>` content and run `node --check`:
   ```bash
   python3 -c "import re;h=open('CyberOps.html',encoding='utf-8').read();\
   m=re.search(r'<script>(.*)</script>',h,re.S);\
   open('/tmp/check.js','w',encoding='utf-8').write(m.group(1))"
   node --check /tmp/check.js && echo SYNTAX_OK
   ```
   (The file has two `<script>` tags; the regex above is greedy and captures the data/logic block. Confirm `SYNTAX_OK`.)

### Do NOT
- Do **not** use `grep`/`sed` to count or rewrite categories or entries — single-line minification and `"cat":"x"` vs `"cat": "x"` spacing differences cause silent miscounts. Use the Python extractor for any statistic.
- Do **not** close `</script>` inside a JS string literal (it terminates the block early). Escape or split if a command legitimately contains it.
- Do **not** introduce CRLF into the file; the copy path already converts to CRLF at runtime.

---

## 4. Data schemas & conventions

### A command entry
```json
{
  "cat": "adattack",
  "name": "Kerberoasting — request TGS",
  "tags": ["critical", "ad", "lin"],
  "cmd": "GetUserSPNs.py {DOMAIN}/{USER}:{PASS} -dc-ip {DC} -request -outputfile kerb.hash",
  "install": "https://github.com/fortra/impacket"
}
```

- **`cat`** must be an existing `CATEGORIES[].id`. Don't invent categories without also adding them to `CATEGORIES` and the team mappings.
- **`name`** — concise, Portuguese, `Tool — what it does` style. Unique within its `cat`.
- **`tags`** — drawn from `TAG_MAP` keys only. Conventions:
  - Severity (pick one): `critical | high | medium | low` (cards sort by this order).
  - OS: `win` and/or `lin` (use `win` for PowerShell/CMD — a frequent past bug was Windows commands tagged `lin`).
  - Meta: `new`, `osep`. Domain: `recon web creds lateral privesc persist evasion misconfig audit cve forensics network cloud ssl threat exploit`, plus `ad`.
- **`cmd`** — multi-line uses `\n` (real newlines in the JSON string). Use `{VAR}` placeholders that exist in `VAR_DEFS` where possible.
- **`install`** — one of: `native://windows`, `native://linux`, `native://cisco`, `native://manual`, a `https://…` URL, or a literal install command (e.g. `pip3 install x`).

### Session variables (`VAR_DEFS`)
`{k, ph, grp}` — key, placeholder example, group. Add a new variable only when a placeholder is used meaningfully across multiple commands; otherwise reuse an existing one. When the **count of `VAR_DEFS` changes**, update the two hard-coded `/29` strings in the VARS button (search the file for `/29`) and the README.

---

## 5. Keeping README.md in sync

`README.md` publishes live statistics that **must match** the actual data: total commands, online-tools count, per-team category counts, `VAR_DEFS` count, and the `COMMANDS[]`/`ONLINE_TOOLS[]` array-size notes. After any data change, recompute counts with the Python extractor (group `COMMANDS` by `cat`, map `cat → team` via `CATEGORIES`) and update:
- The overview line and the `CYBER_OPS_TERMINAL` banner block.
- The per-team category tables (🔴 RED / 🔵 BLUE / 🚨 IR / ⚙ SYSOPS / ⌬ NEUTRAL).
- The "Estrutura Técnica" array-size comments.
- Add a milestone bullet under **Desenvolvimento** describing the change.

> Note: Online Tools use a **separate** category set (`recon_osint, dns, ssl, web_sec, …`) that has zero entries in `COMMANDS`. Never conflate the two when counting the 41 command categories.

---

## 6. Testing & verification

There is **no headless browser** available in this environment. Automated verification is `python3 validate.py` (also wired into CI), which covers:
1. `node --check` on the extracted script (syntax).
2. Python `json.loads()` on each touched array (data validity + counts).
3. Cross-reference integrity (unique keys, valid cats/tags, install format).

UI/interaction behaviour **cannot be exercised here** — review the relevant JS by hand and **say so explicitly** rather than claiming a visual test occurred. When a change is purely behavioural (e.g. click handlers), describe what you reasoned through.

---

## 7. Git & GitHub workflow

- **Branch:** develop on `claude/loving-pasteur-tlb2jb`. Never force-push. Never push to another branch without explicit permission.
- **Push:** `git push -u origin claude/loving-pasteur-tlb2jb`. Retry transient network failures with backoff.
- **Commits:** clear, imperative subject; body explaining the *why*. Footer:
  ```
  Co-Authored-By: Claude <noreply@anthropic.com>
  Claude-Session: <session url>
  ```
- **PRs:** the maintainer (`REstorninho`) frequently opens and merges PRs from this branch via the GitHub UI as work is pushed, so `main` may already contain your commits — check `list_commits` on `main` before assuming a PR is needed. **Do not open a PR unless explicitly asked.** GitHub access is via the `mcp__github__*` tools (no `gh` CLI); scope is limited to `restorninho/cyberops-guide`.

---

## 8. Quick recipe — add new commands

1. Write the entries to `/tmp/new_entries.json` (valid JSON array; pt-PT names; valid `cat`/`tags`/`install`).
2. Splice into `COMMANDS` with the bracket-match + assert-then-slice insertion (§3).
3. Validate: re-extract + `json.loads` (confirm new count) **and** `node --check` (confirm `SYNTAX_OK`).
4. Recompute statistics and update `README.md` (§5), including a Desenvolvimento milestone.
5. Commit (with footer) and push to the working branch. Do not open a PR unless asked.
