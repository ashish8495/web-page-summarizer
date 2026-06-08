# 🏗️ Architecture Guide - Web Page Summarizer

This document explains how the Web Page Summarizer works in simple terms, with visual diagrams.

---

## 🎯 The Big Picture

Think of the application as a pipeline with 4 main stages:

```
┌─────────┐    ┌─────────┐    ┌─────────┐    ┌─────────┐
│  User   │ -> │ Scraper │ -> │   AI    │ -> │ Display │
│  Input  │    │ Module  │    │ Summary │    │ Results │
└─────────┘    └─────────┘    └─────────┘    └─────────┘
```

Let's break down each stage:

---

## 📊 Detailed Flow Diagram

```
                    USER INTERACTION
                          │
                          ▼
        ┌─────────────────────────────────────┐
        │     Streamlit Web Interface         │
        │  ┌───────────────────────────────┐  │
        │  │  1. User enters URL           │  │
        │  │  2. Selects options           │  │
        │  │  3. Clicks "Summarize"        │  │
        │  └───────────────────────────────┘  │
        └──────────────┬──────────────────────┘
                       │
                       ▼
        ┌─────────────────────────────────────┐
        │      URL Validation                  │
        │  ┌───────────────────────────────┐  │
        │  │  • Check URL format           │  │
        │  │  • Verify accessibility       │  │
        │  │  • Handle errors              │  │
        │  └───────────────────────────────┘  │
        └──────────────┬──────────────────────┘
                       │
                       ▼
        ┌─────────────────────────────────────┐
        │      Web Scraping Module             │
        │  ┌───────────────────────────────┐  │
        │  │  Step 1: Fetch HTML           │  │
        │  │  ├─ Send HTTP request         │  │
        │  │  └─ Download page content     │  │
        │  │                               │  │
        │  │  Step 2: Parse HTML           │  │
        │  │  ├─ Use BeautifulSoup         │  │
        │  │  └─ Extract text elements     │  │
        │  │                               │  │
        │  │  Step 3: Clean Content        │  │
        │  │  ├─ Remove ads & navigation   │  │
        │  │  ├─ Remove scripts & styles   │  │
        │  │  └─ Extract main article      │  │
        │  │                               │  │
        │  │  Step 4: Preprocess Text      │  │
        │  │  ├─ Remove extra whitespace   │  │
        │  │  ├─ Fix encoding issues       │  │
        │  │  └─ Prepare for AI           │  │
        │  └───────────────────────────────┘  │
        └──────────────┬──────────────────────┘
                       │
                       ▼
        ┌─────────────────────────────────────┐
        │    Content Preparation               │
        │  ┌───────────────────────────────┐  │
        │  │  • Check content length       │  │
        │  │  • Chunk if too long          │  │
        │  │  • Format for AI prompt       │  │
        │  └───────────────────────────────┘  │
        └──────────────┬──────────────────────┘
                       │
                       ▼
        ┌─────────────────────────────────────┐
        │    Google Gemini API                 │
        │  ┌───────────────────────────────┐  │
        │  │  Step 1: Build Prompt         │  │
        │  │  ├─ Add instructions          │  │
        │  │  ├─ Include user options      │  │
        │  │  └─ Attach content            │  │
        │  │                               │  │
        │  │  Step 2: Send to Gemini       │  │
        │  │  ├─ Authenticate with API key │  │
        │  │  ├─ Set parameters            │  │
        │  │  └─ Make API call             │  │
        │  │                               │  │
        │  │  Step 3: Receive Response     │  │
        │  │  ├─ Get AI-generated summary  │  │
        │  │  ├─ Handle errors             │  │
        │  │  └─ Parse response            │  │
        │  └───────────────────────────────┘  │
        └──────────────┬──────────────────────┘
                       │
                       ▼
        ┌─────────────────────────────────────┐
        │    Summary Formatting                │
        │  ┌───────────────────────────────┐  │
        │  │  • Format as bullets/paragraph│  │
        │  │  • Add metadata               │  │
        │  │  • Calculate statistics       │  │
        │  └───────────────────────────────┘  │
        └──────────────┬──────────────────────┘
                       │
                       ▼
        ┌─────────────────────────────────────┐
        │    Display Results                   │
        │  ┌───────────────────────────────┐  │
        │  │  • Show summary               │  │
        │  │  • Display statistics         │  │
        │  │  • Provide copy/download      │  │
        │  │  • Show success message       │  │
        │  └───────────────────────────────┘  │
        └─────────────────────────────────────┘
```

