from transformers import pipeline

# LOAD MODEL (THIS WAS MISSING)
toxicity_model = pipeline(
    "text-classification",
    model="unitary/toxic-bert"
)

def detect_toxicity(text):

    # safety trim (prevents crashes)
    text = str(text)[:300]

    result = toxicity_model(text)

    return result