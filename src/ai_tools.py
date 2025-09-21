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


def cv_analyser(cv):
    """
    Analyse the user's CV in accordance to ATS format.

    Parameters
    ----------
    cv : str
        The path to the user's CV file.

    Returns
    -------
    str
        The analysis of the user's CV in markdown format.
    """
    api_key = os.getenv("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)
    os.makedirs("userdata/ai_analysis", exist_ok=True)
    with open(cv, "r") as file:
        file_content = file.read()
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=f"Analyse my CV in accordance to ATS format. Split it into Whats great, whats lacking and recommended actionables sections. provide only what i asked for, get straight to point. Here is my cv \n {file_content}",
    )
    with open("userdata/ai_analysis/cv_analysis.md", "w") as f:
        f.write(response.text)
    return response.text


def cv_scorer(cv):
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
    with open(cv, "r") as file:
        file_content = file.read()
    with open("rubric.md", "r") as file:
        rubric = file.read()
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=f"Using this rubric anaylse my cv:{rubric}\n. Here is my cv \n {file_content}\nDont add advise.Just summary for each criteria and the overall (for example, 54 out of 75)",
    )
    with open("userdata/ai_analysis/cv_score.md", "w") as f:
        f.write(response.text)
    print(response.text)
    return response.text


# maybe manually inputting all the details needed for the cv
# tool that will now personalise the cv for the specific job post
# repurpose cv cleaner to be a tool that creates a generic cv for user
