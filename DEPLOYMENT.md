# Deployment Instructions

## Prerequisites

Before deploying, you need to set up a Supabase project and configure the environment variables:

1. Create a Supabase account at [supabase.com](https://supabase.com)
2. Create a new project
3. Set up the required database tables (see SUPABASE_INTEGRATION.md)
4. Get your project URL and API key

## Environment Variables

You must set the following environment variables in your deployment platform:

```
SUPABASE_URL=your_supabase_project_url
SUPABASE_KEY=your_supabase_api_key
```

## Vercel Deployment

1. Install the Vercel CLI:
   ```bash
   npm install -g vercel
   ```

2. Set environment variables:
   ```bash
   vercel env add SUPABASE_URL
   vercel env add SUPABASE_KEY
   ```

3. Deploy the application:
   ```bash
   vercel
   ```

The `vercel.json` file in the root directory configures the deployment for Vercel.

## Netlify Deployment

1. Install the Netlify CLI:
   ```bash
   npm install -g netlify-cli
   ```

2. Set environment variables in the Netlify dashboard:
   - Go to your site settings
   - Navigate to "Build & deploy" > "Environment"
   - Add `SUPABASE_URL` and `SUPABASE_KEY` as environment variables

3. Deploy the application:
   ```bash
   netlify deploy
   ```

The `netlify.toml` file configures the deployment for Netlify. The application uses Netlify Functions to run the Python Flask backend.

## Benefits of Using Supabase

- **Persistent Data**: Unlike SQLite which is ephemeral on serverless platforms, Supabase provides persistent data storage
- **Real-time Updates**: Supabase supports real-time data updates
- **Scalability**: Supabase can scale with your application's needs
- **Authentication**: Built-in user authentication (optional)
- **Dashboard**: Web-based dashboard for database management

## Notes

- Both platforms will automatically detect and use the appropriate configuration files.
- The application should work on both platforms with the provided configurations.
- Static assets are served from the `static` directory.
- With Supabase integration, your data will now be persistently stored and accessible across deployments.
- For detailed Supabase setup instructions, see SUPABASE_INTEGRATION.md