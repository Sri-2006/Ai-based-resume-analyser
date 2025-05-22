import fitz  # PyMuPDF
import nltk
from nltk.tokenize import word_tokenize

nltk.download('punkt')

# Function to extract text from the uploaded PDF
def extract_text_from_pdf(path):
    doc = fitz.open(path)
    text = ""
    for page in doc:
        text += page.get_text()
    return text

# Main analyzer function that returns resume analysis
def analyze_resume(filepath):
    text = extract_text_from_pdf(filepath)
    tokens = word_tokenize(text.lower())

    # Define a simple skill set for matching
    skills = [
        'python', 'java', 'sql', 'machine learning', 'data analysis',
        'communication', 'teamwork', 'problem solving', 'django', 'flask'
    ]

    matched_skills = [skill for skill in skills if skill in tokens]

    result = {
        "skills": matched_skills,
        "score": len(matched_skills) * 10,
        "summary": f"Found {len(matched_skills)} matching skills."
    }

    return result
