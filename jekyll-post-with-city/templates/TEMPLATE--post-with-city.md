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
# Judul Artikel — Nama Kota — Hubungi 0813-1140-0177 — Tagline
title:
# Deskripsi meta untuk SEO, 150-160 karakter.
description:
# Ringkasan singkat untuk tampilan grid/card.
excerpt:
# YYYY-MM-DD
date:
# Admin
author:
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
  # Isi dengan keunggulan daya tahan (contoh: tahan 20-30 tahun, anti rayap)
  tahan_lama:
  # Isi dengan keunggulan kekuatan dan kepadatan
  kuat_padat:
  # Isi dengan keunggulan perawatan mudah
  minim_perawatan:
keunggulan_nilai:
  # Isi dengan keunggulan ramah lingkungan
  ramah_lingkungan:
  # Isi dengan keunggulan hemat biaya jangka panjang
  hemat_biaya:
nama_kota: "NamaKota"

# ============================================================================
# AREA PENGIRIMAN (SIMPLE LIST) - REQUIRED
# ============================================================================
# Instruksi: Isi 5-10 area/kecamatan populer di kota ini
area_pengiriman:
  # isi nama kecamatan/area populer #1
  -
  # isi nama kecamatan/area populer #2
  -
  # isi nama kecamatan/area populer #3
  -
  # isi nama kecamatan/area populer #4
  -
  # isi nama kecamatan/area populer #5
  -
  # Tambahkan hingga 10 area jika perlu

# ============================================================================
# KEUNGGULAN - PRODUK (REQUIRED)
# ============================================================================
# Instruksi: HARUS 3 items. Tulis keunggulan produk yang disesuaikan dengan kota
keunggulan_produk:
  # berikan judul keunggulan produk #1 (misal: Kualitas Premium, Tahan Lama, dll)
  - judul:
    # jelaskan keunggulan ini, sesuaikan dengan karakteristik iklim/kondisi kota (misal: cocok untuk iklim pesisir/dataran tinggi/metropolitan)
    deskripsi:
    warna: "warning"
    icon: "bi-award-fill"
  # berikan judul keunggulan produk #2 (misal: Harga Terjangkau, Harga Terbaik, dll)
  - judul:
    # jelaskan keunggulan harga, mention harga mulai Rp 15.000/batang atau sesuaikan dengan market kota
    deskripsi:
    warna: "danger"
    icon: "bi-cash-coin"
  # berikan judul keunggulan produk #3 (misal: Stok Lengkap, Selalu Ready, dll)
  - judul:
    # jelaskan ketersediaan stok, mention diameter yang tersedia (2-12 cm)
    deskripsi:
    warna: "info"
    icon: "bi-boxes"

# ============================================================================
# KEUNGGULAN - LAYANAN (REQUIRED)
# ============================================================================
# Instruksi: HARUS 3 items. Tulis keunggulan layanan yang disesuaikan dengan kota
keunggulan_layanan:
  # berikan judul keunggulan layanan #1 (misal: Pengiriman Gratis [Nama Kota], Free Ongkir [Kota], dll)
  - judul:
    # jelaskan keunggulan pengiriman gratis, mention area kota yang dicakup, benefit untuk customer
    deskripsi:
    warna: "success"
    icon: "bi-truck"
  # berikan judul keunggulan layanan #2 (misal: COD Tersedia, Bayar di Tempat, dll)
  - judul:
    # jelaskan sistem pembayaran COD, benefit aman untuk customer, cek kualitas dulu
    deskripsi:
    warna: "primary"
    icon: "bi-shield-check"
  # berikan judul keunggulan layanan #3 (misal: Fast Response, Konsultasi Gratis, dll)
  - judul:
    # jelaskan layanan konsultasi/response cepat, mention 24/7 atau waktu operasional
    deskripsi:
    warna: "secondary"
    icon: "bi-headset"

