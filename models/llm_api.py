from transformers import pipeline

# lightweight model (fast + stable)
llm = pipeline("text-generation", model="gpt2")

def get_response(prompt):
    result = llm(
        prompt,
        max_new_tokens=80,
        do_sample=True,
        temperature=0.7,
        truncation=True,
        pad_token_id=50256
    )

    return result[0]["generated_text"]