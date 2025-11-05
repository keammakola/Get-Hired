from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from src.tools import cv_scorer, cv_improver, cover_letter
from src.job_collector import job_scraper, job_info
from pypdf import PdfReader
from google import genai
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class JobData(BaseModel):
    method: str
    link: str = None
    companyName: str = None
    text: str = None


class CVAnalysisRequest(BaseModel):
    cv: str
    job: dict


class CVImproveRequest(BaseModel):
    cv: str
    report: str


class CoverLetterRequest(BaseModel):
    cv: str
    job: dict


class JobScrapeRequest(BaseModel):
    url: str


@app.get("/")
def read_root():
    return {"message": "Get Hired API"}


@app.post("/api/cv/upload")
async def upload_cv(cv: UploadFile = File(...)):
    try:
        if cv.content_type not in ["application/pdf", "application/vnd.openxmlformats-officedocument.wordprocessingml.document"]:
            raise HTTPException(status_code=400, detail="Only PDF and DOCX files are supported")

        content = await cv.read()

        if cv.content_type == "application/pdf":
            with open("/tmp/temp_cv.pdf", "wb") as f:
                f.write(content)

            reader = PdfReader("/tmp/temp_cv.pdf")
            text = ""
            for page in reader.pages:
                text += page.extract_text()

            api_key = os.getenv("GEMINI_API_KEY")
            client = genai.Client(api_key=api_key)
            response = client.models.generate_content(
                model="gemini-2.5-flash",
                contents=f"Here is a CV:\n{text}\nplease put this information in a normal format and remove unnecessary data and only keep the CV info. just the information, no ai filler like 'Here is the CV information in a normal format:' etc"
            )

            os.remove("/tmp/temp_cv.pdf")

            return {"cv_text": response.text}
        else:
            return {"cv_text": "DOCX parsing not yet implemented"}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/api/cv/analyze")
async def analyze_cv(request: CVAnalysisRequest):
    try:
        job_name = request.job.get('companyName', 'job')

        os.makedirs("userdata/jobs", exist_ok=True)
        with open(f"userdata/jobs/{job_name}.md", "w") as f:
            if request.job.get('method') == 'link':
                f.write(request.job.get('text', ''))
            else:
                f.write(request.job.get('text', ''))

        report = cv_scorer(request.cv, job_name)

        return {
            "report": report,
            "score": 75,
            "compatible": True
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/api/cv/improve")
async def improve_cv(request: CVImproveRequest):
    try:
        improved = cv_improver(request.report, request.cv)

        return {"improved_cv": improved}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/api/cover-letter/generate")
async def generate_cover_letter(request: CoverLetterRequest):
    try:
        job_name = request.job.get('companyName', 'job')

        letter = cover_letter(request.cv, job_name)

        return {"cover_letter": letter}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/api/job/scrape")
async def scrape_job(request: JobScrapeRequest):
    try:
        name, info_text = job_scraper()

        return {
            "company_name": name,
            "job_info": info_text
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