# ============================================================================
# AREA PENGIRIMAN DETAIL - TEKS JUDUL & DESKRIPSI (REQUIRED)
# ============================================================================
# Instruksi: Semua field di bawah HARUS ditulis manual sesuai karakteristik kota
area_pengiriman_detail:
  # berikan judul untuk jangkauan pengiriman di kota ini
  judul_jangkauan:
  # jelaskan area mana saja yang dilayani di kota ini, mention gratis ongkir dan jumlah kecamatan
  deskripsi_jangkauan:

  # berikan judul untuk wilayah pusat kota ini
  judul_pusat:
  # jelaskan mengapa wilayah pusat kota ini strategis, mention jumlah kecamatan dan akses mudah
  deskripsi_pusat:

  # berikan judul untuk wilayah utara & selatan (OPTIONAL - hapus jika tidak relevan)
  judul_utara_selatan:
  # jelaskan karakteristik wilayah utara & selatan kota ini (OPTIONAL - hapus jika tidak ada)
  deskripsi_utara_selatan:

  # berikan judul untuk wilayah pengembangan/pinggiran kota ini
  judul_pengembangan:
  # jelaskan karakteristik area pengembangan, mention pertumbuhan dan potensi
  deskripsi_pengembangan:

  # berikan judul untuk kecamatan lainnya (OPTIONAL - hapus jika tidak perlu)
  judul_lainnya:

  # berikan judul untuk landmark & lokasi strategis di kota ini
  judul_landmark:
  # jelaskan mengapa landmark ini penting untuk proyek komersial
  deskripsi_landmark:

  # berikan judul untuk destinasi wisata di kota ini
  judul_wisata:
  # jelaskan landmark wisata dan sejarah yang terkenal di kota ini
  deskripsi_wisata:

  # berikan judul untuk fasilitas pendidikan & komersial di kota ini
  judul_fasilitas:
  # jelaskan fasilitas strategis seperti kampus, mall, pelabuhan di kota ini
  deskripsi_fasilitas:

# ============================================================================
# AREA PENGIRIMAN DETAIL - WILAYAH PUSAT (REQUIRED - min 3 items)
# ============================================================================
# Instruksi: Research kecamatan NYATA di pusat kota ini, cari kelurahan yang ada
  wilayah_pusat:
    # isi nama kecamatan pusat #1
    - nama:
      kelurahan:
        # isi 3-5 kelurahan di kecamatan ini
        -
        # isi kelurahan lainnya (bisa gabung beberapa dengan koma)
        -
      warna: "primary"
    # isi nama kecamatan pusat #2
    - nama:
      kelurahan:
        # isi 3-5 kelurahan di kecamatan ini
        -
      warna: "success"
    # isi nama kecamatan pusat #3
    - nama:
      kelurahan:
        # isi 3-5 kelurahan di kecamatan ini
        -
      warna: "info"
    # Tambah lebih banyak jika perlu (5-7 kecamatan ideal)

# ============================================================================
# AREA PENGIRIMAN DETAIL - WILAYAH UTARA & SELATAN (OPTIONAL)
# ============================================================================
# Instruksi: Hapus section ini jika kota tidak punya pembagian utara-selatan yang jelas
  wilayah_utara_selatan:
    # isi nama kecamatan di bagian utara kota
    - nama:
      kelurahan:
        # isi kelurahan di kecamatan ini
        -
      warna: "danger"
    # isi nama kecamatan di bagian selatan kota
    - nama:
      kelurahan:
        # isi kelurahan di kecamatan ini
        -
      warna: "warning"

# ============================================================================
# AREA PENGIRIMAN DETAIL - WILAYAH PENGEMBANGAN (REQUIRED - min 2 items)
# ============================================================================
# Instruksi: Isi kecamatan yang sedang berkembang/pinggiran kota
  wilayah_pengembangan:
    # isi nama kecamatan pengembangan #1
    - nama:
      kelurahan:
        # isi kelurahan di kecamatan ini
        -
      warna: "primary"
    # isi nama kecamatan pengembangan #2
    - nama:
      kelurahan:
        # isi kelurahan di kecamatan ini
        -
      warna: "info"
    # isi nama kecamatan pengembangan #3
    - nama:
      kelurahan:
        # isi kelurahan di kecamatan ini
        -
      warna: "wood"

# ============================================================================
# AREA PENGIRIMAN DETAIL - KECAMATAN LAINNYA (OPTIONAL)
# ============================================================================
# Instruksi: Isi kecamatan tambahan yang tidak masuk kategori lain (OPTIONAL - bisa dihapus)
  kecamatan_lainnya:
    # isi nama kecamatan tambahan #1
    -
    # isi nama kecamatan tambahan #2
    -
    # isi nama kecamatan tambahan #3
    -

