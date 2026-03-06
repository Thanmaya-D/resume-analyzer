from flask import Flask, render_template, request
import PyPDF2
import os

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER


def extract_text(pdf_file):
    reader = PyPDF2.PdfReader(pdf_file)
    text = ""

    for page in reader.pages:
        text += page.extract_text()

    return text


@app.route("/", methods=["GET", "POST"])
def index():
    result = ""

    if request.method == "POST":
        file = request.files["resume"]
        path = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)
        file.save(path)

        text = extract_text(path)

        skills = ["python","java","c++","sql","html","css","javascript","machine learning","data science"]

        found_skills = []

        for skill in skills:
             if skill in text.lower():
                 found_skills.append(skill)

        result = "Skills found: " + " , ".join(found_skills)

    return render_template("index.html", result=result)


if __name__ == "__main__":
    app.run(debug=True)
