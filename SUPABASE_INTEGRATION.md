# Supabase Integration Guide

This guide explains how to set up Supabase as the database backend for the Catering Finance Tracker application.

## Prerequisites

1. A Supabase account (free tier available at [supabase.com](https://supabase.com))
2. Python 3.9 or higher
3. The required Python packages installed (`pip install -r requirements.txt`)

## Setting up Supabase

### 1. Create a Supabase Project

1. Go to [supabase.com](https://supabase.com) and sign up or log in
2. Click "New Project"
3. Enter a project name (e.g., "catering-finance-tracker")
4. Set a database password (save this for later)
5. Select a region
6. Click "Create New Project"

### 2. Get Project Credentials

1. After the project is created, go to the "Project Settings" (gear icon)
2. Click "API" in the sidebar
3. Copy the following values:
   - Project URL (SUPABASE_URL)
   - anon public key or service role key (SUPABASE_KEY)

### 3. Create Database Tables

In the Supabase dashboard:

1. Go to "Table Editor"
2. Create the `transactions` table with the following columns:
   - `id` (int8, primary key, auto increment)
   - `date` (text)
   - `day` (text)
   - `description` (text)
   - `income` (float8, default: 0)
   - `expense` (float8, default: 0)
   - `balance` (float8, default: 0)
   - `created_at` (timestamptz, default: now())

3. Create the `finance_summary` table with the following columns:
   - `id` (int8, primary key)
   - `total_income` (float8, default: 0)
   - `total_expense` (float8, default: 0)
   - `current_balance` (float8, default: 0)
   - `last_updated` (timestamptz, default: now())

4. Insert a default row into `finance_summary`:
   ```sql
   INSERT INTO finance_summary (id, total_income, total_expense, current_balance)
   VALUES (1, 0, 0, 0);
   ```

## Environment Configuration

Set the following environment variables in your deployment platform:

```
SUPABASE_URL=your_supabase_project_url
SUPABASE_KEY=your_supabase_api_key
```

For local development, you can create a `.env` file:
```
SUPABASE_URL=https://your-project.supabase.co
SUPABASE_KEY=your-service-role-or-anon-key
```

## Local Development

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Set environment variables:
   ```bash
   export SUPABASE_URL=your_supabase_project_url
   export SUPABASE_KEY=your_supabase_api_key
   ```

3. Run the application:
   ```bash
   python app.py
   ```

## Deployment

### Netlify

1. Set environment variables in Netlify:
   - Go to your site settings
   - Navigate to "Build & deploy" > "Environment"
   - Add `SUPABASE_URL` and `SUPABASE_KEY` as environment variables

2. Deploy as usual

### Vercel

1. Set environment variables in Vercel:
   - Go to your project settings
   - Navigate to "Environment Variables"
   - Add `SUPABASE_URL` and `SUPABASE_KEY` as environment variables

2. Deploy as usual

## Benefits of Using Supabase

1. **Persistent Data**: Unlike SQLite which is ephemeral on serverless platforms, Supabase provides persistent data storage
2. **Real-time Updates**: Supabase supports real-time data updates
3. **Scalability**: Supabase can scale with your application's needs
4. **Authentication**: Built-in user authentication (optional)
5. **Dashboard**: Web-based dashboard for database management

## Troubleshooting

### Common Issues

1. **Connection Errors**: Verify that your SUPABASE_URL and SUPABASE_KEY are correct
2. **Permission Errors**: Ensure your API key has the necessary permissions
3. **Table Not Found**: Make sure you've created the required tables in your Supabase project

### Debugging

Enable debug logging by setting:
```
SUPABASE_DEBUG=true
```

This will provide more detailed error messages in case of issues.