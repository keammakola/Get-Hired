import re
import os
import time
import subprocess  # New import for running command line tools

# --- Configuration ---
TEMPLATE_FILE = "resources/base_template.tex"
OUTPUT_FILE = "userdata/cv/my_generated_resume.tex"
PDF_FILE = "userdata/cv/my_generated_resume.pdf"  # Define the output PDF name
AUX_FILES = [".aux", ".log", ".out", ".toc", ".nav", ".snm"]  # Files to clean up later

PLACEHOLDERS = {
    # Heading
    "__FULL_NAME__": "Your Full Name",
    "__EMAIL__": "Your Email Address",
    "__PHONE__": "Your Phone Number (e.g., +441234567890)",
    "__WEBSITE__": "Your Portfolio Website URL",
    "__LINKEDIN__": "Your LinkedIn Profile URL",
    # Professional Summary
    "__PROFESSIONAL_SUMMARY__": "Professional Summary (2-3 sentences)",
    # Education
    "__UNIVERSITY__": "University Name",
    "__UNI_LOCATION__": "University Location (City, Country)",
    "__DEGREE__": "Degree Name (e.g., M.Sc. in Computer Science)",
    "__UNI_DATES__": "Education Dates (e.g., Sep 2018 -- Jun 2019)",
    # Tech Stack
    "__PROGRAMMING_LANGUAGES__": "Programming Languages (e.g., Python, Java, JavaScript)",
    "__FRAMEWORKS__": "Frameworks \\& Libraries (e.g., React, Django, Spring)",
    "__DATABASES__": "Databases (e.g., MySQL, PostgreSQL, MongoDB)",
    "__TOOLS__": "Tools \\& Technologies (e.g., Git, Docker, AWS)",
    # Experience
    "__COMPANY__": "Company Name",
    "__COMP_LOCATION__": "Company Location (City, Country)",
    "__JOB_TITLE__": "Job Title",
    "__JOB_DATES__": "Job Dates (e.g., Oct 2020 -- Present)",
    "__PROJECT_1_TITLE__": "Project 1 Title",
    "__PROJECT_1_DESC__": "Description of achievement 1",
    "__PROJECT_2_TITLE__": "Project 2 Title",
    "__PROJECT_2_DESC__": "Description of achievement 2",
    # Projects
    "__PERSONAL_PROJECT_1__": "Personal Project 1 Name",
    "__PROJECT_1_TECH__": "Technologies Used",
    "__PROJECT_1_ROLE__": "Your Role",
    "__PROJECT_1_DATES__": "Project Dates",
    "__PERSONAL_PROJECT_1_DESC__": "Project 1 Description",
    "__PERSONAL_PROJECT_2__": "Personal Project 2 Name",
    "__PROJECT_2_TECH__": "Technologies Used",
    "__PROJECT_2_ROLE__": "Your Role",
    "__PROJECT_2_DATES__": "Project Dates",
    "__PERSONAL_PROJECT_2_DESC__": "Project 2 Description",
    # Skills
    "__TECHNICAL_SKILLS__": "Technical Skills (e.g., Problem Solving, Data Analysis)",
    "__SOFT_SKILLS__": "Soft Skills (e.g., Leadership, Communication, Teamwork)",
    # Certificates
    "__CERT_1_NAME__": "Certificate 1 Name",
    "__CERT_1_ISSUER__": "Issuing Organization",
    "__CERT_1_ID__": "Certificate ID (optional)",
    "__CERT_1_DATE__": "Issue Date",
    "__CERT_2_NAME__": "Certificate 2 Name",
    "__CERT_2_ISSUER__": "Issuing Organization",
    "__CERT_2_ID__": "Certificate ID (optional)",
    "__CERT_2_DATE__": "Issue Date",
    # Languages
    "__LANGUAGES__": "Languages (e.g., English (Native), Spanish (Fluent), French (Intermediate))",
    # Volunteering
    "__VOLUNTEER_ORG__": "Volunteer Organization",
    "__VOLUNTEER_LOCATION__": "Location",
    "__VOLUNTEER_ROLE__": "Volunteer Role",
    "__VOLUNTEER_DATES__": "Volunteer Dates",
    "__VOLUNTEER_DESC__": "Volunteer Description",
}


