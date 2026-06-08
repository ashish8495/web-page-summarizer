# 🔧 Troubleshooting Guide

Common issues and their solutions for the Web Page Summarizer.

---

## ❌ ImportError: lxml.html.clean module

### Error Message:
```
ImportError: lxml.html.clean module is now a separate project lxml_html_clean.
Install lxml[html-clean] or lxml_html_clean directly.
```

### Solution:
This is a compatibility issue with newer versions of lxml. Install the missing package:

```bash
pip install lxml_html_clean
```

Or reinstall all requirements:
```bash
pip install -r requirements.txt
```

**Status**: ✅ FIXED - requirements.txt has been updated to include this package.

---

## ❌ Module Not Found Errors

### Error Message:
```
ModuleNotFoundError: No module named 'streamlit'
```

### Solution:
Install all required packages:

```bash
pip install -r requirements.txt
```

Or install individually:
```bash
pip install streamlit google-generativeai beautifulsoup4 requests lxml lxml_html_clean python-dotenv trafilatura validators
```

---

## ❌ Invalid API Key

### Error Message:
```
❌ Please provide a Google Gemini API key in the sidebar.
```

### Solution:

**Option 1: Use .env file (Recommended)**
1. Create a file named `.env` in the project folder
2. Add this line:
   ```
   GEMINI_API_KEY=your_actual_api_key_here
   ```
3. Restart the app

**Option 2: Enter in sidebar**
1. Look at the left sidebar in the app
2. Find "API Configuration" section
3. Paste your API key in the password field

**Get API Key:**
- Visit: https://makersuite.google.com/app/apikey
- Click "Create API Key"
- Copy the key (starts with "AIza...")

---

## ❌ Cannot Access URL

### Error Message:
```
❌ Failed to fetch the web page. Please check the URL and try again.
```

### Possible Causes & Solutions:

**1. Invalid URL Format**
- Make sure URL starts with `http://` or `https://`
- Example: `https://example.com/article`

**2. Website Blocks Automated Access**
- Some websites block bots
- Try a different website
- News sites and Wikipedia usually work well

**3. Page Requires Login**
- The app cannot access pages behind login
- Try public articles instead

**4. Network Issues**
- Check your internet connection
- Try the URL in your browser first
- Some corporate networks block certain sites

---

## ❌ No Content Found

### Error Message:
```
❌ No readable content found on this page.
```

### Solutions:

**1. Page Has Very Little Text**
- Try a page with more content (at least 100 words)
- Articles and blog posts work best

**2. Page Structure Not Recognized**
- Some websites have unusual structures
- Try a different page from the same site
- News articles usually work well

**3. Page is Mostly Images/Videos**
- The app extracts text only
- Try a text-heavy page instead

---

## ❌ Streamlit Not Recognized

### Error Message:
```
'streamlit' is not recognized as an internal or external command
```

### Solution:

**Option 1: Use Python module syntax**
```bash
python -m streamlit run app.py
```

**Option 2: Add Python Scripts to PATH**
1. Find your Python Scripts folder (usually `C:\Users\YourName\AppData\Local\Programs\Python\Python3XX\Scripts`)
2. Add it to your system PATH
3. Restart terminal

**Option 3: Use full path**
```bash
C:\Users\YourName\AppData\Local\Programs\Python\Python3XX\Scripts\streamlit.exe run app.py
```

---

## ❌ Port Already in Use

### Error Message:
```
OSError: [Errno 98] Address already in use
```

### Solution:

**Option 1: Use different port**
```bash
streamlit run app.py --server.port 8502
```

**Option 2: Kill existing process**

Windows:
```bash
netstat -ano | findstr :8501
taskkill /PID <PID_NUMBER> /F
```

Mac/Linux:
```bash
lsof -ti:8501 | xargs kill -9
```

---

## ❌ API Rate Limit Exceeded

### Error Message:
```
⚠️ API rate limit reached. Please wait a moment and try again.
```

### Solution:

**Free Tier Limits:**
- Google Gemini free tier has rate limits
- Wait 1-2 minutes between requests
- Or upgrade to paid tier for higher limits

**Tips:**
- Don't spam the summarize button
- Process one page at a time
- Wait for completion before next request

---

## ❌ Summary Too Short/Long

### Issue:
Summary doesn't match expected length

### Solution:

**Adjust Summary Length:**
1. Click "Customization Options"
2. Select different length:
   - **Short**: 3-5 key points (~150 words)
   - **Medium**: 5-8 key points (~300 words)
   - **Long**: 8-12 key points (~500 words)

**Note:** AI may adjust length based on content complexity

---

## ❌ App Won't Start

### Checklist:

1. **Python Installed?**
   ```bash
   python --version
   ```
   Should show Python 3.8 or higher

2. **In Correct Directory?**
   ```bash
   cd "c:/Users/000M0E744/Desktop/Bob The Builder"
   ```

3. **All Files Present?**
   - Check that `app.py` exists
   - Check that `modules/` folder exists

4. **Dependencies Installed?**
   ```bash
   pip list
   ```
   Should show streamlit, google-generativeai, etc.

5. **Try Clean Install:**
   ```bash
   pip uninstall -y streamlit google-generativeai beautifulsoup4 requests lxml lxml_html_clean python-dotenv trafilatura validators
   pip install -r requirements.txt
   ```

---

## ❌ Encoding Errors

### Error Message:
```
UnicodeDecodeError: 'charmap' codec can't decode byte
```

### Solution:

This usually happens with non-English content. The app should handle this automatically, but if it persists:

1. Make sure you're using Python 3.8+
2. Try a different web page
3. Check if the page has unusual characters

---

## ❌ Slow Performance

### Issue:
App takes too long to generate summaries

### Solutions:

**1. Check Internet Speed**
- Slow connection affects page fetching
- Test with a simple page first

**2. Page Too Large**
- Very long articles take longer
- Try shorter content first
- App limits content to 50,000 characters

**3. API Response Time**
- Gemini API response varies
- Usually 3-10 seconds
- Peak times may be slower

---

## 🆘 Still Having Issues?

### Debug Steps:

1. **Check Error Message Carefully**
   - Read the full error in terminal
   - Note the exact error type

2. **Verify File Structure**
   ```
   Bob The Builder/
   ├── app.py
   ├── config.py
   ├── .env
   └── modules/
       ├── __init__.py
       ├── scraper.py
       ├── summarizer.py
       └── utils.py
   ```

3. **Test Components Individually**
   - Try opening Python and importing modules
   - Test if API key works

4. **Check Logs**
   - Look at terminal output
   - Streamlit shows detailed errors

5. **Fresh Start**
   - Close all terminals
   - Restart VS Code
   - Try again

---

## 📝 Reporting Issues

If you still have problems, gather this information:

- Python version: `python --version`
- Installed packages: `pip list`
- Error message (full text)
- Steps to reproduce
- Operating system

---

## ✅ Quick Fixes Summary

| Problem | Quick Fix |
|---------|-----------|
| lxml error | `pip install lxml_html_clean` |
| Module not found | `pip install -r requirements.txt` |
| No API key | Create `.env` file with key |
| Can't access URL | Try different website |
| Streamlit not found | Use `python -m streamlit run app.py` |
| Port in use | Use `--server.port 8502` |
| Rate limit | Wait 1-2 minutes |

---

**Most issues are solved by reinstalling dependencies:**
```bash
pip install -r requirements.txt
```

**Then restart the app:**
```bash
streamlit run app.py