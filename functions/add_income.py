import json
import os
import sys
from datetime import datetime

# Add the current directory to the Python path
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
if parent_dir not in sys.path:
    sys.path.insert(0, parent_dir)

def handler(event, context):
    try:
        # Set environment variable to indicate we're in a serverless environment
        os.environ['NETLIFY'] = 'true'
        
        # Import modules after setting environment variable
        from supabase_db import init_database, add_income, get_day_name
        
        # Initialize database
        init_database()
        
        # Parse the request body
        body = json.loads(event.get('body', '{}'))
        date = body.get('date')
        description = body.get('description')
        amount = float(body.get('amount', 0))
        
        # Validate input
        if not date or not description or amount <= 0:
            return {
                'statusCode': 400,
                'headers': {
                    'Content-Type': 'application/json'
                },
                'body': json.dumps({
                    'status': 'error',
                    'message': 'Invalid input data'
                })
            }
        
        # Format tanggal untuk tampilan (DD/MM/YYYY)
        display_date = datetime.strptime(date, "%Y-%m-%d").strftime("%d/%m/%Y")
        day = get_day_name(display_date)
        
        # Add income
        balance = add_income(display_date, day, description, amount)
        
        # Return success response
        return {
            'statusCode': 200,
            'headers': {
                'Content-Type': 'application/json'
            },
            'body': json.dumps({
                'status': 'success',
                'message': f'Pemasukan berhasil ditambahkan! Saldo terbaru: Rp {balance:,.0f}',
                'balance': balance
            })
        }
    except Exception as e:
        import traceback
        error_message = f"Error: {str(e)}\nTraceback: {traceback.format_exc()}"
        print(error_message)
        return {
            'statusCode': 500,
            'headers': {
                'Content-Type': 'application/json'
            },
            'body': json.dumps({
                'status': 'error',
                'message': f'Terjadi kesalahan: {str(e)}'
            })
        }