# Get Hired

Get Hired is your career companion, using AI to polish your CV, guide your cover letters, and give you the confidence to stand out and secure the job you deserve.

The app analyzes your CV against a job posting, scores how well you match, suggests improvements, and drafts a tailored cover letter.

---

## Features

* **Upload your CV (PDF or DOCX)**
  Import your CV in common formats for analysis.

* **Provide a job link or manual entry**
  Paste a link to a job posting (LinkedIn, Indeed) or manually enter the job details.

* **ATS compatibility scoring**
  Get a detailed score showing how closely your CV matches ATS requirements.

* **Keyword and skill gap analysis**
  Identify missing or weak skills compared to the posting and get actionable advice.

* **Automated CV improvement**
  Receive an enhanced version of your CV with better phrasing and alignment.

* **AI-generated cover letter**
  Instantly create a tailored cover letter highlighting your strengths for the role.

---

## Tech Stack

### Backend
- **Python 3.12+** - Core backend language
- **FastAPI** - Modern API framework with automatic documentation
- **pypdf** - PDF parsing and text extraction
- **Google Gemini AI** - CV analysis and content generation
- **BeautifulSoup** - Web scraping for job postings
- **Uvicorn** - ASGI server

### Frontend
- **React 18** - Modern UI library
- **Vite** - Fast build tool and dev server
- **Axios** - HTTP client for API communication
- **React Dropzone** - Drag-and-drop file uploads

### Architecture
```
get-hired/
├── frontend/          # React + Vite frontend application
├── api/              # FastAPI backend server
├── src/              # Core Python modules (CV processing, AI tools)
├── userdata/         # Generated files and analysis results
└── docs/             # Documentation files
```

---

## Quick Start

### Prerequisites
- **Node.js 18+** and npm
- **Python 3.12+**
- **Gemini API key** ([Get one here](https://aistudio.google.com/apikey))

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/keammakola/get-hired.git
   cd get-hired
   ```

2. **Set up environment variables**
   ```bash
   cp .env.example .env
   # Edit .env and add your GEMINI_API_KEY
   ```

3. **Install Python dependencies**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

4. **Install frontend dependencies**
   ```bash
   cd frontend
   npm install
   cd ..
   ```

### Running the Application

#### Option 1: Run Everything (Recommended)
Use the provided start script:
```bash
./start.sh
```

This starts both the backend API (port 8000) and frontend (port 5173).

#### Option 2: Run Separately

**Backend API:**
```bash
cd api
python main.py
```

**Frontend:**
```bash
cd frontend
npm run dev
```

### Access the Application
- **Frontend UI**: http://localhost:5173
- **Backend API**: http://localhost:8000
- **API Documentation**: http://localhost:8000/docs

---

## Usage Guide

### Step 1: Job Details
- Choose to paste a job link or manually enter the job description
- Provide company name and position details

### Step 2: Upload CV
- Drag and drop your CV (PDF or DOCX) or browse to select
- Alternatively, create a new CV from scratch (guided process)

### Step 3: Analysis & Results
- View your ATS compatibility score
- Review strengths, weaknesses, and recommendations
- Get your CV automatically improved
- Generate a tailored cover letter
- Download all documents in Markdown format

---

## Project Structure

```
get-hired/
├── frontend/
│   ├── src/
│   │   ├── components/       # React components
│   │   │   ├── JobInput.jsx
│   │   │   ├── CVUpload.jsx
│   │   │   └── Analysis.jsx
│   │   ├── api/
│   │   │   └── backend.js    # API service layer
│   │   ├── App.jsx           # Main app component
│   │   └── main.jsx          # Entry point
│   ├── public/               # Static assets
│   └── package.json
├── api/
│   └── main.py               # FastAPI application
├── src/
│   ├── main.py               # CLI version (original)
│   ├── tools.py              # CV processing utilities
│   ├── job_collector.py      # Job scraping
│   ├── cv_collector.py       # CV creation wizard
│   └── user_details.py       # User info management
├── userdata/                 # Generated files
│   ├── cv/                   # Processed CVs
│   ├── jobs/                 # Job postings
│   ├── ai_analysis/          # Analysis reports
│   └── final docs/           # Output documents
├── requirements.txt          # Python dependencies
├── rubric.md                 # ATS scoring rubric
├── start.sh                  # Startup script
├── FRONTEND_SETUP.md         # Frontend documentation
├── API_DOCUMENTATION.md      # API reference
└── README.md
```

---

## Documentation

- **[Frontend Setup Guide](FRONTEND_SETUP.md)** - Detailed frontend documentation
- **[API Documentation](API_DOCUMENTATION.md)** - Complete API reference
- **[Sprint 1 MVP Documentation](SPRINT1_MVP_BACKEND.md)** - Backend implementation details

---

## Development

### Backend Development
```bash
cd api
uvicorn main:app --reload
```

### Frontend Development
```bash
cd frontend
npm run dev
```

### Running Tests
```bash
pytest
```

### Building for Production
```bash
cd frontend
npm run build
```

The production build will be in `frontend/dist/`.

---

## Features in Detail

### ATS Compatibility Analysis
Uses a comprehensive 15-point rubric covering:
- File format compatibility
- Text-based content parsing
- Keyword optimization
- Standard section headings
- Font and typography
- And more...

### AI-Powered Improvements
- Rewording for better ATS compatibility
- Keyword optimization
- Structure and formatting enhancements
- Professional tone adjustments

### Cover Letter Generation
- Tailored to specific job requirements
- Highlights relevant experience
- Professional formatting
- Ready to use

---

## Roadmap

### Completed
- Backend CV processing and analysis
- AI integration with Google Gemini
- Modern React frontend with step-by-step workflow
- FastAPI REST API
- File upload handling
- Job posting scraping

### In Progress
- Enhanced job scraping (LinkedIn, Indeed support)
- User authentication
- CV history and version management

### Planned
- Multiple job comparison
- Export to PDF, DOCX formats
- Real-time collaboration
- Mobile app
- Database integration (PostgreSQL/Supabase)
- Background task processing (Celery + Redis)
- Docker containerization

---

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

---

## License

This project is licensed under the Apache License 2.0 - see the [LICENSE](LICENSE) file for details.

---

## Support

If you encounter any issues or have questions, please open an issue on GitHub.

---

## Acknowledgments

- Google Gemini AI for powering the analysis
- FastAPI for the excellent API framework
- React and Vite for modern frontend development
- The open-source community for amazing tools and libraries
