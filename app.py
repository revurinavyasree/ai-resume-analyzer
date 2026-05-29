from flask import Flask, render_template, request, redirect, url_for, session, flash, send_from_directory
from werkzeug.utils import secure_filename
from functools import wraps
import os

from analyzer.extractor import extract_text
from analyzer.skills import detect_skills
from analyzer.ats import calculate_ats_score
from analyzer.matcher import company_match
from analyzer.recommendations import generate_recommendations
from analyzer.questions import generate_questions
from analyzer.strengths import analyze_resume
from analyzer.jd_matcher import calculate_jd_match
from analyzer.report_generator import generate_pdf_report

from database.db import register_user, login_user, save_resume, get_user_resumes

app = Flask(__name__)
app.secret_key = "resumeanalyzer_secret_2024"

UPLOAD_FOLDER  = "uploads"
REPORTS_FOLDER = "reports"

app.config["UPLOAD_FOLDER"]  = UPLOAD_FOLDER
app.config["REPORTS_FOLDER"] = REPORTS_FOLDER

ALLOWED_EXTENSIONS = {"pdf", "docx"}

for folder in [UPLOAD_FOLDER, REPORTS_FOLDER, "database"]:
    if not os.path.exists(folder):
        os.makedirs(folder)


def allowed_file(filename):
    return "." in filename and \
           filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS


def login_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        if "user_id" not in session:
            flash("Please login to continue.", "warning")
            return redirect(url_for("login"))
        return f(*args, **kwargs)
    return decorated


# ── AUTH ROUTES ──────────────────────────────────────────────────────────────

@app.route("/register", methods=["GET", "POST"])
def register():
    if "user_id" in session:
        return redirect(url_for("index"))
    if request.method == "POST":
        name     = request.form.get("name", "").strip()
        email    = request.form.get("email", "").strip()
        password = request.form.get("password", "").strip()
        if not name or not email or not password:
            flash("All fields are required.", "danger")
            return render_template("register.html")
        if len(password) < 6:
            flash("Password must be at least 6 characters.", "danger")
            return render_template("register.html")
        success, message = register_user(name, email, password)
        if success:
            flash("Account created! Please login.", "success")
            return redirect(url_for("login"))
        else:
            flash(message, "danger")
    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if "user_id" in session:
        return redirect(url_for("index"))
    if request.method == "POST":
        email    = request.form.get("email", "").strip()
        password = request.form.get("password", "").strip()
        if not email or not password:
            flash("Email and password are required.", "danger")
            return render_template("login.html")
        success, data = login_user(email, password)
        if success:
            session["user_id"]    = data["id"]
            session["user_name"]  = data["name"]
            session["user_email"] = data["email"]
            flash(f"Welcome back, {data['name']}!", "success")
            return redirect(url_for("index"))
        else:
            flash(data, "danger")
    return render_template("login.html")


@app.route("/logout")
def logout():
    session.clear()
    flash("You have been logged out.", "info")
    return redirect(url_for("login"))


# ── MAIN ROUTES ───────────────────────────────────────────────────────────────

@app.route("/")
@login_required
def index():
    resumes = get_user_resumes(session["user_id"])
    return render_template("index.html", resumes=resumes)


@app.route("/upload", methods=["POST"])
@login_required
def upload_resume():
    if "resume" not in request.files:
        flash("No file uploaded.", "danger")
        return redirect(url_for("index"))
    file = request.files["resume"]
    if file.filename == "":
        flash("No file selected.", "danger")
        return redirect(url_for("index"))
    if not allowed_file(file.filename):
        flash("Only PDF and DOCX files allowed.", "danger")
        return redirect(url_for("index"))

    filename = secure_filename(file.filename)
    filepath = os.path.join(app.config["UPLOAD_FOLDER"], filename)
    file.save(filepath)

    try:
        resume_text = extract_text(filepath)
    except Exception as e:
        flash(f"Error reading file: {e}", "danger")
        return redirect(url_for("index"))

    job_description = request.form.get("job_description", "")

    skills                = detect_skills(resume_text)
    ats_score             = calculate_ats_score(resume_text, skills)
    jd_match_score        = calculate_jd_match(resume_text, job_description) if job_description else 0
    questions             = generate_questions(skills)
    strengths, weaknesses = analyze_resume(resume_text, skills)
    company_scores        = company_match(skills)
    recommendations       = generate_recommendations(resume_text, skills)
    pdf_report            = generate_pdf_report(filename, ats_score, skills, recommendations)

    save_resume(session["user_id"], filename, ats_score, skills)

    return render_template(
        "result.html",
        resume_text     = resume_text,
        skills          = skills,
        ats_score       = ats_score,
        jd_match_score  = jd_match_score,
        company_scores  = company_scores,
        recommendations = recommendations,
        pdf_report      = filename,
        questions       = questions,
        strengths       = strengths,
        weaknesses      = weaknesses,
    )


@app.route("/history")
@login_required
def history():
    resumes = get_user_resumes(session["user_id"])
    return render_template("history.html", resumes=resumes)


@app.route("/reports/<filename>")
@login_required
def download_report(filename):
    return send_from_directory(
        app.config["REPORTS_FOLDER"],
        filename,
        as_attachment=True
    )


if __name__ == "__main__":
    app.run(debug=True)