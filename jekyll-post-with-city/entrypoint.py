#!/usr/bin/env python3
"""
jekyll_post_with_city — Entrypoint (v2)

Usage:
  python3 entrypoint.py --city "Maros" \\
      --template templates/TEMPLATE--post-with-city.md \\
      --output _post_with_city/2026-06-29-jual-kayu-dolken-maros.md

Pipeline: Research -> Writer -> Editor -> Reviewer -> Output .md

Changes from v1:
- Mengimpor implementasi agent dari scripts/*.py (sebelumnya duplikat inline).
- template kosong: Writer hanya substitusi placeholder generik kota. Section
  fields dibiarkan kosong untuk diisi via workflow REPORT -> FIX manual.
- Editor REJECT (exit nonzero) bila ada placeholder leak, bukan hanya WARNING.
- Reviewer parse YAML frontmatter deklaratif, deteksi field required kosong.
- --skip-research benar-benar skip spawn sub-agent: load cache saja.
- Bug C3 diperbaiki: tidak lagi menyalahgunakan hermes_tools.execute_code
  sebagai LLM prompt. Research agent hanya dukung mode: (a) cache JSON,
  (b) fallback fail-loud dengan pesan jelas.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import subprocess
import sys
from datetime import date
from pathlib import Path

SCRIPT_DIR = Path(__file__).parent / "scripts"
if SCRIPT_DIR.exists():
    sys.path.insert(0, str(SCRIPT_DIR))

# Import dari scripts/*.py agar tidak duplikat
import writer_agent  # noqa: E402
import editor_agent  # noqa: E402
import reviewer_agent  # noqa: E402
import research_agent  # noqa: E402


# ---------------------------------------------------------------------------
# Research runner — fail-loud tanpa hermes_tools.execute_code misuse
# ---------------------------------------------------------------------------

def run_research(city: str, skip_agent: bool = False) -> dict:
    """Kumpulkan data kota untuk pengisian template.

    Sumber yang didukung:
      1. Cache JSON di /tmp/research-output/{city}.json (disiapkan manual
         atau oleh delegate_task sebelum panggil entrypoint)
      2. --skip-research: paksa pakai cache tanpa spawn sub-agent

    Returns:
        dict data kota.
    Raises:
        FileNotFoundError bila skip_agent=True dan cache tidak ada.
    """
    print(f"[Research] Gathering data for: {city}")
    return research_agent.research(city, skip_agent=skip_agent)


# ---------------------------------------------------------------------------
# Main CLI
# ---------------------------------------------------------------------------

def main() -> None:
    parser = argparse.ArgumentParser(prog="jekyll-post-with-city")
    parser.add_argument("--city", required=True, help="Target kota/kabupaten")
    parser.add_argument(
        "--template",
        default="templates/TEMPLATE--post-with-city.md",
        help="Path ke TEMPLATE--post-with-city.md",
    )
    parser.add_argument(
        "--output", required=True,
        help="Path output .md (mis. _post_with_city/YYYY-MM-DD-jual-kayu-dolken-{kota}.md)"
    )
    parser.add_argument(
        "--skip-research", action="store_true",
        help="Skip Research Agent — load cache /tmp/research-output/{city}.json saja",
    )
    args = parser.parse_args()

    today = date.today().isoformat()

    print("=== jekyll-post-with-city (v2) ===")
    print(f"City:     {args.city}")
    print(f"Template: {args.template}")
    print(f"Output:   {args.output}")
    print(f"Date:     {today}")
    print("=" * 30)

    # Step 1: Research (cache-only fallback)
    try:
        data = run_research(args.city, skip_agent=args.skip_research)
    except FileNotFoundError as e:
        print(f"[ERROR] Research data tidak tersedia: {e}")
        print(
            "[HINT] Jalankan delegate_task sebagai Research sub-agent dulu, "
            "atau bekukan JSON ke /tmp/research-output/%s.json" % args.city
        )
        sys.exit(1)

    # Step 2: Writer — substitusi placeholder generik
    draft = writer_agent.write(args.city, args.template, args.output)

    # Step 3: Editor
    edited_path, clean = editor_agent.edit(draft)
    if not clean:
        print("[ERROR] Editor REJECT — selesaikan placeholder dulu.")
        sys.exit(1)

    # Step 4: Reviewer
    if not reviewer_agent.review(edited_path, city=args.city):
        print("[ERROR] Reviewer REJECTED.")
        sys.exit(1)

    # Finalize: copy edited -> output
    final_content = Path(edited_path).read_text(encoding="utf-8")
    Path(args.output).write_text(final_content, encoding="utf-8")
    print(f"\n[OK] OUTPUT: {args.output}")

    # Print follow-up next steps
    slug_city = re.sub(r"\s+", "", args.city.strip().lower())
    print("\nNext steps:")
    print(f"  1. Siapkan images: assets/images/posts/jual-kayu-dolken-{slug_city}/001-004.webp")
    print(f"  2. Isi frontmatter meta (title/description/excerpt/date) — sekarang kosong")
    print(f"  3. Isi section fields satu per satu via REPORT -> WAIT -> FIX (lihat SKILL.md)")
    print(f"  4. Build: bundle exec jekyll build 2>&1 | tail -20")
    print(f"  5. Commit: git add {args.output} && git commit -m 'Add post for {args.city}'")


if __name__ == "__main__":
    main()