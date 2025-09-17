from pypdf import PdfReader


def parse_pdf():
    pdf_path = input("Enter the path to the PDF file: ")
    reader = PdfReader(pdf_path)
    f = open("userdata/mycv.txt", "w")
    for page in reader.pages:
        text = page.extract_text()
        f.write(text)
    f.close()


parse_pdf()
