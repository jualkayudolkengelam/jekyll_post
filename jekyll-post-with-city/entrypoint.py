#!/usr/bin/env python3
"""
jekyll_post_with_city — Entrypoint

Usage:
  python3 entrypoint.py --city "Maros" --template "TEMPLATES/TEMPLATE--post-with-city.md" --output "_post_with_city/2026-06-29-jual-kayu-dolken-maros.md"

Workflow: Research → Writer → Editor → Reviewer → Output .md
Requires: Python 3.9+, internet (for Research step)
Compatible with: Hermes, Claude Code, any LLM agent that runs shell commands.
"""

import argparse
import json
import os
import sys
from datetime import date
from pathlib import Path

# Add scripts/ to path so we can import agent modules
SCRIPT_DIR = Path(__file__).parent / "scripts"
if SCRIPT_DIR.exists():
    sys.path.insert(0, str(SCRIPT_DIR))

# ---------------------------------------------------------------------------
# Template filler (no external deps — pure stdlib)
# ---------------------------------------------------------------------------

def fill_template(template: str, data: dict) -> str:
    """Replace {key} placeholders in template with values from data dict.
    Supports dot-notation: {key.subkey} → data["key"]["subkey"]
    Supports list access: {list.0.field} → data["list"][0]["field"]
    """
    import re

    def resolve(data_dict, key):
        parts = key.split(".")
        val = data_dict
        for p in parts:
            if isinstance(val, list) and p.isdigit():
                val = val[int(p)]
            elif isinstance(val, dict):
                val = val.get(p, "")
            else:
                return ""
        return str(val) if val is not None else ""

    def replacer(m):
        key = m.group(1).strip()
        return resolve(data, key)

    return re.sub(r"\{([^}]+)\}", replacer, template)


# ---------------------------------------------------------------------------
# Agent runners — called via subprocess or inline
# ---------------------------------------------------------------------------

def run_research_agent(city: str) -> dict:
    """Spawn Research Agent to gather city data.
    Returns JSON dict with all template fields.
    Fallback: load from /tmp/research-output/{city}.json cache.
    Demo mode: return minimal placeholder if no cache.
    """
    print(f"[Research] Gathering data for: {city}")

    # Option A: inline call if hermes_tools.execute_code is available
    try:
        from hermes_tools import execute_code

        prompt = f"""Anda adalah Research Agent. Kumpulkan data akurat tentang kabupaten/kota {city} di Sulawesi Selatan, Indonesia.

Output dalam format JSON (tanpa markdown, hanya JSON mentah) dengan field-field berikut — SEMUA WAJIB DIISI:
- kota, tagline, deskripsi_singkat, overview
- tentang_kota_1..4 (judul, konten, info_tambahan)
- keunggulan_kayu_dolken (3 items)
- aplikasi_konstruksi (5 items), aplikasi_dekorasi (5 items)
- studi_kasus_residensial (4 items: nama, lokasi, detail)
- studi_kasus_publik (2 items: nama, lokasi, detail)
- testimoni_residential (4 items), testimoni_komersial (4 items)
- relevansi_kayu_dolken (karakteristik_iklim, keunggulan_lokal, aplikasi_lokal)
- area_pengiriman (5+ kecamatan nyata), area_kota_sekitar (3 kota), landmark (3 landmark)
- telepon, whatsapp, wa_text

JANGAN tambahkan markdown, backtick, atau penjelasan. HANYA JSON mentah.
"""
        result = execute_code(code=prompt)
        data = json.loads(result)
        print(f"[Research] Done — {len(data)} fields collected")
        return data
    except ImportError:
        pass

    # Option B: load from cache
    cache_path = Path(f"/tmp/research-output/{city}.json")
    if cache_path.exists():
        print(f"[Research] Loading from cache: {cache_path}")
        data = json.loads(cache_path.read_text())
        print(f"[Research] Cache loaded — {len(data)} fields")
        return data

    # Option C: demo placeholder (Hermes will generate real data)
    print(f"[Research] DEMO MODE — using minimal placeholder for {city}")
    return {
        "kota": city,
        "tagline": f"Solusi Konstruksi Kayu Dolken di {city}",
        "deskripsi_singkat": f"Jual kayu dolken berkualitas di {city}. Siap kirim ke seluruh kecamatan.",
        "overview": f"Kayu dolken gelam terpercaya untuk konstruksi di {city} dan sekitarnya. Harga langsung pabrik, kualitas terjamin.",
    }


def run_writer_agent(city: str, data: dict, template_path: str) -> str:
    """Spawn Writer Agent to fill template with research data.
    Returns filled markdown string.
    """
    print("[Writer] Filling template with research data...")
    template = Path(template_path).read_text()

    # Build replacements for all YAML keys from data
    replacements = {}

    # Flatten data for simple key substitution
    def flatten(d, prefix=""):
        for k, v in d.items():
            key = f"{prefix}.{k}" if prefix else k
            if isinstance(v, dict):
                flatten(v, key)
            elif isinstance(v, list):
                # Lists handled specially below
                pass
            else:
                replacements[key] = v

    flatten(data)

    # Build the filled template
    filled = fill_template(template, data)

    # Handle lists: find YAML list sections and replace placeholder items
    # This is a simplified approach — full implementation uses template sections
    # For now, the template markers guide the caller (Hermes) to fill sections one-by-one
    print("[Writer] Template filled (section-by-section fill recommended for complex nested lists)")
    return filled


