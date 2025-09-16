# Deployment Instructions

## Vercel Deployment

To deploy this application on Vercel, you need to set up environment variables for Supabase integration.

### Environment Variables

You need to set the following environment variables in your Vercel project settings:

1. `SUPABASE_URL` - Your Supabase project URL
2. `SUPABASE_KEY` - Your Supabase service role key

### Setting Up Environment Variables on Vercel

1. Go to your Vercel dashboard
2. Select your project
3. Go to Settings > Environment Variables
4. Add the following variables:
   - Name: `SUPABASE_URL`, Value: Your Supabase project URL
   - Name: `SUPABASE_KEY`, Value: Your Supabase service role key

### Supabase Setup

Make sure you have set up your Supabase database tables by running the SQL commands in `supabase_schema.sql`.

## Local Development

For local development, create a `.env` file in the root directory with your Supabase credentials:

```
SUPABASE_URL=your_supabase_project_url_here
SUPABASE_KEY=your_supabase_service_role_key_here
```

Then run the application:

```bash
python app.py
```