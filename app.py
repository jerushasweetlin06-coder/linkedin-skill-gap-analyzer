from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/analyze", methods=["POST"])
def analyze():
    # Get data from form
    job_role = request.form["job_role"]
    user_skills = request.form["skills"]

    # Convert skills to list
    user_skills_list = [skill.strip().lower() for skill in user_skills.split(",")]

    # Example required skills (you can expand this later)
    required_skills_dict = {
        "data scientist": ["python", "machine learning", "statistics", "sql"],
        "web developer": ["html", "css", "javascript", "flask"],
        "software engineer": ["python", "data structures", "algorithms", "git"]
    }

    required_skills = required_skills_dict.get(job_role.lower(), [])

    # Find matched and missing skills
    matched_skills = [skill for skill in required_skills if skill in user_skills_list]
    missing_skills = [skill for skill in required_skills if skill not in user_skills_list]

    # Calculate match percentage
    if len(required_skills) > 0:
        match_percentage = (len(matched_skills) / len(required_skills)) * 100
    else:
        match_percentage = 0

    return render_template(
        "result.html",
        job_role=job_role,
        match_percentage=round(match_percentage, 2),
        matched_skills=matched_skills,
        missing_skills=missing_skills
    )


if __name__ == "__main__":
    app.run(debug=True)