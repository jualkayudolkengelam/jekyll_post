# Pitfalls & User Preferences

## Common Pitfalls
- **Missing REQUIRED fields** in front‑matter → content looks empty on site. Always verify with the reference list.
- **Escaped quotes in section tags** (`\"`) break Liquid parsing. Use plain `"` in `<section id="...">`.
- **WebP is mandatory** – no JPEG/PNG files should remain in the assets directory.
- **Only 2 source images available** – set those in `images: []` and omit the missing 3rd & 4th entries.
- **YAML quoting errors** – a single missing closing quote causes Jekyll to abort with "YAML Exception: did not find expected key". Always double-check quotes on multiline YAML values.
- **Jangan restore/revert file tanpa bertanya** — Jika TEMPLATES/ atau file lain termodifikasi (`git checkout --`), JANGAN langsung restore. User mungkin sengaja mengeditnya. Restore tanpa izin menghilangkan pekerjaan user dan menyebabkan frustrasi.
- **Include path errors** – `reusable/block--*.html` files live in `reusable/post-with-city/` sub-directory, not directly under `reusable/`. Using the wrong path gives "Could not locate the included file" errors.

## Placeholder Audit (critical)
- **Placeholder values WILL render** — `# Instruksi:` comments are YAML comments (invisible), but string values like `"tulis deskripsi 1 kalimat..."` are REAL YAML values that appear on the published page. This is the #1 source of template-instruction-leaked-into-content bugs.
- **SANGAT MEMALUKAN** — petunjuk/instruksi template yang terbawa ke konten adalah error kualitas paling serius. User menganggapnya memalukan dan tidak profesional. Wajib 0% placeholder di setiap post.
- **Most commonly missed sections**: `tentang_kota` (4 cards), `proyek_publik`, `tagline`, `deskripsi_singkat`, `overview`. These require city-specific research — cannot be generic.
- **Remove ALL `# Instruksi:` and instruction comments** — even though they don't render, user considers them embarrassing in source file. Delete every comment that contains instructions/template guidance.
- **grep audit after every post build**: `grep -n 'tulis\|isi \|contoh\|ganti\|deskripsi\|jelaskan\|pilih icon\|lapisi\|pilih ' _post_with_city/{nama-post}.md` — any match = placeholder still present.
- **tentang_kota structure**: 4 cards total (2 in `tentang_kota_1` with `fakta:`, 2 in `tentang_kota_2` with `list_item:` + optional `info_tambahan`). Each card needs: judul, icon (bi-*), subjudul, icon_subjudul, deskripsi (2-3 paragraf/cukup). Topik: sejarah, ekonomi, budaya, kuliner, wisata, landmark, pendidikan, bisnis, infrastruktur — research per kota.
- **`proyek_publik` section**: HARUS berisi proyek NYATA di kota tersebut dengan nama proyek, tahun, deskripsi, jumlah batang, diameter, hasil. Jangan isi placeholder.
- **`# Instruksi:` lines**: `sed -n '/# Instruksi:/p'` the post to find all — then delete them all.

## Workflow: Section-by-Section (WAJIB)

- **REPORT-FIRST protocol** — User calls out a section name (e.g. "# SECTION KEUNGGULAN - LAYANAN"). You READ that section only (targeted line range), REPORT back which lines are still instructions, WAIT for user to say "ya, perbaiki", then FIX only that section, VERIFY. Never fix without confirmation.
- **Answer first, THEN modify** — When user asks about status/content of a section, ANSWER directly from what you already know. Jangan mulai baca file/ubah dokumen sebelum menjawab pertanyaan.
- **Report as TABLE, not raw dump** — When user asks "mana yang masih instruksi", output a table:
  | Baris | Key | Masih instruksi? |
  |-------|-----|------------------|
  | L230  | `tahan_lama` | YA — `"jelaskan daya tahan..."` |
  Raw file output gets CCR-encoded (unreadable). Summary table is immediately actionable.
- **"Jawab, jangan baca file" = STOP reading** — When user says this, stop all file-read operations entirely. Answer from context you already have. If context insufficient, say so directly.
- **Read section-by-section, not the whole document** — File is 700+ lines → truncation/CCR encoding. Always target the specific section by line range.
- **Use execute_code for targeted reads (BEST)** — Avoid `read_file` and `terminal` for section reads; they get CCR-truncated. Use `execute_code` to find section start, print lines with ` <-- INSTRUKSI` markers, and scan for placeholders. Example in SKILL.md.
- **grep one section at a time** — Use:
  ```bash
  grep -n "SECTION NAME" file.md  # get line numbers
  ```
