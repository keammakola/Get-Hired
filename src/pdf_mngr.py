from pypdf import PdfReader
import os


def parse_pdf():
    """
    Parse the given PDF file and save the text content to userdata/unprocessed cv/mycv.md

    Parameters
    ----------
    None

    Returns
    -------
    None

    Raises
    ------
    FileNotFoundError
        If the file does not exist
    Exception
        If any other error occurs during parsing
    """
    try:
        pdf_path = input("Enter the path to the PDF file: ")
        if not os.path.exists(pdf_path):
            raise FileNotFoundError("File does not exist")

        reader = PdfReader(pdf_path)
        os.makedirs("userdata/unprocessed cv", exist_ok=True)

        with open("userdata/unprocessed cv/mycv.md", "w") as f:
            for page in reader.pages:
                text = page.extract_text()
                f.write(text)

    except FileNotFoundError as e:
        print(f"Error: {e}")
        return
    except Exception as e:
        print(f"Error: {e}")
        return
