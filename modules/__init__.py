"""
Web Page Summarizer Modules
Contains core functionality for web scraping and AI summarization
"""

from .scraper import fetch_and_extract_content, validate_url
from .summarizer import generate_summary, initialize_gemini
from .utils import calculate_statistics, format_summary

__all__ = [
    'fetch_and_extract_content',
    'validate_url',
    'generate_summary',
    'initialize_gemini',
    'calculate_statistics',
    'format_summary'
]

# Made with Bob