def load_template(filepath):
    """Loads the LaTeX template content from a file."""
    try:
        with open(filepath, "r") as f:
            return f.read()
    except FileNotFoundError:
        print(f"Error: Template file '{filepath}' not found.")
        print("Please ensure 'base_template.tex' is in the same directory.")
        return None


def get_user_input(placeholder_key, description):
    """Prompts the user for input with a descriptive label."""
    # Use the description as the default prompt hint
    user_input = input(
        f"Enter {description} [{placeholder_key.strip('_')}] (or leave blank to skip): "
    )
    # If the user enters nothing, we will use the default/placeholder text
    return user_input.strip()


def compile_latex_to_pdf(filename, pdf_output=None):
    """Compiles the LaTeX file into a PDF using pdflatex."""
    print(f"\nAttempting to compile '{filename}' to PDF...")

    # Change to the directory containing the .tex file for compilation
    tex_dir = os.path.dirname(filename)
    tex_basename = os.path.basename(filename)

    # The pdflatex compiler often needs to run twice to resolve cross-references
    # and table of contents, but once is usually fine for a simple resume.

    try:
        # Run pdflatex command in the correct directory
        result = subprocess.run(
            ["pdflatex", "-interaction=batchmode", tex_basename],
            cwd=tex_dir if tex_dir else ".",
            check=False,  # Don't raise an exception if pdflatex fails, we check return code below
            capture_output=True,
            text=True,
        )

        if result.returncode == 0:
            final_pdf = pdf_output if pdf_output else filename.replace(".tex", ".pdf")
            print(f"✅ Compilation successful! PDF created: '{final_pdf}'.")
            return True
        else:
            print("❌ Compilation failed. Check the .log file for errors.")
            print(f"Error output:\n{result.stderr}")
            return False

    except FileNotFoundError:
        print("\n\n*****************************************************************")
        print("CRITICAL ERROR: 'pdflatex' command not found.")
        print(
            "Please ensure you have a LaTeX distribution (like TeX Live or MiKTeX) installed."
        )
        print("*****************************************************************\n")
        return False

    except Exception as e:
        print(f"An unexpected error occurred during compilation: {e}")
        return False


def cleanup_auxiliary_files(filename):
    """Removes the temporary files generated by pdflatex."""
    base_name, _ = os.path.splitext(filename)

    for ext in AUX_FILES:
        temp_file = base_name + ext
        if os.path.exists(temp_file):
            os.remove(temp_file)
            # print(f"Cleaned up {temp_file}") # Optional: show cleanup steps


def generate_resume():
    """Main function to collect input and generate the resume."""
    print("\n--- LaTeX Resume Builder ---")
    print(f"Please enter the details for your CV.")
    time.sleep(0.5)

    # 1. Load the template
    template_content = load_template(TEMPLATE_FILE)
    if not template_content:
        return

    # 2. Collect user input and perform replacement
    replacements = {}
    full_name = ""
    for key, description in PLACEHOLDERS.items():
        user_value = get_user_input(key, description)
        if user_value:
            replacements[key] = user_value
            if key == "__FULL_NAME__":
                full_name = user_value.replace(" ", "_")
        else:
            replacements[key] = description

    # 3. Set dynamic file names based on user's full name
    if full_name:
        output_file = f"userdata/cv/{full_name}_resume.tex"
        pdf_file = f"userdata/cv/{full_name}_resume.pdf"
    else:
        output_file = OUTPUT_FILE
        pdf_file = PDF_FILE

    final_content = template_content
    for key, value in replacements.items():
        final_content = final_content.replace(key, value)

    # 4. Create output directory and save the new LaTeX file
    os.makedirs(os.path.dirname(output_file), exist_ok=True)
    try:
        with open(output_file, "w") as f:
            f.write(final_content)

        print(f"\n📄 Text file saved: '{output_file}'.")

    except IOError:
        print(f"Error: Could not write to the output file '{output_file}'.")
        return

    # 5. Compile to PDF
    if compile_latex_to_pdf(output_file, pdf_file):
        # 6. Clean up temporary files
        cleanup_auxiliary_files(output_file)
        print(f"✨ Cleanup complete. Your final PDF is ready: '{pdf_file}'.")


if __name__ == "__main__":
    generate_resume()
