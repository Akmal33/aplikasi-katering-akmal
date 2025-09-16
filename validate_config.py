"""
Helper script to validate Supabase configuration
"""
import os
from dotenv import load_dotenv

def validate_supabase_config():
    """Validate Supabase configuration"""
    # Load environment variables from .env file
    load_dotenv()
    
    # Supabase configuration
    SUPABASE_URL = os.environ.get("SUPABASE_URL", "")
    SUPABASE_KEY = os.environ.get("SUPABASE_KEY", "")
    
    print("Supabase Configuration Validation:")
    print("=" * 40)
    
    # Check if .env file exists
    if not os.path.exists(".env"):
        print("ERROR: .env file not found!")
        print("   Please create a .env file with your Supabase credentials")
        return False
    
    # Check if credentials are set
    if not SUPABASE_URL or not SUPABASE_KEY:
        print("ERROR: Supabase credentials not found in .env file!")
        print("   Please set SUPABASE_URL and SUPABASE_KEY in your .env file")
        return False
    
    # Check if credentials are placeholder values
    if SUPABASE_URL == "your_supabase_project_url_here" or SUPABASE_KEY == "your_supabase_service_role_key_here":
        print("ERROR: Supabase credentials are still placeholder values!")
        print("   Please update your .env file with actual Supabase credentials")
        return False
    
    # Check if URL looks valid
    if not SUPABASE_URL.startswith("https://"):
        print("ERROR: Supabase URL doesn't look valid!")
        print("   URL should start with 'https://'")
        return False
    
    print("SUCCESS: Supabase configuration appears to be valid!")
    print(f"   URL: {SUPABASE_URL[:30]}...")
    print("   Key: ********** (hidden for security)")
    return True

if __name__ == "__main__":
    validate_supabase_config()