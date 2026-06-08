"""
Web Page Summarizer - Main Application
A Streamlit app that uses AI to summarize web pages
"""

import streamlit as st
from datetime import datetime
import config
from modules import (
    fetch_and_extract_content,
    validate_url,
    generate_summary,
    calculate_statistics,
    format_summary
)
from modules.utils import (
    extract_domain,
    sanitize_filename,
    create_download_content,
    format_number
)


# Page configuration
st.set_page_config(
    page_title="Web Page Summarizer",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)


def initialize_session_state():
    """Initialize session state variables"""
    if 'summary_result' not in st.session_state:
        st.session_state.summary_result = None
    if 'api_key' not in st.session_state:
        st.session_state.api_key = config.GEMINI_API_KEY


def render_sidebar():
    """Render the sidebar with settings and information"""
    with st.sidebar:
        st.title("⚙️ Settings")
        
        # API Key input
        st.subheader("🔑 API Configuration")
        api_key = st.text_input(
            "Google Gemini API Key",
            value=st.session_state.api_key,
            type="password",
            help="Get your free API key from https://makersuite.google.com/app/apikey"
        )
        st.session_state.api_key = api_key
        
        if not api_key or api_key == "your_api_key_here":
            st.warning("⚠️ Please enter your Gemini API key to use the summarizer")
            st.markdown("[Get API Key →](https://makersuite.google.com/app/apikey)")
        
        st.divider()
        
        # About section
        st.subheader("ℹ️ About")
        st.markdown("""
        **Web Page Summarizer** uses AI to extract key points from any web page.
        
        **Features:**
        - 🚀 Fast summarization
        - 🎯 Customizable length
        - 📝 Multiple formats
        - 💾 Download summaries
        
        **How to use:**
        1. Enter a URL
        2. Choose options
        3. Click Summarize
        4. Get key points!
        """)
        
        st.divider()
        
        # Tips
        with st.expander("💡 Tips for Best Results"):
            st.markdown("""
            - Use URLs with substantial text content
            - News articles work great
            - Blog posts are perfect
            - Avoid login-required pages
            - Try different summary lengths
            """)
        
        st.divider()
        st.caption("Made with ❤️ using Streamlit & Google Gemini")


def render_header():
    """Render the main header"""
    st.title(f"{config.APP_ICON} {config.APP_TITLE}")
    st.markdown(f"**{config.APP_DESCRIPTION}**")
    st.markdown("---")


def render_input_section():
    """Render the URL input and options section"""
    col1, col2 = st.columns([3, 1])
    
    with col1:
        url = st.text_input(
            "🔗 Enter Web Page URL",
            placeholder="https://example.com/article",
            help="Paste the URL of any web page you want to summarize"
        )
    
    with col2:
        st.write("")  # Spacing
        st.write("")  # Spacing
        summarize_button = st.button("✨ Summarize", type="primary", use_container_width=True)
    
    # Options in expandable section
    with st.expander("⚙️ Customization Options", expanded=False):
        col1, col2 = st.columns(2)
        
        with col1:
            length = st.selectbox(
                "📏 Summary Length",
                options=list(config.SUMMARY_LENGTHS.keys()),
                index=1,  # Default to Medium
                help="Choose how detailed you want the summary"
            )
            
            # Show length description
            st.caption(config.SUMMARY_LENGTHS[length]['description'])
        
        with col2:
            format_type = st.radio(
                "📋 Output Format",
                options=["Bullets", "Paragraph"],
                index=0,
                help="Choose how to display the summary"
            )
    
    return url, length, format_type, summarize_button


def render_example_urls():
    """Render example URLs for testing"""
    with st.expander("📚 Try These Example URLs"):
        st.markdown("""
        Click any URL to copy it:
        - [BBC News Article](https://www.bbc.com/news)
        - [Wikipedia - AI](https://en.wikipedia.org/wiki/Artificial_intelligence)
        - [TechCrunch Article](https://techcrunch.com)
        - [Medium Blog Post](https://medium.com)
        """)


