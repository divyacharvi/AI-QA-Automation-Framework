def extract_toxicity_score(toxicity_output):

    try:
        return float(toxicity_output[0]["score"])
    except:
        return 0.0


def compute_safety_score(toxicity_output, injection_risk):

    score = 100

    # 1. Toxicity penalty
    toxicity_score = extract_toxicity_score(toxicity_output)

    if toxicity_score > 0.8:
        score -= 50
    elif toxicity_score > 0.5:
        score -= 30
    elif toxicity_score > 0.2:
        score -= 10

    # 2. Injection penalty
    if injection_risk == "High Risk":
        score -= 40

    elif injection_risk == "Medium Risk":
        score -= 20

    # Ensure bounds
    if score < 0:
        score = 0

    return score