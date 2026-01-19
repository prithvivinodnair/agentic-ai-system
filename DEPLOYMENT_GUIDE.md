# 🚀 Deployment Guide - Make Your App Live!

This guide will help you deploy your Agentic AI System so it's accessible online with working demo links.

---

## 🎯 What We're Deploying

- **Frontend (Next.js)** → Vercel (FREE)
- **Backend (FastAPI)** → Railway or Render (FREE tier)

**Total Cost:** $0/month

---

## 📦 Step 1: Deploy Backend First

We deploy the backend first so we can get its URL for the frontend.

### Option A: Railway (Recommended - Easier)

1. **Sign up for Railway:**
   - Go to [railway.app](https://railway.app)
   - Click "Login with GitHub"
   - Authorize Railway

2. **Create New Project:**
   - Click "New Project"
   - Select "Deploy from GitHub repo"
   - Choose `agentic-ai-system`

3. **Configure Environment Variables:**
   - Click on your service
   - Go to "Variables" tab
   - Add these variables:
     ```
     GOOGLE_API_KEY=your_actual_gemini_api_key_here
     LLM_PROVIDER=gemini
     PORT=8000
     ```

4. **Deploy:**
   - Railway will auto-deploy
   - Wait 2-3 minutes
   - Click "Generate Domain" to get your URL
   - Copy this URL (e.g., `https://your-app.railway.app`)

### Option B: Render

1. **Sign up for Render:**
   - Go to [render.com](https://render.com)
   - Sign up with GitHub

2. **Create New Web Service:**
   - Click "New +"
   - Select "Web Service"
   - Connect to `agentic-ai-system` repo

3. **Configure:**
   - Name: `agentic-ai-backend`
   - Environment: Python 3
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `uvicorn api_server:app --host 0.0.0.0 --port $PORT`

4. **Environment Variables:**
   ```
   GOOGLE_API_KEY=your_actual_gemini_api_key_here
   LLM_PROVIDER=gemini
   ```

5. **Deploy:**
   - Click "Create Web Service"
   - Wait 3-5 minutes
   - Copy the URL (e.g., `https://your-app.onrender.com`)

---

## 🎨 Step 2: Deploy Frontend

### Using Vercel (Recommended)

1. **Sign up for Vercel:**
   - Go to [vercel.com](https://vercel.com)
   - Click "Sign Up with GitHub"
   - Authorize Vercel

2. **Import Project:**
   - Click "Add New..." → "Project"
   - Select `agentic-ai-system` repository
   - Click "Import"

3. **Configure Build Settings:**
   - Framework Preset: Next.js
   - Root Directory: `frontend`
   - Build Command: `npm run build`
   - Output Directory: `.next`

4. **Add Environment Variable:**
   - Click "Environment Variables"
   - Add:
     ```
     NEXT_PUBLIC_API_URL=https://your-backend-url.railway.app
     ```
   - Replace with your actual backend URL from Step 1

5. **Deploy:**
   - Click "Deploy"
   - Wait 2-3 minutes
   - Vercel will give you a URL like `https://agentic-ai-system.vercel.app`

---

## 🔗 Step 3: Update Frontend to Use Backend URL

After deploying the backend, update your frontend code:

### Edit frontend/app/page.tsx:

Find this line (around line 150):
```typescript
const API_URL = 'http://localhost:8000';
```

Change it to:
```typescript
const API_URL = process.env.NEXT_PUBLIC_API_URL || 'http://localhost:8000';
```

### Redeploy Frontend:

1. Commit and push this change:
   ```bash
   cd "c:\Users\Prithvi Nair\OneDrive\Desktop\Agentic AI"
   git add .
   git commit -m "Update API URL for production deployment"
   git push
   ```

2. Vercel will automatically redeploy (takes ~2 minutes)

---

## ✅ Step 4: Test Your Deployment

1. **Open your Vercel URL:** `https://your-app.vercel.app`
2. **Click "Run Emergency Scenario"**
3. **Watch it work!** The agents should run and show results

If it works, you're done! 🎉

---

## 🐛 Troubleshooting

### Backend Issues

**Error: "Application failed to start"**
- Check Railway/Render logs
- Verify `GOOGLE_API_KEY` is set correctly
- Make sure `requirements.txt` includes all dependencies

**Error: "API endpoint not found"**
- Verify your backend URL is accessible
- Test: `https://your-backend-url.railway.app/health`
- Should return `{"status":"healthy"}`

### Frontend Issues

**Error: "Failed to fetch"**
- Check `NEXT_PUBLIC_API_URL` environment variable
- Verify backend is running
- Check browser console for CORS errors

**CORS Error:**
- Add this to `api_server.py` (already included):
  ```python
  app.add_middleware(
      CORSMiddleware,
      allow_origins=["*"],
      allow_methods=["*"],
      allow_headers=["*"],
  )
  ```

---

## 💰 Free Tier Limits

### Railway:
- **FREE:** $5 credit/month (enough for 500+ API calls)
- **Usage:** ~$0.01 per hour of uptime
- **Sleep:** App sleeps after inactivity (good for demos)

### Render:
- **FREE:** 750 hours/month
- **Sleep:** App sleeps after 15 min inactivity
- **Restart:** Takes ~30 seconds on first request

### Vercel:
- **FREE:** Unlimited deployments
- **Bandwidth:** 100GB/month
- **Perfect for:** Static + SSR Next.js apps

---

## 🎯 After Deployment

### Update Your README:

Add these badges at the top:
```markdown
[![Live Demo](https://img.shields.io/badge/demo-live-success)](https://your-app.vercel.app)
[![Backend](https://img.shields.io/badge/backend-railway-purple)](https://your-backend.railway.app)
```

### Update Your CV:

**Before:**
```
Agentic AI System for Automating National-Scale Operational Decisions
```

**After:**
```
Agentic AI System for Automating National-Scale Operational Decisions
🔗 Live Demo: https://your-app.vercel.app
📂 GitHub: https://github.com/prithvivinodnair/agentic-ai-system
```

---

## 📱 Share Your Live Demo

Now you can share a working link!

**LinkedIn:**
```
🚀 Check out my AI project LIVE: https://your-app.vercel.app

Built a full-stack multi-agent system that makes complex decisions
using AI. Try the demo - it analyzes disaster scenarios in real-time!

#AI #GenAI #NextJS #Python
```

---

## 🎉 You're Done!

Your app is now:
- ✅ Live on the internet
- ✅ Accessible to anyone with the link
- ✅ Running on FREE tier
- ✅ Auto-deploying on every git push

**Demo it in interviews, share it on LinkedIn, add it to your portfolio!**
