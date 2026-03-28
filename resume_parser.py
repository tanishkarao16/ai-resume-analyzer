import pdfplumber


def parse_resume(uploaded_file):
    """
    Extracts text from uploaded PDF resume
    """

    text = ""

    with pdfplumber.open(uploaded_file) as pdf:

        for page in pdf.pages:

            page_text = page.extract_text()

            if page_text:
                text += page_text

    return text