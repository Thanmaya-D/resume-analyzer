from flask import Flask, render_template, request
import os

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER


@app.route("/", methods=["GET","POST"])
def home():

    result = []
    missing = []
    score = 0

    if request.method == "POST":

        file = request.files["resume"]

        if file.filename != "":

            filepath = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)
            file.save(filepath)

            result = ["python","java","sql","html","css","javascript"]

            required = ["python","java","sql","html","css","javascript","react","aws"]

            missing = [skill for skill in required if skill not in result]

            score = int((len(result)/len(required))*100)

    return render_template("index.html", result=result, missing=missing, score=score)


if __name__ == "__main__":
    app.run(debug=True)
