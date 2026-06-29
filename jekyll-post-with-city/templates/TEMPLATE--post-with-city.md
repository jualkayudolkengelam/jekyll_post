---
# ============================================================================
# TEMPLATE: POST WITH CITY (Format Instruksi)
# ============================================================================
# File: TEMPLATE--post-with-city.md
# Purpose: Template untuk membuat artikel post_with_city dengan konten UNIQUE
# Version: 2.0.0 (Instruction Format)
# Date: 2025-11-19
#
# CARA PENGGUNAAN:
# 1. Copy file ini ke _post_with_city/ dengan nama: YYYY-MM-DD-jual-kayu-dolken-{kota}.md
# 2. Siapkan 4 foto produk (PENTING: harus format WebP):
#    a. Buat direktori:
#       mkdir -p assets/images/posts/jual-kayu-dolken-{kota}/
#    b. Copy 1,2,3,atau 4 foto sesuai yang diberikan ke direktori dan rename:
#       cp foto1.jpg assets/images/posts/jual-kayu-dolken-{kota}/jual-kayu-dolken-{kota}-001.jpeg
#       cp foto2.jpg assets/images/posts/jual-kayu-dolken-{kota}/jual-kayu-dolken-{kota}-002.jpeg
#       (dst untuk 003 dan 004)
#    c. Convert semua JPEG ke WebP (akan menghasilkan file .webp baru):
#       cd assets/images/posts/jual-kayu-dolken-{kota}/
#       for file in *.jpeg; do cwebp -q 85 "$file" -o "${file%.jpeg}.webp"; done
#    d. Hapus file JPEG yang lama (sekarang ada 2x file: .jpeg dan .webp):
#       rm *.jpeg
#    e. Pastikan hanya ada 4 file .webp: 001.webp, 002.webp, 003.webp, 004.webp
# 3. Baca INSTRUKSI di setiap field (yang ditulis dengan huruf kecil)
# 4. Ganti instruksi dengan konten yang sesuai untuk kota tersebut
# 5. Field yang sudah ada teksnya (UPPERCASE) bisa dipakai langsung atau disesuaikan
# 6. Test dengan rebuild.sh sebelum commit
#
# CATATAN PENTING:
# - Field dengan "isi ..." atau "tulis ..." atau "berikan ..." = HARUS DITULIS MANUAL
# - Field dengan teks lengkap (misal: "Kualitas Premium Grade A") = boleh pakai langsung
# - Jangan ubah struktur frontmatter (nama field, hierarki, indentasi)
# - Semua section dengan REQUIRED wajib diisi
# - Section OPTIONAL boleh dihapus jika tidak relevan
# - PENTING: Semua foto HARUS dalam format WebP (bukan JPEG/PNG) untuk optimasi performa
# ============================================================================

# ============================================================================
# META INFORMATION (REQUIRED)
# ============================================================================
layout: node--post-with-city
title: "Judul Artikel — Nama Kota —  Hubungi 0813-1140-0177 — Tagline"
description: "Deskripsi meta untuk SEO, 150-160 karakter."
excerpt: "Ringkasan singkat untuk tampilan grid/card."
date: YYYY-MM-DD
author: Admin
image: /assets/images/posts/jual-kayu-dolken-{nama_kota}/jual-kayu-dolken-{nama_kota}-001.webp
image_alt: "Jual Kayu Dolken {Nama Kota} — kualitas premium"
images:
  - /assets/images/posts/jual-kayu-dolken-{nama_kota}/jual-kayu-dolken-{nama_kota}-001.webp
  - /assets/images/posts/jual-kayu-dolken-{nama_kota}/jual-kayu-dolken-{nama_kota}-002.webp
  - /assets/images/posts/jual-kayu-dolken-{nama_kota}/jual-kayu-dolken-{nama_kota}-003.webp
  - /assets/images/posts/jual-kayu-dolken-{nama_kota}/jual-kayu-dolken-{nama_kota}-004.webp
images_alt:
  - "Jual Kayu Dolken {Nama Kota} — foto 1"
  - "Jual Kayu Dolken {Nama Kota} — foto 2"
  - "Jual Kayu Dolken {Nama Kota} — foto 3"
  - "Jual Kayu Dolken {Nama Kota} — foto 4"
last_modified_at: YYYY-MM-DD
keywords: "kata kunci, pisah koma, seo"
rating: 5
review_count: 120
author_url: https://jualkayudolken.com
show_products: true
keunggulan_durabilitas:
  tahan_lama: "Isi dengan keunggulan daya tahan (contoh: tahan 20-30 tahun, anti rayap)"
  kuat_padat: "Isi dengan keunggulan kekuatan dan kepadatan"
  minim_perawatan: "Isi dengan keunggulan perawatan mudah"
