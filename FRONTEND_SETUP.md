# Frontend Setup Guide

## Overview
The frontend is built with React + Vite and provides a modern, intuitive interface for the Get-Hired CV analysis application.

## Architecture

### Technology Stack
- **React 18** - UI framework
- **Vite** - Build tool and dev server
- **Axios** - HTTP client for API calls
- **React Dropzone** - File upload component

### Project Structure
```
frontend/
├── src/
│   ├── components/
│   │   ├── JobInput.jsx       # Step 1: Job details input
│   │   ├── JobInput.css
│   │   ├── CVUpload.jsx        # Step 2: CV upload
│   │   ├── CVUpload.css
│   │   ├── Analysis.jsx        # Step 3: Results and actions
│   │   └── Analysis.css
│   ├── api/
│   │   └── backend.js          # API service layer
│   ├── App.jsx                 # Main application component
│   ├── App.css
│   ├── main.jsx                # Entry point
│   └── index.css               # Global styles
├── public/                     # Static assets
├── .env                        # Environment variables
└── package.json
```

## Installation

### Prerequisites
- Node.js 18+ and npm
- Python 3.12+ with requirements installed
- Gemini API key in `.env` file

### Install Dependencies
```bash
cd frontend
npm install
```

## Running the Application

### Option 1: Run Everything (Recommended)
Use the provided start script from the project root:
```bash
./start.sh
```

This will start both the backend API and frontend dev server.

### Option 2: Run Frontend Only
```bash
cd frontend
npm run dev
```

Backend must be running separately:
```bash
cd api
python main.py
```

### Access Points
- **Frontend**: http://localhost:5173
- **Backend API**: http://localhost:8000
- **API Docs**: http://localhost:8000/docs

## Features

### 1. Job Input (Step 1)
- Two input methods:
  - **Job Link**: Paste URL from LinkedIn, Indeed, etc.
  - **Manual Entry**: Company name + job description text
- Form validation
- Clean, intuitive UI

### 2. CV Upload (Step 2)
- Two upload methods:
  - **File Upload**: Drag-and-drop or click to browse (PDF/DOCX)
  - **Create New**: Guided CV creation process
- File type validation
- Visual feedback for uploaded files
- Back navigation

### 3. Analysis & Results (Step 3)
- **ATS Compatibility Score**: Visual circular progress indicator
- **Analysis Breakdown**:
  - What's Great (strengths)
  - What's Lacking (weaknesses)
  - Recommended Actions
- **Automated CV Improvement**: One-click enhancement
- **Cover Letter Generation**: Tailored to the job
- **Download Options**: Export improved CV and cover letter
- **Reset**: Start new analysis

## Design System

### Color Palette
- **Primary Gradient**: Purple (#667eea) to Violet (#764ba2)
- **Success**: Green (#10b981)
- **Warning**: Orange (#f59e0b)
- **Error**: Red (#ef4444)
- **Neutral**: Gray scale

### Layout
- Responsive design with mobile-first approach
- Glassmorphism effects on header
- Card-based content sections
- Consistent 8px spacing system
- Professional transitions and hover states

### Typography
- System fonts for optimal performance
- Clear hierarchy with weight variations
- Readable line-height (1.5 for body, 1.2 for headings)

## API Integration

### Backend Service (`src/api/backend.js`)
All API calls are centralized in the backend service:

```javascript
import { uploadCV, analyzeCV, improveCV, generateCoverLetter } from './api/backend'
```

### Environment Configuration
Create `.env` file in frontend directory:
```
VITE_API_URL=http://localhost:8000
```

## Development

### Available Scripts
- `npm run dev` - Start development server
- `npm run build` - Build for production
- `npm run preview` - Preview production build
- `npm run lint` - Run ESLint

### Adding New Features
1. Create component in `src/components/`
2. Add corresponding CSS file
3. Import and use in `App.jsx`
4. Add API methods to `src/api/backend.js` if needed

### Code Style
- Functional components with hooks
- Consistent naming conventions
- Component-scoped CSS files
- Clear prop types and documentation

## Production Build

### Build the Frontend
```bash
cd frontend
npm run build
```

### Preview Production Build
```bash
npm run preview
```

The build output will be in the `dist/` directory.

### Deployment Considerations
- Set production `VITE_API_URL` in environment
- Ensure CORS is properly configured on backend
- Optimize images and assets
- Enable compression
- Configure proper caching headers

## Troubleshooting

### Common Issues

**Frontend can't connect to backend**
- Verify backend is running on port 8000
- Check `.env` file has correct `VITE_API_URL`
- Ensure CORS is enabled in FastAPI

**File upload fails**
- Check file size limits
- Verify file type (PDF/DOCX only)
- Ensure backend has write permissions

**Build errors**
- Clear `node_modules` and reinstall: `rm -rf node_modules && npm install`
- Check Node.js version: `node --version` (should be 18+)
- Clear cache: `npm cache clean --force`

## Future Enhancements
- User authentication
- CV history and version management
- Multiple job comparison
- Real-time collaboration
- Export to multiple formats
- Mobile app version
