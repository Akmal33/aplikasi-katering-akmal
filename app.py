from flask import Flask, render_template, request, jsonify, send_file, url_for
import os
from datetime import datetime
from database import init_database, add_income, add_expense, get_all_transactions, get_finance_summary, get_day_name, export_to_excel

app = Flask(__name__, static_url_path='/static')

# Inisialisasi database
init_database()

@app.context_processor
def override_url_for():
    return dict(url_for=dated_url_for)

def dated_url_for(endpoint, **values):
    if endpoint == 'static':
        filename = values.get('filename', None)
        if filename:
            file_path = os.path.join(app.root_path, endpoint, filename)
            values['q'] = int(os.stat(file_path).st_mtime)
    return url_for(endpoint, **values)

@app.route('/')
def index():
    """Halaman utama"""
    transactions = get_all_transactions()
    summary = get_finance_summary()
    
    return render_template('index.html', 
                         transactions=transactions,
                         total_income=summary['total_income'],
                         total_expense=summary['total_expense'],
                         current_balance=summary['current_balance'])

@app.route('/add_income', methods=['POST'])
def add_income_route():
    """Route untuk menambahkan pemasukan"""
    try:
        data = request.get_json()
        date = data['date']
        description = data['description']
        amount = float(data['amount'])
        
        # Format tanggal untuk tampilan (DD/MM/YYYY)
        display_date = datetime.strptime(date, "%Y-%m-%d").strftime("%d/%m/%Y")
        day = get_day_name(display_date)
        
        balance = add_income(display_date, day, description, amount)
        
        return jsonify({
            'status': 'success',
            'message': f'Pemasukan berhasil ditambahkan! Saldo terbaru: Rp {balance:,.0f}',
            'balance': balance
        })
    except Exception as e:
        return jsonify({
            'status': 'error',
            'message': f'Terjadi kesalahan: {str(e)}'
        }), 400

@app.route('/add_expense', methods=['POST'])
def add_expense_route():
    """Route untuk menambahkan pengeluaran"""
    try:
        data = request.get_json()
        date = data['date']
        description = data['description']
        amount = float(data['amount'])
        
        # Format tanggal untuk tampilan (DD/MM/YYYY)
        display_date = datetime.strptime(date, "%Y-%m-%d").strftime("%d/%m/%Y")
        day = get_day_name(display_date)
        
        balance = add_expense(display_date, day, description, amount)
        
        return jsonify({
            'status': 'success',
            'message': f'Pengeluaran berhasil ditambahkan! Saldo terbaru: Rp {balance:,.0f}',
            'balance': balance
        })
    except Exception as e:
        return jsonify({
            'status': 'error',
            'message': f'Terjadi kesalahan: {str(e)}'
        }), 400

@app.route('/export_excel')
def export_excel_route():
    """Route untuk mengekspor data ke Excel"""
    try:
        filename = export_to_excel()
        if filename:
            return send_file(filename, as_attachment=True)
        else:
            return jsonify({'status': 'error', 'message': 'Gagal mengekspor data'}), 500
    except Exception as e:
        return jsonify({'status': 'error', 'message': f'Terjadi kesalahan: {str(e)}'}), 500

# Route untuk file statis PWA
@app.route('/manifest.json')
def manifest():
    return app.send_static_file('manifest.json')

@app.route('/service-worker.js')
def service_worker():
    return app.send_static_file('service-worker.js')

# Untuk Netlify Functions
if __name__ != '__main__':
    application = app
else:
    app.run(debug=True, host='0.0.0.0', port=5000)