keunggulan_nilai:
  ramah_lingkungan: "Isi dengan keunggulan ramah lingkungan"
  hemat_biaya: "Isi dengan keunggulan hemat biaya jangka panjang"
nama_kota: "NamaKota"

# ============================================================================
# AREA PENGIRIMAN (SIMPLE LIST) - REQUIRED
# ============================================================================
# Instruksi: Isi 5-10 area/kecamatan populer di kota ini
area_pengiriman:
  - "isi nama kecamatan/area populer #1"
  - "isi nama kecamatan/area populer #2"
  - "isi nama kecamatan/area populer #3"
  - "isi nama kecamatan/area populer #4"
  - "isi nama kecamatan/area populer #5"
  # Tambahkan hingga 10 area jika perlu

# ============================================================================
# KEUNGGULAN - PRODUK (REQUIRED)
# ============================================================================
# Instruksi: HARUS 3 items. Tulis keunggulan produk yang disesuaikan dengan kota
keunggulan_produk:
  - judul: "berikan judul keunggulan produk #1 (misal: Kualitas Premium, Tahan Lama, dll)"
    deskripsi: "jelaskan keunggulan ini, sesuaikan dengan karakteristik iklim/kondisi kota (misal: cocok untuk iklim pesisir/dataran tinggi/metropolitan)"
    warna: "warning"
    icon: "bi-award-fill"
  - judul: "berikan judul keunggulan produk #2 (misal: Harga Terjangkau, Harga Terbaik, dll)"
    deskripsi: "jelaskan keunggulan harga, mention harga mulai Rp 15.000/batang atau sesuaikan dengan market kota"
    warna: "danger"
    icon: "bi-cash-coin"
  - judul: "berikan judul keunggulan produk #3 (misal: Stok Lengkap, Selalu Ready, dll)"
    deskripsi: "jelaskan ketersediaan stok, mention diameter yang tersedia (2-12 cm)"
    warna: "info"
    icon: "bi-boxes"

# ============================================================================
# KEUNGGULAN - LAYANAN (REQUIRED)
# ============================================================================
# Instruksi: HARUS 3 items. Tulis keunggulan layanan yang disesuaikan dengan kota
keunggulan_layanan:
  - judul: "berikan judul keunggulan layanan #1 (misal: Pengiriman Gratis [Nama Kota], Free Ongkir [Kota], dll)"
    deskripsi: "jelaskan keunggulan pengiriman gratis, mention area kota yang dicakup, benefit untuk customer"
    warna: "success"
    icon: "bi-truck"
  - judul: "berikan judul keunggulan layanan #2 (misal: COD Tersedia, Bayar di Tempat, dll)"
    deskripsi: "jelaskan sistem pembayaran COD, benefit aman untuk customer, cek kualitas dulu"
    warna: "primary"
    icon: "bi-shield-check"
  - judul: "berikan judul keunggulan layanan #3 (misal: Fast Response, Konsultasi Gratis, dll)"
    deskripsi: "jelaskan layanan konsultasi/response cepat, mention 24/7 atau waktu operasional"
    warna: "secondary"
    icon: "bi-headset"

# ============================================================================
# AREA PENGIRIMAN DETAIL - TEKS JUDUL & DESKRIPSI (REQUIRED)
# ============================================================================
# Instruksi: Semua field di bawah HARUS ditulis manual sesuai karakteristik kota
area_pengiriman_detail:
  judul_jangkauan: "berikan judul untuk jangkauan pengiriman di kota ini"
  deskripsi_jangkauan: "jelaskan area mana saja yang dilayani di kota ini, mention gratis ongkir dan jumlah kecamatan"

  judul_pusat: "berikan judul untuk wilayah pusat kota ini"
  deskripsi_pusat: "jelaskan mengapa wilayah pusat kota ini strategis, mention jumlah kecamatan dan akses mudah"

  judul_utara_selatan: "berikan judul untuk wilayah utara & selatan (OPTIONAL - hapus jika tidak relevan)"
  deskripsi_utara_selatan: "jelaskan karakteristik wilayah utara & selatan kota ini (OPTIONAL - hapus jika tidak ada)"

  judul_pengembangan: "berikan judul untuk wilayah pengembangan/pinggiran kota ini"
  deskripsi_pengembangan: "jelaskan karakteristik area pengembangan, mention pertumbuhan dan potensi"

  judul_lainnya: "berikan judul untuk kecamatan lainnya (OPTIONAL - hapus jika tidak perlu)"

  judul_landmark: "berikan judul untuk landmark & lokasi strategis di kota ini"
  deskripsi_landmark: "jelaskan mengapa landmark ini penting untuk proyek komersial"

  judul_wisata: "berikan judul untuk destinasi wisata di kota ini"
  deskripsi_wisata: "jelaskan landmark wisata dan sejarah yang terkenal di kota ini"

  judul_fasilitas: "berikan judul untuk fasilitas pendidikan & komersial di kota ini"
  deskripsi_fasilitas: "jelaskan fasilitas strategis seperti kampus, mall, pelabuhan di kota ini"

