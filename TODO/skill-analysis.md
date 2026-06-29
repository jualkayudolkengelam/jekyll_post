# Skill Analysis: jekyll-post-with-city

Tanggal analisis: 2026-06-29
Target: `jekyll-post-with-city/SKILL.md` + `entrypoint.py` + `scripts/*.py` + `references/*.md`

Peringkat: CRITICAL (skill dirancang untuk autopilot Research→Writer→Editor→Reviewer, tetapi pipeline yang dijalankan hari ini menghasilkan post dengan 160+ placeholder instruksi dan di-APPROVE oleh Reviewer).

---

## Ringkasan Eksekusi Percobaan

Perintah dijalankan langsung dari repo (cwd `public_html/`):

```
python3 entrypoint.py --city Maros \
  --template TEMPLATES/TEMPLATE--post-with-city.md \
  --output /tmp/test-maros.md
```

Hasil:
- Research loaded cache `/tmp/research-output/Maros.json` (22 field)
- Editor WARNING: 211 placeholder(s) found — tapi tidak diperbaiki
- Reviewer APPROVED ✅
- Output `test-maros.md` 664 baris 31.4KB — ISINYA MASIH TEMPLATE dengan 160 baris `"tulis ..."`, `"isi ..."`, dll.

Reviewer meng-APPROVE file yang sebenarnya cacat. Inilah bug paling berbahaya: skill mengklaim sukses padahal hasilnya tidak layak publish.

---

## CRITICAL

### C1. Reviewer salah deteksi placeholder (false APPROVED)
- File: `entrypoint.py:run_reviewer_agent` (cek `no_placeholder`) dan `scripts/reviewer_agent.py:review` (loop `no_placeholder_tulis/isi/berikan`)
- Kedua Reviewer mencari substring literal `"tulis..."`, `"isi..."`, `"berikan..."` (dengan tiga titik `...`). Template nyata tidak memakai literal `...` — polanya `"tulis deskripsi 1 kalimat..."`, `"isi nama proyek..."` tanpa ellipsis literal.
- Akibat: regex `any(k in final.lower() for k in ["tulis...", "isi...", "berikan..."])` selalu False → check passed.
- Skrip `reviewer_agent.py` punya pola sama: `re.search(r'\b(tulis|isi|berikan)\.{3}\b', ...)` → butuh literal `...`.
- Editor sudah pakai regex yang benar `r'"tulis[^"]*"'` tapi hanya WARNING, tidak fix.
- FIX: samakan pola Reviewer dengan Editor (`r'"(tulis|isi|berikan|contoh|misal|ganti|jelaskan|pilih)[^"]*"'`), hitung kemunculan, REJECT bila >0.

### C2. fill_template hanya handle `{key}` placeholder, abaikan `"tulis..."` quoted placeholder
- `entrypoint.py:fill_template` dan `scripts/writer_agent.py:fill_template` hanya `re.sub(r"\{([^}]+)\}", ...)`.
- Template asli (`TEMPLATES/TEMPLATE--post-with-city.md`) memakai DUA gaya placeholder:
  1. `{kota}` / `{nama_kota}` — 12 kemunculan (generik kota)
  2. `"tulis ..."`, `"isi ..."`, `"berikan..."` — 160+ kemunculan (instruksi section)
- Writer hanya replace yang #1, semua instruksi section #2 dibiarkan utuh di output.
- FIX: tambah pass kedua yang menangkan `"tulis..."`/`"isi..."` quoted instruction dengan pengisian manual via data dict (atau delegasi sub-agent), atau ubah workflow sehingga Writer jelas hanya substitusi dasar dan section fill WAJIB lewat REPORT→FIX manual sesuai SKILL.md.

