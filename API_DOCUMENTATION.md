# Get-Hired API Documentation

## Overview
FastAPI backend that connects the React frontend with the Python CV analysis tools.

## Base URL
```
http://localhost:8000
```

## Endpoints

### 1. Health Check
**GET** `/`

Check if API is running.

**Response**
```json
{
  "message": "Get Hired API"
}
```

---

### 2. Upload CV
**POST** `/api/cv/upload`

Upload and extract text from CV file.

**Request**
- Content-Type: `multipart/form-data`
- Body: Form data with `cv` file (PDF or DOCX)

**Response**
```json
{
  "cv_text": "Extracted and formatted CV text..."
}
```

**Errors**
- `400`: Invalid file type
- `500`: Processing error

---

### 3. Analyze CV
**POST** `/api/cv/analyze`

Analyze CV against job requirements using ATS rubric.

**Request Body**
```json
{
  "cv": "CV text content...",
  "job": {
    "method": "text",
    "companyName": "Google",
    "text": "Job description...",
    "link": "https://..."
  }
}
```

**Response**
```json
{
  "report": "Detailed analysis report...",
  "score": 75,
  "compatible": true
}
```

---

### 4. Improve CV
**POST** `/api/cv/improve`

Generate improved version of CV based on analysis report.

**Request Body**
```json
{
  "cv": "Original CV text...",
  "report": "Analysis report with recommendations..."
}
```

**Response**
```json
{
  "improved_cv": "Enhanced CV text..."
}
```

---

### 5. Generate Cover Letter
**POST** `/api/cover-letter/generate`

Create tailored cover letter for the job.

**Request Body**
```json
{
  "cv": "CV text content...",
  "job": {
    "companyName": "Google",
    "text": "Job description..."
  }
}
```

**Response**
```json
{
  "cover_letter": "Tailored cover letter text..."
}
```

---

### 6. Scrape Job
**POST** `/api/job/scrape`

Extract job information from URL.

**Request Body**
```json
{
  "url": "https://linkedin.com/jobs/..."
}
```

**Response**
```json
{
  "company_name": "Company - Position",
  "job_info": "Extracted job information..."
}
```

---

## Running the API

### Start Server
```bash
cd api
python main.py
```

Or use uvicorn directly:
```bash
uvicorn api.main:app --reload --host 0.0.0.0 --port 8000
```

### Interactive Documentation
FastAPI provides automatic interactive API documentation:
- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

## CORS Configuration
The API allows all origins in development. For production, update the CORS settings in `api/main.py`:

```python
app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://yourdomain.com"],  # Specific domains
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
```

## Environment Variables
Required environment variables (in `.env` at project root):
```
GEMINI_API_KEY=your_gemini_api_key_here
```

## Error Handling
All endpoints return proper HTTP status codes:
- `200`: Success
- `400`: Bad request (invalid input)
- `500`: Server error

Error response format:
```json
{
  "detail": "Error message description"
}
```

## Data Storage
- Job information is temporarily stored in `userdata/jobs/`
- CV files are processed in `/tmp/` and immediately removed
- No persistent database is used (stateless API)

## Dependencies
- FastAPI
- Uvicorn
- Python-multipart (for file uploads)
- pypdf (PDF parsing)
- google-generativeai (AI processing)

Install all dependencies:
```bash
pip install -r requirements.txt
```

## Development Tips
1. Use the interactive docs at `/docs` for testing
2. Monitor logs for debugging
3. Ensure `GEMINI_API_KEY` is set correctly
4. Check file permissions for `userdata/` directory
