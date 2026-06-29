# Known Issues & Verification (v2, 2026-06-29)

## Status: Tercatat dalam TODO/skill-analysis.md

File `TODO/skill-analysis.md` berisi analisis lengkap bug pipeline v1. Sebagian
besar sudah ditambal di v2. Berikut ringkas status dan verification commands.

## v2 — Yang sudah ditambal

### C1 — Reviewer false-APPROVE (TERTAMBAL)
- v1 mencari literal `tulis...` (dengan tiga titik `...`) → tidak cocok dengan
  template nyata yang memakai `"tulis deskripsi..."` TANPA ellipsis.
- v2 Reviewer pakai regex `"([^"]*\b(isi|tulis|berikan|jelaskan|contoh|misal|ganti|pilih|nama)\b[^"]*)"`
  dan parse YAML deklaratif. REJECT bila ada leak atau field required kosong.
- Verifikasi cepat:
  ```bash
  python3 scripts/reviewer_agent.py _post_with_city/{post}.md {kota}
  # EXIT=1 bila REJECTED. EXIT=0 bila APPROVED.
  ```

### C2 — Writer hanya substitusi `{key}`, abaikan quoted placeholder (TERTAMBAL)
- v2 template kosongkan semua field & pindahkan instruksi ke YAML comment,
  sehingga Writer tidak perlu tangani quoted placeholder. Writer v2 hanya
  substitusi generik `{kota}`, `{nama_kota}`, `{Nama Kota}`, `{NAMA_KOTA}`
  dan literal `"NamaKota"`.
- Verifikasi:
  ```bash
  grep -c '{kota}\|{nama_kota}\|{Nama Kota}\|{NAMA_KOTA}\|"NamaKota"' _post_with_city/{post}.md
  # Seharusnya 0 setelah Writer jalan.
  ```

### C3 — `hermes_tools.execute_code` disalahgunakan sebagai LLM prompt (TERTAMBAL)
- v2 tidak lagi mencoba memanggil `execute_code` untuk spawn research agent.
  Research sekarang cache-only fail-loud: `/tmp/research-output/{city}.json`.
  Untuk spawn research sub-agent, gunakan `delegate_task` dari Hermes sebelum
  panggil entrypoint.

### C4 — `--skip-research` no-op (TERTAMBAL)
- v2 menghormati flag: pass `skip_agent=True` ke `research_agent.research()`,
  yang langsung pakai cache tanpa spawn.

## v1 — Yang sengaja dipertahankan

### Pipeline manual REPORT → WAIT → FIX tetap jalan utama
- v2 menjadikan entrypoint pipeline sebagai pembantu, bukan autopilot yang
  memproduksi post siap-publish. Template v2 memang mengosongkan field section
  supaya user/agent mengisi manual via workflow section-by-section (lihat
  `references/pitfalls-and-user-preferences.md`).

## Quick health-check commands

```bash
# Compile check
python3 -m py_compile entrypoint.py scripts/*.py

# Pipeline test (bila punya cache research)
python3 entrypoint.py --city Maros \
    --template /path/ke/TEMPLATE--post-with-city.md \
    --output /tmp/testmaros.md
# v2 seharusnya: Editor PASS (template kosong), Reviewer REJECT (meta kosong).

# Bila meta sudah diisi manual: Reviewer APPROVED
python3 scripts/reviewer_agent.py /path/ke/post.md {kota}
```