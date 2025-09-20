from google import genai
import os


def cv_cleaner(cv):
    api_key = os.getenv("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)
    os.makedirs("userdata/processed cv", exist_ok=True)
    with open(cv, "r") as file:
        file_content = file.read()
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=f"Please structure my CV in an ATS-compatible format. Provide only the formatted CV in markdown that can be converted to pdf, with no additional explanation or text.This will be the final version, so no placeholders. Here is my current cv \n {file_content}",
    )
    with open("userdata/processed cv/new_cv.md", "w") as f:
        f.write(response.text)
    print("Your new CV is now ready for viewing")
    return response.text


# maybe manually inputting all the details needed for the cv
# tool that will now personalise the cv for the specific job post
# repurpose cv cleaner to be a tool that creates a generic cv for user
