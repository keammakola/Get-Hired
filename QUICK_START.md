# Get-Hired Quick Start Guide

## 1-Minute Setup

### Prerequisites Check
```bash
node --version    # Should be 18+
python --version  # Should be 3.12+
```

### Installation
```bash
cd get-hired
cp .env.example .env
# Add your GEMINI_API_KEY to .env

pip install -r requirements.txt
cd frontend && npm install && cd ..
```

### Run Application
```bash
./start.sh
```

Visit **http://localhost:5173**

---

## Manual Start

### Terminal 1 - Backend
```bash
cd api
python main.py
```

### Terminal 2 - Frontend
```bash
cd frontend
npm run dev
```

---

## Quick Reference

### URLs
| Service | URL |
|---------|-----|
| Frontend | http://localhost:5173 |
| Backend | http://localhost:8000 |
| API Docs | http://localhost:8000/docs |

### Key Files
| File | Purpose |
|------|---------|
| `frontend/src/App.jsx` | Main application |
| `api/main.py` | Backend API |
| `src/tools.py` | CV processing |
| `.env` | API keys |

### Commands
| Command | Action |
|---------|--------|
| `./start.sh` | Start everything |
| `cd frontend && npm run dev` | Start frontend |
| `cd api && python main.py` | Start backend |
| `cd frontend && npm run build` | Build for production |

---

## User Workflow

1. **Job Details** → Paste link or enter manually
2. **Upload CV** → Drag PDF file
3. **View Results** → See score and analysis
4. **Improve CV** → Click to enhance
5. **Cover Letter** → Generate automatically
6. **Download** → Export documents

---

## Troubleshooting

### Backend won't start
- Check `GEMINI_API_KEY` in `.env`
- Install dependencies: `pip install -r requirements.txt`

### Frontend won't start
- Install dependencies: `cd frontend && npm install`
- Check Node.js version: `node --version`

### API connection fails
- Verify backend is running on port 8000
- Check `.env` file in frontend directory

---

## Documentation

- **Full Guide**: [README.md](README.md)
- **Frontend Details**: [FRONTEND_SETUP.md](FRONTEND_SETUP.md)
- **API Reference**: [API_DOCUMENTATION.md](API_DOCUMENTATION.md)
- **Architecture**: [ARCHITECTURE.md](ARCHITECTURE.md)

---

## Support

Issues? Check the documentation or review error logs in terminal.
