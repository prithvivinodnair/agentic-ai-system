# Frontend Setup Guide - Beautiful Web Interface

Your Agentic AI System now has a beautiful web-based frontend! 🎨

## What You Get

- ✨ Modern, responsive web interface
- 🎯 Real-time workflow progress tracking
- 📊 Beautiful visualization of results
- 🌙 Dark mode support
- 📱 Mobile-friendly design
- ⚡ Built with Next.js + TypeScript + Tailwind CSS

---

## Quick Start (5 Minutes)

### Step 1: Install Node.js (if not installed)

**Windows:**
Download from: https://nodejs.org/
(Choose LTS version)

**Mac:**
```bash
brew install node
```

**Verify installation:**
```bash
node --version
npm --version
```

### Step 2: Install Frontend Dependencies

```bash
cd frontend
npm install
```

This will install:
- Next.js (React framework)
- Tailwind CSS (styling)
- Axios (API calls)
- TypeScript
- Icons and charts

### Step 3: Start the Backend API

Open a **NEW terminal** and run:

```bash
# Make sure you're in the project root
cd "c:\Users\Prithvi Nair\OneDrive\Desktop\Agentic AI"

# Activate virtual environment
.venv\Scripts\Activate.ps1

# Start the API server
python api_server.py
```

You should see:
```
🚀 Starting Agentic AI System API Server
📡 LLM Provider: gemini
🌐 Server will be available at: http://localhost:8000
📚 API Documentation: http://localhost:8000/docs
```

**Keep this terminal running!**

### Step 4: Start the Frontend

Open **ANOTHER terminal**:

```bash
cd frontend
npm run dev
```

You should see:
```
- ready started server on 0.0.0.0:3000, url: http://localhost:3000
```

### Step 5: Open in Browser

Go to: **http://localhost:3000**

🎉 You should see the beautiful dashboard!

---

## Using the Interface

### 1. Select a Scenario

Choose from:
- **Emergency Resource Allocation** - Hurricane disaster response
- **Infrastructure Investment Planning** - Long-term budget allocation

### 2. Run Analysis

Click "Run Analysis" button

### 3. Watch Progress

See real-time updates as the agents work:
- Data Ingestion
- Analysis
- Reasoning
- Decision Making
- Execution Planning

### 4. View Results

Beautiful cards showing:
- ✅ Recommended Decision
- 📊 Confidence Level
- 🎯 Implementation Priority
- 📋 Key Supporting Factors
- 🔢 Next Steps
- ⚠️ Identified Risks

---

## Project Structure

```
frontend/
├── app/
│   ├── page.tsx          # Main dashboard (the UI you see)
│   ├── layout.tsx        # App layout
│   └── globals.css       # Global styles
├── package.json          # Dependencies
├── tsconfig.json         # TypeScript config
├── tailwind.config.ts    # Tailwind CSS config
└── next.config.js        # Next.js config
```

---

## Customization

### Change Colors

Edit `frontend/tailwind.config.ts`:

```typescript
colors: {
  primary: {
    500: '#3b82f6',  // Change this!
    600: '#2563eb',
  },
}
```

### Add New Features

Edit `frontend/app/page.tsx` to:
- Add more visualization
- Show different data
- Add charts with Recharts
- Add export buttons

### Change API URL

If your backend runs on a different port:

Edit `frontend/app/page.tsx`:
```typescript
const API_URL = 'http://localhost:8000'  // Change port if needed
```

---

## Running in Production

### Build the Frontend

```bash
cd frontend
npm run build
npm start
```

This creates an optimized production build.

### Deploy Options

**Vercel (Easiest - FREE):**
1. Push code to GitHub
2. Go to vercel.com
3. Import your repository
4. Deploy! (takes 2 minutes)

**Netlify (Also FREE):**
Similar to Vercel

**Your Own Server:**
```bash
npm run build
npm start
# Runs on port 3000
```

---

## Troubleshooting

### Port Already in Use

**Frontend (3000):**
```bash
# Kill process on port 3000
# Windows:
netstat -ano | findstr :3000
taskkill /PID <PID> /F

# Mac/Linux:
lsof -ti:3000 | xargs kill
```

**Backend (8000):**
```bash
# Kill process on port 8000
# Windows:
netstat -ano | findstr :8000
taskkill /PID <PID> /F

# Mac/Linux:
lsof -ti:8000 | xargs kill
```

### CORS Errors

Make sure backend is running on `localhost:8000`

Check `api_server.py` has:
```python
allow_origins=["*"]
```

### Cannot Connect to API

1. Check backend is running: http://localhost:8000
2. Check API docs: http://localhost:8000/docs
3. Verify `.env` has your Gemini API key

### npm install Fails

```bash
# Clear cache
npm cache clean --force

# Delete node_modules
rm -rf node_modules package-lock.json

# Reinstall
npm install
```

---

## API Documentation

Your backend automatically generates API docs!

Go to: **http://localhost:8000/docs**

