import os
import pathlib
import time
from google import genai
from google.genai.errors import ServerError
from dotenv import load_dotenv


def cover_creator(cv_path, job_path):
    load_dotenv()
    api_key = os.getenv("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)

    output_dir = "userdata/covers"
    output_file = pathlib.Path(output_dir) / "cover_letter.md"

    os.makedirs(output_dir, exist_ok=True)

    uploaded_file = client.files.upload(file=cv_path)

    with open(job_path, "r") as file:
        job = file.read()

    print(f"File uploaded successfully")

    system_prompt = "you are a professional Job seekers' advisor. Your goal is to build curated cover letters based on the candidates CV and job post. YOu provide ONLY the formatted cover letter without adding false information. It must be professional"
    user_query = f"{system_prompt}\n Using the following job, create a cover letter\n Here is the job post: {job} to match this CV"

    max_retries = 3

    for attempt in range(max_retries):
        try:
            response = client.models.generate_content(
                model="gemini-2.5-flash", contents=[uploaded_file, user_query]
            )
            break
        except ServerError as e:
            if ("503" in str(e) or "500" in str(e)) and attempt < max_retries - 1:
                wait_time = (attempt + 1) * 10
                print(f"Server error. Retrying in {wait_time} seconds...")
                time.sleep(wait_time)
            else:
                raise

    with open(output_file, "w") as f:
        f.write(response.text)
        print(f"Cover letter complete. Results saved to: {output_file}")

    if uploaded_file:
        print(f"Deleting uploaded file: {uploaded_file.name}...")
        client.files.delete(name=uploaded_file.name)
        print("File successfully deleted from the service.")
