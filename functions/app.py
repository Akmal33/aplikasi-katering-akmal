# Netlify function for handling requests
import json
import os
import sys

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
        from app import application
        from database import init_database
        
        # Initialize database
        init_database()
        
        # For Netlify functions, we need to return a response object
        # Let's create a simple response for testing
        return {
            'statusCode': 200,
            'headers': {
                'Content-Type': 'text/plain'
            },
            'body': 'Function is working!'
        }
    except Exception as e:
        import traceback
        error_message = f"Error: {str(e)}\
Traceback: {traceback.format_exc()}"
        print(error_message)
        return {
            'statusCode': 500,
            'body': json.dumps({
                'error': str(e),
                'details': error_message
            })
        }