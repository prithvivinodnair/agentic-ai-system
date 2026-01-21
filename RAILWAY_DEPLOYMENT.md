# 🚂 Railway Deployment Guide

Quick guide to deploy your backend on Railway.

---

## ✅ Fixed: Python Build Error

**Error you saw:**
```
mise ERROR Failed to install core:python@3.11.0: no precompiled python found
```

**Solution:**
I've added `nixpacks.toml` which tells Railway to use Python 3.11 correctly. Railway will auto-redeploy now.

---

## 🚀 Deploy Steps

### 1. Wait for Auto-Deploy

Railway detected the new commit and should be redeploying automatically. Check your Railway dashboard.

### 2. Add Environment Variables

Once the build succeeds, add these environment variables in Railway:

1. Click on your service
2. Go to "Variables" tab
3. Click "+ New Variable"
4. Add:

```
GOOGLE_API_KEY=AIza... (your actual Gemini API key)
LLM_PROVIDER=gemini
```

### 3. Generate Domain

1. Go to "Settings" tab
2. Scroll to "Networking"
3. Click "Generate Domain"
4. Copy the URL (e.g., `https://agentic-ai-system-production.up.railway.app`)

---

## 🧪 Test Your Backend

Once deployed, test it:

```bash
# Replace with your Railway URL
curl https://your-app.railway.app/health
```

Should return:
```json
{"status":"healthy"}
```

---

## 📝 Configuration Details

### nixpacks.toml
Tells Railway:
- Use Python 3.11
- Install dependencies from requirements.txt
- Start with uvicorn command

### Start Command
```
uvicorn api_server:app --host 0.0.0.0 --port $PORT
```

Railway automatically sets `$PORT` (usually 8000 or random).

---

## 🐛 Common Issues

### Build Still Failing?

**Check Build Logs:**
1. Go to "Deployments" tab
2. Click on the failed deployment
3. Click "View Logs"
4. Look for errors

**Common fixes:**
- Missing dependency in requirements.txt
- Typo in nixpacks.toml
- Wrong Python version

### App Crashes on Start?

**Check Deploy Logs:**
1. Go to "Deploy Logs" tab
2. Look for Python errors

**Common causes:**
- Missing GOOGLE_API_KEY variable
- Import error (missing package)
- Port binding issue

### Health Check Failing?

Make sure your api_server.py has:
```python
@app.get("/health")
async def health_check():
    return {"status": "healthy"}
```

---

## 💰 Free Tier Limits

Railway Free Trial:
- **$5 credit** (about 500 hours of usage)
- **After free trial:** $0.01/hour (~$7/month)
- **Sleep mode:** Can enable to save costs

**Pro Tip:** Enable "Sleep on Idle" in Settings to pause the app when not in use.

---

## 🔗 Next Steps

After backend deploys successfully:

1. **Copy your Railway URL**
2. **Deploy Frontend on Vercel**
3. **Add Railway URL to Vercel env vars:**
   ```
   NEXT_PUBLIC_API_URL=https://your-app.railway.app
   ```

---

## ✅ Verification Checklist

- [ ] Build succeeded (check Deployments tab)
- [ ] Environment variables added
- [ ] Domain generated
- [ ] Health endpoint returns `{"status":"healthy"}`
- [ ] Ready to deploy frontend!

---

**Need help? Check the Railway docs: https://docs.railway.app**