---

## 🔧 Component Breakdown

### 1. Streamlit Interface (app.py)

**What it does**: Creates the web page you see and interact with

**Key Parts**:
```
┌─────────────────────────────────────┐
│         Streamlit App               │
├─────────────────────────────────────┤
│  Header                             │
│  ├─ Title                           │
│  └─ Description                     │
│                                     │
│  Sidebar                            │
│  ├─ API Key Input                   │
│  ├─ Settings                        │
│  └─ About                           │
│                                     │
│  Main Area                          │
│  ├─ URL Input Field                 │
│  ├─ Options (length, format)        │
│  ├─ Summarize Button                │
│  └─ Results Display                 │
└─────────────────────────────────────┘
```

**User Actions**:
- Type URL
- Choose options
- Click button
- See results

---

### 2. Web Scraper (modules/scraper.py)

**What it does**: Visits the URL and extracts the text content

**Process**:
```
URL Input
   │
   ▼
┌─────────────────┐
│ Send Request    │ <- Uses 'requests' library
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ Get HTML        │ <- Receives raw HTML code
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ Parse HTML      │ <- Uses BeautifulSoup
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ Extract Text    │ <- Finds main content
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ Clean Text      │ <- Removes junk
└────────┬────────┘
         │
         ▼
    Clean Content
```

**What it removes**:
- Navigation menus
- Advertisements
- Sidebars
- Footer content
- JavaScript code
- CSS styles
- Comments

**What it keeps**:
- Article title
- Main text content
- Paragraphs
- Headings
- Important lists

---

### 3. AI Summarizer (modules/summarizer.py)

**What it does**: Sends content to Google Gemini and gets a summary

**Process**:
```
Clean Content
   │
   ▼
┌─────────────────────┐
│ Build AI Prompt     │
│ ┌─────────────────┐ │
│ │ Instructions    │ │
│ │ User Options    │ │
│ │ Content         │ │
│ └─────────────────┘ │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│ Send to Gemini API  │
│ ┌─────────────────┐ │
│ │ API Key         │ │
│ │ Model: gemini   │ │
│ │ Temperature     │ │
│ └─────────────────┘ │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│ Receive Summary     │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│ Format Output       │
└──────────┬──────────┘
           │
           ▼
    Final Summary
```

**AI Prompt Structure**:
```
System: You are an expert summarizer
Task: Summarize this content
Options: 
  - Length: [short/medium/long]
  - Format: [bullets/paragraph]
Content: [The actual text]
Output: [AI generates summary]
```

---

## 🔄 Data Flow Example

Let's follow a real example:

**User Action**: Summarize "https://example.com/article"

```
Step 1: User Input
├─ URL: https://example.com/article
├─ Length: Medium
└─ Format: Bullets

Step 2: Validation
├─ ✓ URL format is valid
├─ ✓ Website is accessible
└─ ✓ Ready to proceed

Step 3: Web Scraping
├─ Fetch HTML (2 seconds)
├─ Parse with BeautifulSoup
├─ Extract 5,000 words
└─ Clean to 4,500 words

Step 4: AI Processing
├─ Build prompt with instructions
├─ Send to Gemini API (3 seconds)
├─ Receive summary (500 words)
└─ Format as bullet points

Step 5: Display
├─ Show 8 key points
├─ Display statistics
│   ├─ Original: 4,500 words
│   ├─ Summary: 500 words
│   └─ Reduction: 89%
└─ Provide copy button
```

**Total Time**: ~5-7 seconds

---

## 🗂️ File Structure & Responsibilities

```
web-page-summarizer/
│
├── app.py                          # Main application
│   ├─ Creates UI
│   ├─ Handles user input
│   ├─ Coordinates modules
│   └─ Displays results
│
├── config.py                       # Configuration
│   ├─ API settings
│   ├─ Default values
│   └─ Constants
│
├── modules/
│   │
│   ├── scraper.py                 # Web scraping
│   │   ├─ fetch_page()
│   │   ├─ extract_content()
│   │   ├─ clean_text()
│   │   └─ validate_url()
│   │
│   ├── summarizer.py              # AI integration
│   │   ├─ initialize_gemini()
│   │   ├─ generate_summary()
│   │   ├─ format_output()
│   │   └─ handle_errors()
│   │
│   └── utils.py                   # Helper functions
│       ├─ calculate_stats()
│       ├─ format_text()
│       └─ validate_input()
│
└── .env                           # Secret keys
    └─ GEMINI_API_KEY
```

