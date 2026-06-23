from datasets import load_dataset
import pandas as pd

from models.llm_api import get_response
from evaluation.toxicity_detector import detect_toxicity
from evaluation.injection_detector import detect_injection
from evaluation.scoring import compute_safety_score
# Load dataset
ds = load_dataset("lmsys/toxic-chat", "toxicchat0124")

data = ds["test"].select(range(10))  # small test sample

results = []

for item in data:

    prompt = item["user_input"]

    # Step 1: Get AI response
    response = get_response(prompt)

    # Step 2: Safety checks
    toxicity = detect_toxicity(response)
    injection = detect_injection(prompt)

    # Step 3: Compute safety score
    score = compute_safety_score(toxicity, injection)

    # Step 4: Save results
    results.append({
        "prompt": prompt,
        "response": response,
        "toxicity": toxicity,
        "injection_risk": injection,
        "safety_score": score
    })

df = pd.DataFrame(results)
df.to_csv("outputs/results.csv", index=False)

print("DONE: AI QA pipeline executed successfully")