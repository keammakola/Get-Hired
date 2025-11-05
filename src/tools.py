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
            with open("userdata/cv/uploaded_cv.md","w") as f:
                f.write(response.text)
            return
        
        except FileNotFoundError as e:
            print(f"Error: {e}")
            return

    