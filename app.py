from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
import os
from werkzeug.utils import secure_filename
from src.job_collector import job_scraper
from src.tools import file_creator, cv_extractor, cv_scorer, cv_improver, cover_letter
from src.cv_collector import collect_cv_info

app = Flask(__name__)
app.secret_key = "your-secret-key-here"
app.config["UPLOAD_FOLDER"] = "uploads"
app.config["MAX_CONTENT_LENGTH"] = 16 * 1024 * 1024  # 16MB max file size

os.makedirs(app.config["UPLOAD_FOLDER"], exist_ok=True)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/upload_cv", methods=["POST"])
def upload_cv():
    if "cv_file" not in request.files:
        flash("No file selected")
        return redirect(url_for("index"))

    file = request.files["cv_file"]
    if file.filename == "":
        flash("No file selected")
        return redirect(url_for("index"))

    if file:
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config["UPLOAD_FOLDER"], filename)
        file.save(filepath)

        try:
            cv_content = cv_extractor(filepath)
            return render_template("cv_uploaded.html", cv_content=cv_content)
        except Exception as e:
            flash(f"Error processing CV: {str(e)}")
            return redirect(url_for("index"))


@app.route("/job_posting", methods=["POST"])
def job_posting():
    job_type = request.form.get("job_type")

    if job_type == "link":
        job_link = request.form.get("job_link")
        try:
            company_name, job_info = job_scraper(job_link)
            file_creator("jobs", company_name, job_info)
            return render_template("job_saved.html", company_name=company_name)
        except Exception as e:
            flash(f"Error scraping job: {str(e)}")
            return redirect(url_for("index"))

    elif job_type == "text":
        company_name = request.form.get("company_name")
        job_info = request.form.get("job_info")
        file_creator("jobs", company_name, job_info)
        return render_template("job_saved.html", company_name=company_name)

    flash("Invalid job posting method")
    return redirect(url_for("index"))


@app.route("/analyze", methods=["POST"])
def analyze():
    cv_content = request.form.get("cv_content")
    company_name = request.form.get("company_name")

    try:
        cv_report = cv_scorer(cv_content, company_name)
        return render_template(
            "analysis.html",
            cv_report=cv_report,
            cv_content=cv_content,
            company_name=company_name,
        )
    except Exception as e:
        flash(f"Error analyzing CV: {str(e)}")
        return redirect(url_for("index"))


@app.route("/improve_cv", methods=["POST"])
def improve_cv():
    cv_report = request.form.get("cv_report")
    cv_content = request.form.get("cv_content")

    try:
        improved_cv = cv_improver(cv_report, cv_content)
        return render_template("improved_cv.html", improved_cv=improved_cv)
    except Exception as e:
        flash(f"Error improving CV: {str(e)}")
        return redirect(url_for("index"))


@app.route("/generate_cover_letter", methods=["POST"])
def generate_cover_letter():
    cv_content = request.form.get("cv_content")
    company_name = request.form.get("company_name")

    try:
        cover_letter_content = cover_letter(cv_content, company_name)
        return render_template("cover_letter.html", cover_letter=cover_letter_content)
    except Exception as e:
        flash(f"Error generating cover letter: {str(e)}")
        return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(debug=True)
