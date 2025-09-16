# Aplikasi Keuangan Katering - Web Version

Aplikasi web untuk mengelola keuangan katering dengan fitur input manual dan perhitungan otomatis.

## Fitur Utama

- **Input Manual**: Form untuk memasukkan pemasukan dan pengeluaran dengan tanggal, deskripsi, dan jumlah
- **Perhitungan Otomatis**: Menghitung sisa uang secara real-time
- **Laporan Transaksi**: Menampilkan semua transaksi dalam format tabel
- **Ringkasan Keuangan**: Menampilkan total pemasukan, pengeluaran, dan sisa uang
- **Penyimpanan ke Excel**: Menyimpan semua data ke file Excel secara otomatis

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

## Struktur File

- `app.py` - File utama aplikasi Flask
- `templates/index.html` - Template HTML untuk antarmuka web
- `requirements.txt` - Daftar dependensi Python
- `catering_finance_web.xlsx` - File Excel untuk menyimpan data (akan dibuat otomatis)

## Teknologi yang Digunakan

- **Flask** - Framework web Python
- **Bootstrap 5** - Framework CSS untuk tampilan responsif
- **OpenPyXL** - Library untuk bekerja dengan file Excel
- **JavaScript** - Untuk interaksi frontend

## Perhitungan Keuangan

Sistem secara otomatis menghitung:
- **Total Pemasukan** = Jumlah semua pemasukan
- **Total Pengeluaran** = Jumlah semua pengeluaran
- **Sisa Uang** = Total Pemasukan - Total Pengeluaran

Setiap transaksi baru akan memperbarui saldo secara otomatis berdasarkan rumus:
```
Saldo Baru = Saldo Sebelumnya + Pemasukan - Pengeluaran
```

## Pengembangan Lebih Lanjut

Anda dapat mengembangkan aplikasi ini lebih lanjut dengan menambahkan fitur seperti:
- Autentikasi pengguna
- Kategori transaksi
- Laporan bulanan/tahunan
- Ekspor ke PDF
- Notifikasi saldo rendah