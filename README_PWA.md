# Aplikasi Keuangan Katering - PWA Version

Progressive Web App (PWA) untuk mengelola keuangan katering dengan fitur input manual dan perhitungan otomatis.

## Fitur Utama

- **Input Manual**: Form untuk memasukkan pemasukan dan pengeluaran dengan tanggal, deskripsi, dan jumlah
- **Perhitungan Otomatis**: Menghitung sisa uang secara real-time
- **Laporan Transaksi**: Menampilkan semua transaksi dalam format tabel
- **Ringkasan Keuangan**: Menampilkan total pemasukan, pengeluaran, dan sisa uang
- **Penyimpanan ke Excel**: Menyimpan semua data ke file Excel secara otomatis
- **PWA Support**: Dapat diinstall sebagai aplikasi mobile/desktop
- **Offline Support**: Bekerja offline dengan service worker
- **Responsive Design**: Tampilan yang responsif untuk semua perangkat

## Persyaratan Sistem

- Python 3.6+
- Pip (package installer untuk Python)

## Instalasi

1. Clone atau download repository ini
2. Instal dependensi yang diperlukan:
   ```bash
   pip install -r requirements.txt
   ```

## Cara Menjalankan

1. Jalankan aplikasi:
   ```bash
   python app.py
   ```

2. Buka browser dan akses:
   ```
   http://localhost:5000
   ```

## Cara Menggunakan

1. **Menambahkan Pemasukan**:
   - Isi form "Tambah Pemasukan" dengan tanggal, deskripsi, dan jumlah
   - Klik tombol "Tambah Pemasukan"

2. **Menambahkan Pengeluaran**:
   - Isi form "Tambah Pengeluaran" dengan tanggal, deskripsi, dan jumlah
   - Klik tombol "Tambah Pengeluaran"

3. **Melihat Laporan**:
   - Semua transaksi akan ditampilkan dalam tabel secara otomatis
   - Ringkasan keuangan diperbarui secara real-time

4. **Install sebagai Aplikasi**:
   - Di browser yang mendukung PWA (Chrome, Edge, dll), akan muncul prompt untuk menginstall aplikasi
   - Klik "Install" untuk menginstall sebagai aplikasi desktop/mobile

## Struktur File

- `app.py` - File utama aplikasi Flask
- `templates/index.html` - Template HTML untuk antarmuka web
- `static/css/style.css` - File CSS untuk styling
- `static/js/app.js` - File JavaScript untuk interaksi frontend
- `static/icons/` - Direktori untuk icon aplikasi
- `manifest.json` - File manifest untuk PWA
- `service-worker.js` - Service worker untuk offline support
- `requirements.txt` - Daftar dependensi Python
- `catering_finance_pwa.xlsx` - File Excel untuk menyimpan data (akan dibuat otomatis)

## Teknologi yang Digunakan

- **Flask** - Framework web Python
- **Progressive Web App (PWA)** - Untuk pengalaman aplikasi native
- **Service Worker** - Untuk offline support dan caching
- **Web App Manifest** - Untuk installability
- **CSS3 & HTML5** - Untuk tampilan dan struktur
- **JavaScript** - Untuk interaksi frontend
- **OpenPyXL** - Library untuk bekerja dengan file Excel

## Perhitungan Keuangan

Sistem secara otomatis menghitung:
- **Total Pemasukan** = Jumlah semua pemasukan
- **Total Pengeluaran** = Jumlah semua pengeluaran
- **Sisa Uang** = Total Pemasukan - Total Pengeluaran

Setiap transaksi baru akan memperbarui saldo secara otomatis berdasarkan rumus:
```
Saldo Baru = Saldo Sebelumnya + Pemasukan - Pengeluaran
```

## Fitur PWA

1. **Installable**: Dapat diinstall sebagai aplikasi desktop/mobile
2. **Offline Support**: Dapat digunakan tanpa koneksi internet
3. **Responsive**: Berfungsi di semua perangkat (desktop, tablet, mobile)
4. **Push Notifications**: (Dapat dikembangkan lebih lanjut)
5. **Home Screen Access**: Dapat diakses langsung dari home screen

## Pengembangan Lebih Lanjut

Anda dapat mengembangkan aplikasi ini lebih lanjut dengan menambahkan fitur seperti:
- Autentikasi pengguna
- Kategori transaksi
- Laporan bulanan/tahunan
- Ekspor ke PDF
- Notifikasi saldo rendah
- Sinkronisasi data antar perangkat
- Grafik keuangan