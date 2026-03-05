# AI Text-to-SQL Bot

Convert natural language questions to SQL queries using Groq AI.

## Features
- Natural language to SQL conversion
- Beautiful modern UI
- Powered by Groq's Llama 3.3 70B model
- In-memory SQLite database with employee data

## Deploy to Vercel (Recommended - Free & Fast)

### Quick Deploy
1. Push your code to GitHub (already done!)
2. Go to https://vercel.com
3. Sign up/login with GitHub
4. Click "Add New" → "Project"
5. Import your repository: `GayathriAbhirami/text-to-sql-bot`
6. Vercel auto-detects settings from `vercel.json`
7. Add Environment Variable:
   - Key: `GROQ_API_KEY`
   - Value: Your Groq API key
8. Click "Deploy"
9. Done! Your app is live in ~1 minute

Your app will be at: `https://your-project-name.vercel.app`

### Using Vercel CLI (Alternative)
```bash
npm i -g vercel
vercel login
vercel
```

## Deploy to Render (Alternative)

### Step 1: Push to GitHub
1. Create a new repository on GitHub
2. Run these commands:
```bash
git init
git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin YOUR_GITHUB_REPO_URL
git push -u origin main
```

### Step 2: Deploy on Render
1. Go to https://render.com and sign up/login
2. Click "New +" → "Web Service"
3. Connect your GitHub repository
4. Render will auto-detect settings from render.yaml
5. Add environment variable:
   - Key: `GROQ_API_KEY`
   - Value: `YOUR_GROQ_API_KEY_HERE` (get it from https://console.groq.com)
6. Click "Create Web Service"
7. Wait 2-3 minutes for deployment

Your app will be live at: `https://your-app-name.onrender.com`

## Alternative: Deploy to Railway (Free)

1. Go to https://railway.app
2. Sign up with GitHub
3. Click "New Project" → "Deploy from GitHub repo"
4. Select your repository
5. Add environment variable `GROQ_API_KEY`
6. Railway will auto-deploy

## Alternative: Deploy to PythonAnywhere (Free)

1. Go to https://www.pythonanywhere.com
2. Sign up for free account
3. Upload your files
4. Set up a web app with Flask
5. Configure WSGI file to point to app.py

## Local Development
```bash
pip install -r requirements.txt
python app.py
```
Visit http://localhost:5000

## Example Queries
- Show all employees
- Get employees in IT department
- Find employees with salary greater than 50000
- Show the highest paid employee
