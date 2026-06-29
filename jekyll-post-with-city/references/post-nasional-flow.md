# User Preference: Tahap Workflow for Filling Template

User mengisi city post secara bertahap, mengirim pesan "silahkan dilanjutkan" setiap kali selesai
satu tahap. Jangan selesaikan semua tahap dalam satu respon tanpa diminta.

## Urutan Tahap

Tahap | Isi | Catatan
------|-----|--------
1 | **Frontmatter** (title, description, date, image, images x4, keywords, nama_kota) | Ganti semua {kota} placeholder
2 | **area_pengiriman**, **keunggulan_produk**, **keunggulan_layanan** | Minimal 5-8 kecamatan, 3 item masing-masing
3 | **area_pengiriman_detail** (judul+deskripsi jangkauan/pusat/utara-selatan/pengembangan) | Semua judul+deskripsi harus spesifik kota
4 | **wilayah_pusat**, **wilayah_utara_selatan**, **wilayah_pengembangan**, **kecamatan_lainnya** | Nama nyata kecamatan & kelurahan
5 | **landmark_wisata**, **landmark_fasilitas** | Min 3 item masing-masing, real landmark
6 | **keunggulan_durabilitas**, **keunggulan_nilai**, **keunggulan_kayu_dolken**, **aplikasi_kayu_dolken** | Deskripsi spesifik kota
7 | **proses_awal_pemesanan**, **finalisasi_pengiriman**, **studi_kasus_proyek**, **testimoni** | Studi kasus & testimoni dengan lokasi nyata
8 | **tips_ukuran**, **FAQ** (pemesanan/produk/pengiriman/relevansi) | Jawaban FAQ spesifik kota
9 | **tentang_kota** (tagline, overview, tentang_kota_1, tentang_kota_2) | 4 cards total, topik bebas
10 | **social_metrics** (like/comment/share) | Angka wajar

Aturan:
1. Satu tahap = satu batch patch, lalu informasikan progres.
2. User ketik "silahkan dilanjutkan" untuk lanjut ke tahap berikutnya.
3. Jika user memberikan informasi tambahan (foto, detail kota), akomodasi di tahap yang relevan.