# ============================================================================
# AREA PENGIRIMAN DETAIL - WILAYAH PUSAT (REQUIRED - min 3 items)
# ============================================================================
# Instruksi: Research kecamatan NYATA di pusat kota ini, cari kelurahan yang ada
  wilayah_pusat:
    - nama: "isi nama kecamatan pusat #1"
      kelurahan:
        - "isi 3-5 kelurahan di kecamatan ini"
        - "isi kelurahan lainnya (bisa gabung beberapa dengan koma)"
      warna: "primary"
    - nama: "isi nama kecamatan pusat #2"
      kelurahan:
        - "isi 3-5 kelurahan di kecamatan ini"
      warna: "success"
    - nama: "isi nama kecamatan pusat #3"
      kelurahan:
        - "isi 3-5 kelurahan di kecamatan ini"
      warna: "info"
    # Tambah lebih banyak jika perlu (5-7 kecamatan ideal)

# ============================================================================
# AREA PENGIRIMAN DETAIL - WILAYAH UTARA & SELATAN (OPTIONAL)
# ============================================================================
# Instruksi: Hapus section ini jika kota tidak punya pembagian utara-selatan yang jelas
  wilayah_utara_selatan:
    - nama: "isi nama kecamatan di bagian utara kota"
      kelurahan:
        - "isi kelurahan di kecamatan ini"
      warna: "danger"
    - nama: "isi nama kecamatan di bagian selatan kota"
      kelurahan:
        - "isi kelurahan di kecamatan ini"
      warna: "warning"

# ============================================================================
# AREA PENGIRIMAN DETAIL - WILAYAH PENGEMBANGAN (REQUIRED - min 2 items)
# ============================================================================
# Instruksi: Isi kecamatan yang sedang berkembang/pinggiran kota
  wilayah_pengembangan:
    - nama: "isi nama kecamatan pengembangan #1"
      kelurahan:
        - "isi kelurahan di kecamatan ini"
      warna: "primary"
    - nama: "isi nama kecamatan pengembangan #2"
      kelurahan:
        - "isi kelurahan di kecamatan ini"
      warna: "info"
    - nama: "isi nama kecamatan pengembangan #3"
      kelurahan:
        - "isi kelurahan di kecamatan ini"
      warna: "wood"

# ============================================================================
# AREA PENGIRIMAN DETAIL - KECAMATAN LAINNYA (OPTIONAL)
# ============================================================================
# Instruksi: Isi kecamatan tambahan yang tidak masuk kategori lain (OPTIONAL - bisa dihapus)
  kecamatan_lainnya:
    - "isi nama kecamatan tambahan #1"
    - "isi nama kecamatan tambahan #2"
    - "isi nama kecamatan tambahan #3"

# ============================================================================
# AREA PENGIRIMAN DETAIL - LANDMARK WISATA (REQUIRED - min 3 items)
# ============================================================================
# Instruksi: Isi landmark WISATA dan sejarah yang terkenal di kota ini
  landmark_wisata:
    - nama: "isi nama landmark wisata/sejarah #1"
      icon: "bi-building"
      warna: "warning"
    - nama: "isi nama landmark wisata/sejarah #2"
      icon: "bi-building"
      warna: "warning"
    - nama: "isi nama landmark wisata/sejarah #3"
      icon: "bi-building"
      warna: "warning"

# ============================================================================
# AREA PENGIRIMAN DETAIL - LANDMARK FASILITAS (REQUIRED - min 3 items)
# ============================================================================
# Instruksi: Isi fasilitas strategis seperti mall, kampus, pelabuhan di kota ini
  landmark_fasilitas:
    - nama: "isi nama mall/pusat perbelanjaan terkenal"
      icon: "bi-cart"
      warna: "info"
    - nama: "isi nama mall/pusat perbelanjaan lainnya"
      icon: "bi-cart"
      warna: "primary"
    - nama: "isi nama kampus/universitas/pelabuhan terkenal"
      icon: "bi-mortarboard"  # gunakan bi-shop untuk pelabuhan
      warna: "success"

# ============================================================================
# KEUNGGULAN PRODUK - DURABILITAS (OPTIONAL)
# ============================================================================
# Instruksi: Format lama (object), OPTIONAL - bisa dihapus jika pakai keunggulan_kayu_dolken (array) di bawah
keunggulan_durabilitas:
  tahan_lama: "jelaskan daya tahan kayu gelam 20-30 tahun, sesuaikan dengan iklim kota ini"
  anti_rayap: "jelaskan keunggulan anti rayap natural tanpa obat"
  tahan_cuaca: "jelaskan cocok untuk outdoor/indoor, tahan hujan/panas, mention karakteristik cuaca kota ini"
  kuat_padat: "jelaskan kepadatan tinggi, cocok untuk beban berat"

