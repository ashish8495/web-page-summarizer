"""
Script to list all available Gemini models
Run this to see what models are available with your API key
"""

from google import genai
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Get API key
api_key = os.getenv("GEMINI_API_KEY", "")

if not api_key or api_key == "your_api_key_here":
    print("ERROR: Please set your GEMINI_API_KEY in the .env file")
    print("Get your API key from: https://makersuite.google.com/app/apikey")
    exit(1)

print("Fetching available models...")
print()

try:
    # Initialize client
    client = genai.Client(api_key=api_key)
    
    # List all models
    models = client.models.list()
    
    print("Available Models:")
    print("=" * 80)
    
    for model in models:
        print(f"Model Name: {model.name}")
        if hasattr(model, 'display_name'):
            print(f"Display Name: {model.display_name}")
        if hasattr(model, 'description'):
            print(f"Description: {model.description}")
        print("-" * 80)
    
    print()
    print("Use one of these model names in your config.py file")
    print("Recommended: Use a model with 'flash' in the name for faster responses")
    
except Exception as e:
    print(f"ERROR: {e}")
    print()
    print("Troubleshooting:")
    print("1. Check your API key is correct")
    print("2. Make sure you have internet connection")
    print("3. Try generating a new API key from https://makersuite.google.com/app/apikey")

# Made with Bob
