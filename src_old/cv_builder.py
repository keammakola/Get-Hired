
import os
from google import genai
def collect_cv_info():
    cv_data = {}
    
    # Personal Information
    cv_data['personal'] = {
        'name': input("Enter your full names: "),
        'email': input("Enter your email address: "),
        'phone': input("Enter your phone number: "),
        'location': input("Enter your location (City): "),
        'linkedin': input("Enter your LinkedIn URL (optional): "),
        'portfolio': input("Enter your portfolio/website URL (optional): ")
    }

    # Professional Summary
    cv_data['summary'] = input("Enter a brief professional summary (2-3 sentences): ")

    # Work Experience
    cv_data['experience'] = []
    while True:
        print("\nEnter work experience (press enter twice to finish):")
        exp = {
            'company': input("\nEnter company name (or press enter to skip): ")
        }
        if not exp['company']:
            break
        exp.update({
            'title': input("Enter job title: "),
            'location': input("Enter job location: "),
            'start_date': input("Enter start date (MM/YYYY): "),
            'end_date': input("Enter end date (MM/YYYY or 'Present'): "),
            'responsibilities': []
        })
        
        print("Enter job responsibilities (one per line, press enter twice to finish):")
        while True:
            resp = input()
            if not resp:
                break
            exp['responsibilities'].append(resp)
        
        cv_data['experience'].append(exp)

    # Education
    cv_data['education'] = []
    while True:
        print("\nEnter education details (press enter twice to finish):")
        edu = {
            'institution': input("\nEnter institution name (or press enter to skip): ")
        }
        if not edu['institution']:
            break
        edu.update({
            'degree': input("Enter degree: "),
            'field': input("Enter field of study: "),
            'graduation_date': input("Enter graduation date (MM/YYYY): "),
            'gpa': input("Enter GPA (optional): ")
        })
        cv_data['education'].append(edu)

    # Skills
    cv_data['skills'] = {
        'technical': input("\nEnter technical skills (comma-separated): ").split(','),
        'soft': input("Enter soft skills (comma-separated): ").split(','),
        'languages': input("Enter languages (comma-separated): ").split(','),
        'certifications': []
    }

    # Certifications
    print("\nEnter certifications (press enter twice to finish):")
    while True:
        cert = input()
        if not cert:
            break
        cv_data['skills']['certifications'].append(cert)

    # Projects
    cv_data['projects'] = []
    while True:
        proj = {
            'name': input("\nEnter project name (or press enter to skip): ")
        }
        if not proj['name']:
            break
        proj.update({
            'description': input("Enter project description: "),
            'technologies': input("Enter technologies used (comma-separated): ").split(','),
            'url': input("Enter project URL (optional): ")
        })
        cv_data['projects'].append(proj)
    os.makedirs("userdata/cv", exist_ok=True)
    api_key = os.getenv("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=f"Here is a CV:\n{cv_data}\nplease put this information in a normal format and remove unnecessary data and only keep the CV info. just the information, no ai filler like 'Here is the CV information in a normal format:' etc"
    )
    with open("userdata/cv/cv.md","w") as f:
        f.write(response.text)
    return response.text
