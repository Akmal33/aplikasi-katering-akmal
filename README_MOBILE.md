# Aplikasi Keuangan Katering & Stock Card Tracker

Repositori ini berisi dua aplikasi yang berguna untuk manajemen usaha katering:

1. **Aplikasi Keuangan Katering** - Untuk melacak pemasukan, pengeluaran harian, dan sisa uang
2. **Stock Card Tracker** - Untuk melacak stok barang

## Aplikasi Keuangan Katering Mobile (Android)

Aplikasi ini dapat dibangun menjadi file .apk untuk dijalankan di perangkat Android.

### Fitur Utama

- **Pencatatan Pemasukan**: Mencatat semua uang masuk dari penjualan katering
- **Pencatatan Pengeluaran Harian**: Mencatat pengeluaran harian seperti belanja bahan baku, biaya operasional, dll.
- **Perhitungan Otomatis**: Menghitung sisa uang secara otomatis setelah setiap transaksi
- **Laporan Keuangan**: Menampilkan laporan keuangan dengan rinci
- **Ringkasan Keuangan**: Menampilkan ringkasan total pemasukan, pengeluaran, dan sisa uang
- **Ekspor ke Excel**: Menyimpan data ke file Excel untuk arsip

### Membangun Aplikasi Android (.apk)

Untuk membangun aplikasi menjadi file .apk, ikuti langkah-langkah berikut:

#### Prasyarat
1. Sistem operasi Linux atau macOS (direkomendasikan)
2. Python 3.6+
3. Buildozer

#### Instalasi Buildozer (Linux/macOS)
```bash
pip install buildozer
```

#### Membangun Aplikasi
1. Buka terminal/command prompt
2. Navigasi ke direktori proyek
3. Jalankan perintah berikut:
```bash
buildozer android debug
```

4. File .apk akan dibuat di direktori `bin/`

#### Instalasi di Perangkat Android
1. Aktifkan "Sumber Tidak Dikenal" di pengaturan perangkat Android
2. Salin file .apk ke perangkat Android
3. Buka file .apk dan instal

### Struktur File Proyek Mobile
- `main.py` - File utama aplikasi Kivy
- `buildozer.spec` - Konfigurasi untuk membangun aplikasi Android
- `requirements.txt` - Dependensi aplikasi

## Aplikasi Desktop (Versi Sebelumnya)

### Aplikasi Keuangan Katering

File Terkait:
- `catering_finance_example.py` - Contoh penggunaan aplikasi
- `catering_finance_tracker.py` - Aplikasi interaktif (memerlukan input)
- `catering_finance_demo.py` - Demo aplikasi dengan data contoh
- `catering_finance_interactive.xlsx` - File Excel hasil dari contoh penggunaan
- `catering_finance_demo.xlsx` - File Excel hasil dari demo

### Stock Card Tracker

File Terkait:
- `stock_tracker_final.py` - Aplikasi interaktif untuk pelacakan stok
- `stock_tracker_demo.py` - Demo aplikasi dengan data contoh
- `create_excel.py` - Script untuk membuat file Excel baru
- `kartu_stok_proper.xlsx` - File Excel dengan data stok contoh

## Persyaratan Sistem Desktop

- Python 3.6+
- Library openpyxl

## Instalasi Desktop

```bash
pip install openpyxl
```

## Cara Menjalankan Desktop

### Untuk melihat contoh penggunaan aplikasi keuangan:
```bash
python catering_finance_example.py
```

### Untuk melihat demo stock tracker:
```bash
python stock_tracker_demo.py
```

## Perhitungan Keuangan

Sistem secara otomatis menghitung:
- **Total Pemasukan** = Jumlah semua pemasukan
- **Total Pengeluaran** = Jumlah semua pengeluaran
- **Sisa Uang** = Total Pemasukan - Total Pengeluaran

Setiap transaksi baru akan memperbarui saldo secara otomatis berdasarkan rumus:
```
Saldo Baru = Saldo Sebelumnya + Pemasukan - Pengeluaran
```