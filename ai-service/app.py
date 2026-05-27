from flask import Flask, request, jsonify
import PyPDF2

app = Flask(__name__)

# Skills database
SKILLS_DB = ["Python", "Java", "SQL", "React", "Machine Learning", "AI", "HTML", "CSS"]

def extract_text(file):
    reader = PyPDF2.PdfReader(file)
    text = ""
    for page in reader.pages:
        text += page.extract_text()
    return text

def extract_skills(text):
    found = []
    for skill in SKILLS_DB:
        if skill.lower() in text.lower():
            found.append(skill)
    return found

@app.route("/analyze", methods=["POST"])
def analyze():
    file = request.files["file"]

    text = extract_text(file)
    skills = extract_skills(text)

    return jsonify({"skills": skills})

if __name__ == "__main__":
    app.run(port=5000)