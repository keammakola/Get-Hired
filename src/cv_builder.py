def build_cv():
    try:
        # Personal Details
        details = personal_details()

        # Experience
        experience = experience()

        # Skills
        skills = skills()

        # Education
        education = education()

        # Certificates
        certificates = certificates()

        # Professional Summary
        summary = professional_summary()

        # Combine all sections into CV
        cv = {
            "Personal Details": details,
            "Professional Summary": summary,
            "Experience": experience,
            "Education": education,
            "Skills": skills,
            "Certificates": certificates,
        }

        return cv
    except Exception as e:
        print(f"Error building CV: {str(e)}")
        return None


def personal_details():
    details = {}
    try:
        details["name"] = input("Enter your first name: ").strip()
        if not details["name"]:
            raise ValueError("First name cannot be empty")

        details["surname"] = input("Enter your last name: ").strip()
        if not details["surname"]:
            raise ValueError("Last name cannot be empty")

        details["field"] = input("Enter your field of expertise: ").strip()
        details["phone"] = input("Enter your phone number: ").strip()
        details["email"] = input("Enter your email address: ").strip()
        if "@" not in details["email"]:
            raise ValueError("Invalid email format")

        details["location"] = input("Where are you based: ").strip()
        details["website"] = input(
            "Please provide a link to your personal portfolio: "
        ).strip()
        details["linkedin"] = input(
            "Please provide a link to your linkedin profile: "
        ).strip()
        return details
    except Exception as e:
        print(f"Error in personal details: {str(e)}")
        return None


def experience():
    experience = {}
    try:
        usage = input(
            "Would you like to add any work experience?:\n1. Yes\n2. No\n>"
        ).strip()
        if usage not in ["1", "2"]:
            raise ValueError("Invalid input - please enter 1 or 2")

        if usage == "1":
            while True:
                try:
                    title = input("Enter your job title: ").strip()
                    if not title:
                        raise ValueError("Job title cannot be empty")

                    company = input("Enter the company name: ").strip()
                    if not company:
                        raise ValueError("Company name cannot be empty")

                    start_date = input(
                        "Enter the start date of your experience: "
                    ).strip()
                    end_date = input("Enter the end date of your experience: ").strip()
                    description = input(
                        "Enter a description of your experience: "
                    ).strip()

                    exp_text = (
                        f"{title}\n{company}\n{start_date}-{end_date}\n{description}"
                    )
                    experience[company] = {
                        "title": title,
                        "start_date": start_date,
                        "end_date": end_date,
                        "description": description,
                        "full_text": exp_text,
                    }

                    another = input(
                        "Would you like to add another experience? (yes/no):\n1. Yes\n2. No\n>"
                    ).strip()
                    if another not in ["1", "2"]:
                        raise ValueError("Invalid input - please enter 1 or 2")
                    if another == "2":
                        break
                except Exception as e:
                    print(f"Error adding experience: {str(e)}")
                    continue
        else:
            experience = "None"

        return experience
    except Exception as e:
        print(f"Error in experience section: {str(e)}")
        return None


def skills():
    skills = []
    try:
        while True:
            skill = input("Enter a skill (or press enter to finish): ").strip()
            if skill == "":
                break
            skills.append(skill)
        return skills
    except Exception as e:
        print(f"Error adding skills: {str(e)}")
        return None


def education():
    education = []
    try:
        while True:
            degree = input(
                "Enter degree/qualification (or press enter to finish): "
            ).strip()
            if degree == "":
                break

            institution = input("Enter institution name: ").strip()
            if not institution:
                raise ValueError("Institution name cannot be empty")

            year = input("Enter completion year: ").strip()
            try:
                year = int(year)
            except ValueError:
                raise ValueError("Year must be a number")

            education.append(
                {"degree": degree, "institution": institution, "year": year}
            )
        return education
    except Exception as e:
        print(f"Error adding education: {str(e)}")
        return None


def certificates():
    certificates = []
    try:
        while True:
            cert = input("Enter certificate name (or press enter to finish): ").strip()
            if cert == "":
                break

            issuer = input("Enter certificate issuer: ").strip()
            if not issuer:
                raise ValueError("Certificate issuer cannot be empty")

            year = input("Enter year obtained: ").strip()
            try:
                year = int(year)
            except ValueError:
                raise ValueError("Year must be a number")

            certificates.append({"name": cert, "issuer": issuer, "year": year})
        return certificates
    except Exception as e:
        print(f"Error adding certificates: {str(e)}")
        return None


def professional_summary():
    try:
        summary = input("Enter your professional summary: ").strip()
        if not summary:
            raise ValueError("Professional summary cannot be empty")
        return summary
    except Exception as e:
        print(f"Error adding professional summary: {str(e)}")
        return None
