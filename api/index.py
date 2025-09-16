import os
import json

# Set environment variable to indicate we're in a serverless environment
os.environ['VERCEL'] = 'true'

# Import the Flask app after setting the environment variable
from app import application

# Initialize the database
from database import init_database
init_database()

def handler(event, context):
    try:
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
        # Handle any errors
        return {
            'statusCode': 500,
            'body': json.dumps({
                'error': str(e)
            })
        }