### C3. run_research_agent menyalahgunakan `execute_code` sebagai antarmuka LLM
- `entrypoint.py:run_research_agent` dan `scripts/research_agent.py:research` memanggil `from hermes_tools import execute_code; execute_code(code=prompt)` dengan `prompt` berisi instruksi natural-language ("Anda adalah Research Agent...").
- `hermes_tools.execute_code` menjalankan kode PYTHON, bukan prompt LLM. Bila dipanggil dari dalam Hermes, pemanggilan ini akan mengeksekusi teks Indonesia sebagai Python → `SyntaxError` (tidak ditangkap oleh `except ImportError`).
- Hanya berhasil kalau `/tmp/research-output/{city}.json` cache sudah ada — itulah sebabnya percobaan tadi "berjalan" padahal sebenarnya pakai hasil cache lama.
- FIX: gunakan `delegate_task` (Hermes sub-agent) untuk spawn Research agent LLM, atau ganti dengan `web_search` + parsing terstruktur, atau hapus blok Option A dan paksa cache mode.

### C4. `--skip-research` flag tidak melakukan apa pun
- `entrypoint.py:main` blok:
  ```python
  if args.skip_research:
      data = run_research_agent(args.city)
  else:
      try:
          data = run_research_agent(args.city)
      except Exception as e: ...
  ```
- Kedua cabang memanggil fungsi yang sama. Flag tidak skip apa pun — hanya menghilangkan try/except.
- FIX: bila `--skip-research`, load cache langsung tanpa mencoba spawn sub-agent / Option B di run_research_agent.

---

## HIGH

### H1. Editor tidak memperbaiki apa pun — hanya lapor WARNING
- `entrypoint.py:run_editor_agent` dan `scripts/editor_agent.py:edit` membaca draft, validasi YAML, mencatat 211 placeholder via regex BENAR, lalu menulis ulang konten yang SAMA ke `-edited.md`.
- Output editor = input editor byte-for-byte. Stage "Editor" tidak ada gunanya.
- Akibat: bug C1 (Reviewer false-approve) tidak ditambal oleh Editor.
- FIX: Editor harus REJECT/exit-nonzero bila placeholder count > 0, atau lakukan cleaning otomatis (mark baris placeholder sebagai TODO dengan marker konsisten agar Reviewer bisa cek).

### H2. Skrip entrypoint vs scripts/*_agent.py duplikat dengan perilaku berbeda
- `entrypoint.py` mengandung implementasi inline `run_research_agent`, `run_writer_agent`, `run_editor_agent`, `run_reviewer_agent` yang meniru (tapi tak konsisten dengan) `scripts/{research,writer,editor,reviewer}_agent.py`.
- Contoh perbedaan:
  - `reviewer_agent.py` pakai `tuple[bool, list[str]]` type hint (Python 3.9+), entrypoint tidak.
  - `editor_agent.py` punya pola regex placeholder 5 kategori; entrypoint hanya 4.
  - `research_agent.py` cache otomatis ke `/tmp/...`, entrypoint Option A tidak.
- Skrip `scripts/*` tidak pernah diimpor entrypoint — `SCRIPT_DIR.insert(0, ...)` hanya deklarasi tanpa import modul-modul tersebut. Dead infrastructure.
- FIX: hapus salah satu lapisan. Pilih: (a) entrypoint mengimpor dari `scripts/` (DRY), atau (b) hapus `entrypoint.py` dan arahkan SKILL.md ke `scripts/*_agent.py` yang di-orchestrate via shell.

