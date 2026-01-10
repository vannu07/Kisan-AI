"""
Vercel Serverless Function Entry Point
This file exports the Flask app for Vercel deployment
"""
import sys
import os

# Add parent directory to path so we can import from src/
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from flask import Flask, render_template, send_from_directory
from flask_cors import CORS
from api.routes import api_bp
from src.logger.logging import logger

app = Flask(__name__, 
            static_folder='../frontend', 
            template_folder='../frontend', 
            static_url_path='')
CORS(app)

# Register API Blueprint
app.register_blueprint(api_bp, url_prefix='/api')

# Routes to serve frontend pages
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login.html')
def login():
    return render_template('login.html')

@app.route('/signup.html')
def signup():
    return render_template('signup.html')

@app.route('/create_profile.html')
def create_profile():
    return render_template('create_profile.html')

@app.route('/dashboard.html')
def dashboard():
    return render_template('dashboard.html')

@app.route('/scan.html')
def scan():
    return render_template('scan.html')

@app.route('/chat.html')
def chat():
    return render_template('chat.html')

@app.route('/history.html')
def history():
    return render_template('history.html')

@app.route('/profile.html')
def profile():
    return render_template('profile.html')

@app.route('/recommendations.html')
def recommendations():
    return render_template('recommendations.html')

# Serve uploaded files if needed (for displaying in history)
@app.route('/uploads/<filename>')
def uploaded_file(filename):
    upload_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'static', 'uploads')
    return send_from_directory(upload_dir, filename)

# Health check endpoint
@app.route('/health')
def health():
    return {"status": "ok", "message": "KisanAI API is running"}

# Export app for Vercel
# Vercel will look for an 'app' variable or 'handler' function
# For Vercel, just export the app
# The Vercel Python runtime will handle WSGI automatically

if __name__ == "__main__":
    # Only for local development
    logger.info("Starting KisanAI Local Development Server...")
    debug_mode = os.environ.get("FLASK_DEBUG", "").lower() in ("1", "true", "yes", "on")
    app.run(host='0.0.0.0', port=5000, debug=debug_mode)
else:
    # Running as a Vercel serverless function
    logger.info("KisanAI running as Vercel serverless function")
