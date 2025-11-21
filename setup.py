#!/usr/bin/env python3
"""
Setup script for Get-Hired application
Creates necessary directories and installs dependencies
"""

import os
import subprocess
import sys


def create_directories():
    """Create required directory structure"""
    directories = [
        "userdata/cv",
        "userdata/analysis",
        "userdata/covers",
        "userdata/jobs",
    ]

    for directory in directories:
        os.makedirs(directory, exist_ok=True)
        print(f"✓ Created directory: {directory}")


def install_dependencies():
    """Install Python dependencies"""
    print("Installing Python dependencies...")
    try:
        subprocess.run(
            [sys.executable, "-m", "pip", "install", "-r", "requirements.txt"],
            check=True,
        )
        print("✓ Python dependencies installed")
    except subprocess.CalledProcessError:
        print("❌ Failed to install Python dependencies")
        return False
    return True


def check_latex():
    """Check if LaTeX is installed"""
    try:
        subprocess.run(["pdflatex", "--version"], capture_output=True, check=True)
        print("✓ LaTeX installation found")
        return True
    except (subprocess.CalledProcessError, FileNotFoundError):
        print("❌ LaTeX not found. Please install TeX Live or MiKTeX")
        print("Ubuntu/Debian: sudo apt install texlive-latex-extra")
        print("macOS: brew install --cask mactex")
        return False


def create_env_file():
    """Create .env file if it doesn't exist"""
    if not os.path.exists(".env"):
        with open(".env", "w") as f:
            f.write("# Add your API keys here\n")
            f.write("GEMINI_API_KEY=your_gemini_api_key_here\n")
            f.write("OPENAI_API_KEY=your_openai_api_key_here\n")
        print("✓ Created .env file - please add your API keys")
    else:
        print("✓ .env file already exists")


def main():
    print("🚀 Setting up Get-Hired application...\n")

    create_directories()
    print()

    if not install_dependencies():
        sys.exit(1)
    print()

    check_latex()
    print()

    create_env_file()
    print()

    print("✅ Setup complete!")
    print("\nNext steps:")
    print("1. Add your API keys to the .env file")
    print("2. Run: python3 src/main.py")


if __name__ == "__main__":
    main()
