from transformers import pipeline

print("Loading model...")

llm = pipeline(
    "text-generation",
    model="distilgpt2"
)

print("Model loaded!")

def get_response(prompt):

    result = llm(
        prompt,
        max_new_tokens=100,
        do_sample=True,
        temperature=0.7
    )

    return result[0]["generated_text"]