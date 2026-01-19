# Agentic AI System - Frontend

Beautiful Next.js dashboard for the Agentic AI System.

## Quick Start

```bash
# Install dependencies
npm install

# Run development server
npm run dev

# Open browser
http://localhost:3000
```

## Make Sure Backend is Running!

The frontend needs the backend API to work.

In another terminal:
```bash
cd ..
python api_server.py
```

Backend will run on: http://localhost:8000

## Development

```bash
# Development server with hot reload
npm run dev

# Build for production
npm run build

# Run production build
npm start
```

## Project Structure

```
frontend/
├── app/
│   ├── page.tsx       # Main dashboard
│   ├── layout.tsx     # App layout
│   └── globals.css    # Global styles
├── package.json       # Dependencies
├── tsconfig.json      # TypeScript config
└── tailwind.config.ts # Tailwind CSS config
```

## Technologies

- **Next.js 14** - React framework
- **TypeScript** - Type safety
- **Tailwind CSS** - Styling
- **Axios** - HTTP client
- **Lucide React** - Icons

## Customization

### Change Colors

Edit `tailwind.config.ts`:
```typescript
theme: {
  extend: {
    colors: {
      primary: {
        500: '#3b82f6', // Change this
      },
    },
  },
}
```

### Add Features

Edit `app/page.tsx` to add:
- More visualizations
- Export buttons
- Custom scenarios
- Charts and graphs

## Environment

The frontend expects the backend API at:
```
http://localhost:8000
```

To change this, edit `app/page.tsx`:
```typescript
const API_URL = 'http://your-backend-url'
```

## Deployment

### Vercel (Recommended)

```bash
vercel deploy
```

### Build Manually

```bash
npm run build
npm start
```

## Need Help?

See the main documentation:
- [FRONTEND_SETUP.md](../FRONTEND_SETUP.md)
- [FULLSTACK_README.md](../FULLSTACK_README.md)
