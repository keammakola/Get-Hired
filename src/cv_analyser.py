import os
import pathlib
import time
from google import genai
from google.genai.errors import ServerError
from dotenv import load_dotenv




def cv_analyser(pdf_path):
    load_dotenv()
    api_key = os.getenv("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)

    rubric_path = "resources/rubric.md"
    output_dir = "userdata/analysis"
    output_file = pathlib.Path(output_dir) / "cv_score.md"

    os.makedirs(output_dir, exist_ok=True)

    with open(rubric_path, "r") as file:
        rubric = file.read()

    uploaded_file = client.files.upload(file=pdf_path)
    print(f"File uploaded successfully")

    system_prompt = (
        "You are a professional CV analyst. Your goal is to provide a comprehensive "
        "review based strictly on the provided rubric. The response MUST ONLY contain "
        "three markdown sections: 'What's Great', 'What's Lacking',  'Recommended Actionables' , and a final CV score out of 100. "
        "Be direct, concise, and professional."
    )

    user_query = (
        f"{system_prompt}\n\n"
        f"Using the following rubric, analyse the uploaded CV file. "
        f"The rubric is:\n---\n{rubric}\n---"
    )

    max_retries = 3
    for attempt in range(max_retries):
        try:
            response = client.models.generate_content(
                model="gemini-2.5-flash",
                contents=[uploaded_file, user_query]
            )
            break
        except ServerError as e:
            if "503" in str(e) and attempt < max_retries - 1:
                wait_time = (attempt + 1) * 10
                print(f"Model overloaded. Retrying in {wait_time} seconds...")
                time.sleep(wait_time)
            else:
                raise

    with open(output_file, "w") as f:
        f.write(response.text)
    print(f"Analysis complete. Results saved to: {output_file}")

    if uploaded_file:
        print(f"Deleting uploaded file: {uploaded_file.name}...")
        client.files.delete(name=uploaded_file.name)
        print("File successfully deleted from the service.")

