"""
Helper script to validate Supabase configuration and provide setup instructions
"""
import os
from dotenv import load_dotenv

def validate_supabase_config():
    """Validate Supabase configuration and provide setup instructions"""
    # Load environment variables from .env file
    load_dotenv()
    
    # Supabase configuration
    SUPABASE_URL = os.environ.get("SUPABASE_URL", "")
    SUPABASE_KEY = os.environ.get("SUPABASE_KEY", "")
    
    print("Supabase Configuration Validation:")
    print("=" * 50)
    
    # Check if .env file exists
    if not os.path.exists(".env"):
        print("X .env file not found!")
        print("\nTo fix this issue:")
        print("1. Copy .env.example to .env:")
        print("   cp .env.example .env")
        print("2. Edit .env file with your actual Supabase credentials")
        return False
    
    # Check if credentials are set
    if not SUPABASE_URL or not SUPABASE_KEY:
        print("X Supabase credentials not found in .env file!")
        print("\nTo fix this issue:")
        print("1. Edit your .env file and add your Supabase credentials")
        print("2. The file should contain:")
        print("   SUPABASE_URL=your_actual_supabase_url")
        print("   SUPABASE_KEY=your_actual_service_role_key")
        return False
    
    # Check if credentials are placeholder values
    if SUPABASE_URL == "your_supabase_project_url_here" or SUPABASE_KEY == "your_supabase_service_role_key_here":
        print("X Supabase credentials are still placeholder values!")
        print("\nTo fix this issue:")
        print("1. Get your Supabase credentials from your Supabase dashboard:")
        print("   - Go to https://app.supabase.com/")
        print("   - Select your project")
        print("   - Go to Project Settings > API")
        print("   - Copy your Project URL and Service Role Key")
        print("2. Update your .env file with these values")
        return False
    
    # Check if URL looks valid
    if not SUPABASE_URL.startswith("https://"):
        print("X Supabase URL doesn't look valid!")
        print("   URL should start with 'https://'")
        return False
    
    print("[OK] Supabase configuration appears to be valid!")
    print(f"   URL: {SUPABASE_URL[:30]}...")
    print("   Key: ********** (hidden for security)")
    return True

def show_supabase_setup_instructions():
    """Show detailed instructions for setting up Supabase"""
    print("\n" + "=" * 50)
    print("SUPABASE SETUP INSTRUCTIONS")
    print("=" * 50)
    print("\n1. Create a Supabase account:")
    print("   - Go to https://app.supabase.com/")
    print("   - Sign up for a free account")
    print("\n2. Create a new project:")
    print("   - Click 'New Project'")
    print("   - Enter project name and password")
    print("   - Select region")
    print("   - Click 'Create Project'")
    print("\n3. Get your API credentials:")
    print("   - After project is created, go to Project Settings > API")
    print("   - Copy your 'Project URL' (SUPABASE_URL)")
    print("   - Copy your 'Service Role Key' (SUPABASE_KEY)")
    print("\n4. Update your .env file:")
    print("   - Open .env file in your project directory")
    print("   - Replace the placeholder values with your actual credentials")
    print("\n5. Set up database tables:")
    print("   - Go to SQL Editor in your Supabase dashboard")
    print("   - Copy and paste the contents of supabase_schema.sql")
    print("   - Run the SQL commands")
    print("\n6. Run the application:")
    print("   python app.py")

if __name__ == "__main__":
    if not validate_supabase_config():
        show_supabase_setup_instructions()
    else:
        print("\n[OK] Your Supabase configuration is ready!")
        print("You can now run your application with: python app.py")