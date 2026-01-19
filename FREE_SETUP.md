# FREE Setup Guide - No Credit Card Required! 🎉

This guide shows you how to run the Agentic AI system **completely FREE** using Google Gemini or Ollama.

## Option 1: Google Gemini (RECOMMENDED - Cloud-based, Free) ⭐

Google Gemini is **100% free** with generous limits perfect for this project.

### Step 1: Get Your Free API Key (2 minutes)

1. Go to [Google AI Studio](https://makersuite.google.com/app/apikey)
2. Click "Create API Key"
3. Copy the key (it will look like: `AIzaSy...`)

**Free Tier Limits:**
- 60 requests per minute
- Completely FREE
- No credit card needed
- Perfect for development and demos

### Step 2: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 3: Configure the System

Create a `.env` file:

```bash
# On Windows:
copy .env.example .env

# On Mac/Linux:
cp .env.example .env
```

Edit the `.env` file and add:

```env
LLM_PROVIDER=gemini
GOOGLE_API_KEY=AIzaSy...your-key-here...
```

### Step 4: Run It!

```bash
python main.py
```

That's it! You're running a multi-agent AI system for FREE! 🚀

---

## Option 2: Ollama (100% Local, No Internet Required)

Run AI models **completely offline** on your own computer.

### Pros:
- ✅ 100% free
- ✅ No API key needed
- ✅ Works offline
- ✅ Unlimited usage
- ✅ Privacy (data never leaves your computer)

### Cons:
- ❌ Requires downloading models (4-7GB)
- ❌ Slower than cloud options
- ❌ Needs decent computer (8GB+ RAM recommended)

### Step 1: Install Ollama

**Windows:**
```bash
# Download from: https://ollama.ai/download
# Run the installer
```

**Mac:**
```bash
brew install ollama
```

**Linux:**
```bash
curl -fsSL https://ollama.ai/install.sh | sh
```

### Step 2: Download a Model

```bash
# Start Ollama server
ollama serve

# In another terminal, download a model (choose one):

# Llama 2 (4GB) - Good balance
ollama pull llama2

# Mistral (4GB) - Faster, good quality
ollama pull mistral

# Llama 3 (4GB) - Latest, best quality
ollama pull llama3
```

### Step 3: Configure

Edit `.env`:

```env
LLM_PROVIDER=ollama
OLLAMA_MODEL=llama2
# Or: OLLAMA_MODEL=mistral
# Or: OLLAMA_MODEL=llama3
```

### Step 4: Run

Make sure Ollama is running:

```bash
# Terminal 1: Start Ollama
ollama serve

# Terminal 2: Run the system
python main.py
```

---

## Quick Comparison

| Feature | Google Gemini | Ollama | OpenAI GPT-4 |
|---------|---------------|--------|--------------|
| **Cost** | FREE | FREE | ~$2/run |
| **Speed** | Fast (1-3 sec) | Slow (5-15 sec) | Fast (1-3 sec) |
| **Quality** | Excellent | Good | Excellent |
| **Setup** | 2 minutes | 10 minutes | 5 minutes |
| **Internet** | Required | Not required | Required |
| **Limits** | 60 req/min | Unlimited | Pay per use |

---

## Troubleshooting

### Google Gemini Issues

**Error: "API key not valid"**
```bash
# Make sure .env has:
LLM_PROVIDER=gemini
GOOGLE_API_KEY=AIzaSy...
# (No quotes, no spaces)
```

**Error: "Resource exhausted"**
- You hit the rate limit (60 requests/min)
- Wait 1 minute and try again
- This is rare with our system

### Ollama Issues

**Error: "Connection refused"**
```bash
# Make sure Ollama is running:
ollama serve

# Check it's working:
ollama list
```

**Model not found:**
```bash
# Download the model first:
ollama pull llama2

# See all downloaded models:
ollama list
```

**Too slow:**
```bash
# Try a smaller/faster model:
ollama pull mistral

# Update .env:
OLLAMA_MODEL=mistral
```

---

## Testing Your Setup

### Quick Test

```python
# Create test.py
from config import config

config.validate()
print(f"✓ Using {config.LLM_PROVIDER}")
print("✓ Configuration is valid!")
```

```bash
python test.py
```

### Full Test

```bash
python main.py
# Select option 1 (Emergency Response)
# Should work without errors!
```

---

## Cost Breakdown

### Google Gemini (FREE)
- **Setup cost:** $0
- **Per run:** $0
- **Monthly:** $0
- **Total:** $0 🎉

### Ollama (FREE)
- **Setup cost:** $0
- **Per run:** $0 (uses your electricity ≈$0.01)
- **Monthly:** $0
- **Total:** $0 🎉

### OpenAI GPT-4 (For comparison)
- **Setup cost:** $0
- **Per run:** $1.50 - $2.50
- **Monthly:** $50-100 if used regularly
- **Total:** 💰💰💰

---

## Which Should You Choose?

### Choose **Google Gemini** if:
- ✅ You want the easiest setup
- ✅ You have internet connection
- ✅ You want fast responses
- ✅ You're demoing to others

### Choose **Ollama** if:
- ✅ You want complete privacy
- ✅ You don't want to depend on external APIs
- ✅ You have a decent computer
- ✅ You're okay with slower responses

### Choose **OpenAI** if:
- ✅ You have a budget for API calls
- ✅ You need the absolute best quality
- ✅ You're willing to pay for convenience

---

## Switching Between Providers

You can easily switch! Just edit `.env`:

```env
# Use Gemini (free, cloud)
LLM_PROVIDER=gemini
GOOGLE_API_KEY=your-key

# OR use Ollama (free, local)
LLM_PROVIDER=ollama
OLLAMA_MODEL=llama2

# OR use OpenAI (paid, cloud)
LLM_PROVIDER=openai
OPENAI_API_KEY=sk-your-key
```

No code changes needed! 🎯

---

## Pro Tips for FREE Usage

### Google Gemini:
1. **Rate Limits:** 60 requests/minute is plenty for our system
2. **Quality:** Nearly as good as GPT-4 for most tasks
3. **Speed:** Very fast responses
4. **Reliability:** Google's infrastructure is rock solid

### Ollama:
1. **First run is slow:** Model needs to load into memory
2. **Keep it running:** Leave `ollama serve` running in background
3. **RAM matters:** Close other apps for better performance
4. **Model choice:**
   - Mistral = Fastest
   - Llama2 = Balanced
   - Llama3 = Best quality

---

## Getting Help

### Google Gemini
- Docs: [ai.google.dev](https://ai.google.dev)
- Get API key: [makersuite.google.com/app/apikey](https://makersuite.google.com/app/apikey)

### Ollama
- Docs: [ollama.ai](https://ollama.ai)
- Models: [ollama.ai/library](https://ollama.ai/library)
- Discord: [discord.gg/ollama](https://discord.gg/ollama)

---

## You're All Set! 🎉

You now have a production-ready, multi-agent AI system running **completely FREE**.

Next steps:
1. Run `python main.py`
2. Try both example scenarios
3. Customize for your own use cases
4. Add it to your resume/portfolio
5. Demo it in interviews

Good luck with your job hunt! 🚀

---

## Interview Talking Points

When discussing why you used free LLMs:

**Good answer:**
> "I architected the system to be provider-agnostic, supporting OpenAI, Google Gemini, and Ollama. This demonstrates flexibility and cost-consciousness. For development, I use Gemini's free tier, but the system can easily switch to GPT-4 for production workloads. This approach reduces development costs while maintaining production-ready architecture."

**Shows:**
- Cost awareness
- Architectural flexibility
- Production readiness
- Smart engineering decisions
