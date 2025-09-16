# Aplikasi Keuangan Katering & Stock Card Tracker

Repositori ini berisi dua aplikasi yang berguna untuk manajemen usaha katering:

1. **Aplikasi Keuangan Katering** - Untuk melacak pemasukan, pengeluaran harian, dan sisa uang
2. **Stock Card Tracker** - Untuk melacak stok barang

## Aplikasi Keuangan Katering

Aplikasi ini digunakan untuk melacak pemasukan dan pengeluaran harian usaha katering, dengan fokus pada hari kerja (Senin-Jumat).

### Fitur Utama

- **Pencatatan Pemasukan**: Mencatat semua uang masuk dari penjualan katering
- **Pencatatan Pengeluaran Harian**: Mencatat pengeluaran harian seperti belanja bahan baku, biaya operasional, dll.
- **Perhitungan Otomatis**: Menghitung sisa uang secara otomatis setelah setiap transaksi
- **Laporan Mingguan**: Menampilkan laporan keuangan mingguan dengan rinci
- **Ekspor ke Excel**: Menyimpan data ke file Excel untuk arsip

### File Terkait

- `catering_finance_example.py` - Contoh penggunaan aplikasi
- `catering_finance_tracker.py` - Aplikasi interaktif (memerlukan input)
- `catering_finance_demo.py` - Demo aplikasi dengan data contoh
- `catering_finance_interactive.xlsx` - File Excel hasil dari contoh penggunaan
- `catering_finance_demo.xlsx` - File Excel hasil dari demo

### Cara Menjalankan

Untuk melihat contoh penggunaan:
```bash
python catering_finance_example.py
```

### Perhitungan Keuangan

Sistem secara otomatis menghitung:
- **Total Pemasukan** = Jumlah semua pemasukan
- **Total Pengeluaran** = Jumlah semua pengeluaran
- **Sisa Uang** = Total Pemasukan - Total Pengeluaran

Setiap transaksi baru akan memperbarui saldo secara otomatis berdasarkan rumus:
```
Saldo Baru = Saldo Sebelumnya + Pemasukan - Pengeluaran
```

## Stock Card Tracker

Aplikasi ini digunakan untuk melacak pergerakan stok barang secara detail.

### Fitur Utama

- **Pelacakan Stok**: Mencatat barang masuk dan keluar
- **Perhitungan Saldo Otomatis**: Menghitung saldo stok saat ini
- **Antarmuka Interaktif**: Mudah digunakan dengan menu
- **Ekspor ke Excel**: Menyimpan data ke file Excel

### File Terkait

- `stock_tracker_final.py` - Aplikasi interaktif untuk pelacakan stok
- `stock_tracker_demo.py` - Demo aplikasi dengan data contoh
- `create_excel.py` - Script untuk membuat file Excel baru
- `kartu_stok_proper.xlsx` - File Excel dengan data stok contoh

### Cara Menjalankan

Untuk melihat demo:
```bash
python stock_tracker_demo.py
```

## Persyaratan Sistem

- Python 3.6+
- Library openpyxl

## Instalasi

```bash
pip install openpyxl
```

## Struktur Kolom Excel

### Keuangan Katering
1. **Tanggal** - Tanggal transaksi
2. **Hari** - Hari dalam seminggu (Senin-Jumat)
3. **Deskripsi** - Keterangan transaksi
4. **Pemasukan (Rp)** - Jumlah uang masuk
5. **Pengeluaran (Rp)** - Jumlah uang keluar
6. **Saldo (Rp)** - Saldo terkini setelah transaksi

### Stock Card
1. **No.** - Nomor urut entri
2. **Tanggal** - Tanggal transaksi
3. **Keterangan** - Keterangan transaksi
4. **Masuk** - Jumlah barang masuk
5. **Keluar** - Jumlah barang keluar
6. **Sisa** - Saldo stok terkini

Kedua aplikasi ini dirancang untuk membantu pemilik usaha katering dalam mengelola keuangan dan stok barang secara efektif.