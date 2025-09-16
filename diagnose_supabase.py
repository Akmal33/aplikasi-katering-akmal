"""
Detailed diagnostic script for Supabase connection
"""
import os
from dotenv import load_dotenv
from supabase import create_client, Client

def diagnose_supabase_connection():
    """Diagnose Supabase connection issues"""
    print("Supabase Connection Diagnostic:")
    print("=" * 40)
    
    # Load environment variables from .env file
    load_dotenv()
    
    # Supabase configuration
    SUPABASE_URL = os.environ.get("SUPABASE_URL", "")
    SUPABASE_KEY = os.environ.get("SUPABASE_KEY", "")
    
    print(f"Environment Variables:")
    print(f"  SUPABASE_URL: {repr(SUPABASE_URL)}")
    print(f"  SUPABASE_KEY: {repr(SUPABASE_KEY)}")
    
    # Check for common issues
    if not SUPABASE_URL:
        print("ERROR: SUPABASE_URL is empty!")
        return
    
    if not SUPABASE_KEY:
        print("ERROR: SUPABASE_KEY is empty!")
        return
    
    if SUPABASE_URL == "your_supabase_project_url_here":
        print("ERROR: SUPABASE_URL is still the placeholder value!")
        return
    
    if SUPABASE_KEY == "your_supabase_service_role_key_here":
        print("ERROR: SUPABASE_KEY is still the placeholder value!")
        return
    
    if not SUPABASE_URL.startswith("https://"):
        print("ERROR: SUPABASE_URL doesn't start with 'https://'")
        return
    
    # Try to create client
    print("\nAttempting to create Supabase client...")
    try:
        supabase = create_client(SUPABASE_URL, SUPABASE_KEY)
        print("SUCCESS: Supabase client created successfully!")
        
        # Try a simple operation
        print("\nAttempting to access finance_summary table...")
        result = supabase.table("finance_summary").select("id").eq("id", 1).execute()
        print("SUCCESS: Table access successful!")
        print(f"  Result: {result}")
        
    except Exception as e:
        print(f"ERROR: Failed to create Supabase client or access table: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    diagnose_supabase_connection()