#!/usr/bin/env python3
"""
Research Agent — kumpulkan data akurat tentang kota target.

Versi 2 (fail-loud): Tidak lagi menyalahgunakan hermes_tools.execute_code sebagai
antarmuka LLM (execute_code menjalankan kode PYTHON, bukan prompt natural-language,
sehingga Option A versi lama crash dengan SyntaxError ketika tidak ada cache).

Sumber yang didukung sekarang:
  1. Cache JSON di /tmp/research-output/{city}.json — disiapkan oleh Hermes
     agent via delegate_task sebelum entrypoint.py dipanggil, atau ditarik dari
     data riset manual.
  2. skip_agent=True: pakai cache saja, fail-loud bila tidak ada.

Untuk spawn research sub-agent, panggil pipeline dari Hermes via delegate_task
(food jadi data.json) — entrypoint tidak lagi mencoba-melakukan sendiri.
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path


_CACHE_DIR = Path("/tmp/research-output")


def _city_key(city: str) -> str:
    """Normalisasi nama kota untuk cache key (lowercase + strip)."""
    return re.sub(r"\s+", "", city.strip().lower())


def research(city: str, skip_agent: bool = False) -> dict:
    """Kumpulkan data kota dari cache.

    Args:
        city: Nama kota/kabupaten target.
        skip_agent: Bila True, langsung pakai cache. False pun sekarang
            menggunakan cache (spawn agent dihapus); flag dipertahankan
            untuk kompatibilitas CLI existing.

    Returns:
        dict data kota.

    Raises:
        FileNotFoundError: bila cache belum tersedia. Penanganan cache
            harus dilakukan oleh pemanggil (lihat hint di entrypoint.py).
    """
    cache_path = _CACHE_DIR / f"{_city_key(city)}.json"
    if cache_path.exists():
        print(f"[Research] Cache loaded: {cache_path}")
        data = json.loads(cache_path.read_text(encoding="utf-8"))
        print(f"[Research] {len(data)} fields collected")
        return data

    raise FileNotFoundError(
        f"Cache research tidak ditemukan: {cache_path}. "
        "Sebelum menjalankan entrypoint.py, bekukan JSON data kota ke file "
        f"ini (lihat references/multi-agent-pipeline.md)."
    )


if __name__ == "__main__":
    city_arg = sys.argv[1] if len(sys.argv) > 1 else "Maros"
    try:
        data = research(city_arg)
        print(json.dumps(data, ensure_ascii=False, indent=2))
    except FileNotFoundError as e:
        print(str(e), file=sys.stderr)
        sys.exit(1)