### H3. Field name Research prompt tidak cocok dengan field template
- `entrypoint.py` Research prompt minta: `kota, tagline, deskripsi_singkat, overview, tentang_kota_1..4, keunggulan_kayu_dolken, aplikasi_konstruksi, aplikasi_dekorasi, studi_kasus_residensial, studi_kasus_publik, testimoni_residential, testimoni_komersial, relevansi_kayu_dolken, area_pengiriman, area_kota_sekitar, landmark`.
- `research_agent.py` minta field serupa (sama dengan di atas).
- Template nyata (per `references/section-content-patterns.md` dan `_includes/reusable/post-with-city/`) memakai: `nama_kota`, `keunggulan_produk`, `keunggulan_layanan`, `keunggulan_durabilitas`, `keunggulan_nilai`, `aplikasi_kayu_dolken.konstruksi_dekorasi`, `aplikasi_kayu_dolken.furniture_komersial`, `proses_awal_pemesanan`, `finalisasi_pengiriman`, `studi_kasus_proyek.proyek_residensial`, `testimoni.testimoni_residential`, `tentang_kota_1`, `tentang_kota_2`, `tips_ukuran`, `FAQ`, `area_pengiriman_detail`, `wilayah_pusat/utara_selatan/pengembangan`.
- Skew: banyak field template tidak ada di output Research; banyak field Research tidak dipakai template.
- FIX: samakan Research prompt dengan manifest field template (dapat dibangkitkan otomatis dari `references/jekyll-post-fields.md` atau `_includes` includes — utamakan jadi satu sumber kebenaran).

### H4. Demo mode (Option C) menghasilkan dict 4 field — pipeline akan crash
- `entrypoint.py:run_research_agent` Option C mengembalikan `{kota, tagline, deskripsi_singkat, overview}` saja.
- `run_writer_agent.fill_template` menulis ulang hanya `{kota}` / `{nama_kota}` (12 placeholder generik) → 160+ instruksi section tetap utuh; Editor lapor WARNING, Reviewer APPROVE (bug C1). Output tidak layak.
- FIX: demo mode sebaiknya langsung REJECT + jelaskan butuh Research nyata, bukan di-APPROVE.

---

## MEDIUM

### M1. Dead code: `replacements` di run_writer_agent dihitung lalu dibuang
- `entrypoint.py:run_writer_agent` memanggil `flatten(data)` mengisi `replacements`, lalu langsung `fill_template(template, data)` — `replacements` tidak pernah dipakai.
- FIX: hapus blok flatten, atau gunakan `replacements` (tapi lihat C2 — pendekatan flatten pun tidak menyelesaikan masalah section-list).

### M2. `edited_path = draft_path.replace(".md", "-edited.md")` mengganti semua `.md`
- Bila `draft_path` memuat banyak `.md` (mis. `...-template-md-copy.md`), substitusi global menghasilkan path aneh. Kecil risk tapi fragile.
- FIX: `edited_path = re.sub(r"\.md$", "-edited.md", draft_path)` atau pakai `Path.with_stem(...)`.

### M3. `run_editor_agent.validate_yaml`: skema exception rapuh
- Blok `try: import yaml; ... yaml.safe_load(...) ... except ImportError: ...; except yaml.YAMLError as e: ...`.
- Bila `import yaml` gagal (`ImportError`), handler pertama append "PyYAML not installed". OK.
- Bila `import yaml` berhasil tapi parsing gagal, `except yaml.YAMLError` berjalan — referensi `yaml` sudah didefinisikan lokal dalam try. Berfungsi tapi mudah rusak saat refaktor.
- `scripts/editor_agent.py` punya masalah sama tapi urutan berbeda.
- FIX: import yaml di modul-level (dengan fallback), validasi di fungsi terpisah.

### M4. Reviewer hardcoded telepon `081311400177`
- `entrypoint.py:run_reviewer_agent` & `scripts/reviewer_agent.py` check `"081311400177" in final`. Angka kini sesuai memory user, tapi:
  - Tidak parameterizable (kalau nomor berubah, banyak file perlu diedit).
  - Tidak verifikasi YAML struktur, hanya substring — akan lolos bila nomor muncul di komentar/komentar test.
- FIX: jadikan parameter / env var (`HERMES_PHONE`), atau baca dari satu file konfig.

### M5. Reviewer check `images:` / `images_alt:` pakai substring — mudah lolos
- Kedua kemunculan key selalu ada di template walau value kosong/instruksi. Check tidak bermakna.
- FIX: parse frontmatter via PyYAML, verifikasi list non-empty, len match.