- **Don't speculate** — If output is truncated, say so and ask which specific section to check.
- **Patch failure recovery** — When `patch` returns "modified since you last read it on disk", DO NOT guess old_string. Use `execute_code` with `content.find() + repr(content[i:end])` to get the file's EXACT whitespace/indentation then build a matching old_string. This avoids second failure.
- **CCR-encoded output workaround** — When `read_file` or `terminal` output gets CCR-encoded (unreadable), switch to `execute_code` with Python `print()` statements. For section reads, print line-by-line with `f"{i+1}|{lines[i].rstrip()}"`. For section extraction, use `content.find()` + `print(repr(section))` to get exact text with all whitespace visible.

## Section Content Reference (NEW)

Setiap section type punya struktur YAML spesifik. Lihat `references/section-content-patterns.md` untuk format exact:
- **Aplikasi Kayu Dolken** — 4 sub-groups × 5 items each: konstruksi_dekorasi (2 cards) + furniture_komersial (2 cards)
- **Studi Kasus Residensial** — 4+ items dengan field: judul, lokasi, tahun, deskripsi, jumlah, diameter, hasil, warna, icon
- **Studi Kasus Publik** — 2+ items, field sama — HARUS proyek publik NYATA (taman kota, balai desa, Islamic Center)
- **Testimoni Residential** — nama orang + lokasi=kecamatan, rating=5, judul, komentar personal natural, warna
- **Testimoni Komersial** — nama orang + lokasi=profesi/bisnis+area, rating=5, judul, komentar dari sudut bisnis
- **Keunggulan Produk - Durabilitas** — DUAL FORMAT: object (`keunggulan_durabilitas`: 4 field + `keunggulan_nilai`: 2 field) AND array (`keunggulan_kayu_dolken`: 6 items × judul+deskripsi+warna+icon). Both must be filled. Template says "opsional" for object but FILL BOTH.
- **Tips Memilih Ukuran** — 3 categories (Ringan/Sedang/Berat) each with 3 `keunggulan:` items. Header says "BOLEH PAKAI LANGSUNG" but keunggulan still has `"keunggulan #1-3"` placeholders — must fix.
- **FAQ sections** — 3 separate sections: FAQ PEMESANAN (2 items), FAQ PRODUK (2 items, fix `{nama_kota}` placeholder), FAQ PENGIRIMAN (1 item, fix `{nama_kota}`). Each has `pertanyaan:` + `jawaban:` + `icon:`.
- **Relevansi Kayu Dolken** — `karakteristik_iklim` (jelaskan kontras iklim kota: pesisir+pegunungan+dll) + `keunggulan_lokal` (generic, boleh pakai) + `aplikasi_lokal` (4 items with lokasi SPESIFIK).
- **Tentang Kota (tersulit)** — 4 cards total: `tentang_kota_1` (2 cards with `fakta:` array), `tentang_kota_2` (2 cards with `list_item:` array). `info_tambahan` field only on card #4. Setiap card: judul, icon (bi-*), subjudul, icon_subjudul, deskripsi. Topik bebas — riset per kota.

Gunakan referensi ini saat menuliskan `new_string` untuk patch.

## User Preferences (from session)
- **Concise, direct communication** – user prefers terse answers with no filler phrases or hedging. Respond with minimal ceremony; drop pleasantries, hedging, and explicit reasoning for trivial decisions.
- **Indonesian language** – all generated content and documentation must be in Bahasa Indonesia.
- **GitHub credential handling** – store tokens per‑repo using `git config credential.helper store` WITHOUT `--global` and enable `credential.useHttpPath true` to isolate credentials per repository.
- **Template is sacred** – never edit the template file in `TEMPLATES/`; always copy to `_post_with_city/` first.
- **Wrong layout** – post kota (`_post_with_city/`) HARUS `layout: node--post-with-city`, BUKAN `node--post-with-product`. Wrong layout causes blank/empty rendered page.
- **TEMPLATE fields are sacred** – jangan HAPUS field dari TEMPLATE walau terkesan tidak dipakai. `author_url`, `keunggulan_durabilitas`, `keunggulan_nilai` adalah bagian struktur template.
- **cwebp conversion** – sumber foto di `/home/mkt01/Documents/ANDRI/Dolken/foto/WhatsApp Unknown/`. Convert: `cwebp -q 85 {input.jpeg} -o assets/images/posts/jual-kayu-dolken-{kota}/jual-kayu-dolken-{kota}-00N.webp`
- **GitHub Actions Node 24** – update action versions: `actions/checkout@v7`, `actions/configure-pages@v6`, `actions/upload-pages-artifact@v5`, `actions/deploy-pages@v5`.
- **Verifikasi setelah deploy** – page kosong/tidak seperti post lain? Cek `layout:` di frontmatter dulu sebelum cari masalah lain.
- **Patch vs replace** – untuk fix placeholder di section, gunakan `patch` tool dengan exact `old_string`/`new_string` matching file indentation (2/4/6 spasi). Jangan pakai `content.replace()` — indentasi di file tidak selalu match ekspektasi.