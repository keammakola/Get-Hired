# Get-Hired

Get Hired is your career companion, using AI to polish your CV, guide your cover letters, and give you the confidence to stand out and secure the job you deserve.
The app analyses your CV against a job posting, scores how well you match, suggests improvements, and drafts a tailored cover letter.

---

## Features

### ✅ Currently Implemented
* **CV Analysis & Scoring** - Upload your CV (PDF) and get a comprehensive analysis with scoring out of 100
* **Job Scraping** - Scrape job postings from web links using BeautifulSoup
* **Cover Letter Generation** - Generate tailored cover letters based on your CV and job requirements
* **LaTeX CV Builder** - Interactive CV builder that generates professional LaTeX/PDF resumes
* **ATS Optimization** - Analysis includes ATS-friendly formatting recommendations

### 🚧 Planned Features
* Web-based UI (React frontend)
* LinkedIn/Indeed direct integration
* Database storage for job history
* Batch processing capabilities
* Advanced analytics dashboard

---

## Tech Stack

### Current Implementation
- **Python 3.12+** – Core backend language
- **Google Gemini AI** – CV analysis, job matching, and cover letter generation
- **BeautifulSoup4** – Web scraping for job postings
- **PyPDF** – PDF parsing and processing
- **PyLaTeX** – LaTeX document generation for CVs
- **python-dotenv** – Environment variable management
- **Pre-commit hooks** – Code quality and formatting

### Planned Additions
- **FastAPI** – REST API layer
- **React** – Frontend UI
- **PostgreSQL** – Data persistence
- **Docker** – Containerization
- **Celery + Redis** – Background task processing

---

## Quick Start

### Prerequisites
- Python 3.12 or higher
- LaTeX distribution (TeX Live or MiKTeX) for CV generation
- Google Gemini API key

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/keammakola/get-hired.git
   cd get-hired
   ```

2. **Run the setup script:**
   ```bash
   python3 setup.py
   ```
   This will:
   - Create necessary directories
   - Install Python dependencies
   - Check for LaTeX installation
   - Create a `.env` file template

3. **Configure your API key:**
   Edit the `.env` file and add your Google Gemini API key:
   ```bash
   GEMINI_API_KEY=your_actual_api_key_here
   ```

### Alternative Setup (Manual)

```bash
# Create virtual environment
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Install pre-commit hooks
pre-commit install

# Create directories
mkdir -p userdata/{cv,analysis,covers,jobs}
```

---

## Usage

### CV Analysis
Analyze your CV against professional standards:
```python
from src.cv_analyser import cv_analyser
cv_analyser("path/to/your/cv.pdf")
```
Results saved to: `userdata/analysis/cv_score.md`

### Job Scraping
Scrape job postings from web links:
```python
from src.job_collector import job_scraper
name, info = job_scraper()
# Follow prompts to enter job URL
```

### Cover Letter Generation
Generate tailored cover letters:
```python
from src.cover_creator import cover_creator
cover_creator("path/to/cv.pdf", "userdata/jobs/job_posting.txt")
```
Results saved to: `userdata/covers/cover_letter.md`

### CV Builder
Create professional LaTeX CVs interactively:
```python
from src.cv_builder import generate_resume
generate_resume()
# Follow interactive prompts
```
Outputs: `.tex` and `.pdf` files in `userdata/cv/`

---

## Project Structure

```
Get-Hired/
├── src/                    # Source code
│   ├── cv_analyser.py     # CV analysis and scoring
│   ├── cv_builder.py      # LaTeX CV generation
│   ├── cover_creator.py   # Cover letter generation
│   ├── job_collector.py   # Job scraping utilities
│   └── main.py           # Main application entry
├── resources/             # Templates and rubrics
│   ├── base_template.tex  # LaTeX CV template
│   └── rubric.md         # CV scoring rubric
├── userdata/             # User-generated content
│   ├── cv/               # Generated CVs
│   ├── analysis/         # CV analysis results
│   ├── covers/           # Cover letters
│   └── jobs/             # Job postings
├── requirements.txt      # Python dependencies
├── setup.py             # Setup script
├── Makefile            # Development commands
└── .env.example        # Environment template
```

---

## Development

### Available Make Commands
```bash
make setup      # Setup virtual environment and dependencies
make run        # Run the main application
make pre-commit # Run code quality checks
make api        # Update Google GenAI package
```

### Code Quality
The project uses pre-commit hooks for:
- Code formatting
- Linting
- Type checking

Run checks manually:
```bash
pre-commit run --all-files
```

---

## API Keys

Currently supports:
- **Google Gemini API** (primary)
- OpenAI API (planned)

Get your Gemini API key from: [Google AI Studio](https://makersuite.google.com/app/apikey)

---

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Run pre-commit checks
5. Submit a pull request

---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## Roadmap

- [ ] Web interface (React)
- [ ] Database integration
- [ ] LinkedIn API integration
- [ ] Batch processing
- [ ] Advanced analytics
- [ ] Docker deployment
- [ ] CI/CD pipeline
