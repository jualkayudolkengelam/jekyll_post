# Section Content Patterns (per Template)

Setiap section di TEMPLATE--post-with-city.md punya format spesifik. Gunakan ini sebagai panduan saat mengisi konten nyata.

---

## Aplikasi Kayu Dolken

```yaml
aplikasi_kayu_dolken:
  deskripsi: "Kalimat 1 tentang kegunaan Dolken di kota ini."

  konstruksi_dekorasi:           # 2 sub-item
    - judul: "3 kata & (misal: Konstruksi & Bangunan)"
      icon: "bi-building"
      warna: "wood"
      aplikasi:                   # 5 item
        - "Struktur atap rumah & villa di X"
        - "Kolom & balok kayu perumahan Y"
        - "Lantai kayu tahan beban"
        - "Pagar & gate kayu solid"
        - "Rangka carport & gazebo"

    - judul: "3 kata & (misal: Dekorasi & Landscaping)"
      icon: "bi-palette-fill"
      warna: "primary"
      aplikasi:                   # 5 item
        - "Dinding aksen kayu ruang tamu"
        - "Dek kayu outdoor taman/kolam"
        - "Pergola & gazebo taman"
        - "Furniture taman kayu"
        - "Pagar dekoratif & trellis"

  furniture_komersial:            # 2 sub-item
    - judul: "3 kata & (misal: Furniture & Lainnya)"
      icon: "bi-chair-fill"
      warna: "info"
      aplikasi:                   # 5 item
        - "Meja & kursi makan kayu solid"
        - "Bed frame & headboard natural"
        - "Rak buku & wardrobe custom"
        - "Bar counter & meja cafe"
        - "Aksesoris kayu: lampu, frame"

    - judul: "Proyek Komersial Terpercaya"
      icon: "bi-briefcase-fill"
      warna: "success"
      deskripsi: "1 kalimat tentang kepercayaan klien."
      aplikasi:                   # 5 item
        - "Hotel/resort di area X"
        - "Cafe di area Y"
        - "Restoran di area Z"
        - "Mall & apartment"
        - "Developer perumahan"
```

---

## Studi Kasus Proyek — Residensial (Required, min 4)

```yaml
proyek_residensial:
  - judul: "Nama Proyek + Lokasi (misal: Pagar Villa di Kecamatan X)"
    lokasi: "Desa/Kel. X, Kec. Y, Kota"
    tahun: "2024"
    deskripsi: "Detail: diameter kayu, tipe bangunan, panjang/luas, kondisi cuaca"
    jumlah: "angka batang"
    diameter: "range (misal: 8-10)"
    hasil: "Hasil dan kepuasan klien (1 kalimat)"
    warna: "success"
    icon: "bi-house-door"
```

Setiap item perlu: lokasi REAL (kecamatan/kelurahan), jumlah dan diameter masuk akal, hasil menyebut benefit konkret.

---

## Studi Kasus Proyek — Publik (Optional, min 2)

```yaml
proyek_publik:
  - judul: "Nama Proyek Publik di Area X"
    tahun: "2024"
    deskripsi: "Detail proyek publik (taman, mushola, balai desa)"
    jumlah: "angka batang"
    diameter: "range"
    hasil: "Manfaat untuk publik / respons masyarakat"
    warna: "info"
    icon: "bi-signpost-2"
```

Gunakan proyek nyata: taman kota, Islamic Center, pasar, GOR, balai desa.

---

## Testimoni — Residential (Required, min 2)

```yaml
testimoni_residential:
  - nama: "Pak/Ibu Nama"
    lokasi: "Kecamatan, Kota"
    rating: 5
    judul: "3-4 kata (aspek yang dipuji)"
    komentar: "2 kalimat natural — sebut lokasi, pengalaman, durasi, hasil"
    warna: "primary"
```

Pola nama: Pak/Ibu + nama asli Indonesia. Lokasi: kecamatan real. Komentar: cerita personal, natural, sebutkan produk spesifik.

---

## Testimoni — Komersial (Required, min 4)

```yaml
testimoni_komersial:
  - nama: "Nama Panggilan"
    lokasi: "Profesi/Bisnis + Area (misal: Owner Cafe di Area X)"
    rating: 5
    judul: "3-4 kata"
    komentar: "Perspektif bisnis — harga, kualitas, repeat order"
    warna: "warning"
```

Pola nama: nama panggilan. Lokasi: jabatan/profesi + venue di area real. Komentar: nilai bisnis, skala proyek, kualitas.

---

## Tips Konten per Kota

- **Susun kecamatan jadi referensi**: 3-5 kecamatan real = konten konsisten sepanjang post
- **Tema tiap kecamatan**: pesisir → kayu tahan air laut, dataran tinggi/pegunungan → tahan cuaca dingin, perkotaan → hunian mewah & komersial
- **Gunakan landmark real**: pasar, alun-alun, Islamic center, GOR, mall
- **Pricing truth**: "hemat X% vs baja" — 25-30% adalah angka realistis
- **Nama customer**: nama Indonesia asli, jangan dibuat terlalu unik
