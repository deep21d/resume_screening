import pdfplumber

def parse_resume(file_path: str) -> str:
    """
    Extracts text from a PDF resume.

    Args:
        file_path (str): Path to the resume PDF

    Returns:
        str: Extracted text
    """
    text = ""

    with pdfplumber.open(file_path) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n"

    return text.strip()