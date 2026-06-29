# Template Model — Empty-Field Design

## Ringkasan

Template TEMPLATE--post-with-city.md mengadopsi model "empty-field" — semua value field frontmatter di-set `null` (kosong), dengan instruksi pengisian dipindah ke YAML comment. Ini dirancang untuk workflow agentic REPORT → WAIT → FIX per-section.

## Struktur Frontmatter

- **Field meta (title, description, excerpt, date, author)**: wajib pre-filled dengan placeholder `{kota}` agar pipeline sukses. Editor/Reviewer menolak null values di field-field ini.
- **Field section content**: kosong (`null`), instruksi ada di YAML comment. Diisi satu per satu oleh user via REPORT → WAIT → FIX.
- **Field structural (layout, image, images, dll)**: berisi path/branding, bukan content — biarkan apa adanya.

## Pipeline Behavior

```
TEMPLATE (empty/null fields)
  → Writer: substitusi {kota} placeholder generik
  → Editor: validasi YAML + scan placeholder leak
  → Reviewer: cek meta field ada + non-null, images path, layout
  → OUTPUT: draft .md siap diisi section-by-section
```

## Checklist Pre-run

Sebelum pipeline bisa sukses dengan model ini:

- [x] Meta fields pre-filled dengan placeholder valid (title, description, excerpt, date, author)
- [ ] Research cache tersedia di `/tmp/research-output/{city}.json` (atau skip-research untuk test)
- [x] Template path benar: `templates/` (lowercase), bukan `TEMPLATES/`
- [ ] Images 001-004.webp tersedia di `assets/images/posts/jual-kayu-dolken-{kota}/`

## Revalidasi Setelah Perubahan

Setiap kali mengedit template, jalankan test pipeline:
```bash
echo '{"city": "TestKota"}' > /tmp/research-output/testkota.json
python3 entrypoint.py --city "TestKota" --skip-research --output /tmp/test.md
# Expected: exit 0
```