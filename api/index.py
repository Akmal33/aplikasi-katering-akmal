# Vercel function for handling requests
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
        os.environ['VERCEL'] = 'true'
        
        # Import modules after setting environment variable
        from app import application
        from supabase_db import init_database
        
        # Initialize database
        init_database()
        
        # Extract the request details from the event
        path = event.get('path', '/')
        http_method = event.get('httpMethod', 'GET')
        headers = event.get('headers', {})
        query_string_parameters = event.get('queryStringParameters', {})
        body = event.get('body', '')
        
        # Handle base64 encoded body for binary data
        is_base64_encoded = event.get('isBase64Encoded', False)
        
        # Create a test client with the Flask app
        with application.test_client() as client:
            # Make the request to our Flask app
            response = client.open(
                path=path,
                method=http_method,
                headers=headers,
                data=body,
                query_string=query_string_parameters
            )
            
            # Prepare the response for Vercel
            return {
                'statusCode': response.status_code,
                'headers': dict(response.headers),
                'body': response.get_data(as_text=True)
            }
    except Exception as e:
        import traceback
        error_message = f"Error: {str(e)}\nTraceback: {traceback.format_exc()}"
        print(error_message)
        return {
            'statusCode': 500,
            'body': json.dumps({
                'error': str(e),
                'details': error_message
            })
        }