You'll see:
- All available endpoints
- Request/response schemas
- Try it out feature

### Available Endpoints

```
GET  /                    # Health check
GET  /scenarios           # List available scenarios
POST /workflow/run        # Start a workflow
GET  /workflow/{id}       # Get workflow status
GET  /workflows           # List all workflows
DELETE /workflow/{id}     # Delete workflow
```

---

## Development Workflow

### Running Both Servers

**Terminal 1 (Backend):**
```bash
cd "c:\Users\Prithvi Nair\OneDrive\Desktop\Agentic AI"
.venv\Scripts\Activate.ps1
python api_server.py
```

**Terminal 2 (Frontend):**
```bash
cd frontend
npm run dev
```

**Browser:**
- Frontend: http://localhost:3000
- Backend API Docs: http://localhost:8000/docs

### Making Changes

**Frontend changes:**
- Edit files in `frontend/app/`
- Hot reload automatically updates browser
- No restart needed!

**Backend changes:**
- Edit `api_server.py` or agents
- Restart backend: Ctrl+C and run again

---

## Adding More Features

### 1. Add Charts

Install Recharts (already in package.json):

```tsx
import { LineChart, Line, XAxis, YAxis } from 'recharts'

<LineChart data={data}>
  <Line type="monotone" dataKey="value" stroke="#8884d8" />
  <XAxis dataKey="name" />
  <YAxis />
</LineChart>
```

### 2. Add Export to PDF

```bash
npm install jspdf
```

```tsx
import jsPDF from 'jspdf'

const exportPDF = () => {
  const doc = new jsPDF()
  doc.text('Decision Report', 10, 10)
  doc.save('report.pdf')
}
```

### 3. Add User Authentication

Use NextAuth.js:
```bash
npm install next-auth
```

### 4. Add Database

Use Prisma + PostgreSQL:
```bash
npm install prisma @prisma/client
```

---

## Performance Tips

### Frontend Optimization

1. **Use loading states**
   - Shows users something is happening
   - Prevents confusion

2. **Debounce API calls**
   - Don't call API on every keystroke
   - Wait for user to finish typing

3. **Cache results**
   - Store completed workflows
   - Don't re-fetch unnecessarily

### Backend Optimization

1. **Add caching** (Redis)
2. **Use database** (instead of in-memory storage)
3. **Add rate limiting**
4. **Implement pagination**

---

## Tech Stack

### Frontend
- **Next.js 14** - React framework
- **TypeScript** - Type safety
- **Tailwind CSS** - Styling
- **Axios** - HTTP client
- **Lucide React** - Beautiful icons

### Backend
- **FastAPI** - Modern Python API framework
- **Uvicorn** - ASGI server
- **Pydantic** - Data validation
- **CORS** - Cross-origin support

---

## Interview Talking Points

### "I built a full-stack application..."

**Frontend:**
- Modern React with Next.js 14 and TypeScript
- Responsive design with Tailwind CSS
- Real-time progress tracking
- Clean component architecture

**Backend:**
- RESTful API with FastAPI
- Async/await for performance
- Auto-generated API documentation
- CORS-enabled for frontend integration

**Integration:**
- Real-time polling for workflow status
- Clean separation of concerns
- Error handling and loading states
- Production-ready deployment

### "Why this tech stack?"

**Next.js:**
- Server-side rendering for SEO
- File-based routing
- Built-in optimization
- Industry standard

**FastAPI:**
- Automatic API docs
- Type hints with Pydantic
- Async support
- Fast performance

**Tailwind CSS:**
- Rapid development
- Consistent design
- Small bundle size
- Easy customization

---

## What's Next?

### Short-term (Weekend Projects)

- [ ] Add export to PDF/Excel
- [ ] Add charts and visualizations
- [ ] Add workflow history page
- [ ] Add custom scenario builder

### Medium-term (Week Projects)

- [ ] User authentication
- [ ] Save workflows to database
- [ ] Add comparison of multiple runs
- [ ] Email notifications

### Long-term (Production)

- [ ] Deploy to Vercel/Netlify
- [ ] Add monitoring (Sentry)
- [ ] Add analytics
- [ ] Multi-user support
- [ ] Role-based access control

---

## 🎉 You're Done!

You now have a **production-ready full-stack AI application** with:

✅ Beautiful web interface
✅ Real-time progress tracking
✅ Professional visualization
✅ RESTful API with docs
✅ Modern tech stack
✅ Ready to demo!

**Perfect for:**
- Portfolio showcase
- Interview demos
- Client presentations
- Further development

---

## Quick Reference

**Start Everything:**
```bash
# Terminal 1: Backend
python api_server.py

# Terminal 2: Frontend
cd frontend && npm run dev
```

**URLs:**
- Frontend: http://localhost:3000
- Backend API: http://localhost:8000
- API Docs: http://localhost:8000/docs

**Stop Everything:**
- Ctrl+C in both terminals

---

Good luck with your demos! 🚀
