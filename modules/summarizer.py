"""
AI Summarization Module
Handles integration with Google Gemini API for text summarization
"""

from google import genai
from google.genai import types
from typing import Dict, Optional
import config


def initialize_gemini(api_key: str) -> Optional[genai.Client]:
    """
    Initialize Google Gemini API with the provided key
    
    Args:
        api_key: Google Gemini API key
        
    Returns:
        Client instance if successful, None otherwise
    """
    try:
        if not api_key or api_key == "your_api_key_here":
            return None
            
        client = genai.Client(api_key=api_key)
        return client
        
    except Exception as e:
        return None


def build_prompt(content: str, length: str, format_type: str) -> str:
    """
    Build the prompt for the AI model
    
    Args:
        content: Text content to summarize
        length: Summary length (Short/Medium/Long)
        format_type: Output format (Bullets/Paragraph)
        
    Returns:
        str: Formatted prompt
    """
    # Get length instruction
    length_instruction = config.SUMMARY_LENGTHS.get(
        length, 
        config.SUMMARY_LENGTHS[config.DEFAULT_SUMMARY_LENGTH]
    )['instruction']
    
    # Get format instruction
    format_instruction = config.FORMAT_INSTRUCTIONS.get(
        format_type,
        config.FORMAT_INSTRUCTIONS['Bullets']
    )
    
    # Build the prompt
    prompt = config.PROMPT_TEMPLATE.format(
        length_instruction=length_instruction,
        format_instruction=format_instruction,
        content=content
    )
    
    return prompt


def generate_summary_with_model(
    client: genai.Client,
    model: str,
    prompt: str,
    generation_config: types.GenerateContentConfig
) -> Optional[str]:
    """
    Try to generate summary with a specific model
    
    Args:
        client: Gemini client instance
        model: Model name to use
        prompt: The prompt to send
        generation_config: Generation configuration
        
    Returns:
        str: Generated summary if successful, None otherwise
    """
    try:
        response = client.models.generate_content(
            model=model,
            contents=prompt,
            config=generation_config
        )
        
        if response and response.text:
            return response.text.strip()
        return None
        
    except Exception as e:
        error_str = str(e)
        # Only return None for 503 errors (server overload)
        # Re-raise other errors
        if '503' in error_str or 'UNAVAILABLE' in error_str.upper():
            return None
        raise


def generate_summary(
    content: str,
    api_key: str,
    length: str = "Medium",
    format_type: str = "Bullets"
) -> Dict[str, any]:
    """
    Generate a summary using Google Gemini API with automatic fallback
    
    Args:
        content: Text content to summarize
        api_key: Google Gemini API key
        length: Summary length (Short/Medium/Long)
        format_type: Output format (Bullets/Paragraph)
        
    Returns:
        dict: Contains 'summary', 'success', 'model_used', and optional 'error'
    """
    try:
        # Initialize Gemini
        client = initialize_gemini(api_key)
        if not client:
            return {
                'success': False,
                'error': config.ERROR_MESSAGES['no_api_key']
            }
        
        # Build prompt
        prompt = build_prompt(content, length, format_type)
        
        # Configure generation parameters
        generation_config = types.GenerateContentConfig(
            temperature=config.GEMINI_TEMPERATURE,
            max_output_tokens=config.GEMINI_MAX_TOKENS,
        )
        
        # Try primary model first
        models_to_try = [config.GEMINI_MODEL] + config.GEMINI_FALLBACK_MODELS
        summary = None
        model_used = None
        last_error = None
        
        for model in models_to_try:
            try:
                summary = generate_summary_with_model(
                    client, model, prompt, generation_config
                )
                
                if summary:
                    model_used = model
                    break
                    
            except Exception as e:
                last_error = str(e)
                # Continue to next model
                continue
        
        if not summary:
            # All models failed
            error_message = last_error if last_error else "Failed to generate summary with any available model."
            
            # Handle specific API errors
            if last_error:
                if 'API_KEY' in last_error.upper() or 'INVALID' in last_error.upper():
                    error_message = config.ERROR_MESSAGES['api_error']
                elif 'QUOTA' in last_error.upper() or 'RATE_LIMIT' in last_error.upper():
                    error_message = "⚠️ API rate limit reached. Please wait a moment and try again."
                elif '404' in last_error or 'not found' in last_error.lower():
                    error_message = f"⚠️ Model not available. Please check your API configuration. Details: {last_error}"
                else:
                    error_message = f"{config.ERROR_MESSAGES['api_error']} Details: {last_error}"
            
            return {
                'success': False,
                'error': error_message
            }
        
        # Post-process the summary
        summary = post_process_summary(summary, format_type)
        
        return {
            'success': True,
            'summary': summary,
            'length': length,
            'format': format_type,
            'model_used': model_used
        }
        
    except Exception as e:
        error_message = str(e)
        
        # Handle specific API errors
        if 'API_KEY' in error_message.upper() or 'INVALID' in error_message.upper():
            error_message = config.ERROR_MESSAGES['api_error']
        elif 'QUOTA' in error_message.upper() or 'RATE_LIMIT' in error_message.upper():
            error_message = "⚠️ API rate limit reached. Please wait a moment and try again."
        elif '404' in error_message or 'not found' in error_message.lower():
            error_message = f"⚠️ Model not available. Please check your API configuration. Details: {error_message}"
        else:
            error_message = f"{config.ERROR_MESSAGES['api_error']} Details: {error_message}"
        
        return {
            'success': False,
            'error': error_message
        }


def post_process_summary(summary: str, format_type: str) -> str:
    """
    Clean and format the generated summary
    
    Args:
        summary: Raw summary from AI
        format_type: Desired format (Bullets/Paragraph)
        
    Returns:
        str: Cleaned and formatted summary
    """
    # Remove any markdown formatting that might interfere
    summary = summary.replace('**', '')
    
    if format_type == "Bullets":
        # Ensure bullet points are properly formatted
        lines = summary.split('\n')
        formatted_lines = []
        
        for line in lines:
            line = line.strip()
            if not line:
                continue
                
            # Add bullet if not present
            if not line.startswith(('•', '-', '*', '·')):
                # Check if it looks like a point (starts with number or letter)
                if line[0].isdigit() or (len(line) > 2 and line[1] in '.):'):
                    # Remove numbering
                    line = line.split('.', 1)[-1].strip()
                    line = line.split(')', 1)[-1].strip()
                    line = line.split(':', 1)[-1].strip() if ':' in line[:3] else line
                
                line = '• ' + line
            elif line.startswith(('-', '*')):
                line = '• ' + line[1:].strip()
                
            formatted_lines.append(line)
        
        summary = '\n'.join(formatted_lines)
    
    return summary.strip()


def validate_api_key(api_key: str) -> bool:
    """
    Validate if the API key is properly formatted
    
    Args:
        api_key: API key to validate
        
    Returns:
        bool: True if valid format, False otherwise
    """
    if not api_key or not isinstance(api_key, str):
        return False
    
    # Basic validation - Gemini keys typically start with 'AIza'
    if len(api_key) < 20:
        return False
    
    if api_key == "your_api_key_here":
        return False
    
    return True
