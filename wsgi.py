# WSGI entry point for the application
# This is a common pattern for Python web applications deployment

from app import app

if __name__ == "__main__":
    app.run()