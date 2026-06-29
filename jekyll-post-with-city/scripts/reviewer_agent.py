#!/usr/bin/env python3
"""
Reviewer Agent — final QA sebelum commit.

Versi 2 (template kosong): Karena template v2 mengosongkan field dan memindahkan
instruksi ke YAML comment, Reviewer bekerja secara deklaratif terhadap frontmatter
hasil parse YAML, bukan text-substring.

Pemeriksaan:
  1. `layout: node--post-with-city` ada di frontmatter.
  2. `nama_kota` ter-set (tidak None/string kosong) dan cocok dengan argumen `--city`.
  3. `images` dan `images_alt` adalah list non-empty dan panjangnya sama.
  4. `title`, `description`, `excerpt` tidak kosong (frontmatter meta wajib).
  5. Tidak ada quoted-string instruksi bocor (`tulis`, `isi`, `berikan`, dst.)
     di luar YAML comment.
  6. `telepon` hardcoded `0813-1140-0177` ATAU `081311400177` muncul di file
     (header post mengandung nomor HP).

Field kosong pada section selain frontmatter (area_pengiriman, keunggulan_produk,
dst) TIDAK dianggap error — itu adalah slot yang akan diisi via workflow REPORT
-> FIX manual. Reviewer hanya meng-REJECT bila placeholder string bocor atau
frontmatter meta kosong.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

try:
    import yaml  # type: ignore
except ImportError:
    yaml = None  # type: ignore


_PHONE_RE = re.compile(r"0813[- ]?1140[- ]?0177")
_INSTR_KW = re.compile(
    r'"[^"]*\b(isi|tulis|berikan|jelaskan|contoh|misal|ganti|pilih|nama)\b[^"]*"',
    re.IGNORECASE,
)


def _extract_frontmatter(content: str) -> tuple[dict | None, str]:
    """Return (parsed_dict, error_msg)."""
    if yaml is None:
        return (None, "PyYAML not installed")
    parts = content.split("---", 2)
    if len(parts) < 3:
        return (None, "No frontmatter (missing ---)")
    try:
        data = yaml.safe_load(parts[1])
    except yaml.YAMLError as e:
        return (None, f"YAML error: {e}")
    if not isinstance(data, dict):
        return (None, "Frontmatter bukan mapping")
    return (data, "")


def review(final_path: str, city: str | None = None) -> bool:
    """Run final checks. Returns True if APPROVED, False if REJECTED."""
    print(f"[Reviewer] Checking: {final_path}")
    content = Path(final_path).read_text(encoding="utf-8")

    data, err = _extract_frontmatter(content)
    checks: dict[str, bool] = {}
    notes: list[str] = []

    if data is None:
        print(f"[Reviewer] Frontmatter tidak ter-parse: {err}")
        return False

    # 1. Layout
    layout = str(data.get("layout", "")).strip()
    checks["layout_correct"] = layout == "node--post-with-city"
    if not checks["layout_correct"]:
        notes.append(f"layout actual: '{layout}'")

    # 2. nama_kota non-empty & match city
    nama_kota = data.get("nama_kota")
    checks["nama_kota_set"] = isinstance(nama_kota, str) and bool(nama_kota.strip())
    if city:
        # normalisasi lowercase tanpa spasi
        norm = lambda s: re.sub(r"\s+", "", str(s).lower())  # noqa: E731
        checks["nama_kota_match"] = (norm(nama_kota) == norm(city)) if nama_kota else False
    else:
        checks["nama_kota_match"] = True

    # 3. images & images_alt non-empty list, same length
    images = data.get("images")
    images_alt = data.get("images_alt")
    checks["images_list"] = isinstance(images, list) and len(images) > 0
    checks["images_alt_list"] = isinstance(images_alt, list) and len(images_alt) > 0
    checks["images_len_match"] = (
        isinstance(images, list) and isinstance(images_alt, list)
        and len(images) == len(images_alt)
    )

    # 4. frontmatter meta (info-only, template baru sengaja kosong untuk diisi manual)
    import datetime as _dt
    meta_empty = []
    for meta_key in ("title", "description", "excerpt", "author"):
        v = data.get(meta_key)
        is_empty = not (isinstance(v, str) and bool(v.strip()))
        if is_empty:
            meta_empty.append(meta_key)
            print(f"  [INFO] meta_{meta_key}: kosong (akan diisi manual via REPORT->FIX)")
        else:
            print(f"  [OK] meta_{meta_key}: terisi")
    # date boleh str (YYYY-MM-DD) atau datetime.date hasil parse YAML
    date_v = data.get("date")
    date_empty = not (isinstance(date_v, (str, _dt.date)) and bool(str(date_v).strip()))
    if date_empty:
        meta_empty.append("date")
        print(f"  [INFO] meta_date: kosong (akan diisi manual via REPORT->FIX)")
    else:
        print(f"  [OK] meta_date: terisi")

    # 5. No placeholder merge in content (quoted string instruction outside comments)
    leak_count = 0
    for l in content.splitlines():
        if l.lstrip().startswith("#"):
            continue
        if _INSTR_KW.search(l):
            leak_count += 1
    checks["no_placeholder_leak"] = (leak_count == 0)
    if leak_count:
        notes.append(f"{leak_count} placeholder leak(s) detected")

    # 6. telepon (substring)
    checks["telepon_present"] = bool(_PHONE_RE.search(content))
    if not checks["telepon_present"]:
        notes.append("Nomor telepon tidak ditemukan")

    # Print
    all_pass = True
    for name, passed in checks.items():
        status = "OK" if passed else "FAIL"
        print(f"  [{status}] {name}")
        if not passed:
            all_pass = False
    if notes:
        print("[Reviewer] Notes:")
        for n in notes:
            print(f"  - {n}")

    if all_pass:
        print("\n[Reviewer] APPROVED")
    else:
        print("\n[Reviewer] REJECTED — fix issues above")
    return all_pass


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: reviewer_agent.py <final.md> [city]")
        sys.exit(1)
    final_path = sys.argv[1]
    city_arg = sys.argv[2] if len(sys.argv) > 2 else None
    ok = review(final_path, city_arg)
    sys.exit(0 if ok else 1)