# ============================================================================
# AREA PENGIRIMAN DETAIL - LANDMARK WISATA (REQUIRED - min 3 items)
# ============================================================================
# Instruksi: Isi landmark WISATA dan sejarah yang terkenal di kota ini
  landmark_wisata:
    # isi nama landmark wisata/sejarah #1
    - nama:
      icon: "bi-building"
      warna: "warning"
    # isi nama landmark wisata/sejarah #2
    - nama:
      icon: "bi-building"
      warna: "warning"
    # isi nama landmark wisata/sejarah #3
    - nama:
      icon: "bi-building"
      warna: "warning"

# ============================================================================
# AREA PENGIRIMAN DETAIL - LANDMARK FASILITAS (REQUIRED - min 3 items)
# ============================================================================
# Instruksi: Isi fasilitas strategis seperti mall, kampus, pelabuhan di kota ini
  landmark_fasilitas:
    # isi nama mall/pusat perbelanjaan terkenal
    - nama:
      icon: "bi-cart"
      warna: "info"
    # isi nama mall/pusat perbelanjaan lainnya
    - nama:
      icon: "bi-cart"
      warna: "primary"
    # isi nama kampus/universitas/pelabuhan terkenal
    - nama:
      icon: "bi-mortarboard"  # gunakan bi-shop untuk pelabuhan
      warna: "success"

# ============================================================================
# KEUNGGULAN PRODUK - DURABILITAS (OPTIONAL)
# ============================================================================
# Instruksi: Format lama (object), OPTIONAL - bisa dihapus jika pakai keunggulan_kayu_dolken (array) di bawah
keunggulan_durabilitas:
  # jelaskan daya tahan kayu gelam 20-30 tahun, sesuaikan dengan iklim kota ini
  tahan_lama:
  # jelaskan keunggulan anti rayap natural tanpa obat
  anti_rayap:
  # jelaskan cocok untuk outdoor/indoor, tahan hujan/panas, mention karakteristik cuaca kota ini
  tahan_cuaca:
  # jelaskan kepadatan tinggi, cocok untuk beban berat
  kuat_padat:

keunggulan_nilai:
  # jelaskan material natural, sustainable, mendukung green building
  ramah_lingkungan:
  # jelaskan warna natural coklat, cocok untuk dekorasi modern/tradisional
  estetika:

# Format Array (lebih baru, direkomendasikan) - HARUS 6 items
keunggulan_kayu_dolken:
  # berikan judul keunggulan #1 (misal: Tahan Lama, Awet Puluhan Tahun, dll)
  - judul:
    # jelaskan daya tahan 20-30 tahun tanpa treatment, sesuaikan dengan iklim kota ini (pesisir/dataran tinggi/metropolitan)
    deskripsi:
    warna: "success"
    icon: "bi-clock-history"
  # berikan judul keunggulan #2 (misal: Anti Rayap, Tahan Hama, dll)
  - judul:
    # jelaskan tidak perlu obat anti rayap, tekstur padat menolak rayap natural
    deskripsi:
    warna: "danger"
    icon: "bi-bug"
  # berikan judul keunggulan #3 (misal: Tahan Cuaca, Tahan Air, dll)
  - judul:
    # jelaskan cocok outdoor/indoor, tahan hujan/panas/lembab, mention kondisi cuaca kota ini
    deskripsi:
    warna: "primary"
    icon: "bi-cloud-rain"
  # berikan judul keunggulan #4 (misal: Kuat & Padat, Super Kuat, dll)
  - judul:
    # jelaskan kepadatan tinggi, kekuatan maksimal, cocok beban berat dan struktur penyangga
    deskripsi:
    warna: "warning"
    icon: "bi-hammer"
  # berikan judul keunggulan #5 (misal: Ramah Lingkungan, Eco-Friendly, dll)
  - judul:
    # jelaskan material natural sustainable, biodegradable, mendukung green building
    deskripsi:
    warna: "success"
    icon: "bi-recycle"
  # berikan judul keunggulan #6 (misal: Estetika Natural, Cantik Alami, dll)
  - judul:
    # jelaskan warna coklat natural indah, cocok dekorasi modern/tradisional, mempercantik bangunan
    deskripsi:
    warna: "info"
    icon: "bi-palette"