keunggulan_nilai:
  ramah_lingkungan: "jelaskan material natural, sustainable, mendukung green building"
  estetika: "jelaskan warna natural coklat, cocok untuk dekorasi modern/tradisional"

# Format Array (lebih baru, direkomendasikan) - HARUS 6 items
keunggulan_kayu_dolken:
  - judul: "berikan judul keunggulan #1 (misal: Tahan Lama, Awet Puluhan Tahun, dll)"
    deskripsi: "jelaskan daya tahan 20-30 tahun tanpa treatment, sesuaikan dengan iklim kota ini (pesisir/dataran tinggi/metropolitan)"
    warna: "success"
    icon: "bi-clock-history"
  - judul: "berikan judul keunggulan #2 (misal: Anti Rayap, Tahan Hama, dll)"
    deskripsi: "jelaskan tidak perlu obat anti rayap, tekstur padat menolak rayap natural"
    warna: "danger"
    icon: "bi-bug"
  - judul: "berikan judul keunggulan #3 (misal: Tahan Cuaca, Tahan Air, dll)"
    deskripsi: "jelaskan cocok outdoor/indoor, tahan hujan/panas/lembab, mention kondisi cuaca kota ini"
    warna: "primary"
    icon: "bi-cloud-rain"
  - judul: "berikan judul keunggulan #4 (misal: Kuat & Padat, Super Kuat, dll)"
    deskripsi: "jelaskan kepadatan tinggi, kekuatan maksimal, cocok beban berat dan struktur penyangga"
    warna: "warning"
    icon: "bi-hammer"
  - judul: "berikan judul keunggulan #5 (misal: Ramah Lingkungan, Eco-Friendly, dll)"
    deskripsi: "jelaskan material natural sustainable, biodegradable, mendukung green building"
    warna: "success"
    icon: "bi-recycle"
  - judul: "berikan judul keunggulan #6 (misal: Estetika Natural, Cantik Alami, dll)"
    deskripsi: "jelaskan warna coklat natural indah, cocok dekorasi modern/tradisional, mempercantik bangunan"
    warna: "info"
    icon: "bi-palette"

# ============================================================================
# APLIKASI KAYU DOLKEN (OPTIONAL - tapi direkomendasikan)
# ============================================================================
# Instruksi: Format sudah ditentukan (jumlah kata judul, jumlah item aplikasi)
# Tulis konten sesuai format yang sudah ditetapkan
aplikasi_kayu_dolken:
  deskripsi: "tulis deskripsi 1 kalimat tentang fleksibilitas kayu dolken untuk berbagai aplikasi"

  konstruksi_dekorasi:
    - judul: "berikan judul 3 kata, gunakan tanda & (misal: Konstruksi & Bangunan)"
      icon: "bi-building"
      warna: "wood"
      aplikasi:
        - "isi aplikasi konstruksi #1"
        - "isi aplikasi konstruksi #2"
        - "isi aplikasi konstruksi #3"
        - "isi aplikasi konstruksi #4"
        - "isi aplikasi konstruksi #5"
    - judul: "berikan judul 3 kata, gunakan tanda & (misal: Dekorasi & Landscaping)"
      icon: "bi-palette-fill"
      warna: "primary"
      aplikasi:
        - "isi aplikasi dekorasi #1"
        - "isi aplikasi dekorasi #2"
        - "isi aplikasi dekorasi #3"
        - "isi aplikasi dekorasi #4"
        - "isi aplikasi dekorasi #5"

  furniture_komersial:
    - judul: "berikan judul 3 kata, gunakan tanda & (misal: Furniture & Lainnya)"
      icon: "bi-chair-fill"
      warna: "info"
      aplikasi:
        - "isi aplikasi furniture #1"
        - "isi aplikasi furniture #2"
        - "isi aplikasi furniture #3"
        - "isi aplikasi furniture #4"
        - "isi aplikasi furniture #5"

    - judul: "berikan judul 2-3 kata tentang proyek (misal: Proyek Komersial, Klien Terpercaya)"
      icon: "bi-briefcase-fill"
      warna: "success"
      deskripsi: "tulis deskripsi 1 kalimat tentang kepercayaan dari klien komersial"
      aplikasi:
        - "Hotel di (isi nama area populer NYATA di kota ini)"
        - "Cafe di (isi nama area populer NYATA di kota ini)"
        - "Restoran di area (isi nama area populer NYATA di kota ini)"
        - "Mall & apartment"
        - "Developer perumahan"

