# TEMPLATE--post-with-city.md — Content Template Structure

## Purpose
This is a **content creation template** (NOT a Jekyll layout/technical file).
Use it to scaffold SEO-optimized blog posts for "jual kayu dolken" (selling Dolken wood) targeted at a specific city.

## Internal Title
> TEMPLATE: POST WITH CITY (Format Instruksi) v2.0.0 (2025-11-19)

## File Naming
```
YYYY-MM-DD-jual-kayu-dolken-{kota}.md
```
Place in `_post_with_city/` directory.

## Photo Requirements (WebP)
4 product photos required:
```
mkdir -p assets/images/posts/jual-kayu-dolken-{kota}/
```
Copy and rename 4 photos into that directory. Format MUST be WebP.

## Frontmatter Fields
| Field | Description |
|-------|-------------|
| `layout` | Jekyll layout (must be `node--post-with-city`) |
| `title` | Post title (include city name) |
| `description` | SEO meta description (150-160 chars) |
| `date` | Post date (YYYY-MM-DD) |
| `author` | Author name |
| `image` | Featured image path |
| `keywords` | SEO keywords |
| `nama_kota` | Target city name |
| `area_pengiriman` | List of 5-10 subdistricts |
| `keunggulan_produk` | 3 items (title, description, color, icon) |
| `keunggulan_layanan` | 3 items (title, description, color, icon) |
| `area_pengiriman_detail` | Nested container — includes: judul_jangkauan, deskripsi_jangkauan, judul/deskripsi for (pusat, utara_selatan, pengembangan, lainnya, landmark, wisata, fasilitas), then wilayah_pusat (≥3 items), wilayah_utara_selatan (OPTIONAL), wilayah_pengembangan (≥2), kecamatan_lainnya (OPTIONAL), landmark_wisata (≥3), landmark_fasilitas (≥3) — ALL nested under this single key, NOT top-level |
| `keunggulan_durabilitas` | OPTIONAL. DUPLICATE KEY: appears at L71 stub (3 keys) AND L251 detailed (4 keys incl anti_rayap, tahan_cuaca). Use L251; delete L71-77 stub to avoid YAML conflict |
| `keunggulan_nilai` | OPTIONAL. DUPLICATE KEY: appears at L75 stub (2 keys) AND L257 detailed (2 keys: ramah_lingkungan, estetika). Use L257; delete L75-77 stub |
| `keunggulan_kayu_dolken` | Array format, 6 items (newer format, recommended over durabilitas/nilai) |
| `aplikasi_kayu_dolken` | 4 sub-groups (konstruksi_dekorasi 2x, furniture_komersial 2x), 5 aplikasi per group |
| `studi_kasus_proyek` | Single top-level key — nested: proyek_komersial (≥4), proyek_residensial (≥4), proyek_publik (≥2, OPTIONAL). NOT three separate top-level keys |
| `testimoni_residential` | ≥2 residential testimonials |
| `testimoni_komersial` | ≥4 commercial testimonials |
| `tips_ukuran` | 3 size categories (ringan, sedang, berat) — pre-filled, boleh pakai langsung |
| `faq_pemesanan` | Ordering FAQs (min 2) |
| `faq_produk` | Product FAQs (min 2) |
| `faq_pengiriman` | Delivery FAQs (min 1) |
| `relevansi_kayu_dolken` | Climate & local relevance |
| `tentang_kota` | 4 cards: tentang_kota_1 (2 cards with fakta), tentang_kota_2 (2 cards with list_item) |
| `like_count`, `comment_count`, `share_count` | Social metrics |
| `proses_awal_pemesanan` | Ordering process text — pre-filled, boleh pakai langsung |
| `finalisasi_pengiriman` | Delivery finalization text |

## Content Sections (HTML includes referenced in layout)
- `hero-jual-kayu-dolken`
- `mengapa-memilih-kami`
- `area-pengiriman-kayu-dolken`
- `hubungi-kami`
- (and other section includes)

## Pitfalls
- This template is for **content creation**, not Jekyll layout engineering. Don't analyze it as if it were a theme file.
- All photos must be WebP format — the template assumes this.
- Fill every city-specific field; generic/placeholder text must be replaced per city.
- **Duplicate YAML keys**: `keunggulan_durabilitas` and `keunggulan_nilai` each appear 2x (L71-77 stub + L251-259 detailed). YAML parser only reads one. Delete the stub, keep detailed version.
- **Nested keys under area_pengiriman_detail**: `wilayah_pusat`, `wilayah_utara_selatan`, `wilayah_pengembangan`, `kecamatan_lainnya`, `landmark_wisata`, `landmark_fasilitas` are nested under `area_pengiriman_detail` at 2-space indent, NOT top-level keys.
- **studi_kasus_proyek** is ONE top-level key with nested `proyek_komersial`/`proyek_residensial`/`proyek_publik`, NOT three separate top-level keys.
- **Placeholder "jelaskan..."** is used extensively in template (deskripsi, hasil, jawaban fields) but is NOT caught by detection patterns that only look for "tulis/isi/berikan". Always include "jelaskan" in grep/scan patterns.
- **Typo at L534**: "# ini Contoh, silahkan gati kata - katanya." — "gati" should be "ganti". Fix when revising template.