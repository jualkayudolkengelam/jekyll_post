# Multi‑Agent Pipeline for Jekyll Post Generation

## Pipeline Overview

```
Input (Nama Kota)
     ↓
[Research] → data.json          (cari luas, populasi, sejarah, ekonomi, wisata, kuliner)
     ↓
[Writer]   → draft.md            (isi template, semua field YAML)
     ↓
[Editor]   → polished.md         (validasi YAML, perbaiki bahasa, hapus placeholder)
     ↓
[Reviewer] → APPROVED / REJECT   (bandingkan dengan template, cek kelengkapan)
     ↓
Git Commit & Push
```

## Agent Roles

| Agent | Input | Output | Tools | Tokens |
|-------|-------|--------|-------|--------|
| Research | Nama kota | `data.json` | web, terminal, file | High (web search) |
| Writer | `data.json` + template | `draft.md` | file | Medium |
| Editor | `draft.md` | `polished.md` | file, terminal | Low |
| Reviewer | `polished.md` + template | `APPROVED`/`REJECT` | file | Low |

## Entrypoint Script (Generic)

```python
#!/usr/bin/env python3
"""entrypoint.py — reusable across Hermes, Claude Code, GitHub Actions, etc."""
import argparse, json, subprocess, sys
from pathlib import Path

def main():
    parser = argparse.ArgumentParser(prog="jekyll-post-with-city")
    parser.add_argument("--city", required=True)
    parser.add_argument("--template", required=True)
    parser.add_argument("--output", required=True)
    parser.add_argument("--format", choices=["json", "md"], default="md")
    args = parser.parse_args()

    # 1. RESEARCH — spawn a sub‑agent or call external API
    data = research(args.city)

    # 2. WRITER — fill template with data
    template_text = Path(args.template).read_text()
    filled = fill_template(template_text, data)

    # 3. EDITOR — validate YAML & polish
    polished = edit(filled)

    # 4. REVIEWER — final check
    if review(polished):
        Path(args.output).write_text(polished)
        print(f"✓ Written to {args.output}")
    else:
        print("✗ Review rejected. Fix before commit.")
        sys.exit(1)

    if args.format == "json":
        print(json.dumps(data, ensure_ascii=False, indent=2))
```

## Calling from Different Agents

| Agent | Command |
|-------|---------|
| **Hermes** | `hermes skill run jekyll-post-with-city --param city="Maros"` |
| **Claude Code** | `claude-code-tools run-skill --skill-path ~/.hermes/skills/jekyll/jekyll-post-with-city --param city="Maros"` |
| **Bash/CI** | `python3 entrypoint.py --city "Maros" --template "TEMPLATE.md" --output "post.md"` |
| **GitHub Actions** | `run: python3 entrypoint.py --city "Maros" --template "..." --output "..."` |

## Token Efficiency

| Approach | Tokens per Post |
|----------|-----------------|
| Single prompt (full pipeline) | ~120K–200K |
| Multi‑agent (4 separate calls) | ~60K–100K |
| Multi‑agent with `data.json` reuse | ~40K–60K |

Research step is the most expensive; its JSON output is reused by Writer/Editor/Reviewer without re‑researching.
