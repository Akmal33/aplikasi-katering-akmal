# Supabase Database Setup

This application uses Supabase as its database. Follow these steps to set up your Supabase database:

## 1. Create Supabase Project

1. Go to [Supabase Dashboard](https://app.supabase.com/)
2. Create a new project
3. Note down your Project URL and Service Role Key

## 2. Set up Environment Variables

Create a `.env` file in the root directory with your Supabase credentials:

```
SUPABASE_URL=your_supabase_project_url_herehttps://zuanrdxhdpwxpdjcurad.supabase.co
SUPABASE_KEY=yeyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Inp1YW5yZHhoZHB3eHBkamN1cmFkIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NTc5OTkzOTUsImV4cCI6MjA3MzU3NTM5NX0.iW3CBNkFRsH52QEYIA0f5B3fdtgc1l9MqiEyl4qkQ7o
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

## 4. Configure Row Level Security (RLS)

This application uses Row Level Security (RLS) to control access to the database tables. The SQL schema includes policies that allow all operations when using the service role key.

If you're using the service role key (recommended for server-side operations), these policies will allow all operations. However, if you're using the anonymous key, you might need to adjust the policies in the `supabase_schema.sql` file.

## 5. Run the Application

After setting up the database, you can run the application:

```bash
python app.py
```