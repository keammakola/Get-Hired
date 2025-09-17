from pypdf import PdfReader
import os


def parse_pdf():
    pdf_path = input("Enter the path to the PDF file: ")
    reader = PdfReader(pdf_path)

    os.makedirs("userdata/processed cv", exist_ok=True)

    f = open("userdata/processed cv/mycv.txt", "w")
    for page in reader.pages:
        text = page.extract_text()
        f.write(text)
    f.close()


parse_pdf()
