from pdf_mngr import parse_pdf
from job_mngr import scrape_web

print("Welcome to Get_Hired!")
print("First, let's get to know you")
parse_pdf()
print("Now, give us the link for the job post you are applying for")
scrape_web()
