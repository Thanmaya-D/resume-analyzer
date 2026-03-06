import PyPDF2

skills = [
"python","java","sql","html","css","javascript",
"react","nodejs","aws","docker","git","flask"
]

def extract_text(file):

    reader = PyPDF2.PdfReader(file)
    text = ""

    for page in reader.pages:
        text += page.extract_text()

    return text.lower()


def analyze_resume(text):

    detected = []
    missing = []

    for skill in skills:

        if skill in text:
            detected.append(skill)

        else:
            missing.append(skill)

    score = int((len(detected)/len(skills))*100)

    suggestions = []

    if score < 40:
        suggestions.append("Add more programming projects")

    elif score < 70:
        suggestions.append("Improve resume with more technologies")

    else:
        suggestions.append("Your resume looks strong")

    return detected, missing, score, suggestions
