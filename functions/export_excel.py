import json
import os
import sys
import base64

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
        from supabase_db import init_database
        from database import export_to_excel  # Keep using SQLite for export
        
        # Initialize database
        init_database()
        
        # Export to Excel
        filename = export_to_excel()
        
        if filename and os.path.exists(filename):
            # Read the file and encode it as base64
            with open(filename, 'rb') as f:
                file_content = f.read()
            
            # Encode as base64 for JSON serialization
            encoded_content = base64.b64encode(file_content).decode('utf-8')
            
            # Clean up the file
            os.remove(filename)
            
            # Return the file content
            return {
                'statusCode': 200,
                'headers': {
                    'Content-Type': 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
                    'Content-Disposition': 'attachment; filename="catering_finance_export.xlsx"'
                },
                'body': encoded_content,
                'isBase64Encoded': True
            }
        else:
            return {
                'statusCode': 500,
                'headers': {
                    'Content-Type': 'application/json'
                },
                'body': json.dumps({
                    'status': 'error',
                    'message': 'Gagal mengekspor data'
                })
            }
    except Exception as e:
        import traceback
        error_message = f"Error: {str(e)}
Traceback: {traceback.format_exc()}"
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