"""
Configuration file for Web Page Summarizer
Contains all settings and constants used throughout the application
"""

import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# API Configuration
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY", "")

# Gemini Model Settings
GEMINI_MODEL = "gemini-2.5-flash"  # Primary model - Stable and fast
GEMINI_FALLBACK_MODELS = [
    "gemini-1.5-flash",      # Backup 1 - Very stable, widely available
    "gemini-1.5-pro",        # Backup 2 - More powerful, good availability
    "gemini-2.0-flash-exp"   # Backup 3 - Experimental but fast
]
GEMINI_TEMPERATURE = 0.3  # Lower = more focused, higher = more creative
GEMINI_MAX_TOKENS = 2048  # Maximum tokens for response

# Web Scraping Settings
MAX_CONTENT_LENGTH = 50000  # Maximum characters to process
REQUEST_TIMEOUT = 30  # Seconds to wait for web page response
USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"

# Summary Settings
SUMMARY_LENGTHS = {
    "Short": {
        "description": "Quick overview (3-5 key points)",
        "max_words": 150,
        "instruction": "Provide a brief summary with 3-5 key points"
    },
    "Medium": {
        "description": "Balanced summary (5-8 key points)",
        "max_words": 300,
        "instruction": "Provide a comprehensive summary with 5-8 key points"
    },
    "Long": {
        "description": "Detailed summary (8-12 key points)",
        "max_words": 500,
        "instruction": "Provide a detailed summary with 8-12 key points"
    }
}

# Default Settings
DEFAULT_SUMMARY_LENGTH = "Medium"
DEFAULT_FORMAT = "Bullets"  # "Bullets" or "Paragraph"

# UI Settings
APP_TITLE = "🤖 Web Page Summarizer"
APP_DESCRIPTION = "AI-powered tool to extract key points from any web page"
APP_ICON = "🤖"

# Error Messages
ERROR_MESSAGES = {
    "invalid_url": "❌ Please enter a valid URL (e.g., https://example.com)",
    "fetch_failed": "❌ Failed to fetch the web page. Please check the URL and try again.",
    "no_content": "❌ No readable content found on this page.",
    "api_error": "❌ Error communicating with AI service. Please check your API key.",
    "timeout": "❌ Request timed out. The page took too long to load.",
    "no_api_key": "❌ Please provide a Google Gemini API key in the sidebar."
}

# Success Messages
SUCCESS_MESSAGES = {
    "summary_generated": "✅ Summary generated successfully!",
    "content_extracted": "✅ Content extracted from web page"
}

# Prompt Templates
PROMPT_TEMPLATE = """You are an expert at extracting key information from web content.

Task: Read the following web page content and provide a concise summary.

Requirements:
- Extract only the most important points and key takeaways
- Use clear, simple language that anyone can understand
- Focus on main ideas, facts, and conclusions
- {length_instruction}
- Format: {format_instruction}
- Be objective and accurate

Content to summarize:
{content}

Summary:"""

FORMAT_INSTRUCTIONS = {
    "Bullets": "Present the summary as clear bullet points, each starting with a bullet (•)",
    "Paragraph": "Present the summary as a well-structured paragraph with smooth flow"
}

# Cache Settings (for future enhancement)
CACHE_ENABLED = False
CACHE_EXPIRY = 3600  # 1 hour in seconds

# Logging Settings
LOG_LEVEL = "INFO"
LOG_FORMAT = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
