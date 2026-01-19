# Complete Setup Guide

## Quick Start (5 minutes)

### Step 1: Install Python Dependencies

```bash
pip install -r requirements.txt
```

### Step 2: Get Your OpenAI API Key

1. Go to [platform.openai.com](https://platform.openai.com)
2. Sign up or log in
3. Navigate to API Keys section
4. Create a new API key
5. Copy the key (starts with `sk-...`)

### Step 3: Configure Environment

```bash
# Create .env file
cp .env.example .env

# Edit .env and add your key
# On Windows: notepad .env
# On Mac/Linux: nano .env
```

Add this line to `.env`:
```
OPENAI_API_KEY=sk-your-actual-key-here
```

### Step 4: Run the System

```bash
python main.py
```

## Detailed Setup

### Python Environment Setup

#### Option 1: Using Virtual Environment (Recommended)

```bash
# Create virtual environment
python -m venv venv

# Activate it
# Windows:
venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

#### Option 2: Using Conda

```bash
# Create conda environment
conda create -n agentic-ai python=3.9

# Activate it
conda activate agentic-ai

# Install dependencies
pip install -r requirements.txt
```

### API Key Options

#### Option 1: OpenAI (Recommended)

**Cost**: ~$0.50-$2.00 per workflow execution with GPT-4
- Best quality results
- Most reliable
- Fastest response times

Get key at: [platform.openai.com](https://platform.openai.com)

```bash
# In .env file:
OPENAI_API_KEY=sk-...
MODEL_NAME=gpt-4-turbo-preview
```

#### Option 2: Google Gemini (Alternative)

**Cost**: Free tier available
- Good quality
- Free tier: 60 requests/minute

Get key at: [makersuite.google.com](https://makersuite.google.com)

```bash
# In .env file:
GOOGLE_API_KEY=...
MODEL_NAME=gemini-pro
```

### Troubleshooting

#### Issue: "Module not found" errors

```bash
# Make sure you're in the right directory
cd "c:\Users\Prithvi Nair\OneDrive\Desktop\Agentic AI"

# Reinstall dependencies
pip install -r requirements.txt --force-reinstall
```

#### Issue: "OpenAI API key not found"

1. Check `.env` file exists in project root
2. Verify API key is correct (no spaces, quotes)
3. Make sure `.env` has this exact format:
   ```
   OPENAI_API_KEY=sk-proj-...
   ```

#### Issue: "Rate limit exceeded"

You're making too many API calls. Wait a minute and try again, or:
```bash
# In .env, add:
MAX_RETRIES=3
TIMEOUT=60
```

#### Issue: Import errors in IDE

Your IDE might not recognize the virtual environment:
1. In VS Code: Press `Ctrl+Shift+P`, type "Python: Select Interpreter"
2. Choose the interpreter from your `venv` folder

## Testing Your Setup

### Test 1: Quick Validation

```bash
python -c "from config import config; config.validate(); print('✓ Configuration valid!')"
```

### Test 2: Simple Agent Test

Create `test_simple.py`:
```python
import asyncio
from agents import DataIngestionAgent

async def test():
    agent = DataIngestionAgent()
    result = await agent.execute({
        "source_type": "text",
        "data": "Test data"
    })
    print(f"Status: {result.status}")
    print("✓ Agents working!")

asyncio.run(test())
```

Run it:
```bash
python test_simple.py
```

### Test 3: Full Workflow Test

```bash
python main.py
# Select option 1 (Emergency Response)
# This will run the complete workflow
```

## Running Your First Workflow

### Example 1: Using Built-in Scenarios

```bash
python main.py
```

Select from the menu:
1. Emergency Resource Allocation - Shows multi-region disaster response
2. Infrastructure Planning - Shows long-term investment decisions

### Example 2: Custom Text Data

Create `run_custom.py`:
```python
import asyncio
from orchestrator import AgenticOrchestrator

async def main():
    scenario = {
        "data_source": {
            "source_type": "text",
            "data": """
            Your unstructured data here...
            Can be reports, analyses, anything!
            """
        },
        "context": "What decision needs to be made?",
        "objectives": [
            "Objective 1",
            "Objective 2"
        ],
        "options": [
            {
                "option_id": "1",
                "name": "First Option",
                "description": "What this option does"
            },
            {
                "option_id": "2",
                "name": "Second Option",
                "description": "Alternative approach"
            }
        ],
        "constraints": {
            "budget": "Your budget constraint",
            "time": "Your time constraint"
        },
        "resources": {},
        "timeline": "30 days"
    }

    orchestrator = AgenticOrchestrator()
    results = await orchestrator.execute_workflow(scenario, verbose=True)

    print(f"\n✓ Workflow complete! ID: {results['workflow_id']}")

asyncio.run(main())
```

Run it:
```bash
python run_custom.py
```

### Example 3: Using File Data

```python
# Use the sample disaster report
scenario = {
    "data_source": {
        "source_type": "file",
        "source_path": "examples/disaster_report.txt"
    },
    # ... rest of configuration
}
```

## Understanding the Output

### Console Output

You'll see:
1. Header with system name
2. Progress for each stage (Ingestion → Analysis → Reasoning → Decision → Execution)
3. ✓ Checkmarks when stages complete
4. Final executive report

### JSON Output Files

Results are saved to files like:
- `emergency_response_decision.json`
- `infrastructure_decision.json`

These contain:
- Complete workflow data
- All agent responses
- Timestamps and metadata
- Decision details and execution plans

### Reading the Results

```python
import json

# Load results
with open('emergency_response_decision.json', 'r') as f:
    results = json.load(f)

# Access decision
decision = results['stages']['decision']['data']['decision']
print(decision['RECOMMENDED DECISION'])
print(decision['CONFIDENCE LEVEL'])
print(decision['NEXT STEPS'])
```

## Performance Tips

### Reduce API Costs

```bash
# In .env:
MODEL_NAME=gpt-3.5-turbo  # Cheaper than GPT-4
TEMPERATURE=0.5            # More focused responses
MAX_TOKENS=1500           # Shorter responses
```

### Speed Up Execution

The system already runs agents in parallel where possible, but you can:
- Use faster models (gpt-3.5-turbo)
- Reduce `MAX_TOKENS` for shorter responses
- Cache API responses (add Redis in future)

### Handle Large Data Files

For files > 10MB:
- Pre-process to extract key sections
- Use data summarization
- Split into multiple smaller files

## Next Steps

1. **Customize for Your Use Case**: Modify the scenarios in `main.py`
2. **Add New Agents**: Extend the `BaseAgent` class
3. **Integrate with Your Data**: Point to your actual data sources
4. **Build an API**: Wrap the orchestrator in FastAPI
5. **Deploy to Cloud**: Use AWS Lambda or Google Cloud Run

## Getting Help

### Common Questions

**Q: How much does it cost to run?**
A: With GPT-4, each workflow costs $0.50-$2.00. With GPT-3.5, it's $0.05-$0.20.

**Q: Can I use this for real decisions?**
A: This is a demo system. Real decisions should include human oversight and domain experts.

**Q: How do I add my own data sources?**
A: Modify the `DataIngestionAgent` to support your data format, or convert your data to CSV/JSON/TXT.

**Q: Can I run this without internet?**
A: No, it requires API access to OpenAI or Google. You could modify it to use local LLMs like Llama.

### Resources

- OpenAI API Docs: [platform.openai.com/docs](https://platform.openai.com/docs)
- LangChain Docs: [python.langchain.com](https://python.langchain.com)
- Rich Library: [rich.readthedocs.io](https://rich.readthedocs.io)

## Interview Preparation

When discussing this project:

### Technical Details You Should Know
1. **Architecture**: Multi-agent orchestrator pattern
2. **Async Execution**: Why agents use `async/await`
3. **LLM Integration**: How prompts are structured for each agent
4. **Error Handling**: Try-except blocks, AgentResponse status codes
5. **Data Flow**: How data passes between agents

### Demo Flow
1. Show the code structure
2. Run a workflow and explain each stage
3. Show the output JSON
4. Explain how to customize for different scenarios

### Extension Ideas to Discuss
1. Adding a database for persistence
2. Building a web UI
3. Integrating real-time data sources
4. Adding human approval gates
5. Scaling to distributed agents

Good luck! 🚀
