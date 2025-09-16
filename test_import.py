import sys
import os

# Add the current directory to the Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

try:
    # Try to import the app
    from app import app
    print("App imported successfully!")
    
    # Try to import the database module
    from database import init_database
    print("Database module imported successfully!")
    
    # Try to initialize the database
    init_database()
    print("Database initialized successfully!")
    
except Exception as e:
    print(f"Error: {e}")
    import traceback
    traceback.print_exc()