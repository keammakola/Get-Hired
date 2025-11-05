# Get-Hired Architecture

## System Overview

Get-Hired is a full-stack web application that helps job seekers optimize their CVs for Applicant Tracking Systems (ATS) and generate tailored cover letters.

## Architecture Diagram

```
┌─────────────────────────────────────────────────────────────────┐
│                          USER INTERFACE                          │
│                     (React + Vite Frontend)                      │
│                      http://localhost:5173                       │
└─────────────────────┬───────────────────────────────────────────┘
                      │
                      │ HTTP REST API
                      │ (Axios)
                      │
┌─────────────────────▼───────────────────────────────────────────┐
│                        API GATEWAY                               │
│                      (FastAPI Backend)                           │
│                      http://localhost:8000                       │
│                                                                  │
│  Endpoints:                                                      │
│  • POST /api/cv/upload                                          │
│  • POST /api/cv/analyze                                         │
│  • POST /api/cv/improve                                         │
│  • POST /api/cover-letter/generate                             │
│  • POST /api/job/scrape                                         │
└─────────────────────┬───────────────────────────────────────────┘
                      │
                      │ Python Modules
                      │
┌─────────────────────▼───────────────────────────────────────────┐
│                      CORE SERVICES                               │
│                    (Python Backend Logic)                        │
│                                                                  │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐        │
│  │  CV Tools    │  │ Job Scraper  │  │ AI Services  │        │
│  │              │  │              │  │              │        │
│  │ • Extract    │  │ • Scrape Web │  │ • Analyze    │        │
│  │ • Score      │  │ • Parse HTML │  │ • Improve    │        │
│  │ • Improve    │  │ • Extract    │  │ • Generate   │        │
│  └──────────────┘  └──────────────┘  └──────────────┘        │
└─────────────────────┬───────────────────────────────────────────┘
                      │
                      │ API Calls
                      │
┌─────────────────────▼───────────────────────────────────────────┐
│                   EXTERNAL SERVICES                              │
│                                                                  │
│  ┌──────────────────────────────────────────────────────────┐ │
│  │              Google Gemini AI API                         │ │
│  │  • CV Analysis                                            │ │
│  │  • Content Generation                                     │ │
│  │  • Text Processing                                        │ │
│  └──────────────────────────────────────────────────────────┘ │
└──────────────────────────────────────────────────────────────────┘
```

## Component Breakdown

### Frontend Layer (React)

**Technology**: React 18 + Vite

**Components**:
1. **App.jsx** - Main application controller
   - Manages application state
   - Handles step navigation
   - Coordinates component communication

2. **JobInput.jsx** - Step 1
   - Job link or manual text input
   - Form validation
   - Data submission to backend

3. **CVUpload.jsx** - Step 2
   - File upload (PDF/DOCX)
   - Drag-and-drop functionality
   - File type validation

4. **Analysis.jsx** - Step 3
   - Display ATS compatibility score
   - Show analysis breakdown
   - Trigger CV improvement
   - Generate cover letter
   - Download documents

**State Management**:
- React hooks (useState, useEffect)
- Props drilling for simple state
- No complex state management needed (small app)

**Styling**:
- Component-scoped CSS files
- Consistent design system
- Responsive breakpoints
- Gradient theme (purple to violet)

### API Layer (FastAPI)

**Technology**: FastAPI + Uvicorn

**Responsibilities**:
- Request routing
- Request validation
- Response formatting
- Error handling
- CORS configuration

**Endpoints**:
```
POST /api/cv/upload          → Upload and extract CV text
POST /api/cv/analyze         → Analyze CV against job
POST /api/cv/improve         → Enhance CV based on analysis
POST /api/cover-letter/generate → Create tailored cover letter
POST /api/job/scrape         → Extract job info from URL
```

**Features**:
- Automatic API documentation (Swagger/ReDoc)
- Request validation with Pydantic
- Async request handling
- File upload support

### Core Services Layer (Python)

**Technology**: Python 3.12+

**Modules**:

1. **tools.py**
   - `cv_extractor()` - Extract text from PDF
   - `cv_scorer()` - Score CV against rubric
   - `cv_improver()` - Generate improved CV
   - `cover_letter()` - Generate cover letter
   - `file_creator()` - Save files to disk

