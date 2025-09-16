"""
Test script to verify Supabase connection and basic operations
"""
import os
from supabase_db import init_database, add_income, add_expense, get_all_transactions, get_finance_summary

def test_supabase_connection():
    """Test Supabase connection and basic operations"""
    print("Testing Supabase connection...")
    
    try:
        # Initialize database
        init_database()
        print("Database initialization successful!")
        
        # Test adding income
        print("Testing income addition...")
        balance = add_income("16/09/2025", "Selasa", "Test Income", 100000)
        print(f"Income added successfully! New balance: {balance}")
        
        # Test adding expense
        print("Testing expense addition...")
        balance = add_expense("16/09/2025", "Selasa", "Test Expense", 50000)
        print(f"Expense added successfully! New balance: {balance}")
        
        # Test getting transactions
        print("Testing transaction retrieval...")
        transactions = get_all_transactions()
        print(f"Retrieved {len(transactions)} transactions")
        
        # Test getting summary
        print("Testing summary retrieval...")
        summary = get_finance_summary()
        print(f"Summary: {summary}")
        
        print("All tests passed!")
        
    except Exception as e:
        print(f"Test failed with error: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    test_supabase_connection()