# Required front‑matter fields for TEMPLATE--post-with-city.md

## META (REQUIRED)
- layout: `node--post-with-city`
- title: include kota, nomor HP, "Gratis Ongkir & COD"
- description: 150-160 chars SEO meta
- date: `YYYY-MM-DD`
- author: Admin
- author_url: https://jualkayudolkengelam.github.io
- image: path to 001.webp
- image_alt: alt text
- images: list of 2-4 WebP paths
- images_alt: alt text per image
- keywords: 6-8 SEO keywords

## CITY & SHIPPING (REQUIRED)
- show_products: true
- rating: 4.5
- review_count: 0
- nama_kota
- area_pengiriman: list of 5-10 kecamatan/area
- keunggulan_produk: array of 3 items (judul, deskripsi, warna, icon)
- keunggulan_layanan: array of 3 items (judul, deskripsi, warna, icon)

## AREA PENGIRIMAN DETAIL (REQUIRED — many sub‑fields)
- area_pengiriman_detail:
  - judul_jangkauan, deskripsi_jangkauan
  - judul_pusat, deskripsi_pusat
  - judul_utara_selatan, deskripsi_utara_selatan (OPTIONAL)
  - judul_pengembangan, deskripsi_pengembangan
  - judul_lainnya (OPTIONAL)
  - judul_landmark, deskripsi_landmark
  - judul_wisata, deskripsi_wisata
  - judul_fasilitas, deskripsi_fasilitas
  - wilayah_pusat: array (min 3 items with nama, kelurahan[], warna)
  - wilayah_pengembangan: array (min 2 items)
  - landmark_wisata: array (min 3 items with nama, icon, warna)
  - landmark_fasilitas: array (min 3 items with nama, icon, warna)

## ORDER & SHIPPING (REQUIRED)
- proses_awal_pemesanan: pilih_ukuran, hubungi, konsultasi_gratis
- finalisasi_pengiriman: konfirmasi_pesanan, pengiriman_gratis, bayar_cod

## EXTRA SECTIONS (REQUIRED for SEO)
- studi_kasus_proyek:
  - proyek_komersial: min 2 items
  - proyek_residensial: min 2 items
  - proyek_publik (OPTIONAL)
- testimoni_residential: min 2 items (nama, lokasi, rating, judul, komentar, warna)
- testimoni_komersial: min 2 items
- tips_ukuran: 3 kategori (Ringan, Sedang, Berat)
- faq_pemesanan: min 2 items
- faq_produk: min 1 item
- faq_pengiriman: min 1 item
- relevansi_kayu_dolken: karakteristik_iklim, keunggulan_lokal, aplikasi_lokal[]
- tentang_kota: tagline, deskripsi_singkat, overview, tentang_kota_1[], tentang_kota_2[]

## META (OPTIONAL but recommended)
- like_count, comment_count, share_count, total_updates, last_modified_at
