import requests
import os
from bs4 import BeautifulSoup


def scrape_web():
    """
    Scrape the job page from the given link and save the content to a file.

    The file will be saved in the userdata/jobs directory with the name job_page.txt.

    Parameters
    ----------
    None

    Returns
    -------
    None

    Example
    -------
    >>> scrape_web()
    Please provide the job link: https://example.com/job
    """
    print("Please provide the job link:")
    web_link = input(">")
    page = requests.get(web_link)
    page = BeautifulSoup(page.content, "html.parser")
    os.makedirs("userdata/jobs", exist_ok=True)
    page = page.get_text(separator="\n", strip=True)

    with open("userdata/jobs/job_page.txt", "w") as f:
        f.write(page)


def paste_to_text():
    """
    Paste the job information and save it to a file.

    The file will be saved in the userdata/jobs directory with the name job_page.txt.

    Parameters
    ----------
    None

    Returns
    -------
    None

    """
    print("paste the job information:")
    txt = input(">")
    os.makedirs("userdata/jobs", exist_ok=True)
    with open("userdata/jobs/job_page.txt", "w") as f:
        f.write(txt)
