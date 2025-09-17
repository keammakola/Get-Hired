from pypdf import PdfReader
import os


def parse_pdf():
    try:
        pdf_path = input("Enter the path to the PDF file: ")
        if not os.path.exists(pdf_path):
            raise FileNotFoundError("File does not exist")

        reader = PdfReader(pdf_path)
        os.makedirs("userdata/processed cv", exist_ok=True)

        with open("userdata/processed cv/mycv.txt", "w") as f:
            for page in reader.pages:
                text = page.extract_text()
                f.write(text)

    except FileNotFoundError as e:
        print(f"Error: {e}")
        return
    except Exception as e:
        print(f"Error: {e}")
        return
