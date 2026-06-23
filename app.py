from flask import Flask, render_template, request

from models.llm_api import get_response
from evaluation.toxicity_detector import detect_toxicity
from evaluation.injection_detector import detect_injection
from evaluation.security_detector import detect_security_risk
from evaluation.scoring import compute_safety_score

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():

    result = None

    if request.method == "POST":

        prompt = request.form["prompt"]

        # Generate response
        response = get_response(prompt)

        # Run safety checks
        toxicity = detect_toxicity(response)
        injection = detect_injection(prompt)
        security = detect_security_risk(response)

        score = compute_safety_score(
            toxicity,
            injection,
            security
        )

        try:
            toxicity_score = round(
                toxicity[0]["score"],
                3
            )

            toxicity_label = toxicity[0]["label"]

        except Exception:

            toxicity_score = 0
            toxicity_label = "unknown"

        result = {
            "prompt": prompt,
            "response": response,
            "toxicity_label": toxicity_label,
            "toxicity_score": toxicity_score,
            "injection": injection,
            "security": security,
            "score": score
        }

    return render_template(
        "index.html",
        result=result
    )

if __name__ == "__main__":
    app.run(debug=True)