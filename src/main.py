import os
from job_collector import job_scraper
from tools import file_creator,cv_extractor

print("Welcome to Get Hired")

while True:
    name, info = job_scraper()
    file_creator("jobs",name,info)
    os.system("clear")
    print("Job saved!")
    while True:
        instruction = input("Would you like to:\n1. Upload a CV\n2. Create a CV\n>")
        if instruction == "1":
            cv_extractor()
            #add implementation of cv
            break
        elif instruction == "2":
            print("Feature coming soon!")
            break
        else:
            os.system("clear")
            print("Invalid input. Please try again.")
    break
    