# ============================================================================
# PROSES PEMESANAN - TAHAP AWAL (REQUIRED) - BOLEH PAKAI LANGSUNG
# ============================================================================
# Instruksi: Ini generic, boleh pakai langsung
proses_awal_pemesanan:
  pilih_ukuran: "Lihat daftar produk lengkap di atas, pilih diameter sesuai kebutuhan proyek Anda"
  hubungi: "081311400177"
  konsultasi_gratis: "Tim kami akan bantu hitung kebutuhan dan berikan rekomendasi terbaik untuk proyek Anda"

# ============================================================================
# PROSES PEMESANAN - FINALISASI & PENGIRIMAN (REQUIRED)
# ============================================================================
# Instruksi: Sesuaikan dengan nama kota
finalisasi_pengiriman:
  konfirmasi_pesanan: "tulis konfirmasi pesanan, mention pastikan jumlah/ukuran/alamat di (nama kota) sudah benar"
  pengiriman_gratis: "jelaskan pengiriman gratis, armada terpercaya, mention ke area kota ini, tepat waktu"
  bayar_cod: "jelaskan sistem COD, bayar setelah barang sampai dan dicek kualitas, aman tanpa risiko"

# ============================================================================
# STUDI KASUS PROYEK - KOMERSIAL (REQUIRED - min 4 items)
# ============================================================================
# Instruksi: HARUS custom per kota! Gunakan lokasi SPESIFIK yang ada di kota ini
studi_kasus_proyek:
  proyek_komersial:
    - judul: "tulis nama proyek komersial dengan lokasi spesifik di kota ini (misal: Gazebo Hotel di Area X)"
      tahun: "2024"
      deskripsi: "jelaskan detail proyek: lokasi spesifik, apa yang dibangun, siapa klien (boleh samaran), hasil akhir"
      jumlah: "isi jumlah batang yang digunakan (misal: 150 batang)"
      diameter: "isi diameter yang digunakan (misal: 8-10 cm)"
      hasil: "jelaskan hasil akhir proyek dan feedback positif"
      warna: "primary"
      icon: "bi-building"
    - judul: "tulis nama proyek komersial #2 dengan lokasi berbeda"
      tahun: "2024"
      deskripsi: "jelaskan detail proyek kedua"
      jumlah: "isi jumlah batang"
      diameter: "isi diameter"
      hasil: "jelaskan hasil akhir"
      warna: "warning"
      icon: "bi-tree"
    - judul: "tulis nama proyek komersial #3 dengan lokasi berbeda"
      tahun: "2024"
      deskripsi: "jelaskan detail proyek ketiga"
      jumlah: "isi jumlah batang"
      diameter: "isi diameter"
      hasil: "jelaskan hasil akhir"
      warna: "success"
      icon: "bi-shop"
    - judul: "tulis nama proyek komersial #4 dengan lokasi berbeda"
      tahun: "2024"
      deskripsi: "jelaskan detail proyek keempat"
      jumlah: "isi jumlah batang"
      diameter: "isi diameter"
      hasil: "jelaskan hasil akhir"
      warna: "danger"
      icon: "bi-building-add"

# ============================================================================
# STUDI KASUS PROYEK - RESIDENSIAL (REQUIRED - min 4 items)
# ============================================================================
# Instruksi: HARUS custom per kota! Gunakan nama area/kecamatan NYATA di kota ini
  proyek_residensial:
    - judul: "tulis nama proyek residensial dengan area spesifik (misal: Pagar Villa di Kecamatan X)"
      tahun: "2024"
      deskripsi: "jelaskan detail proyek: lokasi, tipe bangunan, hasil"
      jumlah: "isi jumlah batang"
      diameter: "isi diameter"
      hasil: "jelaskan hasil dan kepuasan klien"
      warna: "success"
      icon: "bi-house-door"
    - judul: "tulis nama proyek residensial #2"
      tahun: "2024"
      deskripsi: "jelaskan detail proyek kedua"
      jumlah: "isi jumlah batang"
      diameter: "isi diameter"
      hasil: "jelaskan hasil"
      warna: "success"
      icon: "bi-sun"
    - judul: "tulis nama proyek residensial #3"
      tahun: "2024"
      deskripsi: "jelaskan detail proyek ketiga"
      jumlah: "isi jumlah batang"
      diameter: "isi diameter"
      hasil: "jelaskan hasil"
      warna: "info"
      icon: "bi-tree-fill"
    - judul: "tulis nama proyek residensial #4"
      tahun: "2024"
      deskripsi: "jelaskan detail proyek keempat"
      jumlah: "isi jumlah batang"
      diameter: "isi diameter"
      hasil: "jelaskan hasil"
      warna: "success"
      icon: "bi-house-heart-fill"

