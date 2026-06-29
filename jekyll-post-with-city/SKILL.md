---
name: jekyll-post-with-city
description: "Workflow for building a Jekyll post for a city using TEMPLATE--post-with-city.md – image prep, frontmatter, sections, content fill, commits, and pitfall notes.

## Cross‑Agent Compatibility

The workflow is **tool‑agnostic**.  Any LLM agent that can run a shell command (Hermes, Claude Code, OpenAI CLI, etc.) can invoke the entrypoint script `jekyll-post-with-city/entrypoint.py`.  The script implements the same four‑agent pipeline (Research → Writer → Editor → Reviewer) using *only* standard Python libraries and the `execute_code` helper when the host provides it.  The skill therefore works out‑of‑the‑box on any platform that supports:

- Python 3.9+
- `git` on the repository
- Internet access for the Research step

Agents should call the script rather than manually paste the whole pipeline, which keeps token usage low and ensures consistent behaviour across environments."
---

# Jekyll Post with City

Build a Jekyll post for one city using the `TEMPLATE--post-with-city.md`.

## Prerequisites
- Jekyll site with `_post_with_city/` directory
- TEMPLATE at `TEMPLATES/TEMPLATE--post-with-city.md`
- 2 source photos in WebP format (cwebp -q 80-85)
- Real city info: kecamatan, landmark, proyek, testimoni

## Quick Steps

1. **Copy template** → `_post_with_city/{date}-jual-kayu-dolken-{kota}.md` (JANGAN edit file TEMPLATES/)
2. **Set images**: `images/` dir, convert WebP, set `images: []` + `images_alt: []`
3. **Fill frontmatter**: `nama_kota`, `meta_*`, title, keywords, area_pengiriman
4. **Fill sections one-by-one** — gunakan REPORT → WAIT → FIX workflow
5. **Verify YAML** — `python3 -c "import yaml; yaml.safe_load(open('_post_with_city/{post}.md'))"`
6. **Build** — `bundle exec jekyll build 2>&1 | tail -20`

## Section-by-Section Fill Workflow (WAJIB)

Step flow untuk setiap section:

1. **READ** — gunakan `execute_code` untuk cari section start, cetak semua baris dengan marker ` <-- INSTRUKSI` untuk yang masih placeholder
2. **REPORT** — tampilkan tabel: Baris | Key | Masih instruksi?
3. **WAIT** — user bilang "ya" sebelum fix
4. **FIX** — `patch` dengan exact `old_string`/`new_string` dari konten real
5. **VERIFY** — `execute_code` scan ulang section, pastikan 0 instruksi
6. **KONFIRMASI** — "SECTION X — SELESAI"

### Teknik Baca Section (hindari CCR truncation)

Gunakan `execute_code` bukan `read_file`:

```python
with open('_post_with_city/{file}.md', 'r') as f:
    lines = f.readlines()

start = None
for i, l in enumerate(lines):
    if 'SECTION NAMA SECTION' in l:
        start = i
        break

for i in range(start, min(start+80, len(lines))):
    l = lines[i].rstrip()
    marker = ''
    if 'Instruksi' in l:
        marker = ' <-- INSTRUKSI'
    elif '"' in l and any(kw in l[:60].lower() for kw in ['tulis ', 'isi ', 'berikan ']):
        marker = ' <-- INSTRUKSI'
    print(f"{i+1}|{l}{marker}")
    if l.startswith('# SECTION ') and i > start and 'NAMA' not in l:
        break
```

### Untuk dapat exact content untuk patch (setelah warning "file was modified"):

```python
i = content.find('# SECTION NAMA')
end = content.find('# SECTION', i + 1)
section = content[i:end]
print(repr(section))  # dapatkan exact text untuk old_string
```

## Section Reference

Each section has a specific structure. See `references/section-content-patterns.md` for the exact YAML format of every section type.

**Typical sections (in order):**
1. Intro / basic fields (title, meta, images, nama_kota)
2. AREA PENGIRIMAN (kecamatan simple list + detail)
3. KEUNGGULAN (layanan, durabilitas, nilai, kayu_dolken)
4. APLIKASI KAYU DOLKEN (4 sub-groups, 5 items each)
5. PROSES PEMESANAN
6. STUDI KASUS (residensial 4+ items, publik 2+ items)
7. TESTIMONI (residential 2+, komersial 4+)
8. TIPS MEMILIH UKURAN
9. TENTANG KOTA (4 cards—sejarah, budaya, kuliner, wisata, dll)
10. FAQ (umum + spesifik kota)
11. CTA / RELEVANSI / PENUTUP

## Reference Files
- `references/post-nasional-flow.md` — Overall sequential flow
- `references/jekyll-post-fields.md` — Complete field list per section
- `references/template-structure.md` — Template layout / block diagram
- `references/pitfalls-and-user-preferences.md` — All pitfalls + user preferences (crucial — READ FIRST)
- `references/section-content-patterns.md` — Exact YAML format per section type (NEW)
- `references/multi-agent-pipeline.md` — Multi-agent pipeline definition + entrypoint script (NEW)

## Common Pitfalls
- **Tool output truncation** — `read_file`, `terminal`, `execute_code` all suffer CCR encoding. Use `execute_code` with targeted line ranges, not whole-file reads.
- **Patch fails with "file was modified"** — konten file mungkin beda dari yang dibaca. Gunakan `repr()` untuk dapat exact text, lalu patch dengan `old_string` exact.
- **Template has duplicate YAML keys** — `keunggulan_durabilitas` dan `keunggulan_nilai` muncul 2x (sekitar L66 instruksi, sekitar L245 konten). Pastikan patch target yang benar.
- **Testimoni lokasi: Residential = kecamatan, Komersial = profesi/bisnis + area** — jangan tertukar.
- **Aplikasi: 4 sub-groups, 5 aplikasi per group** — jangan kurang dari 5 items.
- **Studi kasus: butuh `lokasi` field** — template tidak selalu punya, tambahkan jika kurang.
