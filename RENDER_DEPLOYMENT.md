# Deployment to Render.com

This application can be deployed to Render.com using the provided `render.yaml` file.

## Prerequisites

1. A Render.com account
2. A Supabase account with a project created

## Steps to Deploy

1. Fork this repository to your GitHub account
2. Sign up or log in to Render.com
3. Click "New" and select "Web Service"
4. Connect your GitHub account and select your forked repository
5. Configure the service:
   - Name: Choose a name for your service
   - Region: Choose the region closest to you
   - Branch: Select the branch you want to deploy (usually main)
   - Root Directory: Leave empty if the app is in the root of the repository
   - Environment: Python 3
6. Add your environment variables in the "Advanced" section:
   - `SUPABASE_URL`: Your Supabase project URL
   - `SUPABASE_KEY`: Your Supabase service role key
7. Click "Create Web Service"

## Setting up Supabase

Before your application will work correctly, you need to set up the database tables in Supabase:

1. Go to your Supabase project dashboard
2. Navigate to SQL Editor
3. Copy and paste the contents of `supabase_schema.sql` into the editor
4. Run the SQL commands

## Environment Variables

You must set the following environment variables in your Render.com dashboard:

- `SUPABASE_URL`: Your Supabase project URL (e.g., https://your-project.supabase.co)
- `SUPABASE_KEY`: Your Supabase service role key (NOT the anonymous key)

You can find these values in your Supabase project settings under "API".

## Note

Render.com will automatically use the `render.yaml` file to configure your deployment. The file specifies:
- Build command: `pip install -r requirements.txt`
- Start command: `gunicorn wsgi:app`
- Required environment variables

The application will be available at the URL provided by Render after deployment.