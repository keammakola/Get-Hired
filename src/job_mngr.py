import requests
import os
from bs4 import BeautifulSoup


def scrape_web():
    web_link = input("Enter the link to the job you are interested in: ")
    page = requests.get(web_link)
    page = BeautifulSoup(page.content, "html.parser")
    os.makedirs("userdata/jobs", exist_ok=True)
    page = page.get_text(separator="\n", strip=True)

    with open("userdata/jobs/job_page.txt", "w") as f:
        f.write(page)
