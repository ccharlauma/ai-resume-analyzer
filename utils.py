import PyPDF2
import spacy

nlp = spacy.load("en_core_web_sm")

def extract_text(file_path):
    text = ""
    with open(file_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        for page in reader.pages:
            text += page.extract_text()
    return text

def extract_keywords(text):
    doc = nlp(text)
    keywords = []

    for token in doc:
        if token.is_alpha and not token.is_stop:
            keywords.append(token.text.lower())

    return set(keywords)