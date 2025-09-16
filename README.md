# Catering Finance Tracker with Supabase

A simple finance tracking application for catering businesses with Supabase integration.

## Prerequisites

- Python 3.7 or higher
- A Supabase account (free tier available)

## Setup Instructions

### 1. Clone the Repository

```bash
git clone <repository-url>
cd catering-finance-tracker
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Set up Supabase

1. Create a Supabase project:
   - Go to [Supabase Dashboard](https://app.supabase.com/)
   - Create a new project
   - Note down your Project URL and Service Role Key

2. Create the database tables:
   - Go to your Supabase project dashboard
   - Navigate to SQL Editor
   - Copy and paste the contents of `supabase_schema.sql` into the editor
   - Run the SQL commands

### 4. Configure Environment Variables

Create a `.env` file in the root directory with your Supabase credentials:

```env
SUPABASE_URL=your_supabase_project_url_here
SUPABASE_KEY=your_supabase_service_role_key_here
```

Make sure to use the Service Role Key, not the anonymous key, for server-side operations.

### 5. Run the Application

```bash
python app.py
```

The application will be available at `http://localhost:5000`.

## Features

- Add income and expense transactions
- View transaction history
- See financial summary (total income, total expenses, current balance)
- Export data to Excel

## Usage

1. Open the application in your browser
2. Use the forms to add income or expense transactions
3. View your transaction history in the table
4. Export your data to Excel using the "Export to Excel" button

## Troubleshooting

### RLS (Row Level Security) Errors

If you encounter RLS errors, make sure you're using the Service Role Key in your `.env` file, not the anonymous key. The service role key bypasses RLS policies.

### Database Connection Issues

1. Verify your Supabase URL and key in the `.env` file
2. Ensure you've run the SQL schema to create the tables
3. Check that you're using the correct service role key

## Deployment

For deployment instructions, see [DEPLOYMENT.md](DEPLOYMENT.md).