def process_summarization(url: str, length: str, format_type: str):
    """Process the summarization request"""
    
    # Validate API key
    if not st.session_state.api_key or st.session_state.api_key == "your_api_key_here":
        st.error(config.ERROR_MESSAGES['no_api_key'])
        return
    
    # Validate URL
    if not url:
        st.warning("⚠️ Please enter a URL")
        return
    
    if not validate_url(url):
        st.error(config.ERROR_MESSAGES['invalid_url'])
        return
    
    # Create progress container
    progress_container = st.container()
    
    with progress_container:
        # Step 1: Fetch content
        with st.status("🔄 Processing...", expanded=True) as status:
            st.write("📥 Fetching web page...")
            
            try:
                # Fetch and extract content
                result = fetch_and_extract_content(url)
                st.write(f"✅ Content extracted: {len(result['content'])} characters")
                
                # Generate summary
                st.write("🤖 Generating AI summary...")
                summary_result = generate_summary(
                    content=result['content'],
                    api_key=st.session_state.api_key,
                    length=length,
                    format_type=format_type
                )
                
                if not summary_result['success']:
                    st.error(summary_result.get('error', 'Failed to generate summary'))
                    status.update(label="❌ Failed", state="error")
                    return
                
                st.write("✅ Summary generated successfully!")
                
                # Calculate statistics
                stats = calculate_statistics(result['content'], summary_result['summary'])
                stats['timestamp'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                
                # Store in session state
                st.session_state.summary_result = {
                    'title': result['title'],
                    'url': result['url'],
                    'summary': summary_result['summary'],
                    'stats': stats,
                    'length': length,
                    'format': format_type
                }
                
                status.update(label="✅ Complete!", state="complete")
                
            except Exception as e:
                st.error(f"❌ Error: {str(e)}")
                status.update(label="❌ Failed", state="error")
                return


def render_results():
    """Render the summary results"""
    if not st.session_state.summary_result:
        return
    
    result = st.session_state.summary_result
    
    st.markdown("---")
    st.subheader("📊 Summary Results")
    
    # Title and source
    st.markdown(f"### {result['title']}")
    st.caption(f"🔗 Source: [{extract_domain(result['url'])}]({result['url']})")
    
    # Summary in a nice container
    st.markdown("#### 📝 Summary")
    summary_container = st.container()
    with summary_container:
        st.markdown(
            f"""<div style='background-color: #f0f2f6; padding: 20px; border-radius: 10px;
            border-left: 5px solid #1f77b4; color: #1e1e1e; font-size: 16px; line-height: 1.6;'>
            {result['summary'].replace(chr(10), '<br>')}
            </div>""",
            unsafe_allow_html=True
        )
    
    # Statistics
    st.markdown("#### 📈 Statistics")
    col1, col2, col3, col4 = st.columns(4)
    
    stats = result['stats']
    
    with col1:
        st.metric(
            "Original Words",
            format_number(stats['original_words'])
        )
    
    with col2:
        st.metric(
            "Summary Words",
            format_number(stats['summary_words'])
        )
    
    with col3:
        st.metric(
            "Reduction",
            f"{stats['word_reduction']}%"
        )
    
    with col4:
        st.metric(
            "Time Saved",
            f"{stats['original_reading_time'] - stats['summary_reading_time']:.1f} min"
        )
    
    # Action buttons
    st.markdown("#### 💾 Export Options")
    col1, col2, col3 = st.columns([1, 1, 2])
    
    with col1:
        # Copy button (using clipboard)
        if st.button("📋 Copy Summary", use_container_width=True):
            st.code(result['summary'], language=None)
            st.success("✅ Summary displayed above - you can now copy it!")
    
    with col2:
        # Download button
        download_content = create_download_content(
            result['title'],
            result['url'],
            result['summary'],
            stats
        )
        
        filename = sanitize_filename(result['title']) + "_summary.txt"
        
        st.download_button(
            label="⬇️ Download",
            data=download_content,
            file_name=filename,
            mime="text/plain",
            use_container_width=True
        )
    
    with col3:
        if st.button("🔄 Summarize Another Page", use_container_width=True):
            st.session_state.summary_result = None
            st.rerun()


def main():
    """Main application function"""
    # Initialize
    initialize_session_state()
    
    # Render sidebar
    render_sidebar()
    
    # Render main content
    render_header()
    
    # Input section
    url, length, format_type, summarize_button = render_input_section()
    
    # Example URLs
    render_example_urls()
    
    # Process if button clicked
    if summarize_button:
        process_summarization(url, length, format_type)
    
    # Show results if available
    render_results()
    
    # Footer
    st.markdown("---")
    st.markdown(
        "<div style='text-align: center; color: #666;'>"
        "🤖 Powered by Google Gemini AI | Built with Streamlit"
        "</div>",
        unsafe_allow_html=True
    )


if __name__ == "__main__":
    main()

# Made with Bob
