from pdf_mngr import parse_pdf
from job_mngr import scrape_web, paste_to_text
from ai_tools import cv_cleaner
import os

print("Welcome to Get_Hired!")
print("First, let's get to know you")
parse_pdf()
while True:
    job_input = input(
        "\nWould you like to:\n1. Paste the link to the job advert(LinkedIn link support coming soon!)\n2. Paste the text from the job advert\n>"
    )
    if job_input == "1":
        os.system("clear")
        print("Now, give us the link for the job post you are applying for")
        scrape_web()
        break
    elif job_input == "2":
        os.system("clear")
        print("Please paste the text copied from the job advert")
        paste_to_text()

        break
    else:
        os.system("clear")
        print("Invalid entry. Let's try again.")
while True:
    cv_query = input("Would you like your CV to be ATS compatible?\n1. Yes\n2. No\n\n>")
    if cv_query == "1":
        print(cv_cleaner("userdata/unprocessed cv/mycv.txt"))

        break
    elif cv_query == "2":
        break
    else:
        print("Invalid entry. Let's try again.")
