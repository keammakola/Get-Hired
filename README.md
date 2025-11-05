# Get-Hired

# Get Hired

Get Hired is your career companion, using AI to polish your CV, guide your cover letters, and give you the confidence to stand out and secure the job you deserve.
The app analyses your CV against a job posting, scores how well you match, suggests improvements, and drafts a tailored cover letter.

---

## Features

* **Upload your CV (PDF or DOCX)**
  Import your CV in common formats for analysis.

* **Provide a job link or upload a posting**
  Paste a link to a job posting (e.g. LinkedIn, Indeed) or upload the text so the system can fetch and analyse it.

* **Analyse fit with a scoring system**
  See a percentage score or rating that shows how closely your CV matches the role.

* **Get keyword and skill gap suggestions**
  Identify missing or weak skills compared to the posting and get advice on closing the gaps.

* **Improve CV phrasing for better alignment**
  Receive rewording suggestions to better match employer language and pass ATS checks.

* **Generate a draft cover letter customised to the role**
  Instantly create a tailored cover letter highlighting your strengths.

---

## Tech Stack

### Current
- **Python** – Core backend language.
- **pdfplumber / python-docx** – CV parsing from PDF and DOCX.
- **FastAPI** – API layer to handle requests.
- **External AI API (OpenAI / Anthropic / Cohere)** – Analyse CVs, job posts, and generate suggestions/cover letters.

### Planned
- **React** – Frontend UI for users (production-ready).
- **BeautifulSoup / Playwright** – Scraping job postings from links (LinkedIn, Indeed).
- **PostgreSQL** – Database to store CVs, job posts, fit scores, and outputs.
- **Docker** – Containerisation for easier deployment.
- **Celery + Redis** – Background tasks (scraping, AI analysis).
- **Supabase / Firebase** – Optional auth and storage for faster setup.

---

## Usage (prototype)
1. Clone the repo:
   ```bash
   git clone https://github.com/keammakola/get-hired.git
   cd get-hired