# ============================================================================
# APLIKASI KAYU DOLKEN (OPTIONAL - tapi direkomendasikan)
# ============================================================================
# Instruksi: Format sudah ditentukan (jumlah kata judul, jumlah item aplikasi)
# Tulis konten sesuai format yang sudah ditetapkan
aplikasi_kayu_dolken:
  # tulis deskripsi 1 kalimat tentang fleksibilitas kayu dolken untuk berbagai aplikasi
  deskripsi:

  konstruksi_dekorasi:
    # berikan judul 3 kata, gunakan tanda & (misal: Konstruksi & Bangunan)
    - judul:
      icon: "bi-building"
      warna: "wood"
      aplikasi:
        # isi aplikasi konstruksi #1
        -
        # isi aplikasi konstruksi #2
        -
        # isi aplikasi konstruksi #3
        -
        # isi aplikasi konstruksi #4
        -
        # isi aplikasi konstruksi #5
        -
    # berikan judul 3 kata, gunakan tanda & (misal: Dekorasi & Landscaping)
    - judul:
      icon: "bi-palette-fill"
      warna: "primary"
      aplikasi:
        # isi aplikasi dekorasi #1
        -
        # isi aplikasi dekorasi #2
        -
        # isi aplikasi dekorasi #3
        -
        # isi aplikasi dekorasi #4
        -
        # isi aplikasi dekorasi #5
        -

  furniture_komersial:
    # berikan judul 3 kata, gunakan tanda & (misal: Furniture & Lainnya)
    - judul:
      icon: "bi-chair-fill"
      warna: "info"
      aplikasi:
        # isi aplikasi furniture #1
        -
        # isi aplikasi furniture #2
        -
        # isi aplikasi furniture #3
        -
        # isi aplikasi furniture #4
        -
        # isi aplikasi furniture #5
        -

    # berikan judul 2-3 kata tentang proyek (misal: Proyek Komersial, Klien Terpercaya)
    - judul:
      icon: "bi-briefcase-fill"
      warna: "success"
      # tulis deskripsi 1 kalimat tentang kepercayaan dari klien komersial
      deskripsi:
      aplikasi:
        # Hotel di (isi nama area populer NYATA di kota ini)
        -
        # Cafe di (isi nama area populer NYATA di kota ini)
        -
        # Restoran di area (isi nama area populer NYATA di kota ini)
        -
        - "Mall & apartment"
        - "Developer perumahan"

# ============================================================================
# PROSES PEMESANAN - TAHAP AWAL (REQUIRED) - BOLEH PAKAI LANGSUNG
# ============================================================================
# Instruksi: Ini generic, boleh pakai langsung
proses_awal_pemesanan:
  # Lihat daftar produk lengkap di atas, pilih diameter sesuai kebutuhan proyek Anda
  pilih_ukuran:
  hubungi: "081311400177"
  # Tim kami akan bantu hitung kebutuhan dan berikan rekomendasi terbaik untuk proyek Anda
  konsultasi_gratis:

# ============================================================================
# PROSES PEMESANAN - FINALISASI & PENGIRIMAN (REQUIRED)
# ============================================================================
# Instruksi: Sesuaikan dengan nama kota
finalisasi_pengiriman:
  # tulis konfirmasi pesanan, mention pastikan jumlah/ukuran/alamat di (nama kota) sudah benar
  konfirmasi_pesanan:
  # jelaskan pengiriman gratis, armada terpercaya, mention ke area kota ini, tepat waktu
  pengiriman_gratis:
  # jelaskan sistem COD, bayar setelah barang sampai dan dicek kualitas, aman tanpa risiko
  bayar_cod:

# ============================================================================
# STUDI KASUS PROYEK - KOMERSIAL (REQUIRED - min 4 items)
# ============================================================================
# Instruksi: HARUS custom per kota! Gunakan lokasi SPESIFIK yang ada di kota ini
studi_kasus_proyek:
  proyek_komersial:
    # tulis nama proyek komersial dengan lokasi spesifik di kota ini (misal: Gazebo Hotel di Area X)
    - judul:
      tahun: "2024"
      # jelaskan detail proyek: lokasi spesifik, apa yang dibangun, siapa klien (boleh samaran), hasil akhir
      deskripsi:
      # isi jumlah batang yang digunakan (misal: 150 batang)
      jumlah:
      # isi diameter yang digunakan (misal: 8-10 cm)
      diameter:
      # jelaskan hasil akhir proyek dan feedback positif
      hasil:
      warna: "primary"
      icon: "bi-building"
    # tulis nama proyek komersial #2 dengan lokasi berbeda
    - judul:
      tahun: "2024"
      # jelaskan detail proyek kedua
      deskripsi:
      # isi jumlah batang
      jumlah:
      # isi diameter
      diameter:
      # jelaskan hasil akhir
      hasil:
      warna: "warning"
      icon: "bi-tree"
    # tulis nama proyek komersial #3 dengan lokasi berbeda
    - judul:
      tahun: "2024"
      # jelaskan detail proyek ketiga
      deskripsi:
      # isi jumlah batang
      jumlah:
      # isi diameter
      diameter:
      # jelaskan hasil akhir
      hasil:
      warna: "success"
      icon: "bi-shop"
    # tulis nama proyek komersial #4 dengan lokasi berbeda
    - judul:
      tahun: "2024"
      # jelaskan detail proyek keempat
      deskripsi:
      # isi jumlah batang
      jumlah:
      # isi diameter
      diameter:
      # jelaskan hasil akhir
      hasil:
      warna: "danger"
      icon: "bi-building-add"

# ============================================================================
# STUDI KASUS PROYEK - RESIDENSIAL (REQUIRED - min 4 items)
# ============================================================================
# Instruksi: HARUS custom per kota! Gunakan nama area/kecamatan NYATA di kota ini
  proyek_residensial:
    # tulis nama proyek residensial dengan area spesifik (misal: Pagar Villa di Kecamatan X)
    - judul:
      tahun: "2024"
      # jelaskan detail proyek: lokasi, tipe bangunan, hasil
      deskripsi:
      # isi jumlah batang
      jumlah:
      # isi diameter
      diameter:
      # jelaskan hasil dan kepuasan klien
      hasil:
      warna: "success"
      icon: "bi-house-door"
    # tulis nama proyek residensial #2
    - judul:
      tahun: "2024"
      # jelaskan detail proyek kedua
      deskripsi:
      # isi jumlah batang
      jumlah:
      # isi diameter
      diameter:
      # jelaskan hasil
      hasil:
      warna: "success"
      icon: "bi-sun"
    # tulis nama proyek residensial #3
    - judul:
      tahun: "2024"
      # jelaskan detail proyek ketiga
      deskripsi:
      # isi jumlah batang
      jumlah:
      # isi diameter
      diameter:
      # jelaskan hasil
      hasil:
      warna: "info"
      icon: "bi-tree-fill"
    # tulis nama proyek residensial #4
    - judul:
      tahun: "2024"
      # jelaskan detail proyek keempat
      deskripsi:
      # isi jumlah batang
      jumlah:
      # isi diameter
      diameter:
      # jelaskan hasil
      hasil:
      warna: "success"
      icon: "bi-house-heart-fill"

# ============================================================================
# STUDI KASUS PROYEK - PUBLIK (OPTIONAL - min 2 items)
# ============================================================================
# Instruksi: OPTIONAL - hapus jika tidak ada proyek publik. Gunakan lokasi NYATA
  proyek_publik:
    # tulis nama proyek publik jika ada (misal: Taman Kota di Area X)
    - judul:
      tahun: "2023"
      # jelaskan detail proyek publik
      deskripsi:
      # isi jumlah batang
      jumlah:
      # isi diameter
      diameter:
      # jelaskan hasil dan manfaat untuk publik
      hasil:
      warna: "info"
      icon: "bi-signpost-2"

# ============================================================================
# TESTIMONI - RESIDENTIAL (REQUIRED - min 2 items)
# ============================================================================
# Instruksi: HARUS custom per kota! Gunakan nama area/kecamatan NYATA di kota ini
testimoni_residential:
  # tulis nama customer (misal: Pak Budi, Ibu Sari)
  - nama:
    # isi nama area/kecamatan NYATA di kota ini
    lokasi:
    rating: 5
    # tulis judul testimoni singkat tentang aspek yang dipuji (misal: Kualitas Terjamin)
    judul:
    # tulis testimoni yang natural dan personal, mention lokasi dan pengalaman spesifik
    komentar:
    warna: "primary"
  # tulis nama customer #2
  - nama:
    # isi nama area NYATA lainnya di kota ini
    lokasi:
    rating: 5
    # tulis judul testimoni
    judul:
    # tulis testimoni natural
    komentar:
    warna: "success"