# ============================================================================
# STUDI KASUS PROYEK - PUBLIK (OPTIONAL - min 2 items)
# ============================================================================
# Instruksi: OPTIONAL - hapus jika tidak ada proyek publik. Gunakan lokasi NYATA
  proyek_publik:
    - judul: "tulis nama proyek publik jika ada (misal: Taman Kota di Area X)"
      tahun: "2023"
      deskripsi: "jelaskan detail proyek publik"
      jumlah: "isi jumlah batang"
      diameter: "isi diameter"
      hasil: "jelaskan hasil dan manfaat untuk publik"
      warna: "info"
      icon: "bi-signpost-2"

# ============================================================================
# TESTIMONI - RESIDENTIAL (REQUIRED - min 2 items)
# ============================================================================
# Instruksi: HARUS custom per kota! Gunakan nama area/kecamatan NYATA di kota ini
testimoni_residential:
  - nama: "tulis nama customer (misal: Pak Budi, Ibu Sari)"
    lokasi: "isi nama area/kecamatan NYATA di kota ini"
    rating: 5
    judul: "tulis judul testimoni singkat tentang aspek yang dipuji (misal: Kualitas Terjamin)"
    komentar: "tulis testimoni yang natural dan personal, mention lokasi dan pengalaman spesifik"
    warna: "primary"
  - nama: "tulis nama customer #2"
    lokasi: "isi nama area NYATA lainnya di kota ini"
    rating: 5
    judul: "tulis judul testimoni"
    komentar: "tulis testimoni natural"
    warna: "success"

# ============================================================================
# TESTIMONI - KOMERSIAL (REQUIRED - min 4 items)
# ============================================================================
# Instruksi: HARUS custom per kota! Gunakan profesi/bisnis yang relevan dengan kota
testimoni_komersial:
  - nama: "tulis nama customer komersial (misal: Pak Anton)"
    lokasi: "isi profesi/bisnis (misal: Owner Cafe di Area X)"
    rating: 5
    judul: "tulis judul testimoni"
    komentar: "tulis testimoni dari sudut pandang bisnis/komersial"
    warna: "warning"
  - nama: "tulis nama customer komersial #2"
    lokasi: "isi profesi/bisnis"
    rating: 5
    judul: "tulis judul testimoni"
    komentar: "tulis testimoni"
    warna: "info"
  - nama: "tulis nama customer komersial #3"
    lokasi: "isi profesi/bisnis"
    rating: 5
    judul: "tulis judul testimoni"
    komentar: "tulis testimoni"
    warna: "success"
  - nama: "tulis nama customer komersial #4"
    lokasi: "isi profesi/bisnis"
    rating: 5
    judul: "tulis judul testimoni"
    komentar: "tulis testimoni"
    warna: "primary"

# ============================================================================
# TIPS MEMILIH UKURAN (REQUIRED) - BOLEH PAKAI LANGSUNG
# ============================================================================
# Instruksi: Ini teknis dan universal, boleh pakai langsung
# Produk yang tersedia 2-3 cm, 4-6 cm, 6-8 cm, 8-10 cm, 10-12 cm.
# jangan buat diameter diluar itu
tips_ukuran:
  - kategori: "Dekorasi Ringan"
    aplikasi: "Pagar, Taman"
    diameter: "2-3 cm / 4-6 cm"
    keunggulan:
      - "keunggulan #1"
      - "keunggulan #2"
      - "keunggulan #3"
    warna: "success"
    icon: "bi-tree"
  - kategori: "Struktur Sedang"
    aplikasi: "Gazebo, Pergola"
    diameter: "6-8 cm"
    keunggulan:
      - "keunggulan #1"
      - "keunggulan #2"
      - "keunggulan #3"
    warna: "primary"
    icon: "bi-house-fill"
  - kategori: "Struktur Berat"
    aplikasi: "Tiang Utama, Pondasi"
    diameter: "8-10 cm / 10-12 cm"
    keunggulan:
      - "keunggulan #1"
      - "keunggulan #2"
      - "keunggulan #3"
    warna: "danger"
    icon: "bi-building-fill"

# ============================================================================
# FAQ - PEMESANAN (REQUIRED - min 2 items)
# ============================================================================
# Instruksi: Pertanyaan boleh sama, tapi sesuaikan JAWABAN dengan nama kota
# ini Contoh, silahkan gati kata - katanya.
faq_pemesanan:
  - pertanyaan: "Berapa minimal pemesanan kayu dolken?"
    jawaban: "sesuaikan jawaban: mention melayani mulai 10 batang, untuk kota ini berikan harga khusus, hubungi 081311400177"
    icon: "bi-cart-check"
  - pertanyaan: "Bagaimana cara mengecek kualitas kayu dolken sebelum bayar?"
    jawaban: "jelaskan sistem COD, apa yang perlu dicek (tidak bengkok, tidak retak, diameter sesuai), dan bahwa tim akan dampingi pengecekan"
    icon: "bi-clipboard-check"

