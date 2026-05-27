import PyPDF2, spacy
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from skills_database import SKILLS_DB

try:
    nlp = spacy.load("en_core_web_sm")
except OSError:
    nlp = None

def extract_text_from_pdf(path):
    text = ""
    try:
        with open(path, "rb") as f:
            for page in PyPDF2.PdfReader(f).pages:
                page_text = page.extract_text()
                if page_text:
                    text += page_text + "\n"
    except Exception as e:
        print(f"Error: {e}")
    return text

def extract_skills(text):
    found = []
    for category, skills in SKILLS_DB.items():
        for skill in skills:
            if skill.lower() in text.lower() and skill not in found:
                found.append(skill)
    if nlp:
        try:
            for ent in nlp(text).ents:
                if ent.label_ in ["ORG", "PRODUCT"] and ent.text not in found:
                    found.append(ent.text)
        except:
            pass
    return found

def calculate_match_score(resume_skills, job_description):
    job_skills = []
    for category, skills in SKILLS_DB.items():
        for skill in skills:
            if skill.lower() in job_description.lower() and skill not in job_skills:
                job_skills.append(skill)
    resume_text = ", ".join(resume_skills) if resume_skills else "no skills found"
    try:
        vectorizer = TfidfVectorizer().fit_transform([resume_text, job_description])
        similarity = cosine_similarity(vectorizer[0:1], vectorizer[1:2])[0][0] if vectorizer.shape[0] == 2 else 0.0
        return round(similarity * 100, 2), job_skills
    except:
        return 0.0, job_skills

def get_missing_skills(resume_skills, job_skills):
    return [skill for skill in job_skills if skill not in resume_skills]
