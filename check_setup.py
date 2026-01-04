#!/usr/bin/env python3
"""
KisanAI Setup Checker
Validates your environment configuration before running the app
"""

import os
import sys
from dotenv import load_dotenv

def check_env_file():
    """Check if .env file exists"""
    if not os.path.exists('.env'):
        print("❌ .env file not found!")
        print("   Create it by copying .env.example:")
        print("   cp .env.example .env")
        return False
    print("✅ .env file exists")
    return True

def check_api_key():
    """Check if Gemini API key is set and valid"""
    load_dotenv()
    api_key = os.getenv('GEMINI_API_KEY')
    
    if not api_key:
        print("❌ GEMINI_API_KEY not set in .env file")
        print("   Get your API key from: https://makersuite.google.com/app/apikey")
        return False
    
    if 'your_' in api_key.lower():
        print("❌ GEMINI_API_KEY is still set to placeholder value")
        print("   Replace it with your actual API key from: https://makersuite.google.com/app/apikey")
        return False
    
    # Test API key
    try:
        import google.generativeai as genai
        genai.configure(api_key=api_key)
        # Try to list models to verify key works
        models = genai.list_models()
        list(models)  # Force evaluation
        print("✅ GEMINI_API_KEY is valid and working")
        return True
    except Exception as e:
        print(f"❌ GEMINI_API_KEY is invalid: {str(e)}")
        print("   Get a valid API key from: https://makersuite.google.com/app/apikey")
        return False

def check_mongodb():
    """Check MongoDB configuration"""
    load_dotenv()
    mongo_url = os.getenv('MONGODB_URL')
    
    if not mongo_url or 'your_' in mongo_url.lower():
        print("⚠️  MONGODB_URL not configured (will use local JSON storage)")
        print("   For production, get MongoDB Atlas free tier: https://www.mongodb.com/cloud/atlas")
        return True  # Not critical
    
    try:
        import pymongo
        client = pymongo.MongoClient(mongo_url, serverSelectionTimeoutMS=5000)
        client.server_info()  # Force connection
        print("✅ MongoDB connection successful")
        return True
    except Exception as e:
        print(f"⚠️  MongoDB connection failed: {str(e)}")
        print("   Will fall back to local JSON storage")
        return True  # Not critical

def check_dependencies():
    """Check if all required packages are installed"""
    required_packages = [
        ('flask', 'flask'),
        ('flask_cors', 'flask-cors'),
        ('pymongo', 'pymongo'),
        ('google.generativeai', 'google-generativeai'),
        ('PIL', 'Pillow'),
        ('yaml', 'PyYAML')
    ]
    
    missing = []
    for import_name, package_name in required_packages:
        try:
            __import__(import_name.replace('.', '_') if '.' in import_name else import_name)
        except ImportError:
            missing.append(package_name)
    
    if missing:
        print(f"❌ Missing packages: {', '.join(missing)}")
        print("   Install them with: pip install -r requirements.txt")
        return False
    
    print("✅ All required packages are installed")
    return True

def main():
    print("=" * 60)
    print("KisanAI Setup Checker")
    print("=" * 60)
    print()
    
    checks = [
        ("Dependencies", check_dependencies),
        ("Environment File", check_env_file),
        ("Gemini API Key", check_api_key),
        ("MongoDB", check_mongodb),
    ]
    
    results = []
    for name, check_func in checks:
        print(f"Checking {name}...")
        results.append(check_func())
        print()
    
    print("=" * 60)
    if all(results[:3]):  # First 3 are critical
        print("✅ Setup complete! You can now run:")
        print("   python app.py")
        print()
        print("   Or deploy to Vercel:")
        print("   vercel --prod")
        return 0
    else:
        print("❌ Setup incomplete. Please fix the errors above.")
        return 1

if __name__ == "__main__":
    sys.exit(main())