def run_editor_agent(city: str, draft_path: str) -> str:
    """Spawn Editor Agent to validate YAML and fix language.
    Returns path to validated file.
    """
    print("[Editor] Validating YAML syntax and language...")

    draft = Path(draft_path).read_text()

    # Basic YAML validation
    try:
        import yaml
        # Only validate frontmatter (between --- markers)
        parts = draft.split("---")
        if len(parts) >= 3:
            frontmatter = "---".join(parts[1:-1])
            yaml.safe_load(frontmatter)
        print("[Editor] YAML syntax: OK")
    except Exception as e:
        print(f"[Editor] YAML WARNING: {e}")

    # Check for leftover placeholders
    import re
    placeholders = re.findall(r'\b(tulis|isi|berikan|contoh|misal|placeholder)\b', draft, re.IGNORECASE)
    if placeholders:
        print(f"[Editor] WARNING: {len(placeholders)} placeholder(s) found — manual cleanup needed")

    edited_path = draft_path.replace(".md", "-edited.md")
    Path(edited_path).write_text(draft)
    print(f"[Editor] Output: {edited_path}")
    return edited_path


def run_reviewer_agent(city: str, final_path: str, template_path: str) -> bool:
    """Spawn Reviewer Agent for final QA.
    Returns True if APPROVED, False if REJECTED.
    """
    print("[Reviewer] Final QA check...")

    final = Path(final_path).read_text()
    template = Path(template_path).read_text() if Path(template_path).exists() else ""

    checks = {
        "layout": "layout:" in final,
        "images": "images:" in final and "images_alt:" in final,
        "nama_kota": city in final,
        "no_placeholder": not any(k in final.lower() for k in ["tulis...", "isi...", "berikan..."]),
        "telepon": "081311400177" in final,
    }

    print("[Reviewer] Checks:")
    all_pass = True
    for name, passed in checks.items():
        status = "✅" if passed else "❌"
        print(f"  {status} {name}")
        if not passed:
            all_pass = False

    if all_pass:
        print("[Reviewer] APPROVED ✅")
        return True
    else:
        print("[Reviewer] REJECTED ❌ — fix issues and retry")
        return False


# ---------------------------------------------------------------------------
# Main CLI
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(prog="jekyll-post-with-city")
    parser.add_argument("--city", required=True, help="Target kota/kabupaten")
    parser.add_argument(
        "--template",
        default="TEMPLATES/TEMPLATE--post-with-city.md",
        help="Path ke TEMPLATE--post-with-city.md",
    )
    parser.add_argument(
        "--output", required=True, help="Path output .md (mis. _post_with_city/YYYY-MM-DD-jual-kayu-dolken-{kota}.md)"
    )
    parser.add_argument(
        "--format", choices=["json", "md"], default="md", help="Format output (debug)"
    )
    parser.add_argument(
        "--skip-research", action="store_true", help="Skip Research Agent — gunakan cached data"
    )
    args = parser.parse_args()

    today = date.today().isoformat()
    slug = args.output

    print(f"=== jekyll-post-with-city ===")
    print(f"City:     {args.city}")
    print(f"Template: {args.template}")
    print(f"Output:   {args.output}")
    print(f"Date:     {today}")
    print("=" * 30)

    # Step 1: Research
    if args.skip_research:
        data = run_research_agent(args.city)
    else:
        try:
            data = run_research_agent(args.city)
        except Exception as e:
            print(f"[ERROR] Research failed: {e}")
            sys.exit(1)

    # Debug: output JSON
    if args.format == "json":
        print(json.dumps(data, ensure_ascii=False, indent=2))
        sys.exit(0)

    # Step 2: Writer
    draft = run_writer_agent(args.city, data, args.template)

    # Step 3: Editor
    # Write draft to temp path for editor
    draft_path = f"/tmp/{args.city}-draft.md"
    Path(draft_path).write_text(draft)
    edited_path = run_editor_agent(args.city, draft_path)

    # Step 4: Reviewer
    approved = run_reviewer_agent(args.city, edited_path, args.template)

    if approved:
        # Copy approved file to final output
        final_content = Path(edited_path).read_text()
        Path(args.output).write_text(final_content)
        print(f"\n✅ OUTPUT: {args.output}")

        # Auto-commit hint
        print("\nNext steps:")
        print(f"  1. Verify images: assets/images/posts/jual-kayu-dolken-{args.city}/001-004.webp")
        print(f"  2. Build: bundle exec jekyll build")
        print(f"  3. Commit: git add {args.output} && git commit -m 'Add post for {args.city}'")
    else:
        print("\n❌ Reviewer REJECTED — please fix issues manually")
        sys.exit(1)


if __name__ == "__main__":
    main()