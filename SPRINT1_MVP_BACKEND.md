# Sprint 1: MVP Backend Documentation

## Overview
Sprint 1 delivers the core backend functionality for Get-Hired, a CV analysis and job matching application. This MVP provides essential features for CV processing, AI-powered analysis, and job posting management through a command-line interface.

## Architecture

### Core Components
- **PDF Processing** (`pdf_mngr.py`) - CV document parsing
- **AI Integration** (`ai_tools.py`) - CV analysis and scoring using Google Gemini
- **Job Management** (`job_mngr.py`) - Job posting collection and storage
- **User Interface** (`main.py`) - CLI application flow
- **User Data** (`user_details.py`) - Basic user information handling

### Data Flow
```
PDF Upload → Text Extraction → AI Analysis → Results Storage
Job Link/Text → Web Scraping/Manual Input → Text Storage → Future Matching
```

## Module Documentation

### 1. PDF Manager (`pdf_mngr.py`)
**Purpose**: Extract text content from PDF CVs for processing

**Functions**:
- `parse_pdf()`: Main function for PDF text extraction
  - Prompts user for PDF file path
  - Validates file existence
  - Extracts text from all pages using PyPDF
  - Saves extracted text to `userdata/unprocessed cv/mycv.md`
  - Handles file not found and parsing errors

**Dependencies**: `pypdf`, `os`

**Input**: PDF file path from user
**Output**: Markdown file with extracted CV text

### 2. AI Tools (`ai_tools.py`)
**Purpose**: Leverage Google Gemini AI for CV analysis and improvement

**Functions**:

#### `cv_cleaner(cv)`
- **Purpose**: Restructure CV in ATS-compatible format
- **Input**: Path to CV markdown file
- **Process**:
  - Reads CV content
  - Sends to Gemini with ATS formatting prompt
  - Generates clean, structured CV
- **Output**: Formatted CV saved to `userdata/processed cv/new_cv.md`

#### `cv_analyser(cv)`
- **Purpose**: Provide detailed CV analysis
- **Input**: Path to CV markdown file
- **Process**:
  - Analyzes CV against ATS standards
  - Identifies strengths, weaknesses, actionable improvements
- **Output**: Analysis report saved to `userdata/ai_analysis/cv_analysis.md`

#### `cv_scorer(cv)`
- **Purpose**: Score CV against predefined rubric
- **Input**: Path to CV markdown file
- **Process**:
  - Reads CV and rubric file
  - Generates numerical score with criteria breakdown
  - Displays results to user
- **Output**: Score report saved to `userdata/ai_analysis/cv_score.md`

**Dependencies**: `google.genai`, `os`
**API**: Google Gemini 2.5 Flash model
**Authentication**: `GEMINI_API_KEY` environment variable

### 3. Job Manager (`job_mngr.py`)
**Purpose**: Collect and store job posting information

**Functions**:

#### `scrape_web()`
- **Purpose**: Extract job details from web URLs
- **Process**:
  - Prompts user for job posting URL
  - Fetches webpage content using requests
  - Parses HTML with BeautifulSoup
  - Extracts clean text content
- **Output**: Job text saved to `userdata/jobs/job_page.txt`

#### `paste_to_text()`
- **Purpose**: Accept manually pasted job information
- **Process**:
  - Prompts user to paste job details
  - Directly saves input text
- **Output**: Job text saved to `userdata/jobs/job_page.txt`

**Dependencies**: `requests`, `beautifulsoup4`, `os`

### 4. Main Application (`main.py`)
**Purpose**: Orchestrate user interactions and application flow

**Application Flow**:
1. **Welcome & CV Upload**
   - Displays welcome message
   - Calls `parse_pdf()` to upload CV
   - Confirms successful upload

2. **Main Menu Options**:
   - **Option 1**: Detailed CV Analysis
     - Calls `cv_analyser()` with uploaded CV
     - Displays analysis results

   - **Option 2**: ATS Compatibility Check
     - Calls `cv_scorer()` with uploaded CV
     - Shows compatibility score

   - **Option 3**: Job Opportunity Curation
     - Sub-menu for job input method:
       - **3.1**: Web scraping via `scrape_web()`
       - **3.2**: Manual input via `paste_to_text()`

**Dependencies**: All other modules, `os`

### 5. User Details (`user_details.py`)
**Purpose**: Handle basic user information collection

**Functions**:
- `basic_info()`: Collects and displays user's first and last name
- Executes only when run as main module

## Data Storage Structure

```
userdata/
├── unprocessed cv/
│   └── mycv.md                 # Original CV text
├── processed cv/
│   └── new_cv.md              # AI-formatted CV
├── ai_analysis/
│   ├── cv_analysis.md         # Detailed analysis
│   └── cv_score.md           # Scoring results
└── jobs/
    └── job_page.txt          # Job posting content
```

## Configuration Files

### `requirements.txt`
```
pre-commit
pypdf
requests
beautifulsoup4
pytest
pytest-mock
google-generativeai
```

### `pytest.ini`
```ini
[tool:pytest]
testpaths = tests
python_files = test_*.py
python_classes = Test*
python_functions = test_*
addopts = -v --tb=short
```

## Testing Suite

### Test Coverage
- **12 test cases** covering all modules
- **100% pass rate** with comprehensive mocking
- **External dependency isolation** (no real API calls)

### Test Files
- `test_ai_tools.py` - AI functionality testing
- `test_job_mngr.py` - Job management testing
- `test_pdf_mngr.py` - PDF processing testing
- `test_main.py` - Application flow testing
- `test_user_details.py` - User input testing

## Key Features Delivered

### ✅ Core Functionality
- PDF CV upload and text extraction
- AI-powered CV analysis and scoring
- ATS compatibility checking
- Job posting collection (web scraping + manual)
- Structured data storage

### ✅ Error Handling
- File not found errors
- PDF parsing failures
- Network request failures
- Invalid user input handling

### ✅ AI Integration
- Google Gemini API integration
- Prompt engineering for CV analysis
- Structured output generation
- Environment-based API key management

## Technical Specifications

### Environment Requirements
- Python 3.12+
- Virtual environment recommended
- Google Gemini API key required

### External APIs
- **Google Gemini 2.5 Flash**: CV analysis and formatting
- **Web Scraping**: BeautifulSoup for job posting extraction

### File Formats Supported
- **Input**: PDF (CV documents)
- **Processing**: Markdown (internal format)
- **Output**: Markdown (analysis reports)

## Usage Instructions

1. **Setup**:
   ```bash
   pip install -r requirements.txt
   export GEMINI_API_KEY="your_api_key"
   ```

2. **Run Application**:
   ```bash
   python src/main.py
   ```

3. **Follow CLI Prompts**:
   - Upload PDF CV
   - Choose analysis option
   - View results in `userdata/` directories

## Future Enhancements (Next Sprints)
- React frontend interface
- Database integration (PostgreSQL)
- Advanced job matching algorithms
- Cover letter generation
- User authentication system
- Batch processing capabilities

## Sprint 1 Success Metrics
- ✅ All core backend functions implemented
- ✅ Complete test suite with 100% pass rate
- ✅ AI integration functional
- ✅ Data persistence working
- ✅ Error handling robust
- ✅ CLI interface intuitive
