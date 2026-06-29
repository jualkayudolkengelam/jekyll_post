#!/usr/bin/env python3
"""
Editor Agent — validasi YAML frontmatter dan deteksi placeholder bocor.

Versi 2 (template kosong): template baru memindahkan instruksi ke YAML comment
dan mengosongkan value. Editor tidak lagi mencoba "perfect" cleaning, melainkan:
  1. Parse frontmatter via PyYAML — tangkap syntax error.
  2. Scan line-by-line: cari quoted string instruksi (`"tulis ..."`, `"isi ..."`,
     `"berikan ..."`, dst) yang BUKAN di dalam YAML comment. Jika ada, itu
     berarti placeholder template belum terisi — REJECT.
  3. Field kosong (None) diperbolehkan (template memang sengaja kosong). Editor
     hanya melaporkan jumlah field kosong sebagai info, bukan error.

Return exit code nonzero bila ada syntax YAML error ATAU placeholder bocor.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

try:
    import yaml  # type: ignore
except ImportError:
    yaml = None  # type: ignore


# Pattern deteksi instruksi pada quoted string (di luar comment)
_INSTR_KW = re.compile(
    r'"[^"]*\b(isi|tulis|berikan|jelaskan|contoh|misal|ganti|pilih|nama)\b[^"]*"',
    re.IGNORECASE,
)


def validate_yaml(content: str) -> tuple[bool, list[str]]:
    """Validasi YAML frontmatter. Return (is_valid, errors)."""
    errors: list[str] = []
    if yaml is None:
        errors.append("PyYAML not installed — skip YAML validation")
        return (False, errors)

    parts = content.split("---", 2)
    if len(parts) < 3:
        errors.append("No frontmatter found (missing --- delimiters)")
        return (False, errors)

    frontmatter = parts[1]
    try:
        data = yaml.safe_load(frontmatter)
        if not isinstance(data, dict):
            errors.append("Frontmatter bukan mapping YAML (kemungkinan kosong)")
        else:
            # Hitung field kosong untuk info (bukan error)
            empty_top = [k for k, v in data.items() if v is None]
            if empty_top:
                # info-only, tidak masuk errors
                print(f"[Editor] INFO: {len(empty_top)} top-level field kosong (template "
                      f"baru — untuk diisi manual): {empty_top}")
            print(f"[Editor] YAML: OK ({len(data)} top-level keys)")
            return (True, [])
    except yaml.YAMLError as e:
        errors.append(f"YAML syntax error: {e}")
    except Exception as e:
        errors.append(f"Validation error: {e}")
    return (False, errors)


def check_placeholders(content: str) -> list[str]:
    """Cari quoted-string instruksi di luar YAML comment.

    Returns:
        List issue messages. Setiap entry berisi baris dan sampel string.
    """
    issues: list[str] = []
    for i, l in enumerate(content.splitlines(), 1):
        if l.lstrip().startswith("#"):
            continue
        m = _INSTR_KW.search(l)
        if m:
            issues.append(f"L{i}: {m.group(0)[:80]}")
    return issues


def edit(draft_path: str) -> tuple[str, bool]:
    """Validasi + scan placeholder pada draft.

    Returns:
        (edited_path, is_clean). is_clean False bila ada YAML error atau
        placeholder bocor. File output ditulis ulang apa adanya (tidak ada
        perubahan konten — editor v2 tidak mengandalkan "auto-fix").
    """
    print(f"[Editor] Processing: {draft_path}")

    content = Path(draft_path).read_text(encoding="utf-8")
    clean = True

    # 1. YAML validation
    valid, yaml_errors = validate_yaml(content)
    if not valid:
        for e in yaml_errors:
            print(f"[Editor] YAML ERROR: {e}")
        clean = False

    # 2. Placeholder scan
    issues = check_placeholders(content)
    if issues:
        print(f"[Editor] PLACEHOLDER LEAK: {len(issues)} instruksi masih di luar comment:")
        for i, msg in enumerate(issues[:10], 1):
            print(f"  {i}. {msg}")
        if len(issues) > 10:
            print(f"  ... dan {len(issues) - 10} lainnya.")
        print("[Editor] REJECT — selesaikan placeholder sebelum lanjut ke Reviewer.")
        clean = False
    else:
        print("[Editor] Placeholders: CLEAN")

    # 3. Tulis output apa adanya; penamaan tetap konsisten dengan skrip lama
    edited_path = draft_path
    if "-edited" not in draft_path:
        edited_path = re.sub(r"\.md$", "-edited.md", draft_path)
    Path(edited_path).write_text(content, encoding="utf-8")
    print(f"[Editor] Output: {edited_path}")
    return (edited_path, clean)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: editor_agent.py <draft.md>")
        sys.exit(1)
    _, ok = edit(sys.argv[1])
    sys.exit(0 if ok else 1)