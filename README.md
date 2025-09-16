# Stock Card Tracker

A Python application for tracking inventory movements using Excel files.

## Features

- Read and display stock card data from Excel files
- Add new stock entries (incoming and outgoing)
- Automatically calculate current stock balance
- Save updated data back to Excel

## Requirements

- Python 3.6 or higher
- openpyxl library

## Installation

1. Install the required library:
   ```
   pip install openpyxl
   ```

## Usage

### Using the Demo Script

Run the demo script to see the functionality in action:
```
python stock_tracker_demo.py
```

### Using the Interactive Version

Run the interactive version for manual input:
```
python stock_tracker_final.py
```

## File Structure

- `stock_tracker_final.py` - Interactive version with menu system
- `stock_tracker_demo.py` - Demonstration version with predefined entries
- `stock_tracker_fixed.py` - Earlier version (not recommended)
- `stock_tracker.py` - Initial version with issues (not recommended)
- `create_excel.py` - Script to create a new Excel file with sample data
- `kartu_stok_proper.xlsx` - Properly formatted Excel file with sample data

## How It Works

The application tracks inventory movements with the following columns:
1. No. - Entry number
2. Tanggal - Date of transaction
3. Keterangan - Description of transaction
4. Masuk - Incoming quantity
5. Keluar - Outgoing quantity
6. Sisa - Current balance (automatically calculated)

Each new entry automatically calculates the new balance based on:
```
New Balance = Previous Balance + Incoming - Outgoing
```

## Example Data

| No. | Tanggal      | Keterangan           | Masuk | Keluar | Sisa  |
|-----|--------------|----------------------|-------|--------|-------|
| 1   | 01/09/2025   | Pembelian awal       | 100   | 0      | 100   |
| 2   | 05/09/2025   | Barang terjual       | 0     | 20     | 80    |
| 3   | 10/09/2025   | Pembelian tambahan   | 50    | 0      | 130   |
| 4   | 15/09/2025   | Barang terjual       | 0     | 30     | 100   |