import os
from pdf_mngr import parse_pdf
from ai_tools import (
    cv_scorer,
    compatibility_checker,
    cover_generator,
    job_description_normaliser,
)
from job_mngr import scrape_web, paste_to_text
from cv_builder import build_cv

print("Welcome to Get Hired!\n")

print("Let's start off by looking at the job you're interested in")
while True:
    usage = input(
        "Would you like to:\n1. Provide job post link\n2. Paste job information\n>"
    )
    if usage == "1":
        os.system("clear")
        job_info, job_name = scrape_web()
        break
    elif usage == "2":
        os.system("clear")
        job_info, job_name = paste_to_text()
        break
    else:
        print("Invalid entry. Let's try again")

print(
    "The job details have been captured successfully. Now we need to make sure you have a cv"
)
while True:
    usage = input("Would you like to:\n1. Upload CV\n2. Create new CV\n>")
    if usage == "1":
        os.system("clear")
        cv = parse_pdf()
        print(
            "Your CV has been uploaded successfully!. We will now analyse your cv to check compatibility with ATS and the job"
        )
        analysis = cv_scorer(cv, job_name)
        print(analysis)
        while True:
            usage = input(
                "Would you like us to improve your CV based on the above report?\n1. Yes\n2. No\n>"
            )
            if usage == "1":
                print("feature coming soon")
                # add cv improver function
                break
            elif usage == "2":
                break
            else:
                print("Invalid entry. Let's try again")
                os.system("clear")
                continue
        break
    elif usage == "2":
        os.system("clear")
        build_cv()

while True:
    print(
        "Your CV is now ready! Would you like us to create a cover letter that matches the job you just shared?\n1. Yes 2. No"
    )
    usage = input(">")
    if usage == "1":
        os.system("clear")
        cover_generator(job_name, cv)
        break
    elif usage == "2":
        break
    else:
        print("Invalid entry. Let's try again")
        os.system("clear")
        continue


# possibly thread this when doing api calls
