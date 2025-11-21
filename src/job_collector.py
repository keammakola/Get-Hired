from bs4 import BeautifulSoup
import requests
import os

from google import genai


from dotenv import load_dotenv

load_dotenv()


def file_creator(folder, filename, content):
    os.makedirs(f"userdata/{folder}", exist_ok=True)
    filepath = f"userdata/{folder}/{filename}.md"
    with open(filepath, "w") as f:
        f.write(content)
    return filepath


def job_name(page):
    api_key = os.getenv("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=f"Here is the information on a job i found\n{page}. give me the title of the job in the format 'Company name - Position'",
    )
    return response.text


def job_info(page):
    api_key = os.getenv("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=f"Here is a job that i got from the internet:\n{page}\nplease put this information in a normal format and remove unnecessary data and only keep the job info. just the information, no ai filler like 'Here is the job information in a normal format:' etc",
    )
    return response.text


def job_scraper():
    print("Please provide the job link (LinkedIn posts support coming soon!):")
    web_link = input(">")
    page = requests.get(web_link)
    page = BeautifulSoup(page.content, "html.parser")
    name = job_name(page)
    info = job_info(page)
    return name, info