# ============================================================================
# TESTIMONI - KOMERSIAL (REQUIRED - min 4 items)
# ============================================================================
# Instruksi: HARUS custom per kota! Gunakan profesi/bisnis yang relevan dengan kota
testimoni_komersial:
  # tulis nama customer komersial (misal: Pak Anton)
  - nama:
    # isi profesi/bisnis (misal: Owner Cafe di Area X)
    lokasi:
    rating: 5
    # tulis judul testimoni
    judul:
    # tulis testimoni dari sudut pandang bisnis/komersial
    komentar:
    warna: "warning"
  # tulis nama customer komersial #2
  - nama:
    # isi profesi/bisnis
    lokasi:
    rating: 5
    # tulis judul testimoni
    judul:
    # tulis testimoni
    komentar:
    warna: "info"
  # tulis nama customer komersial #3
  - nama:
    # isi profesi/bisnis
    lokasi:
    rating: 5
    # tulis judul testimoni
    judul:
    # tulis testimoni
    komentar:
    warna: "success"
  # tulis nama customer komersial #4
  - nama:
    # isi profesi/bisnis
    lokasi:
    rating: 5
    # tulis judul testimoni
    judul:
    # tulis testimoni
    komentar:
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
    # sesuaikan jawaban: mention melayani mulai 10 batang, untuk kota ini berikan harga khusus, hubungi 081311400177
    jawaban:
    icon: "bi-cart-check"
  - pertanyaan: "Bagaimana cara mengecek kualitas kayu dolken sebelum bayar?"
    # jelaskan sistem COD, apa yang perlu dicek (tidak bengkok, tidak retak, diameter sesuai), dan bahwa tim akan dampingi pengecekan
    jawaban:
    icon: "bi-clipboard-check"

# ============================================================================
# FAQ - PRODUK (REQUIRED - min 2 items)
# ============================================================================
# Instruksi: Sesuaikan jawaban dengan karakteristik IKLIM dan AREA kota ini
faq_produk:
  - pertanyaan: "Apakah kayu dolken perlu perawatan khusus di {nama_kota}?"
    # jelaskan: tidak perlu perawatan khusus, cocok untuk iklim (sebutkan karakteristik iklim kota ini: pesisir/dataran tinggi/metropolitan/dll), untuk aplikasi outdoor di (sebutkan area spesifik kota ini) bisa tambah coating
    jawaban:
    icon: "bi-tools"
  - pertanyaan: "Apakah bisa custom panjang kayu dolken?"
    # jelaskan: ya bisa custom, standar 4 meter, bisa disesuaikan untuk proyek spesifik di kota ini, hubungi 081311400177
    jawaban:
    icon: "bi-rulers"

# ============================================================================
# FAQ - PENGIRIMAN (REQUIRED - min 1 item)
# ============================================================================
# Instruksi: Sesuaikan dengan area-area NYATA di kota ini
faq_pengiriman:
  - pertanyaan: "Berapa lama pengiriman ke {nama_kota}?"
    # jelaskan: untuk area kota ini pengiriman 1-3 hari kerja, gratis ongkir untuk seluruh wilayah termasuk (sebutkan 3-4 area populer NYATA di kota ini), pakai armada terpercaya
    jawaban:
    icon: "bi-truck"

# ============================================================================
# RELEVANSI KAYU DOLKEN (REQUIRED)
# ============================================================================
# Instruksi: HARUS disesuaikan dengan karakteristik UNIK kota ini
relevansi_kayu_dolken:
  # jelaskan karakteristik kota ini (misal: kota pesisir dengan kelembaban tinggi, kota dataran tinggi dengan curah hujan tinggi, kota metropolitan dengan polusi, dll) dan mengapa kayu dolken cocok
  karakteristik_iklim:
  keunggulan_lokal: "Sifat kayu yang <strong>tahan air, tahan rayap, dan tahan cuaca ekstrem</strong> sangat cocok untuk aplikasi seperti:"
  aplikasi_lokal:
    # isi aplikasi dengan lokasi SPESIFIK di kota ini (misal: Gazebo di Area X)
    - nama:
      icon: "bi-check-circle-fill"
    # isi aplikasi dengan lokasi SPESIFIK #2
    - nama:
      icon: "bi-check-circle-fill"
    # isi aplikasi dengan lokasi SPESIFIK #3
    - nama:
      icon: "bi-check-circle-fill"
    # isi aplikasi dengan landmark SPESIFIK (misal: Landscaping di Landmark X)
    - nama:
      icon: "bi-check-circle-fill"

