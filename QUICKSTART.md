# Quick Start Guide - Get Running in 5 Minutes

## Step 1: Get Your FREE API Key (2 min)

1. Go to: **https://makersuite.google.com/app/apikey**
2. Click **"Create API Key"**
3. Copy the key (starts with `AIzaSy...`)

No credit card needed! 🎉

## Step 2: Install (1 min)

```bash
pip install -r requirements.txt
```

## Step 3: Configure (1 min)

Create `.env` file:

**Windows:**
```bash
copy .env.example .env
notepad .env
```

**Mac/Linux:**
```bash
cp .env.example .env
nano .env
```

Add this:
```env
LLM_PROVIDER=gemini
GOOGLE_API_KEY=AIzaSy...your-key-here
```

Save and close.

## Step 4: Run (1 min)

**Windows:**
```bash
run.bat
```

**Mac/Linux:**
```bash
chmod +x run.sh
./run.sh
```

**Or just:**
```bash
python main.py
```

## Step 5: Try It

Select option 1 or 2 from the menu and watch the magic happen! ✨

---

## That's It!

You now have:
- ✅ A working multi-agent AI system
- ✅ Running completely FREE
- ✅ Ready to demo in interviews
- ✅ A great portfolio project

## Next Steps

1. **Try both scenarios** to see different use cases
2. **Read the code** to understand how it works
3. **Customize it** - add your own scenarios
4. **Add to resume** - you built this!

## Troubleshooting

**Error: "API key not valid"**
- Check `.env` has the correct key
- No quotes, no spaces around the `=`

**Error: "Module not found"**
```bash
pip install -r requirements.txt --force-reinstall
```

**Want to run offline?**
See [FREE_SETUP.md](FREE_SETUP.md) for Ollama setup

## Need Help?

See the detailed guides:
- [FREE_SETUP.md](FREE_SETUP.md) - Complete free options guide
- [SETUP_GUIDE.md](SETUP_GUIDE.md) - Full setup documentation
- [README.md](README.md) - Project overview

---

**You're all set! Good luck! 🚀**
