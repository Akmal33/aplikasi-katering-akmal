# Deployment Instructions

## Vercel Deployment

1. Install the Vercel CLI:
   ```bash
   npm install -g vercel
   ```

2. Deploy the application:
   ```bash
   vercel
   ```

The `vercel.json` file in the root directory configures the deployment for Vercel.

## Netlify Deployment

1. Install the Netlify CLI:
   ```bash
   npm install -g netlify-cli
   ```

2. Deploy the application:
   ```bash
   netlify deploy
   ```

The `netlify.toml` file configures the deployment for Netlify. The application uses Netlify Functions to run the Python Flask backend.

## Notes

- Both platforms will automatically detect and use the appropriate configuration files.
- The application should work on both platforms with the provided configurations.
- Static assets are served from the `static` directory.
- The database is stored in a local SQLite file, which will be ephemeral on these platforms. For production use, consider using a persistent database solution.