---

## 🔐 Security & Privacy Flow

```
┌─────────────────────────────────────┐
│  User's Computer                    │
│  ┌───────────────────────────────┐  │
│  │  .env file                    │  │
│  │  └─ API Key (stored locally)  │  │
│  └───────────────────────────────┘  │
│                │                     │
│                ▼                     │
│  ┌───────────────────────────────┐  │
│  │  Application                  │  │
│  │  └─ Reads key securely        │  │
│  └───────────────────────────────┘  │
└────────────────┬────────────────────┘
                 │
                 │ HTTPS (encrypted)
                 ▼
┌─────────────────────────────────────┐
│  Google Gemini API                  │
│  ┌───────────────────────────────┐  │
│  │  Processes request            │  │
│  │  Returns summary              │  │
│  │  No data stored               │  │
│  └───────────────────────────────┘  │
└─────────────────────────────────────┘
```

**Security Measures**:
- ✅ API key never exposed in code
- ✅ Stored in `.env` (not in git)
- ✅ HTTPS encryption for API calls
- ✅ No data logging or storage
- ✅ Input validation to prevent attacks

---

## ⚡ Performance Optimization

```
┌─────────────────────────────────────┐
│  Performance Strategy               │
├─────────────────────────────────────┤
│                                     │
│  1. Caching                         │
│     └─ Store recent summaries       │
│                                     │
│  2. Async Processing                │
│     └─ Don't block UI               │
│                                     │
│  3. Content Chunking                │
│     └─ Handle large articles        │
│                                     │
│  4. Error Recovery                  │
│     └─ Retry failed requests        │
│                                     │
│  5. Rate Limiting                   │
│     └─ Respect API limits           │
└─────────────────────────────────────┘
```

---

## 🎯 Key Design Decisions

### Why Streamlit?
- ✅ Easy to learn for beginners
- ✅ Python-only (no HTML/CSS/JS needed)
- ✅ Fast development
- ✅ Built-in components
- ✅ Free deployment options

### Why Google Gemini?
- ✅ Free tier available
- ✅ Good quality summaries
- ✅ Fast response times
- ✅ Easy API integration
- ✅ Generous rate limits

### Why BeautifulSoup?
- ✅ Simple to use
- ✅ Handles most websites
- ✅ Good documentation
- ✅ Lightweight
- ✅ Reliable parsing

---

## 🔄 Error Handling Flow

```
User Action
   │
   ▼
Try Operation
   │
   ├─ Success? ──────────> Continue
   │
   └─ Error? 
      │
      ▼
   Identify Error Type
      │
      ├─ Invalid URL ────> Show friendly message
      │
      ├─ Network Error ──> Retry with timeout
      │
      ├─ API Error ──────> Check API key/limits
      │
      ├─ Content Error ──> Try alternative method
      │
      └─ Unknown ────────> Log & show generic error
```

---

## 📊 State Management

```
Application State
├─ User Input State
│  ├─ URL
│  ├─ Options
│  └─ API Key
│
├─ Processing State
│  ├─ Loading
│  ├─ Progress
│  └─ Status
│
└─ Results State
   ├─ Summary
   ├─ Statistics
   └─ Errors
```

Streamlit automatically manages state between reruns!

---

## 🎓 Learning Path

To understand this architecture:

1. **Start with**: `app.py` (see the UI)
2. **Then**: `modules/scraper.py` (understand scraping)
3. **Next**: `modules/summarizer.py` (learn AI integration)
4. **Finally**: `config.py` and `utils.py` (see helpers)

---

## 💡 Extension Points

Want to add features? Here's where:

```
New Feature Ideas:
│
├─ Multi-language support
│  └─ Modify: summarizer.py (add language param)
│
├─ Save summaries
│  └─ Add: database.py (SQLite storage)
│
├─ Batch processing
│  └─ Modify: app.py (add file upload)
│
├─ Custom prompts
│  └─ Add: prompts.py (template system)
│
└─ Analytics
   └─ Add: analytics.py (track usage)
```

---

**Questions?** Refer back to this guide as you build and modify the application!