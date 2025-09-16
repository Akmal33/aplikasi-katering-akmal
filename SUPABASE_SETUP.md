# Supabase Database Setup

This application uses Supabase as its database. Follow these steps to set up your Supabase database:

## 1. Create Supabase Project

1. Go to [Supabase Dashboard](https://app.supabase.com/)
2. Create a new project
3. Note down your Project URL and Service Role Key

## 2. Set up Environment Variables

Create a `.env` file in the root directory with your Supabase credentials:

```
SUPABASE_URL=your_supabase_project_url_here
SUPABASE_KEY=your_supabase_service_role_key_here
```

## 3. Create Database Tables

You need to create the required tables in your Supabase database. You can do this in two ways:

### Option A: Using Supabase SQL Editor

1. Go to your Supabase project dashboard
2. Navigate to SQL Editor
3. Copy and paste the contents of `supabase_schema.sql` into the editor
4. Run the SQL commands

### Option B: Using Supabase Table Editor

1. Go to your Supabase project dashboard
2. Navigate to Table Editor
3. Create the following tables manually:

#### transactions table:
- id (int8, primary key, auto-generated)
- date (text)
- day (text)
- description (text)
- income (float8, default: 0)
- expense (float8, default: 0)
- balance (float8, default: 0)
- created_at (timestamptz, default: now())

#### finance_summary table:
- id (int8, primary key)
- total_income (float8, default: 0)
- total_expense (float8, default: 0)
- current_balance (float8, default: 0)
- last_updated (timestamptz, default: now())

Then insert the initial record into finance_summary:
```sql
INSERT INTO finance_summary (id, total_income, total_expense, current_balance)
VALUES (1, 0, 0, 0);
```

## 4. Run the Application

After setting up the database, you can run the application:

```bash
python app.py
```