2. **job_collector.py**
   - `job_scraper()` - Scrape job from URL
   - `job_info()` - Process job information
   - `job_name()` - Extract job title

3. **cv_collector.py**
   - `collect_cv_info()` - Interactive CV builder
   - Guided information collection

**Data Flow**:
```
User Input → API → Core Service → AI Processing → Response
```

### External Services

**Google Gemini AI**:
- Model: gemini-2.5-flash
- Used for:
  - CV text extraction and formatting
  - ATS compatibility analysis
  - CV improvement suggestions
  - Cover letter generation

**Authentication**:
- API key stored in `.env`
- Loaded via environment variables

## Data Flow

### 1. Job Analysis Flow
```
User → Frontend (JobInput)
  ↓
  Submit job details
  ↓
Frontend → API (/api/cv/analyze)
  ↓
  Process job data
  ↓
API → Core Services (cv_scorer)
  ↓
  Analyze with rubric
  ↓
Core → Gemini AI
  ↓
  Generate analysis
  ↓
AI → Core → API → Frontend
  ↓
Display results (Analysis component)
```

### 2. CV Upload Flow
```
User drops/selects file
  ↓
Frontend (CVUpload) validates file
  ↓
Submit to API (/api/cv/upload)
  ↓
API extracts text (pypdf)
  ↓
Format with Gemini AI
  ↓
Return formatted text
  ↓
Store in frontend state
```

### 3. CV Improvement Flow
```
User requests improvement
  ↓
Frontend sends CV + analysis report
  ↓
API (/api/cv/improve)
  ↓
Core (cv_improver)
  ↓
Gemini AI generates improved version
  ↓
Return improved CV
  ↓
Frontend displays with download option
```

## File Storage

```
userdata/
├── cv/              # Processed CVs
│   └── cv.md
├── jobs/            # Job postings
│   └── [company-name].md
├── ai_analysis/     # Analysis reports
│   └── cv_score.md
└── final docs/      # Output documents
    └── coverletter.md
```

**Storage Strategy**:
- File-based (no database yet)
- Markdown format for easy editing
- Organized by purpose
- Temporary storage (cleared between sessions)

## Security Considerations

### Current Implementation
- API key stored in environment variables
- CORS enabled for local development
- File type validation on upload
- No authentication system

### Production Requirements
- Restrict CORS to specific domains
- Add user authentication
- Implement rate limiting
- Secure file storage
- HTTPS only
- API key rotation

## Scalability Considerations

### Current Limitations
- Single-threaded Python backend
- File-based storage
- No caching
- Synchronous AI calls

### Future Improvements
- Add Redis for caching
- Implement database (PostgreSQL/Supabase)
- Background job processing (Celery)
- CDN for static assets
- Load balancing
- Horizontal scaling with containers

## Technology Choices

### Why React?
- Modern, well-supported
- Component-based architecture
- Large ecosystem
- Fast development

### Why FastAPI?
- Automatic API documentation
- Fast performance (async)
- Type validation with Pydantic
- Easy to learn and use

### Why Gemini AI?
- Powerful language model
- Good at text analysis
- Reasonable pricing
- Easy integration

### Why File-based Storage?
- Simple MVP approach
- No database setup required
- Easy to debug
- Fast iteration

## Development Workflow

```
1. Developer makes changes
   ↓
2. Frontend hot-reloads (Vite)
   ↓
3. Backend reloads (--reload flag)
   ↓
4. Test in browser
   ↓
5. Commit changes
```

## Deployment Strategy

### Development
- Frontend: `npm run dev` (port 5173)
- Backend: `python api/main.py` (port 8000)

### Production
- Frontend: Build static files, serve via Nginx/CDN
- Backend: Containerize, deploy to cloud (AWS/GCP/Azure)
- Database: Migrate to PostgreSQL/Supabase
- Environment: Use production secrets manager

## Monitoring and Logging

### Current
- Console logging
- Browser DevTools
- FastAPI automatic logging

### Future
- Centralized logging (ELK stack)
- Error tracking (Sentry)
- Performance monitoring
- Usage analytics

## Testing Strategy

### Current
- pytest for backend (Sprint 1)
- Manual testing for frontend

### Future
- Jest for React components
- Cypress for E2E tests
- API integration tests
- Load testing
- Security audits
