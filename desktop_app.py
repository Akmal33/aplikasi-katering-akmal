import tkinter as tk
from tkinter import ttk, messagebox, filedialog
from datetime import datetime
# Use Supabase database instead of SQLite
from supabase_db import init_database, add_income, add_expense, get_all_transactions, get_finance_summary, get_day_name
# Keep SQLite for export functionality
from database import export_to_excel

class CateringFinanceApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Aplikasi Keuangan Katering")
        self.root.geometry("1000x700")
        
        # Inisialisasi database
        init_database()
        
        # Buat UI
        self.create_widgets()
        self.refresh_data()
    
    def create_widgets(self):
        # Frame utama
        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Frame untuk form pemasukan
        income_frame = ttk.LabelFrame(main_frame, text="Tambah Pemasukan", padding="10")
        income_frame.grid(row=0, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=(0, 10))
        
        ttk.Label(income_frame, text="Tanggal:").grid(row=0, column=0, sticky=tk.W, padx=(0, 5))
        self.income_date = ttk.Entry(income_frame, width=15)
        self.income_date.grid(row=0, column=1, sticky=tk.W, padx=(0, 10))
        self.income_date.insert(0, datetime.now().strftime("%d/%m/%Y"))
        
        ttk.Label(income_frame, text="Deskripsi:").grid(row=0, column=2, sticky=tk.W, padx=(0, 5))
        self.income_desc = ttk.Entry(income_frame, width=30)
        self.income_desc.grid(row=0, column=3, sticky=(tk.W, tk.E), padx=(0, 10))
        
        ttk.Label(income_frame, text="Jumlah (Rp):").grid(row=0, column=4, sticky=tk.W, padx=(0, 5))
        self.income_amount = ttk.Entry(income_frame, width=15)
        self.income_amount.grid(row=0, column=5, sticky=tk.W, padx=(0, 10))
        
        ttk.Button(income_frame, text="Tambah Pemasukan", command=self.add_income).grid(row=0, column=6, sticky=tk.W)
        
        # Frame untuk form pengeluaran
        expense_frame = ttk.LabelFrame(main_frame, text="Tambah Pengeluaran", padding="10")
        expense_frame.grid(row=1, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=(0, 10))
        
        ttk.Label(expense_frame, text="Tanggal:").grid(row=0, column=0, sticky=tk.W, padx=(0, 5))
        self.expense_date = ttk.Entry(expense_frame, width=15)
        self.expense_date.grid(row=0, column=1, sticky=tk.W, padx=(0, 10))
        self.expense_date.insert(0, datetime.now().strftime("%d/%m/%Y"))
        
        ttk.Label(expense_frame, text="Deskripsi:").grid(row=0, column=2, sticky=tk.W, padx=(0, 5))
        self.expense_desc = ttk.Entry(expense_frame, width=30)
        self.expense_desc.grid(row=0, column=3, sticky=(tk.W, tk.E), padx=(0, 10))
        
        ttk.Label(expense_frame, text="Jumlah (Rp):").grid(row=0, column=4, sticky=tk.W, padx=(0, 5))
        self.expense_amount = ttk.Entry(expense_frame, width=15)
        self.expense_amount.grid(row=0, column=5, sticky=tk.W, padx=(0, 10))
        
        ttk.Button(expense_frame, text="Tambah Pengeluaran", command=self.add_expense).grid(row=0, column=6, sticky=tk.W)
        
        # Frame untuk ringkasan keuangan
        summary_frame = ttk.LabelFrame(main_frame, text="Ringkasan Keuangan", padding="10")
        summary_frame.grid(row=2, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=(0, 10))
        
        self.total_income_label = ttk.Label(summary_frame, text="Total Pemasukan: Rp 0", font=("Arial", 12, "bold"), foreground="green")
        self.total_income_label.grid(row=0, column=0, padx=(0, 20))
        
        self.total_expense_label = ttk.Label(summary_frame, text="Total Pengeluaran: Rp 0", font=("Arial", 12, "bold"), foreground="red")
        self.total_expense_label.grid(row=0, column=1, padx=(0, 20))
        
        self.balance_label = ttk.Label(summary_frame, text="Sisa Uang: Rp 0", font=("Arial", 12, "bold"), foreground="blue")
        self.balance_label.grid(row=0, column=2)
        
        # Frame untuk tombol ekspor
        export_frame = ttk.Frame(main_frame)
        export_frame.grid(row=3, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=(0, 10))
        
        ttk.Button(export_frame, text="Ekspor ke Excel", command=self.export_to_excel).grid(row=0, column=0, sticky=tk.W)
        
        # Frame untuk tabel transaksi
        transactions_frame = ttk.LabelFrame(main_frame, text="Daftar Transaksi", padding="10")
        transactions_frame.grid(row=4, column=0, columnspan=2, sticky=(tk.W, tk.E, tk.N, tk.S), pady=(0, 10))
        
        # Scrollbar
        scrollbar_y = ttk.Scrollbar(transactions_frame, orient=tk.VERTICAL)
        scrollbar_y.grid(row=0, column=1, sticky=(tk.N, tk.S))
        
        scrollbar_x = ttk.Scrollbar(transactions_frame, orient=tk.HORIZONTAL)
        scrollbar_x.grid(row=1, column=0, sticky=(tk.W, tk.E))
        
        # Treeview untuk tabel transaksi
        self.transactions_tree = ttk.Treeview(transactions_frame, 
                                             columns=("Tanggal", "Hari", "Deskripsi", "Pemasukan", "Pengeluaran", "Saldo"),
                                             show="headings",
                                             yscrollcommand=scrollbar_y.set,
                                             xscrollcommand=scrollbar_x.set,
                                             height=15)
        
        # Konfigurasi scrollbar
        scrollbar_y.config(command=self.transactions_tree.yview)
        scrollbar_x.config(command=self.transactions_tree.xview)
        
        # Definisikan heading
        self.transactions_tree.heading("Tanggal", text="Tanggal")
        self.transactions_tree.heading("Hari", text="Hari")
        self.transactions_tree.heading("Deskripsi", text="Deskripsi")
        self.transactions_tree.heading("Pemasukan", text="Pemasukan")
        self.transactions_tree.heading("Pengeluaran", text="Pengeluaran")
        self.transactions_tree.heading("Saldo", text="Saldo")
        
        # Definisikan lebar kolom
        self.transactions_tree.column("Tanggal", width=100)
        self.transactions_tree.column("Hari", width=100)
        self.transactions_tree.column("Deskripsi", width=250)
        self.transactions_tree.column("Pemasukan", width=120)
        self.transactions_tree.column("Pengeluaran", width=120)
        self.transactions_tree.column("Saldo", width=120)
        
        self.transactions_tree.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Tombol refresh
        button_frame = ttk.Frame(main_frame)
        button_frame.grid(row=5, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=(10, 0))
        
        ttk.Button(button_frame, text="Refresh Data", command=self.refresh_data).grid(row=0, column=0, sticky=tk.W)
        
        # Konfigurasi grid weights
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        main_frame.columnconfigure(0, weight=1)
        main_frame.rowconfigure(4, weight=1)
        transactions_frame.columnconfigure(0, weight=1)
        transactions_frame.rowconfigure(0, weight=1)
    
    def add_income(self):
        try:
            date = self.income_date.get()
            description = self.income_desc.get()
            amount = float(self.income_amount.get())
            
            if not date or not description or amount <= 0:
                messagebox.showerror("Error", "Harap isi semua field dengan benar!")
                return
            
            day = get_day_name(date)
            balance = add_income(date, day, description, amount)
            
            messagebox.showinfo("Sukses", f"Pemasukan berhasil ditambahkan!\nSaldo terbaru: Rp {balance:,.0f}")
            
            # Reset form
            self.income_desc.delete(0, tk.END)
            self.income_amount.delete(0, tk.END)
            
            # Refresh data
            self.refresh_data()
            
        except ValueError:
            messagebox.showerror("Error", "Jumlah harus berupa angka!")
        except Exception as e:
            messagebox.showerror("Error", f"Terjadi kesalahan: {str(e)}")
    
    def add_expense(self):
        try:
            date = self.expense_date.get()
            description = self.expense_desc.get()
            amount = float(self.expense_amount.get())
            
            if not date or not description or amount <= 0:
                messagebox.showerror("Error", "Harap isi semua field dengan benar!")
                return
            
            day = get_day_name(date)
            balance = add_expense(date, day, description, amount)
            
            messagebox.showinfo("Sukses", f"Pengeluaran berhasil ditambahkan!\nSaldo terbaru: Rp {balance:,.0f}")
            
            # Reset form
            self.expense_desc.delete(0, tk.END)
            self.expense_amount.delete(0, tk.END)
            
            # Refresh data
            self.refresh_data()
            
        except ValueError:
            messagebox.showerror("Error", "Jumlah harus berupa angka!")
        except Exception as e:
            messagebox.showerror("Error", f"Terjadi kesalahan: {str(e)}")
    
    def export_to_excel(self):
        try:
            filename = export_to_excel()
            if filename:
                messagebox.showinfo("Sukses", f"Data berhasil diekspor ke {filename}")
            else:
                messagebox.showwarning("Peringatan", "Gagal mengekspor data. Pastikan openpyxl telah diinstal.")
        except Exception as e:
            messagebox.showerror("Error", f"Gagal mengekspor data: {str(e)}")
    
    def refresh_data(self):
        # Dapatkan data transaksi
        transactions = get_all_transactions()
        summary = get_finance_summary()
        
        # Update ringkasan keuangan
        self.total_income_label.config(text=f"Total Pemasukan: Rp {summary['total_income']:,.0f}")
        self.total_expense_label.config(text=f"Total Pengeluaran: Rp {summary['total_expense']:,.0f}")
        self.balance_label.config(text=f"Sisa Uang: Rp {summary['current_balance']:,.0f}")
        
        # Clear treeview
        for item in self.transactions_tree.get_children():
            self.transactions_tree.delete(item)
        
        # Tambahkan data transaksi ke treeview
        for transaction in transactions:
            # Format nilai dengan pemisah ribuan
            income = f"Rp {transaction['income']:,.0f}" if transaction['income'] > 0 else ""
            expense = f"Rp {transaction['expense']:,.0f}" if transaction['expense'] > 0 else ""
            balance = f"Rp {transaction['balance']:,.0f}"
            
            self.transactions_tree.insert("", "end", values=(
                transaction['date'],
                transaction['day'],
                transaction['description'],
                income,
                expense,
                balance
            ))

def main():
    root = tk.Tk()
    app = CateringFinanceApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()