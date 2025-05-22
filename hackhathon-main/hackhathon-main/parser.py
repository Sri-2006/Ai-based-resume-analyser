import docx2txt
import PyPDF2
import spacy

nlp = spacy.load("en_core_web_sm")

def extract_text(file):
    if file.filename.endswith('.pdf'):
        reader = PyPDF2.PdfReader(file)
        return " ".join(page.extract_text() for page in reader.pages)
    elif file.filename.endswith('.docx'):
        return docx2txt.process(file)
    return ""

def analyze_resume(text):
    doc = nlp(text)
    skills = [ent.text for ent in doc.ents if ent.label_ == "SKILL"]
    return {
        "summary": text[:300],  # Just sample
        "skills": skills,
        "word_count": len(text.split())
    }
