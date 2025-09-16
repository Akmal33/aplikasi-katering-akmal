import json
from app import application

def handler(event, context):
    # Extract the request details from the event
    path = event.get('path', '/')
    http_method = event.get('httpMethod', 'GET')
    headers = event.get('headers', {})
    query_string_parameters = event.get('queryStringParameters', {})
    body = event.get('body', '')
    
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
        
        # Prepare the response for Netlify
        return {
            'statusCode': response.status_code,
            'headers': dict(response.headers),
            'body': response.get_data(as_text=True)
        }