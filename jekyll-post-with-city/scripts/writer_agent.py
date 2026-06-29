#!/usr/bin/env python3
"""
Writer Agent — substitusi placeholder generik pada TEMPLATE--post-with-city.md.

Versi 2 (template kosong): template baru mengosongkan semua field section dan
memindahkan instruksi ke YAML comment di atas key. Writer hanya mengganti
placeholder generik kota:
  {kota}       -> nama kota apa adanya (mis. "Maros")
  {nama_kota}  -> slug lowercase (mis. "maros")
  {Nama Kota}  -> Title Case (mis. "Maros")
  {NAMA_KOTA}  -> UPPER CASE (mis. "MAROS")

Section field (judul, deskripsi, lokasi, dst) dibiarkan kosong untuk diisi
manual via workflow REPORT -> WAIT -> FIX (lihat SKILL.md). Writer tidak
lagi mengganti quoted-instruction placeholder, karena template baru tidak
memilikinya.
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path


_BRACE_RE = re.compile(r"\{([^}]+)\}")


def _title_case(name: str) -> str:
    """Normalisasi nama kota menjadi Title Case.

    'maros' -> 'Maros', 'kota makassar' -> 'Kota Makassar'.
    """
    return " ".join(w.capitalize() for w in name.strip().split())


def _slug(name: str) -> str:
    """Normalisasi menjadi slug lowercase tanpa spasi.

    'Kota Makassar' -> 'kotamakassar'.
    """
    return re.sub(r"\s+", "", name.strip().lower())


def fill_template(template: str, city: str) -> str:
    """Substitusi placeholder generik kota pada template.

    Placeholder yang diganti:
      {kota}       -> city apa adanya
      {nama_kota}  -> slug lowercase tanpa spasi
      {Nama Kota}  -> Title Case
      {NAMA_KOTA}  -> UPPER CASE

    Lainnya (mis. {include ...}) tidak disentuh.
    """

    def _replace(m: re.Match) -> str:
        key = m.group(1).strip()
        if key == "kota":
            return city.strip()
        if key == "nama_kota":
            return _slug(city)
        if key == "Nama Kota":
            return _title_case(city)
        if key == "NAMA_KOTA":
            return _slug(city).upper()
        # include directives, fragile pasangan file%, dsb — biarkan utuh
        return m.group(0)

    out = _BRACE_RE.sub(_replace, template)
    # Template juga memakai literal "NamaKota" (tanpa brace) sebagai placeholder
    # nama_kota di baris `nama_kota: "NamaKota"`. Substitusi sekunder.
    out = out.replace('"NamaKota"', '"%s"' % _title_case(city))
    return out


def write(city: str, template_path: str, output_path: str) -> str:
    """Baca template, ganti placeholder generik, tulis draft.

    Returns:
        path ke draft file.
    """
    print(f"[Writer] Template: {template_path}")
    print(f"[Writer] Output:   {output_path}")

    template = Path(template_path).read_text(encoding="utf-8")
    filled = fill_template(template, city)

    Path(output_path).write_text(filled, encoding="utf-8")
    print(f"[Writer] Draft written — {len(filled)} chars")

    # Cek berapa placeholder generik yang masih tersisa (seharusnya 0)
    remaining = _BRACE_RE.findall(filled)
    unresolved = [r for r in remaining if r.strip() in
                  ("kota", "nama_kota", "Nama Kota", "NAMA_KOTA")]
    if unresolved:
        print(f"[Writer] WARNING: {len(unresolved)} unresolved generic placeholder(s): "
              f"{set(unresolved)}")
    else:
        print("[Writer] Semua placeholder generik terisi ✓")

    return output_path


if __name__ == "__main__":
    if len(sys.argv) < 4:
        print("Usage: writer_agent.py <city> <template.md> <output.md>")
        sys.exit(1)

    city_arg = sys.argv[1]
    template_arg = sys.argv[2]
    output_arg = sys.argv[3]
    write(city_arg, template_arg, output_arg)