# Import required modules
from pdf_mngr import parse_pdf
from ai_tools import cv_analyser, cv_scorer
from job_mngr import scrape_web, paste_to_text
import os

# Display welcome message
print("Welcome to Get Hired!\n")

# Start CV upload process
print("Let's start off by adding your CV into the system")
parse_pdf()
os.system("clear")
print("Great. Your CV has been uploaded successfully!")

# Main program loop
while True:
    # Display main menu options
    usage = input(
        "What would you like to do?\n1. Get a detailed analysis of your CV\n2. Check ATS compatibility of your CV\n3. Curate CV for a job opportunity\n>"
    )
    # Option 1: CV Analysis
    if usage == "1":
        os.system("clear")
        print("CV analysis in progress...")
        print(cv_analyser("userdata/unprocessed cv/mycv.md"))
        break
    # Option 2: ATS Compatibility Check
    elif usage == "2":
        os.system("clear")
        print("CV scoring in progress...")
        print(cv_scorer("userdata/unprocessed cv/mycv.md"))
        break
    # Option 3: CV Curation
    elif usage == "3":
        os.system("clear")
        # Submenu for job information input method
        while True:
            usage = input(
                "Would you like to:\n1. Provide job link\n2. Paste job information\n>"
            )
            # Option 1: Web scraping
            if usage == "1":
                scrape_web()
                break
            # Option 2: Manual input
            elif usage == "2":
                paste_to_text()
                break
            # Handle invalid input
            else:
                print("Invalid entry. Let's try again")
        break

    # Handle invalid main menu input
    else:
        print("That's an invalid entry, lets try again.")
        os.system("clear")
