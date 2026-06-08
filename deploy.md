# 🚀 Quick Deployment Commands

Copy and paste these commands to deploy your app!

---

## Step 1: Check Git Installation

```bash
git --version
```

If not installed, download from: https://git-scm.com/downloads

---

## Step 2: Initialize Git (First Time Only)

```bash
cd "c:/Users/000M0E744/Desktop/Bob The Builder"
git init
git add .
git commit -m "Initial commit - Web Page Summarizer"
```

---

## Step 3: Create GitHub Repository

1. Go to: https://github.com/new
2. Name: `web-page-summarizer`
3. Make it **Public**
4. Click "Create repository"

---

## Step 4: Push to GitHub

**Replace YOUR_USERNAME with your GitHub username!**

```bash
git remote add origin https://github.com/YOUR_USERNAME/web-page-summarizer.git
git branch -M main
git push -u origin main
```

**Example:**
```bash
git remote add origin https://github.com/john123/web-page-summarizer.git
git branch -M main
git push -u origin main
```

---

## Step 5: Deploy to Streamlit Cloud

1. Go to: https://streamlit.io/cloud
2. Sign in with GitHub
3. Click "New app"
4. Select your repository: `YOUR_USERNAME/web-page-summarizer`
5. Main file: `app.py`
6. Click "Deploy"

---

## Step 6: Add API Key Secret

1. In Streamlit Cloud dashboard
2. Go to your app → Settings → Secrets
3. Add this:

```toml
GEMINI_API_KEY = "paste_your_actual_api_key_here"
```

4. Click "Save"

---

## ✅ Done!

Your app will be live at: `https://your-app-name.streamlit.app`

---

## 🔄 Update Your App Later

```bash
git add .
git commit -m "Updated features"
git push
```

Streamlit Cloud will automatically redeploy!

---

## 🆘 Need Help?

Check DEPLOYMENT_GUIDE.md for detailed instructions and troubleshooting!