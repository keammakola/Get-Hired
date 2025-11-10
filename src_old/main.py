import os
from job_collector import job_scraper
from tools import file_creator,cv_extractor, cv_scorer, cv_improver,cover_letter
from cv_builder import collect_cv_info

print("Welcome to Get Hired")

while True:
    while True:
        instruction = input("Would you like to:\n1. Paste the job information\n2. Paste the job link\n>")
        if instruction == "1":
            name = input("What is the company name\n>")
            info = input("Paste the job information\n>")
            file_creator("jobs", name, info)
            os.system("clear")
            print("Job saved!")
            break
        elif instruction == "2":
            os.system("clear")
            name, info = job_scraper()
            file_creator("jobs",name,info)
            os.system("clear")
            print("Job saved!")
            break
    while True:
        instruction = input("Would you like to:\n1. Upload a CV\n2. Create a CV\n>")
        if instruction == "1":
            cv=cv_extractor()
            break
        elif instruction == "2":
            cv=collect_cv_info()
            break
        else:
            os.system("clear")
            print("Invalid input. Please try again.")
    print("We will now check if your CV is ATS compatible and how well you fit into this job")
    os.system("clear")
    cv_report = cv_scorer(cv, name)
    instruction = input("Based on the report, would you like us to automatically improve your CV?")
    if instruction == "yes":
        print("We will now improve your CV")
        os.system("clear")
        cv_improver(cv_report,cv)
        print("Your CV has been improved!")
    print("We will now create a cover letter for you")
    os.system("clear")
    cover_letter(cv,name)
    
        
    
    break
    