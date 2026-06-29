#!/usr/bin/env python3
"""
Research Agent — kumpulkan data akurat tentang kota target.
Output: JSON dengan field-field yang dibutuhkan template.

Cross-AI compatible: bisa dipanggil dari Hermes, Claude Code, atau CLI biasa.
"""

import json
import sys
from pathlib import Path


def research(city: str) -> dict:
    """
    Kumpulkan data tentang kota.
    Jika hermes_tools.execute_code tersedia, spawn Research sub-agent.
    Jika tidak, coba load dari cache /tmp/research-output/{city}.json.

    Returns dict with all template-required fields.
    """
    try:
        from hermes_tools import execute_code

        prompt = _build_research_prompt(city)
        result = execute_code(code=prompt)
        data = json.loads(result)
        # Save cache
        cache_dir = Path("/tmp/research-output")
        cache_dir.mkdir(parents=True, exist_ok=True)
        (cache_dir / f"{city}.json").write_text(json.dumps(data, ensure_ascii=False, indent=2))
        return data
    except ImportError:
        cache_path = Path(f"/tmp/research-output/{city}.json")
        if cache_path.exists():
            return json.loads(cache_path.read_text())
        raise RuntimeError(
            f"No hermes_tools and no cached data for {city}. "
            "Run via Hermes agent or provide cached JSON first."
        )


def _build_research_prompt(city: str) -> str:
    return f"""Anda adalah Research Agent. Kumpulkan data akurat tentang {city} di Sulawesi Selatan.

Output HANYA JSON mentah, tanpa markdown, tanpa backtick, tanpa penjelasan.

Field yang WAJIB diisi:
- kota: "{city}"
- tagline: string 3-5 kata
- deskripsi_singkat: string 1-2 kalimat
- overview: string 3-4 kalimat
- tentang_kota_1 dict: judul, konten, info_tambahan (sejarah/budaya)
- tentang_kota_2 dict: judul, konten, info_tambahan (ekonomi/potensi)
- tentang_kota_3 dict: judul, konten, info_tambahan (wisata/landmark)
- tentang_kota_4 dict: judul, konten, info_tambahan (kuliner/oleh-oleh)
- keunggulan_kayu_dolken: array of 3 strings
- aplikasi_konstruksi: array of 5 strings
- aplikasi_dekorasi: array of 5 strings
- studi_kasus_residensial: array of 4 objects (nama, lokasi, detail)
- studi_kasus_publik: array of 2 objects (nama, lokasi, detail)
- testimoni_residential: array of 4 objects (nama, lokasi, isi)
- testimoni_komersial: array of 4 objects (profesi, area, isi)
- relevansi_kayu_dolken dict: karakteristik_iklim, keunggulan_lokal, aplikasi_lokal
- area_pengiriman: array of min 5 kecamatan nyata
- area_kota_sekitar: array of 3 kota sekitar
- landmark: array of 3 landmark
"""


if __name__ == "__main__":
    city = sys.argv[1] if len(sys.argv) > 1 else "Maros"
    data = research(city)
    print(json.dumps(data, ensure_ascii=False, indent=2))
