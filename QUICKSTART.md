# 🚀 Quick Start Guide

Get your Web Page Summarizer running in 5 minutes!

## ⚡ Fast Setup (For Beginners)

### Step 1: Check Python Installation

Open your terminal (Command Prompt or PowerShell on Windows) and type:

```bash
python --version
```

You should see something like `Python 3.8.x` or higher. If not, [download Python here](https://www.python.org/downloads/).

---

### Step 2: Navigate to Project Folder

```bash
cd "c:/Users/000M0E744/Desktop/Bob The Builder"
```

---

### Step 3: Install Required Packages

Copy and paste this command:

```bash
pip install streamlit google-generativeai beautifulsoup4 requests lxml python-dotenv trafilatura validators
```

Wait for installation to complete (may take 2-3 minutes).

---

### Step 4: Get Your Free API Key

1. Go to: https://makersuite.google.com/app/apikey
2. Click **"Create API Key"**
3. Copy the key (starts with "AIza...")

---

### Step 5: Create Your .env File

Create a new file named `.env` (yes, just `.env` with a dot at the start) in the project folder.

Add this line to the file:

```
GEMINI_API_KEY=paste_your_api_key_here
```

Replace `paste_your_api_key_here` with your actual API key.

**How to create .env file:**
- **Windows**: Right-click in folder → New → Text Document → Name it `.env` (remove .txt extension)
- **Or use command**: `echo GEMINI_API_KEY=your_key_here > .env`

---

### Step 6: Run the Application

```bash
streamlit run app.py
```

The app will automatically open in your web browser! 🎉

---

## 🎯 Using the Application

### First Time Use

1. **Enter API Key** (if not in .env):
   - Look at the sidebar on the left
   - Paste your Gemini API key in the password field

2. **Enter a URL**:
   - Paste any article or blog URL
   - Example: `https://en.wikipedia.org/wiki/Artificial_intelligence`

3. **Choose Options** (optional):
   - Click "Customization Options"
   - Select summary length (Short/Medium/Long)
   - Choose format (Bullets or Paragraph)

4. **Click "Summarize"**:
   - Wait 5-10 seconds
   - See your summary appear!

5. **Export Your Summary**:
   - Click "Copy Summary" to copy text
   - Click "Download" to save as .txt file

---

## 🔧 Troubleshooting

### Problem: "pip is not recognized"

**Solution**: Python not in PATH. Try:
```bash
python -m pip install streamlit google-generativeai beautifulsoup4 requests lxml python-dotenv trafilatura validators
```

### Problem: "streamlit is not recognized"

**Solution**: Try:
```bash
python -m streamlit run app.py
```

### Problem: "Invalid API key"

**Solution**:
- Check your .env file has the correct key
- Make sure there are no spaces around the `=`
- Get a new key from https://makersuite.google.com/app/apikey

### Problem: "Cannot access URL"

**Solution**:
- Check if the URL is correct
- Try a different website
- Some sites block automated access

### Problem: Port already in use

**Solution**: Use a different port:
```bash
streamlit run app.py --server.port 8502
```

---

## 📱 Stopping the Application

Press `Ctrl + C` in the terminal to stop the app.

---

## 🎓 Next Steps

Once you're comfortable:

1. **Read the full README.md** - Detailed documentation
2. **Check ARCHITECTURE.md** - Understand how it works
3. **Modify config.py** - Customize settings
4. **Explore the code** - Learn and experiment!

---

## 💡 Pro Tips

✅ **Bookmark frequently used URLs** - Save time

✅ **Try different summary lengths** - See what works best

✅ **Use bullet format for quick scanning** - Easier to read

✅ **Download important summaries** - Keep for reference

✅ **Test with various content types** - News, blogs, docs

---

## 🆘 Still Need Help?

1. Check the error message carefully
2. Read the full README.md
3. Review ARCHITECTURE.md for technical details
4. Make sure all files are in the correct location

---

## 📁 Expected File Structure

Make sure you have all these files:

```
Bob The Builder/
├── app.py                      ✓ Main application
├── config.py                   ✓ Configuration
├── requirements.txt            ✓ Dependencies
├── .env                        ✓ Your API key (create this!)
├── .env.example               ✓ Template
├── .gitignore                 ✓ Git ignore
├── README.md                  ✓ Full documentation
├── QUICKSTART.md              ✓ This file
├── ARCHITECTURE.md            ✓ Technical details
├── web-summarizer-plan.md     ✓ Project plan
│
└── modules/
    ├── __init__.py            ✓ Package init
    ├── scraper.py             ✓ Web scraping
    ├── summarizer.py          ✓ AI integration
    └── utils.py               ✓ Helper functions
```

---

## ✅ Checklist

Before running, make sure:

- [ ] Python 3.8+ installed
- [ ] All packages installed (`pip install ...`)
- [ ] .env file created with API key
- [ ] In correct directory
- [ ] Terminal/command prompt open

---

**Ready? Run this command:**

```bash
streamlit run app.py
```

**Enjoy your AI-powered web page summarizer! 🎉**