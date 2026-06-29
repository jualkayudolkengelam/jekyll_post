# TEMPLATE--post-with-city.md — Content Template Structure

## Purpose
This is a **content creation template** (NOT a Jekyll layout/technical file).
Use it to scaffold SEO-optimized blog posts for "jual kayu dolken" (selling Dolken wood) targeted at a specific city.

## Internal Title
> TEMPLATE: POST WITH PRODUCT (Format Instruksi) v2.0.0 (2025-11-19)

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
| `layout` | Jekyll layout |
| `title` | Post title (include city name) |
| `description` | SEO meta description |
| `date` | Post date |
| `author` | Author name |
| `image` | Featured image path |
| `keywords` | SEO keywords |
| `nama_kota` | Target city name |
| `area_pengiriman` | List of 5-10 subdistricts |
| `keunggulan_produk` | 3 items (title, description, color, icon) |
| `keunggulan_layanan` | 3 items (title, description, color, icon) |
| `area_pengiriman_detail` | Delivery area segments with descriptions |
| `wilayah_pusat` | Central area subdistricts + villages |
| `wilayah_utara_selatan` | North/south area subdistricts |
| `wilayah_pengembangan` | Development area subdistricts |
| `landmark_wisata` | ≥3 tourist landmarks |
| `landmark_fasilitas` | ≥3 facility landmarks |
| `keunggulan_durabilitas` | Optional, 6 items suggested |
| `keunggulan_kayu_dolken` | Optional, 6 items suggested |
| `aplikasi_kayu_dolken` | Application categories |
| `studi_kasus_proyek_komersial` | ≥4 commercial project cases |
| `studi_kasus_proyek_residensial` | ≥4 residential project cases |
| `testimoni_residential` | ≥2 residential testimonials |
| `testimoni_komersial` | ≥4 commercial testimonials |
| `tips_ukuran` | 3 size categories (ringan, sedang, berat) |
| `faq_pemesanan` | Ordering FAQs |
| `faq_produk` | Product FAQs |
| `faq_pengiriman` | Delivery FAQs |
| `relevansi_kayu_dolken` | Climate & local relevance |
| `tentang_kota` | 4 card-style city overview |
| `like_count`, `comment_count`, `share_count` | Social metrics |
| `proses_awal_pemesanan` | Ordering process text |
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