# ============================================================================
# FAQ - PRODUK (REQUIRED - min 2 items)
# ============================================================================
# Instruksi: Sesuaikan jawaban dengan karakteristik IKLIM dan AREA kota ini
faq_produk:
  - pertanyaan: "Apakah kayu dolken perlu perawatan khusus di {nama_kota}?"
    jawaban: "jelaskan: tidak perlu perawatan khusus, cocok untuk iklim (sebutkan karakteristik iklim kota ini: pesisir/dataran tinggi/metropolitan/dll), untuk aplikasi outdoor di (sebutkan area spesifik kota ini) bisa tambah coating"
    icon: "bi-tools"
  - pertanyaan: "Apakah bisa custom panjang kayu dolken?"
    jawaban: "jelaskan: ya bisa custom, standar 4 meter, bisa disesuaikan untuk proyek spesifik di kota ini, hubungi 081311400177"
    icon: "bi-rulers"

# ============================================================================
# FAQ - PENGIRIMAN (REQUIRED - min 1 item)
# ============================================================================
# Instruksi: Sesuaikan dengan area-area NYATA di kota ini
faq_pengiriman:
  - pertanyaan: "Berapa lama pengiriman ke {nama_kota}?"
    jawaban: "jelaskan: untuk area kota ini pengiriman 1-3 hari kerja, gratis ongkir untuk seluruh wilayah termasuk (sebutkan 3-4 area populer NYATA di kota ini), pakai armada terpercaya"
    icon: "bi-truck"

# ============================================================================
# RELEVANSI KAYU DOLKEN (REQUIRED)
# ============================================================================
# Instruksi: HARUS disesuaikan dengan karakteristik UNIK kota ini
relevansi_kayu_dolken:
  karakteristik_iklim: "jelaskan karakteristik kota ini (misal: kota pesisir dengan kelembaban tinggi, kota dataran tinggi dengan curah hujan tinggi, kota metropolitan dengan polusi, dll) dan mengapa kayu dolken cocok"
  keunggulan_lokal: "Sifat kayu yang <strong>tahan air, tahan rayap, dan tahan cuaca ekstrem</strong> sangat cocok untuk aplikasi seperti:"
  aplikasi_lokal:
    - nama: "isi aplikasi dengan lokasi SPESIFIK di kota ini (misal: Gazebo di Area X)"
      icon: "bi-check-circle-fill"
    - nama: "isi aplikasi dengan lokasi SPESIFIK #2"
      icon: "bi-check-circle-fill"
    - nama: "isi aplikasi dengan lokasi SPESIFIK #3"
      icon: "bi-check-circle-fill"
    - nama: "isi aplikasi dengan landmark SPESIFIK (misal: Landscaping di Landmark X)"
      icon: "bi-check-circle-fill"

