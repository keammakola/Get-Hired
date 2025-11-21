#!/usr/bin/env python3
"""
Get-Hired Main Application
Career companion using AI to polish CVs, guide cover letters, and help secure jobs.
"""

import os
import sys
from pathlib import Path

# Add src directory to path for imports
sys.path.append(str(Path(__file__).parent))

from cv_analyser import cv_analyser
from job_collector import job_scraper, file_creator
from cover_creator import cover_creator
from cv_builder import generate_resume


def display_menu():
    """Display the main menu options."""
    print("\n" + "=" * 50)
    print("🎯 GET-HIRED - Your Career Companion")
    print("=" * 50)
    print("1. 📊 Analyze CV (PDF)")
    print("2. 🔍 Scrape Job Posting")
    print("3. 📝 Generate Cover Letter")
    print("4. 🏗️  Build CV")
    print("5. 🚪 Exit")
    print("=" * 50)


def analyze_cv():
    """Handle CV analysis functionality."""
    print("\n📊 CV Analysis")
    print("-" * 20)

    cv_path = input("Enter path to your CV (PDF): ").strip()

    if not os.path.exists(cv_path):
        print("❌ File not found. Please check the path.")
        return

    if not cv_path.lower().endswith(".pdf"):
        print("❌ Please provide a PDF file.")
        return

    try:
        print("🔄 Analyzing your CV...")
        cv_analyser(cv_path)
        print("✅ Analysis complete! Check userdata/analysis/cv_score.md")
    except Exception as e:
        print(f"❌ Error analyzing CV: {e}")


def scrape_job():
    """Handle job scraping functionality."""
    print("\n🔍 Job Scraping")
    print("-" * 20)

    try:
        name, info = job_scraper()

        # Save the job information
        filename = name.replace(" ", "_").replace("-", "_")
        filepath = file_creator("jobs", filename, info)

        print(f"✅ Job information saved to: {filepath}")
        return filepath
    except Exception as e:
        print(f"❌ Error scraping job: {e}")
        return None


def generate_cover_letter():
    """Handle cover letter generation."""
    print("\n📝 Cover Letter Generation")
    print("-" * 30)

    cv_path = input("Enter path to your CV (PDF): ").strip()
    job_path = input("Enter path to job posting (txt/md): ").strip()

    if not os.path.exists(cv_path):
        print("❌ CV file not found.")
        return

    if not os.path.exists(job_path):
        print("❌ Job posting file not found.")
        return

    try:
        print("🔄 Generating cover letter...")
        cover_creator(cv_path, job_path)
        print("✅ Cover letter generated! Check userdata/covers/cover_letter.md")
    except Exception as e:
        print(f"❌ Error generating cover letter: {e}")


def build_cv():
    """Handle CV building functionality."""
    print("\n🏗️ LaTeX CV Builder")
    print("-" * 20)

    try:
        generate_resume()
    except Exception as e:
        print(f"❌ Error building CV: {e}")


def main():
    """Main application loop."""
    print("Welcome to Get-Hired! 🚀")

    while True:
        display_menu()

        try:
            choice = input("\nSelect an option (1-5): ").strip()

            if choice == "1":
                analyze_cv()
            elif choice == "2":
                scrape_job()
            elif choice == "3":
                generate_cover_letter()
            elif choice == "4":
                build_cv()
            elif choice == "5":
                print(
                    "\n👋 Thank you for using Get-Hired! Good luck with your job search!"
                )
                break
            else:
                print("❌ Invalid option. Please select 1-5.")

        except KeyboardInterrupt:
            print("\n\n👋 Goodbye!")
            break
        except Exception as e:
            print(f"❌ An error occurred: {e}")


if __name__ == "__main__":
    main()
