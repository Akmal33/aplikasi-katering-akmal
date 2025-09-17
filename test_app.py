# This file is used to test that the app can be imported correctly
# It's helpful for deployment services like Render to verify the app is working

try:
    from app import app
    print("App imported successfully!")
except Exception as e:
    print(f"Error importing app: {e}")
    raise