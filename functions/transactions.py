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
        from supabase_db import init_database, get_all_transactions, get_finance_summary
        
        # Initialize database
        init_database()
        
        # Get transactions and summary
        transactions = get_all_transactions()
        summary = get_finance_summary()
        
        # Return JSON response
        return {
            'statusCode': 200,
            'headers': {
                'Content-Type': 'application/json'
            },
            'body': json.dumps({
                'transactions': transactions,
                'summary': summary
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
                'error': str(e),
                'details': error_message
            })
        }