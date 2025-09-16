# Aplikasi Keuangan Katering

Aplikasi ini digunakan untuk melacak pemasukan dan pengeluaran harian usaha katering, dengan fokus pada hari kerja (Senin-Jumat).

## Fitur Utama

- **Pencatatan Pemasukan**: Mencatat semua uang masuk dari penjualan katering
- **Pencatatan Pengeluaran Harian**: Mencatat pengeluaran harian seperti belanja bahan baku, biaya operasional, dll.
- **Perhitungan Otomatis**: Menghitung sisa uang secara otomatis setelah setiap transaksi
- **Laporan Mingguan**: Menampilkan laporan keuangan mingguan dengan rinci
- **Ekspor ke Excel**: Menyimpan data ke file Excel untuk arsip

## Struktur Data

Aplikasi menggunakan file Excel dengan kolom-kolom berikut:
1. **Tanggal** - Tanggal transaksi
2. **Hari** - Hari dalam seminggu (Senin-Jumat)
3. **Deskripsi** - Keterangan transaksi
4. **Pemasukan (Rp)** - Jumlah uang masuk
5. **Pengeluaran (Rp)** - Jumlah uang keluar
6. **Saldo (Rp)** - Saldo terkini setelah transaksi

## Cara Menggunakan

### Menjalankan Demo
```bash
python catering_finance_demo.py
```

### Menjalankan Aplikasi Interaktif
```bash
python catering_finance_tracker.py
```

### Menu Aplikasi
1. **Tambah Pemasukan** - Mencatat pemasukan baru
2. **Tambah Pengeluaran** - Mencatat pengeluaran baru
3. **Lihat Laporan Mingguan** - Menampilkan laporan keuangan
4. **Simpan dan Keluar** - Menyimpan data ke Excel dan keluar
5. **Keluar Tanpa Menyimpan** - Keluar tanpa menyimpan perubahan

## Contoh Penggunaan

### Menambahkan Pemasukan
```
Tanggal: 01/09/2025
Deskripsi: Pembayaran pesanan nasi kotak
Jumlah: 1500000
```

### Menambahkan Pengeluaran
```
Tanggal: 01/09/2025
Deskripsi: Belanja bahan baku
Jumlah: 300000
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

## File yang Dihasilkan

- `catering_finance_demo.xlsx` - File Excel yang dihasilkan dari demo
- `catering_finance.xlsx` - File Excel yang digunakan oleh aplikasi interaktif

## Persyaratan Sistem

- Python 3.6+
- Library openpyxl

## Instalasi

```bash
pip install openpyxl
```