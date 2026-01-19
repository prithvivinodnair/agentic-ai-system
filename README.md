# 🤖 Agentic AI System for National-Scale Operational Decisions

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![Next.js](https://img.shields.io/badge/Next.js-14.0-black.svg)](https://nextjs.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.109-green.svg)](https://fastapi.tiangolo.com/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

A production-ready **full-stack multi-agent GenAI system** that automates complex operational decision-making at national scale by ingesting unstructured data, reasoning across constraints, and executing real-world workflows.

---

## ✨ Features

### 🎨 **Beautiful Web Interface**
- Modern Next.js dashboard with real-time progress tracking
- Interactive data visualization
- Dark mode support
- Responsive design

### 🤖 **Multi-Agent Architecture**
- **5 Specialized AI Agents** working together:
  - Data Ingestion → Analysis → Reasoning → Decision → Execution
- Orchestrator pattern for coordinated workflows
- Async execution for performance

### 🧠 **Intelligent Analysis**
- Handles unstructured data (PDFs, CSVs, text, APIs)
- Works with missing/messy data
- Constraint-based reasoning
- Multi-criteria decision analysis

### 🎯 **Production Ready**
- RESTful API with auto-generated docs
- Comprehensive error handling
- Provider-agnostic (OpenAI, Gemini, Ollama)
- Runs **100% FREE** with Google Gemini

---

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- Node.js 16+ (for frontend)
- Google Gemini API key ([Get it FREE](https://makersuite.google.com/app/apikey))

### Installation

```bash
# Clone the repository
git clone https://github.com/YOUR_USERNAME/agentic-ai-system.git
cd agentic-ai-system

# Install Python dependencies
pip install -r requirements.txt

# Install frontend dependencies
cd frontend
npm install
cd ..

# Configure environment
cp .env.example .env
# Edit .env and add your GOOGLE_API_KEY
```

### Run the System

**Option 1: Full-Stack (Web Interface)**

```bash
# Terminal 1: Start backend
python api_server.py

# Terminal 2: Start frontend
cd frontend
npm run dev

# Open browser: http://localhost:3000
```

**Option 2: CLI Version**

```bash
python main.py
```

---

## 📊 Demo

### Select a Scenario
<img src="https://via.placeholder.com/600x300/3B82F6/FFFFFF?text=Scenario+Selection" alt="Scenario Selection" width="600"/>

### Watch AI Agents Work
<img src="https://via.placeholder.com/600x300/10B981/FFFFFF?text=AI+Agents+Working" alt="Agents" width="600"/>

### View Results
<img src="https://via.placeholder.com/600x300/8B5CF6/FFFFFF?text=Executive+Summary" alt="Results" width="600"/>

---

## 🏗️ Architecture

```
┌─────────────────────────────────────────┐
│         Frontend (Next.js)              │
│    React • TypeScript • Tailwind        │
└─────────────┬───────────────────────────┘
              │ REST API
┌─────────────▼───────────────────────────┐
│      Backend API (FastAPI)              │
│    Async • Background Tasks             │
└─────────────┬───────────────────────────┘
              │
┌─────────────▼───────────────────────────┐
│    Multi-Agent Orchestrator             │
│                                         │
│  Data Ingestion → Analysis → Reasoning  │
│       → Decision → Execution            │
└─────────────┬───────────────────────────┘
              │
┌─────────────▼───────────────────────────┐
│       LLM Provider (Gemini/GPT-4)       │
└─────────────────────────────────────────┘
```

---

## 🛠️ Technology Stack

### Frontend
- **Next.js 14** - React framework with SSR
- **TypeScript** - Type-safe development
- **Tailwind CSS** - Utility-first styling
- **Axios** - HTTP client
- **Lucide Icons** - Beautiful icons

### Backend
- **FastAPI** - Modern Python web framework
- **Pydantic** - Data validation
- **Uvicorn** - ASGI server
- **AsyncIO** - Async processing

### AI/ML
- **LangChain** - Agent framework
- **OpenAI/Gemini APIs** - LLM providers
- **Multi-Agent System** - Specialized agents

---

## 📁 Project Structure

```
agentic-ai-system/
├── agents/                  # AI agents
│   ├── data_ingestion_agent.py
│   ├── analysis_agent.py
│   ├── reasoning_agent.py
│   ├── decision_agent.py
│   └── execution_agent.py
├── frontend/               # Next.js app
│   ├── app/
│   │   ├── page.tsx       # Main dashboard
│   │   └── layout.tsx
│   └── package.json
├── examples/              # Sample data
│   ├── disaster_report.txt
│   └── sample_data.json
├── api_server.py         # FastAPI backend
├── orchestrator.py       # Agent coordinator
├── llm_client.py        # Universal LLM client
├── main.py              # CLI version
├── config.py            # Configuration
└── requirements.txt     # Python deps
```

---

## 🎯 Use Cases

This system can be applied to:

- 🚨 **Emergency Management**: Disaster response, resource allocation
- 🏗️ **Infrastructure Planning**: Long-term investment decisions
- 🏥 **Public Health**: Pandemic response, vaccine distribution
- 📊 **Policy Analysis**: Economic policy evaluation
- 💰 **Budget Allocation**: Multi-sector resource optimization
- 🎯 **Strategic Planning**: Multi-year operational planning

---

## 🧪 Testing

```bash
# Test dynamic output generation
python test_dynamic_output.py

# Test messy data handling
python test_messy_data.py

# Run backend tests
pytest tests/
```

---

## 📖 Documentation

- **[COMPLETE_GUIDE.md](COMPLETE_GUIDE.md)** - Complete overview
- **[QUICKSTART.md](QUICKSTART.md)** - 5-minute setup
- **[FREE_SETUP.md](FREE_SETUP.md)** - Free LLM options
- **[FULLSTACK_README.md](FULLSTACK_README.md)** - Full-stack guide
- **[DEMO_GUIDE.md](DEMO_GUIDE.md)** - How to demo
- **[API Docs](http://localhost:8000/docs)** - Interactive API docs (when server running)

---

## 🌟 Key Features

### Handles Real-World Data
- ✅ Works with messy, incomplete data
- ✅ Processes unstructured text
- ✅ Handles contradictory information
- ✅ Adjusts confidence based on data quality

### Intelligent Decision Making
- ✅ Multi-criteria analysis
- ✅ Constraint-based reasoning
- ✅ Risk identification
- ✅ Actionable recommendations

### Production Ready
- ✅ Comprehensive error handling
- ✅ Auto-generated API docs
- ✅ Real-time progress tracking
- ✅ Background task processing

---

## 💰 Cost

- **Development**: $0 (using Gemini free tier)
- **Production**: ~$2/analysis with GPT-4, or FREE with Gemini
- **Deployment**: FREE (Vercel + Railway/Render)

---

## 🚀 Deployment

### Frontend (Vercel)

```bash
cd frontend
vercel deploy
```

### Backend (Railway/Render)

1. Push to GitHub
2. Connect repository on railway.app
3. Add environment variable: `GOOGLE_API_KEY`
4. Deploy!

---

## 📈 Roadmap

- [ ] User authentication (NextAuth.js)
- [ ] Database persistence (PostgreSQL)
- [ ] Export to PDF/Excel
- [ ] Charts and visualizations
- [ ] Custom scenario builder
- [ ] Webhook integrations
- [ ] Multi-user support

---

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 👤 Author

**Prithvi Nair**

- 🎓 MS in Data Science, University of Texas at Arlington
- 📧 Email: prithvi.nair@gmail.com
- 💼 LinkedIn: [linkedin.com/in/prithvi-vinod-nair-58751323b](https://www.linkedin.com/in/prithvi-vinod-nair-58751323b/)
- 🐙 GitHub: [@prithvivinodnair](https://github.com/prithvivinodnair)

---

## 🙏 Acknowledgments

- Built with [FastAPI](https://fastapi.tiangolo.com/)
- Powered by [Google Gemini](https://ai.google.dev/)
- UI components from [Tailwind CSS](https://tailwindcss.com/)
- Icons by [Lucide](https://lucide.dev/)

---

## ⭐ Show Your Support

If this project helped you, please give it a ⭐️!

---

## 📞 Contact

Have questions? Feel free to reach out!

- Create an [Issue](https://github.com/YOUR_USERNAME/agentic-ai-system/issues)
- Email: prithvi.nair@gmail.com
- LinkedIn: [Message me](https://www.linkedin.com/in/prithvi-vinod-nair-58751323b/)

---

**Built with ❤️ by Prithvi Nair**
