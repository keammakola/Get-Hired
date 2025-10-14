from google import genai
import os


def cv_cleaner(cv):
    """
    Structure the user's CV into an ATS-compatible format.

    Parameters
    ----------
    cv : str
        The path to the user's CV file.

    Returns
    -------
    str
        The formatted CV in markdown format.
    """
    api_key = os.getenv("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)
    os.makedirs("userdata/processed cv", exist_ok=True)
    with open(cv, "r") as file:
        file_content = file.read()
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=f"Structure my CV in an ATS-compatible format. Provide only the formatted CV in markdown that can be converted to pdf, with no additional explanation or text.This will be the final version, so no placeholders. Here is my current cv \n {file_content}",
    )
    with open("userdata/processed cv/new_cv.md", "w") as f:
        f.write(response.text)
    return response.text


def cv_scorer(cv, job_name):
    """
    Analyse the user's CV in accordance to ATS format and score it.

    Parameters
    ----------
    cv : str
        The path to the user's CV file.

    Returns
    -------
    str
        The analysis of the user's CV in markdown format and the score.
    """
    api_key = os.getenv("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)
    os.makedirs("userdata/ai_analysis", exist_ok=True)
    with open("rubric.md", "r") as file:
        rubric = file.read()
    with open(f"userdata/jobs/{job_name}.md", "r") as file:
        job = file.read()
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=f"Using this rubric anaylse my cv:{rubric}\n. Here is my cv \n {cv}\n. This is the job i want to apply for \n{job}\nSplit it into Whats great, whats lacking and recommended actionables sections. Provide only what i asked for, get straight to point.",
    )
    with open("userdata/ai_analysis/cv_score.md", "w") as f:
        f.write(response.text)
    print(response.text)
    return response.text


def compatibility_checker(cv, job):
    api_key = os.getenv("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)
    os.makedirs("userdata/ai_analysis", exist_ok=True)
    with open(cv, "r") as file:
        file_content = file.read()
    with open(job, "r") as file:
        job_data = file.read()
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=f"Here is my CV {file_content}\nplease check if Im compatible for this job {job_data}",
    )
    # with open("userdata/ai_analysis/cv_score.md", "w") as f:
    #     f.write(response.text)
    print(response.text)
    return response.text


def job_description_normaliser(job):
    api_key = os.getenv("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)
    os.makedirs("userdata/jobs", exist_ok=True)
    response1 = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=f"Here is the information on a job i found\n{job}. give me the title of the job in the format 'Company name - Position'",
    )
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=f"Here is a job that i got from the internet:\n{job}\nplease put this information in a normal format and remove unnecessary data and only keep the job info. just the information, no ai filler like 'Here is the job information in a normal format:' etc",
    )
    with open(f"userdata/jobs/{response1.text}.md", "w") as f:
        f.write(response.text)
    return response.text, response1.text


def cover_generator(job, cv_data):
    api_key = os.getenv("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)
    os.makedirs("userdata/final docs", exist_ok=True)
    with open(f"userdata/jobs/{job}.md", "r") as file:
        job_data = file.read()
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=f"Here is a job that i want to apply for \n{job_data}\nusing this cv \n{cv_data}\n. Please create a professional cover letter thats related to this job post",
    )
    with open("userdata/final docs/coverletter.md", "w") as f:
        f.write(response.text)
    return response.text


# maybe manually inputting all the details needed for the cv
# tool that will now personalise the cv for the specific job post
# repurpose cv cleaner to be a tool that creates a generic cv for user
# each prompt should give current date and time