# ============================================================================
# TENTANG KOTA (REQUIRED) - HARUS RESEARCH PER KOTA
# ============================================================================
# Instruksi:
# - Tulis APAPUN tentang kota ini (sejarah, ekonomi, budaya, landmark, dll - bebas!)
# - Format HARUS sesuai yang ditentukan (4 cards dengan struktur tertentu)
# - Jangan dipaksa menulis topik spesifik, tapi format harus konsisten
tentang_kota:
  # tulis tagline singkat 3-5 kata untuk kota ini
  tagline:
  # tulis deskripsi 1 kalimat tentang peran/karakteristik kota ini
  deskripsi_singkat:
  # tulis overview 2-3 kalimat: deskripsi umum, luas wilayah (X km²), populasi (X juta jiwa), jumlah kecamatan & kelurahan
  overview:

  # REQUIRED: EXACTLY 2 cards - Topik bebas, format tetap!
  # Card bisa tentang: sejarah, ekonomi, budaya, kuliner, wisata, atau apapun menarik dari kota ini
  tentang_kota_1:
    # tulis judul tentang aspek kota #1 (bebas topik: sejarah/ekonomi/budaya/dll)
    - judul:
      # pilih icon yang sesuai (bi-clock-history, bi-shop, bi-heart, bi-cup, dll)
      icon:
      # tulis subjudul yang menarik tentang topik ini
      subjudul:
      # pilih icon untuk subjudul (bi-book, bi-graph-up, bi-star, dll)
      icon_subjudul:
      # tulis 2-3 paragraf tentang topik yang dipilih, jelaskan kenapa ini penting/menarik untuk kota ini
      deskripsi:
      fakta:
        # tulis fakta menarik #1 tentang topik ini
        -
        # tulis fakta menarik #2
        -
        # tulis fakta menarik #3
        -

    # tulis judul tentang aspek kota #2 (bebas topik: sejarah/ekonomi/budaya/dll)
    - judul:
      # pilih icon yang sesuai
      icon:
      # tulis subjudul yang menarik
      subjudul:
      # pilih icon untuk subjudul
      icon_subjudul:
      # tulis 2-3 paragraf tentang topik yang dipilih
      deskripsi:
      fakta:
        # tulis fakta menarik #1
        -
        # tulis fakta menarik #2
        -
        # tulis fakta menarik #3
        -

  # REQUIRED: EXACTLY 2 cards - Topik bebas, format tetap!
  # Card bisa tentang: landmark, pendidikan, bisnis, infrastruktur, atau apapun tentang kota ini
  tentang_kota_2:
    # tulis judul tentang aspek kota #3 (bebas topik: landmark/bisnis/wisata/dll)
    - judul:
      # pilih icon yang sesuai (bi-building, bi-pin-map, bi-briefcase, dll)
      icon:
      # tulis subjudul yang menarik
      subjudul:
      # pilih icon untuk subjudul
      icon_subjudul:
      # tulis 1-2 kalimat intro tentang topik ini
      deskripsi:
      list_item:
        # tulis <strong>Item #1</strong> deskripsi singkat (bisa nama tempat, institusi, atau hal menarik lainnya)
        -
        # tulis <strong>Item #2</strong> deskripsi singkat
        -
        # tulis <strong>Item #3</strong> deskripsi singkat
        -
        # tulis item tambahan jika ada (opsional)
        -

    # tulis judul tentang aspek kota #4 (bebas topik: landmark/bisnis/wisata/dll)
    - judul:
      # pilih icon yang sesuai
      icon:
      # tulis subjudul yang menarik
      subjudul:
      # pilih icon untuk subjudul
      icon_subjudul:
      # tulis 1-2 kalimat tentang topik ini
      deskripsi:
      list_item:
        # tulis <strong>Item #1</strong> deskripsi singkat
        -
        # tulis <strong>Item #2</strong> deskripsi singkat
        -
        # tulis item tambahan jika perlu (opsional)
        -
      # tulis info tambahan 1 kalimat (opsional, bisa dihapus jika tidak perlu)
      info_tambahan:

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
  # isi nama kota (sama dengan nama_kota di frontmatter)
  nama_kota: 
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
