
from fastapi import FastAPI, File, UploadFile, Form
from fastapi.middleware.cors import CORSMiddleware
import shutil
from nlp_engine import extract_text_from_pdf, extract_skills, calculate_match_score, get_missing_skills

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.get("/health")
def health():
    return {"status": "healthy"}

@app.post("/extract-skills")
async def extract_skills_endpoint(file: UploadFile = File(...)):
    path = "temp_resume.pdf"
    with open(path, "wb") as f:
        shutil.copyfileobj(file.file, f)
    text = extract_text_from_pdf(path)
    skills = extract_skills(text)
    return {"skills": skills, "skill_count": len(skills)}

@app.post("/match-resume")
async def match_resume_endpoint(file: UploadFile = File(...), job_description: str = Form(...)):
    path = "temp_resume.pdf"
    with open(path, "wb") as f:
        shutil.copyfileobj(file.file, f)
    text = extract_text_from_pdf(path)
    resume_skills = extract_skills(text)
    score, job_skills = calculate_match_score(resume_skills, job_description)
    missing = get_missing_skills(resume_skills, job_skills)
    if score >= 75:
        rec = "Strong candidate"
    elif score >= 50:
        rec = "Moderate fit"
    else:
        rec = "Weak match"
    return {
        "match_score": score,
        "resume_skills": resume_skills,
        "job_skills": job_skills,
        "missing_skills": missing,
        "recommendation": rec
    }