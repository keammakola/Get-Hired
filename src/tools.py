import os
from pypdf import PdfReader
from google import genai




def file_creator(folder, filename, content):
    os.makedirs(f"userdata/{folder}", exist_ok=True)
    filepath = f"userdata/{folder}/{filename}.md"
    with open(filepath, "w") as f:
        f.write(content)
    return filepath

def cv_extractor():
        try:
            pdf = input("Enter the path to the PDF file: ")
            if not os.path.exists(pdf):
                raise FileNotFoundError("File does not exist")
            reader = PdfReader(pdf)
            os.makedirs("userdata/cv", exist_ok=True)
            text = ""
            for page in reader.pages:
                text += page.extract_text()
            api_key = os.getenv("GEMINI_API_KEY")
            client = genai.Client(api_key=api_key)
            response = client.models.generate_content(
                model="gemini-2.5-flash",
                contents=f"Here is a CV:\n{text}\nplease put this information in a normal format and remove unnecessary data and only keep the CV info. just the information, no ai filler like 'Here is the CV information in a normal format:' etc"
            )
            with open("userdata/cv/cv.md","w") as f:
                f.write(response.text)
            return response.text
        
        except FileNotFoundError as e:
            print(f"Error: {e}")
            return

def cv_scorer(cv, job_name):
    api_key = os.getenv("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)
    os.makedirs("userdata/ai_analysis", exist_ok=True)
    with open("rubric.md", "r") as file:
        rubric = file.read()
    with open(f"userdata/jobs/{job_name}.md", "r") as file:
        job = file.read()
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=f"Using this rubric anaylse my cv:{rubric}\n. Here is my cv \n {cv}\n. This is the job i want to apply for \n{job}\nSplit it into Whats great, whats lacking and recommended actionables sections. Provide only what i asked for, get straight to point. Lastly, tell me if I am compatible for this job.",
    )
    with open("userdata/ai_analysis/cv_score.md", "w") as f:
        f.write(response.text)
    return response.text
    
def cv_improver(cv_report,cv):
        api_key = os.getenv("GEMINI_API_KEY")
        client = genai.Client(api_key=api_key)
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=f"Here is my CV {cv}\nplease improve it using information from this report {cv_report}. Do not lie!. Provide only a new CV, get straight to point. No AI fluff. Just CV only! no 'here is a polished cv...'",
        )
        with open("userdata/cv/cv.md", "w") as f:
            f.write(response.text)
        return response.text
    
def cover_letter(cv,job):
    api_key = os.getenv("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)
    os.makedirs("userdata/final docs", exist_ok=True)
    with open(f"userdata/jobs/{job}.md", "r") as file:
        job_data = file.read()
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=f"Here is a job that i want to apply for \n{job_data}\nusing this cv \n{cv}\n. Please create a professional cover letter thats related to this job post.Provide only a new coverletter, get straight to point. Do not lie.  No AI fluff",
    )
    with open("userdata/final docs/coverletter.md", "w") as f:
        f.write(response.text)
    return response.text
        