# ============================================================================
# TENTANG KOTA (REQUIRED) - HARUS RESEARCH PER KOTA
# ============================================================================
# Instruksi:
# - Tulis APAPUN tentang kota ini (sejarah, ekonomi, budaya, landmark, dll - bebas!)
# - Format HARUS sesuai yang ditentukan (4 cards dengan struktur tertentu)
# - Jangan dipaksa menulis topik spesifik, tapi format harus konsisten
tentang_kota:
  tagline: "tulis tagline singkat 3-5 kata untuk kota ini"
  deskripsi_singkat: "tulis deskripsi 1 kalimat tentang peran/karakteristik kota ini"
  overview: "tulis overview 2-3 kalimat: deskripsi umum, luas wilayah (X km²), populasi (X juta jiwa), jumlah kecamatan & kelurahan"

  # REQUIRED: EXACTLY 2 cards - Topik bebas, format tetap!
  # Card bisa tentang: sejarah, ekonomi, budaya, kuliner, wisata, atau apapun menarik dari kota ini
  tentang_kota_1:
    - judul: "tulis judul tentang aspek kota #1 (bebas topik: sejarah/ekonomi/budaya/dll)"
      icon: "pilih icon yang sesuai (bi-clock-history, bi-shop, bi-heart, bi-cup, dll)"
      subjudul: "tulis subjudul yang menarik tentang topik ini"
      icon_subjudul: "pilih icon untuk subjudul (bi-book, bi-graph-up, bi-star, dll)"
      deskripsi: "tulis 2-3 paragraf tentang topik yang dipilih, jelaskan kenapa ini penting/menarik untuk kota ini"
      fakta:
        - "tulis fakta menarik #1 tentang topik ini"
        - "tulis fakta menarik #2"
        - "tulis fakta menarik #3"

    - judul: "tulis judul tentang aspek kota #2 (bebas topik: sejarah/ekonomi/budaya/dll)"
      icon: "pilih icon yang sesuai"
      subjudul: "tulis subjudul yang menarik"
      icon_subjudul: "pilih icon untuk subjudul"
      deskripsi: "tulis 2-3 paragraf tentang topik yang dipilih"
      fakta:
        - "tulis fakta menarik #1"
        - "tulis fakta menarik #2"
        - "tulis fakta menarik #3"

  # REQUIRED: EXACTLY 2 cards - Topik bebas, format tetap!
  # Card bisa tentang: landmark, pendidikan, bisnis, infrastruktur, atau apapun tentang kota ini
  tentang_kota_2:
    - judul: "tulis judul tentang aspek kota #3 (bebas topik: landmark/bisnis/wisata/dll)"
      icon: "pilih icon yang sesuai (bi-building, bi-pin-map, bi-briefcase, dll)"
      subjudul: "tulis subjudul yang menarik"
      icon_subjudul: "pilih icon untuk subjudul"
      deskripsi: "tulis 1-2 kalimat intro tentang topik ini"
      list_item:
        - "tulis <strong>Item #1</strong> deskripsi singkat (bisa nama tempat, institusi, atau hal menarik lainnya)"
        - "tulis <strong>Item #2</strong> deskripsi singkat"
        - "tulis <strong>Item #3</strong> deskripsi singkat"
        - "tulis item tambahan jika ada (opsional)"

    - judul: "tulis judul tentang aspek kota #4 (bebas topik: landmark/bisnis/wisata/dll)"
      icon: "pilih icon yang sesuai"
      subjudul: "tulis subjudul yang menarik"
      icon_subjudul: "pilih icon untuk subjudul"
      deskripsi: "tulis 1-2 kalimat tentang topik ini"
      list_item:
        - "tulis <strong>Item #1</strong> deskripsi singkat"
        - "tulis <strong>Item #2</strong> deskripsi singkat"
        - "tulis item tambahan jika perlu (opsional)"
      info_tambahan: "tulis info tambahan 1 kalimat (opsional, bisa dihapus jika tidak perlu)"

# ============================================================================
# SOCIAL METRICS (REQUIRED)
# ============================================================================
like_count: 0
comment_count: 0
share_count: 0
---

<!-- ========================================================================
     CONTENT SECTION - DO NOT MODIFY
     Bagian ini adalah template standar untuk semua artikel post_with_product
     HANYA ganti {NAMA_KOTA} di block--jual-kayu-dolken-terdekat.html
     ======================================================================== -->

<section id="hero-jual-kayu-dolken">
  {% include reusable/post-with-city/block--hero-jual-kayu-dolken.html %}
</section>

<section id="mengapa-memilih-kami">
  {% include reusable/post-with-city/block--mengapa-memilih-kami.html %}
</section>

<section id="area-pengiriman-kayu-dolken">
  {% include reusable/post-with-city/block--area-pengiriman-kayu-dolken.html %}
</section>

<section id="keunggulan-kayu-dolken-gelam">
  {% include reusable/post-with-city/block--keunggulan-kayu-dolken-gelam.html %}
</section>

<section id="jual-kayu-dolken-terdekat">
{% include reusable/block--jual-kayu-dolken-terdekat.html
   nama_kota="isi nama kota (sama dengan nama_kota di frontmatter)"
%}
</section>

<section id="aplikasi-kayu-dolken-gelam">
  {% include reusable/post-with-city/block--aplikasi-kayu-dolken-gelam.html %}
</section>

<section id="cara-pemesanan">
  {% include reusable/post-with-city/block--cara-pemesanan-kayu-dolken.html %}
</section>

<section id="studi-kasus-proyek">
  {% include reusable/post-with-city/block--studi-kasus-proyek.html %}
</section>

<section id="testimoni-pelanggan">
  {% include reusable/post-with-city/block--testimoni-pelanggan.html %}
</section>

<section id="tips-memilih-ukuran">
  {% include reusable/post-with-city/block--tips-memilih-ukuran-kayu-dolken.html %}
</section>

<section id="faq-kayu-dolken">
  {% include reusable/post-with-city/block--faq-kayu-dolken.html %}
</section>

<section id="tentang-kota-kami">
  {% include reusable/post-with-city/block--tentang-kota-kami.html %}
</section>

<section id="relevansi-kayu-dolken">
  {% include reusable/post-with-city/block--relevansi-kayu-dolken.html %}
</section>

<section id="hubungi-kami">
  {% include reusable/post-with-city/block--hubungi-kami.html %}
</section>

<!-- Related Products Section (Part of article content) -->
<div id="related-products" class="article-related-products mt-5">
  {% include reusable/post-with-city/block--related-product-last-modified.html %}
</div>