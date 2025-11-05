import requests
import os
from bs4 import BeautifulSoup
from ai_tools import job_description_normaliser



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
    print("Please provide the job link (LinkedIn posts support coming soon!):")
    web_link = input(">")
    page = requests.get(web_link)
    page = BeautifulSoup(page.content, "html.parser")

    info, name = job_description_normaliser(page)
    return info, name


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
    return job_description_normaliser(txt)