---

## LOW

### L1. `run_research_agent` Option B: cache path case-sensitive vs city name
- Cache key `f"/tmp/research-output/{city}.json"` case-sensitive. `--city Maros` vs `--city maros` dianggap entri berbeda → manual re-research untuk each casing.
- FIX: normalisasi nama kota (lowercase + strip) sebelum lookup/penyimpanan.

### L2. SKILL.md teknik baca section: marker `'NAMA' not in l` fragile
- Contoh snippet `if l.startswith('# SECTION ') and i > start and 'NAMA' not in l: break` mengasumsikan section target literal mengandung kata "NAMA" (placeholder). Berfungsi untuk `# SECTION NAMA SECTION` tapi tidak untuk section bernama spesifik.
- FIX: lebih andal `if l.startswith('# SECTION ') and i > start: break` (memutus di section header berikutnya, apapun namanya).

### L3. SKILL.md frontmatter description multiline — boleh tapi panjang
- Frontmatter `description` panjang multi-paragraf termasuk tabel-like content. Tidak bermasalah untuk parser YAML tapi membebban listing skill.
- Saran: ringkasan 1-2 kalimat di frontmatter; pindahkan tabel kompatibilitas ke `references/cross-agent-compatibility.md` baru.

### L4. Referensi path include di SKILL.md tidak eksplisit
- SKILL.md tidak menyebut lokasi include block (`_includes/reusable/post-with-city/block--*.html`). Pitfalls file melakukannya, tapi penguna skill baru mungkin lewat SKILL.md dulu.
- FIX: tambahkan baris "Includes: `_includes/reusable/post-with-city/block--*.html` (roster di `references/pitfalls-and-user-preferences.md`)".

### L5. `references/multi-agent-pipeline.md` contoh CLI tidak ada
- Tertulis: `hermes skill run jekyll-post-with-city --param city="Maros"` dan `claude-code-tools run-skill --skill-path ...`. Perintah `hermes skill run` BUKAN command Hermes yang ada. Contoh menyesatkan bagi user yang ingin invoke otomatis.
- FIX:常规赛 CLI saat ini hanya `python3 entrypoint.py --city ...` atau `hermes skill view jekyll-post-with-city`. Hapus contoh `hermes skill run` dan `claude-code-tools` sampai command itu benar-benar terdaftar.

### L6. `references/jekyll-post-fields.md` tidak komprehensif
- File cuma 30 baris awal daftar field frontmatter. Sebagian besar field section deep (aplikasi, testimoni, studi_kasus) tidak terdaftar.
- Sudah ada `section-content-patterns.md` lebih lengkap — overlap parsial.
- Saran: jadikan `jekyll-post-fields.md` sebagai flat list 1-level (semua top-level key + required/optional), link ke `section-content-patterns.md` untuk format nested.

---

## Saran Prioritas Perbaikan

1. **Tambal C1 + C2** dulu (Reviewer + Writer). Pipeline lapor APPROVE padahal rusak — paling memalukan.
2. **Tambal C3 + C4** (Research agent + skip flag) — pastikan entrypoint benar-benar dapat Research data, atau fail-loud bila tidak ada.
3. **H1**: buat Editor REJECT bila placeholder >0 (ulang second-layer defense terhadap C1).
4. **H2**: pilih satu lapis (entrypoint OR scripts) daneliminasi duplikat.
5. **H3**: samakan field Research dengan template (manifest terpadu).
6. Lain-lain LOW bebas ditunda.

Setelah 1-3 dikerjakan, ulang uji: `python3 entrypoint.py --city Maros --template TEMPLATES/TEMPLATE--post-with-city.md --output /tmp/x.md` → harus REJECT dengan daftar 160+ placeholder. Bila APPROVED → belum selesai.