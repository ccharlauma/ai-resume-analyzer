import os

from flask import Flask, render_template, request
from utils import extract_text, extract_keywords

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None

    if request.method == 'POST':
        file = request.files['resume']
        job_desc = request.form['job']

        file.save("resume.pdf")

        resume_text = extract_text("resume.pdf")
        resume_words = extract_keywords(resume_text)
        job_words = extract_keywords(job_desc)

        matched = resume_words & job_words
        missing = job_words - resume_words

        score = (len(matched) / len(job_words)) * 100

        if score < 40:
            level = "Weak 😕"
        elif score < 70:
            level = "Average ⚖️"
        else:
            level = "Strong 💪"


        # ✅ CREATE suggestions FIRST
        suggestions = []

        for skill in missing:
            suggestions.append(f"Add {skill} related projects or experience")

        # ✅ THEN use it
        result = {
            "score": round(score, 2),
            "matched": matched,
            "missing": missing,
            "suggestions": suggestions,  # also fixed key name
            "level": level
        }

    return render_template("index.html", result=result)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)