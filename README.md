# 🤖 Web Page Summarizer - AI Agent

An intelligent web application that reads any web page and generates concise summaries with key points using Google Gemini AI.

## 🌟 What Does This Do?

Simply paste a URL, and the AI agent will:
- 📖 Read the entire web page
- 🧠 Understand the content
- ✨ Extract only the important points
- 📝 Give you a clean summary

Perfect for quickly understanding articles, blog posts, documentation, or any web content!

---

## 🎯 Features

- ✅ **Simple Interface** - Just paste a URL and click summarize
- 🚀 **Fast Processing** - Get summaries in seconds
- 🎨 **Flexible Formats** - Choose bullet points or paragraph style
- 📏 **Length Control** - Short, medium, or long summaries
- 💾 **Easy Export** - Copy or download your summaries
- 🆓 **Free to Use** - Uses Google Gemini's free tier

---

## 📋 Prerequisites

Before you start, you need:

1. **Python 3.8 or higher** installed on your computer
   - Check: Open terminal/command prompt and type `python --version`
   - Download from: https://www.python.org/downloads/

2. **Google Gemini API Key** (Free!)
   - Go to: https://makersuite.google.com/app/apikey
   - Click "Create API Key"
   - Copy and save it somewhere safe

3. **Basic terminal/command prompt knowledge**
   - How to navigate folders (`cd` command)
   - How to run commands

---

## 🚀 Quick Start Guide

### Step 1: Download the Project

```bash
# If you have git installed:
git clone <repository-url>
cd web-page-summarizer

# Or download the ZIP file and extract it
```

### Step 2: Install Required Packages

Open terminal/command prompt in the project folder and run:

```bash
pip install -r requirements.txt
```

This installs all the necessary Python libraries.

### Step 3: Set Up Your API Key

Create a file named `.env` in the project folder and add:

```
GEMINI_API_KEY=your_api_key_here
```

Replace `your_api_key_here` with your actual Google Gemini API key.

### Step 4: Run the Application

```bash
streamlit run app.py
```

The app will open in your web browser automatically! 🎉

---

## 📖 How to Use

1. **Enter a URL** - Paste any web page URL in the input field
2. **Choose Options** (optional)
   - Select summary length (short/medium/long)
   - Choose format (bullet points or paragraph)
3. **Click "Summarize"** - Wait a few seconds
4. **Read Your Summary** - The AI will show you the key points
5. **Copy or Download** - Save the summary if you want

### Example URLs to Try

- News article: `https://www.bbc.com/news`
- Wikipedia: `https://en.wikipedia.org/wiki/Artificial_intelligence`
- Blog post: Any Medium or blog article
- Documentation: Any technical docs page

---

## 🛠️ Project Structure

```
web-page-summarizer/
├── app.py                 # Main application (run this!)
├── config.py              # Settings and configuration
├── requirements.txt       # Python packages needed
├── .env                   # Your API key (create this!)
├── README.md             # This file
│
├── modules/
│   ├── scraper.py        # Extracts content from web pages
│   ├── summarizer.py     # Generates summaries with AI
│   └── utils.py          # Helper functions
│
└── web-summarizer-plan.md # Detailed project plan
```

---

## ⚙️ Configuration Options

You can customize the app by editing `config.py`:

```python
# Maximum content length to process
MAX_CONTENT_LENGTH = 50000

# Request timeout (seconds)
REQUEST_TIMEOUT = 30

# Default summary length
DEFAULT_SUMMARY_LENGTH = "medium"

# Default format
DEFAULT_FORMAT = "bullets"
```

---

## 🐛 Troubleshooting

### Problem: "Module not found" error
**Solution**: Make sure you installed all requirements:
```bash
pip install -r requirements.txt
```

### Problem: "Invalid API key" error
**Solution**: 
- Check your `.env` file has the correct API key
- Make sure there are no extra spaces
- Get a new key from https://makersuite.google.com/app/apikey

### Problem: "Cannot access URL" error
**Solution**:
- Check if the URL is correct and accessible
- Some websites block automated access
- Try a different website

### Problem: App won't start
**Solution**:
- Make sure Python 3.8+ is installed
- Check if port 8501 is available
- Try: `streamlit run app.py --server.port 8502`

---

## 📚 Understanding the Code

### For Non-Coders

Even if you're not a programmer, here's what each part does:

1. **app.py** - The main file that creates the web interface
   - Think of it as the "face" of your application
   - Handles user input and displays results

2. **modules/scraper.py** - Gets content from websites
   - Like a robot that visits the URL and reads everything
   - Cleans up the text to remove ads and menus

3. **modules/summarizer.py** - Talks to Google Gemini AI
   - Sends the content to AI
   - Gets back a nice summary
   - Formats it nicely for you

4. **config.py** - Settings file
   - All the adjustable options in one place
   - Easy to change without touching main code

---

## 🎓 Learning Resources

Want to understand or modify the code? Start here:

### Python Basics
- [Python for Beginners](https://www.python.org/about/gettingstarted/)
- [Learn Python - Interactive](https://www.learnpython.org/)

### Streamlit (UI Framework)
- [Streamlit Documentation](https://docs.streamlit.io)
- [Streamlit Tutorial](https://docs.streamlit.io/library/get-started)

### Web Scraping
- [Beautiful Soup Tutorial](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
- [Web Scraping with Python](https://realpython.com/beautiful-soup-web-scraper-python/)

### Google Gemini AI
- [Gemini API Docs](https://ai.google.dev/docs)
- [Python Quickstart](https://ai.google.dev/tutorials/python_quickstart)

---

## 🔒 Privacy & Security

- ✅ Your API key stays on your computer (in `.env` file)
- ✅ No data is stored or logged
- ✅ URLs are processed in real-time only
- ⚠️ Don't share your `.env` file with anyone
- ⚠️ Don't commit `.env` to git (it's in `.gitignore`)

---

## 🚀 Next Steps

Once you're comfortable with the basic app, you can:

1. **Customize the UI** - Change colors, layout in `app.py`
2. **Add Features** - See `web-summarizer-plan.md` for ideas
3. **Deploy Online** - Use Streamlit Cloud (free!)
4. **Share with Friends** - Let others use your app

---

## 💡 Tips for Best Results

- ✅ Use URLs with substantial text content
- ✅ Try different summary lengths for different content
- ✅ Use bullet format for quick scanning
- ✅ Use paragraph format for detailed understanding
- ❌ Avoid URLs that require login
- ❌ Avoid very short pages (not much to summarize)

---

## 🤝 Need Help?

- 📖 Read the detailed plan: `web-summarizer-plan.md`
- 🐛 Check troubleshooting section above
- 💬 Ask questions in the issues section
- 📧 Contact the developer

---

## 📝 License

This project is open source and available for personal and educational use.

---

## 🎉 Congratulations!

You've set up your first AI agent! This is a great starting point for learning about:
- Web scraping
- AI integration
- Building web applications
- Python programming

Keep experimenting and building! 🚀

---

**Made with ❤️ for beginners learning AI and Python**