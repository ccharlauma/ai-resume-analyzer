import PyPDF2

def extract_text(file_path):
    text = ""
    with open(file_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        for page in reader.pages:
            text += page.extract_text()
    return text


def extract_keywords(text):
    words = text.lower().split()

    # remove common words manually
    stop_words = {"and", "the", "is", "in", "to", "of", "for", "on", "with"}

    keywords = [word for word in words if word.isalpha() and word not in stop_words]

    return set(keywords)