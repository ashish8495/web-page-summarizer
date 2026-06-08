"""
Web Scraping Module
Handles fetching and extracting content from web pages
"""

import requests
from bs4 import BeautifulSoup
import trafilatura
import validators
from typing import Dict, Optional
import re

import config


def validate_url(url: str) -> bool:
    """
    Validate if the provided string is a valid URL
    
    Args:
        url: URL string to validate
        
    Returns:
        bool: True if valid, False otherwise
    """
    if not url or not isinstance(url, str):
        return False
    
    # Add https:// if no protocol specified
    if not url.startswith(('http://', 'https://')):
        url = 'https://' + url
    
    return validators.url(url) is True


def fetch_page(url: str) -> Optional[str]:
    """
    Fetch HTML content from a URL
    
    Args:
        url: URL to fetch
        
    Returns:
        str: HTML content or None if failed
    """
    try:
        # Add https:// if no protocol specified
        if not url.startswith(('http://', 'https://')):
            url = 'https://' + url
            
        headers = {
            'User-Agent': config.USER_AGENT
        }
        
        response = requests.get(
            url,
            headers=headers,
            timeout=config.REQUEST_TIMEOUT,
            allow_redirects=True
        )
        response.raise_for_status()
        
        return response.text
        
    except requests.exceptions.Timeout:
        raise Exception(config.ERROR_MESSAGES['timeout'])
    except requests.exceptions.RequestException as e:
        raise Exception(f"{config.ERROR_MESSAGES['fetch_failed']} Error: {str(e)}")
    except Exception as e:
        raise Exception(f"Unexpected error: {str(e)}")


def extract_content_trafilatura(html: str, url: str) -> Optional[Dict[str, str]]:
    """
    Extract main content using trafilatura library (best for articles)
    
    Args:
        html: HTML content
        url: Original URL (for context)
        
    Returns:
        dict: Extracted content with title and text
    """
    try:
        # Extract with trafilatura
        extracted = trafilatura.extract(
            html,
            include_comments=False,
            include_tables=True,
            no_fallback=False
        )
        
        if not extracted:
            return None
            
        # Try to get title
        soup = BeautifulSoup(html, 'lxml')
        title = None
        
        # Try different title sources
        if soup.title:
            title = soup.title.string
        elif soup.find('h1'):
            title = soup.find('h1').get_text()
        elif soup.find('meta', property='og:title'):
            title = soup.find('meta', property='og:title')['content']
            
        return {
            'title': title.strip() if title else 'Untitled',
            'content': extracted.strip()
        }
        
    except Exception as e:
        return None


def extract_content_beautifulsoup(html: str) -> Optional[Dict[str, str]]:
    """
    Extract main content using BeautifulSoup (fallback method)
    
    Args:
        html: HTML content
        
    Returns:
        dict: Extracted content with title and text
    """
    try:
        soup = BeautifulSoup(html, 'lxml')
        
        # Remove unwanted elements
        for element in soup(['script', 'style', 'nav', 'header', 'footer', 
                            'aside', 'iframe', 'noscript']):
            element.decompose()
            
        # Try to get title
        title = None
        if soup.title:
            title = soup.title.string
        elif soup.find('h1'):
            title = soup.find('h1').get_text()
            
        # Try to find main content area
        main_content = None
        
        # Look for common content containers
        for tag in ['article', 'main', 'div']:
            for class_name in ['content', 'article', 'post', 'entry', 'main']:
                element = soup.find(tag, class_=re.compile(class_name, re.I))
                if element:
                    main_content = element
                    break
            if main_content:
                break
                
        # If no specific container found, use body
        if not main_content:
            main_content = soup.find('body')
            
        if not main_content:
            return None
            
        # Extract text
        text = main_content.get_text(separator='\n', strip=True)
        
        return {
            'title': title.strip() if title else 'Untitled',
            'content': text
        }
        
    except Exception as e:
        return None


def clean_text(text: str) -> str:
    """
    Clean and normalize extracted text
    
    Args:
        text: Raw text to clean
        
    Returns:
        str: Cleaned text
    """
    if not text:
        return ""
        
    # Remove excessive whitespace
    text = re.sub(r'\n\s*\n', '\n\n', text)
    text = re.sub(r' +', ' ', text)
    
    # Remove very short lines (likely navigation/menu items)
    lines = text.split('\n')
    cleaned_lines = [line.strip() for line in lines if len(line.strip()) > 20]
    
    text = '\n'.join(cleaned_lines)
    
    # Limit length
    if len(text) > config.MAX_CONTENT_LENGTH:
        text = text[:config.MAX_CONTENT_LENGTH] + "..."
        
    return text.strip()


def fetch_and_extract_content(url: str) -> Dict[str, str]:
    """
    Main function to fetch and extract content from a URL
    
    Args:
        url: URL to process
        
    Returns:
        dict: Contains 'title', 'content', and 'url'
        
    Raises:
        Exception: If fetching or extraction fails
    """
    # Validate URL
    if not validate_url(url):
        raise Exception(config.ERROR_MESSAGES['invalid_url'])
    
    # Add protocol if missing
    if not url.startswith(('http://', 'https://')):
        url = 'https://' + url
    
    # Fetch HTML
    html = fetch_page(url)
    
    if not html:
        raise Exception(config.ERROR_MESSAGES['fetch_failed'])
    
    # Try trafilatura first (best for articles)
    result = extract_content_trafilatura(html, url)
    
    # Fallback to BeautifulSoup if trafilatura fails
    if not result or not result.get('content'):
        result = extract_content_beautifulsoup(html)
    
    # Check if we got content
    if not result or not result.get('content'):
        raise Exception(config.ERROR_MESSAGES['no_content'])
    
    # Clean the content
    result['content'] = clean_text(result['content'])
    
    # Final check
    if len(result['content']) < 100:
        raise Exception(config.ERROR_MESSAGES['no_content'])
    
    result['url'] = url
    
    return result

# Made with Bob
