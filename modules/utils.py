"""
Utility Functions
Helper functions for the Web Page Summarizer
"""

from typing import Dict
import re


def calculate_statistics(original_content: str, summary: str) -> Dict[str, any]:
    """
    Calculate statistics about the content and summary
    
    Args:
        original_content: Original text content
        summary: Generated summary
        
    Returns:
        dict: Statistics including word counts and reduction percentage
    """
    # Count words
    original_words = len(original_content.split())
    summary_words = len(summary.split())
    
    # Count characters
    original_chars = len(original_content)
    summary_chars = len(summary)
    
    # Calculate reduction
    word_reduction = 0
    if original_words > 0:
        word_reduction = round(((original_words - summary_words) / original_words) * 100, 1)
    
    # Estimate reading time (average 200 words per minute)
    original_reading_time = round(original_words / 200, 1)
    summary_reading_time = round(summary_words / 200, 1)
    
    # Count bullet points if present
    bullet_count = summary.count('•')
    
    return {
        'original_words': original_words,
        'summary_words': summary_words,
        'original_chars': original_chars,
        'summary_chars': summary_chars,
        'word_reduction': word_reduction,
        'original_reading_time': original_reading_time,
        'summary_reading_time': summary_reading_time,
        'bullet_count': bullet_count
    }


def format_summary(summary: str, format_type: str = "Bullets") -> str:
    """
    Format the summary text for display
    
    Args:
        summary: Raw summary text
        format_type: Desired format (Bullets/Paragraph)
        
    Returns:
        str: Formatted summary
    """
    if not summary:
        return ""
    
    # Clean up extra whitespace
    summary = re.sub(r'\n\s*\n', '\n\n', summary)
    summary = summary.strip()
    
    if format_type == "Bullets":
        # Ensure consistent bullet formatting
        lines = summary.split('\n')
        formatted_lines = []
        
        for line in lines:
            line = line.strip()
            if line:
                # Normalize bullet characters
                if line.startswith(('-', '*', '·')):
                    line = '• ' + line[1:].strip()
                elif not line.startswith('•'):
                    line = '• ' + line
                formatted_lines.append(line)
        
        return '\n'.join(formatted_lines)
    
    return summary


def truncate_text(text: str, max_length: int = 100, suffix: str = "...") -> str:
    """
    Truncate text to a maximum length
    
    Args:
        text: Text to truncate
        max_length: Maximum length
        suffix: Suffix to add if truncated
        
    Returns:
        str: Truncated text
    """
    if not text or len(text) <= max_length:
        return text
    
    return text[:max_length - len(suffix)].strip() + suffix


def format_number(number: int) -> str:
    """
    Format large numbers with commas
    
    Args:
        number: Number to format
        
    Returns:
        str: Formatted number
    """
    return f"{number:,}"


def extract_domain(url: str) -> str:
    """
    Extract domain name from URL
    
    Args:
        url: Full URL
        
    Returns:
        str: Domain name
    """
    try:
        # Remove protocol
        domain = re.sub(r'https?://', '', url)
        # Remove path
        domain = domain.split('/')[0]
        # Remove www
        domain = re.sub(r'^www\.', '', domain)
        return domain
    except:
        return url


def sanitize_filename(text: str, max_length: int = 50) -> str:
    """
    Create a safe filename from text
    
    Args:
        text: Text to convert to filename
        max_length: Maximum filename length
        
    Returns:
        str: Safe filename
    """
    # Remove invalid characters
    filename = re.sub(r'[^\w\s-]', '', text)
    # Replace spaces with underscores
    filename = re.sub(r'[\s]+', '_', filename)
    # Truncate
    filename = filename[:max_length]
    # Remove leading/trailing underscores
    filename = filename.strip('_')
    
    return filename.lower()


def format_time(seconds: float) -> str:
    """
    Format time in a human-readable way
    
    Args:
        seconds: Time in seconds
        
    Returns:
        str: Formatted time string
    """
    if seconds < 60:
        return f"{int(seconds)} sec"
    elif seconds < 3600:
        minutes = int(seconds / 60)
        return f"{minutes} min"
    else:
        hours = int(seconds / 3600)
        minutes = int((seconds % 3600) / 60)
        return f"{hours}h {minutes}m"


def validate_content_length(content: str, min_length: int = 100) -> bool:
    """
    Check if content has sufficient length for summarization
    
    Args:
        content: Content to validate
        min_length: Minimum required length
        
    Returns:
        bool: True if valid, False otherwise
    """
    if not content:
        return False
    
    word_count = len(content.split())
    return word_count >= min_length


def create_download_content(title: str, url: str, summary: str, stats: Dict) -> str:
    """
    Create formatted content for download
    
    Args:
        title: Page title
        url: Source URL
        summary: Generated summary
        stats: Statistics dictionary
        
    Returns:
        str: Formatted content for download
    """
    content = f"""WEB PAGE SUMMARY
{'=' * 50}

Title: {title}
Source: {url}
Generated: {stats.get('timestamp', 'N/A')}

SUMMARY
{'-' * 50}
{summary}

STATISTICS
{'-' * 50}
Original Content: {stats.get('original_words', 0)} words
Summary: {stats.get('summary_words', 0)} words
Reduction: {stats.get('word_reduction', 0)}%
Reading Time Saved: {stats.get('original_reading_time', 0) - stats.get('summary_reading_time', 0)} minutes

{'=' * 50}
Generated by Web Page Summarizer
"""
    return content

# Made with Bob
