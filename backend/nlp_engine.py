import PyPDF2
import spacy
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from skills_database import SKILLS_DB

nlp = spacy.load("en_core_web_sm")

def extract_text_from_pdf(path):
    text = ""
    with open(path, "rb") as f:
        reader = PyPDF2.PdfReader(f)
        for page in reader.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n"
    return text

def extract_skills(text):
    found = []
    for category, skills in SKILLS_DB.items():
        for skill in skills:
            if skill.lower() in text.lower():
                if skill not in found:
                    found.append(skill)
    doc = nlp(text)
    for ent in doc.ents:
        if ent.label_ in ["ORG", "PRODUCT"]:
            if ent.text not in found:
                found.append(ent.text)
    return found

def calculate_match_score(resume_skills, job_description):
    job_skills = []
    for category, skills in SKILLS_DB.items():
        for skill in skills:
            if skill.lower() in job_description.lower():
                if skill not in job_skills:
                    job_skills.append(skill)
    resume_text = ", ".join(resume_skills) if resume_skills else ""
    docs = [resume_text, job_description]
    vectorizer = TfidfVectorizer().fit_transform(docs)
    similarity = 0.0
    if vectorizer.shape[0] == 2:
        similarity = cosine_similarity(vectorizer[0:1], vectorizer[1:2])[0][0]
    return round(similarity * 100, 2), job_skills

def get_missing_skills(resume_skills, job_skills):
    missing = []
    for skill in job_skills:
        if skill not in resume_skills:
            missing.append(skill)
    return missing