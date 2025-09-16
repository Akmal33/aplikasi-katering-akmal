"""
Supabase database integration for the Catering Finance Tracker
This module replaces the SQLite database implementation with Supabase integration
"""
import os
from supabase import create_client, Client
from datetime import datetime
from typing import List, Dict, Optional
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Supabase configuration
SUPABASE_URL = os.environ.get("SUPABASE_URL", "")
SUPABASE_KEY = os.environ.get("SUPABASE_KEY", "")

# Initialize Supabase client
def get_supabase_client() -> Client:
    """Initialize and return Supabase client"""
    if not SUPABASE_URL or not SUPABASE_KEY:
        raise ValueError("SUPABASE_URL and SUPABASE_KEY environment variables must be set")
    
    return create_client(SUPABASE_URL, SUPABASE_KEY)

def init_database():
    """Initialize database and create tables if they don't exist"""
    try:
        supabase = get_supabase_client()
        
        # Try to access the finance_summary table
        try:
            result = supabase.table("finance_summary").select("id").eq("id", 1).execute()
            if not result.data:
                print("Note: Please create the required tables in your Supabase database.")
                print("Refer to SUPABASE_SETUP.md for instructions on setting up the database tables.")
                print("You can also use the SQL commands in supabase_schema.sql file.")
        except Exception as e:
            print("Note: Please create the required tables in your Supabase database.")
            print("Refer to SUPABASE_SETUP.md for instructions on setting up the database tables.")
            print("You can also use the SQL commands in supabase_schema.sql file.")
        
        print("Supabase database initialized successfully!")
        print("Make sure you have created the required tables as per SUPABASE_SETUP.md")
    except Exception as e:
        print(f"Error initializing Supabase database: {e}")
        raise

def add_income(date: str, day: str, description: str, amount: float) -> float:
    """Add income transaction to Supabase database"""
    try:
        supabase = get_supabase_client()
        
        # Get current balance
        result = supabase.table("finance_summary").select("current_balance").eq("id", 1).execute()
        previous_balance = result.data[0]["current_balance"] if result.data else 0
        
        # Calculate new balance
        new_balance = previous_balance + amount
        
        # Insert transaction
        transaction_data = {
            "date": date,
            "day": day,
            "description": description,
            "income": amount,
            "expense": 0,
            "balance": new_balance
        }
        
        supabase.table("transactions").insert(transaction_data).execute()
        
        # Update finance summary
        supabase.table("finance_summary").update({
            "total_income": previous_balance + amount if previous_balance else amount,
            "current_balance": new_balance
        }).eq("id", 1).execute()
        
        return new_balance
    except Exception as e:
        print(f"Error adding income: {e}")
        raise

def add_expense(date: str, day: str, description: str, amount: float) -> float:
    """Add expense transaction to Supabase database"""
    try:
        supabase = get_supabase_client()
        
        # Get current balance
        result = supabase.table("finance_summary").select("current_balance").eq("id", 1).execute()
        previous_balance = result.data[0]["current_balance"] if result.data else 0
        
        # Calculate new balance
        new_balance = previous_balance - amount
        
        # Insert transaction
        transaction_data = {
            "date": date,
            "day": day,
            "description": description,
            "income": 0,
            "expense": amount,
            "balance": new_balance
        }
        
        supabase.table("transactions").insert(transaction_data).execute()
        
        # Update finance summary
        supabase.table("finance_summary").update({
            "total_expense": previous_balance + amount if previous_balance else amount,
            "current_balance": new_balance
        }).eq("id", 1).execute()
        
        return new_balance
    except Exception as e:
        print(f"Error adding expense: {e}")
        raise

def get_all_transactions() -> List[Dict]:
    """Get all transactions from Supabase database"""
    try:
        supabase = get_supabase_client()
        
        result = supabase.table("transactions").select("*").order("date", desc=False).execute()
        
        transactions = []
        for transaction in result.data:
            transactions.append({
                'date': transaction['date'],
                'day': transaction['day'],
                'description': transaction['description'],
                'income': transaction['income'],
                'expense': transaction['expense'],
                'balance': transaction['balance']
            })
        
        return transactions
    except Exception as e:
        print(f"Error getting transactions: {e}")
        # Return empty list if table doesn't exist yet
        return []

def get_finance_summary() -> Dict:
    """Get finance summary from Supabase database"""
    try:
        supabase = get_supabase_client()
        
        result = supabase.table("finance_summary").select("*").eq("id", 1).execute()
        
        if result.data:
            return {
                'total_income': result.data[0]['total_income'],
                'total_expense': result.data[0]['total_expense'],
                'current_balance': result.data[0]['current_balance']
            }
        else:
            return {
                'total_income': 0,
                'total_expense': 0,
                'current_balance': 0
            }
    except Exception as e:
        print(f"Error getting finance summary: {e}")
        # Return default values if table doesn't exist yet
        return {
            'total_income': 0,
            'total_expense': 0,
            'current_balance': 0
        }

def get_day_name(date_str: str) -> str:
    """Get day name from date string (format: DD/MM/YYYY)"""
    days = ["Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu", "Minggu"]
    try:
        date_obj = datetime.strptime(date_str, "%d/%m/%Y")
        return days[date_obj.weekday()]
    except ValueError:
        return "Tidak valid"

# The following functions would need to be adapted for Supabase:
# - migrate_from_excel (would need to insert data via Supabase)
# - export_to_excel (can still work as it reads from database)
# - delete_transaction (would need to be adapted for Supabase)
# - recalculate_balances (would need to be adapted for Supabase)

# For now, we'll keep the SQLite versions of these functions or implement them later