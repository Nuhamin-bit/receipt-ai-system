import openai
import json

def parse_receipt(text):
    prompt = f"""
    Extract structured JSON from this receipt:

    Text:
    {text}

    Return JSON with:
    vendor, amount, date, items, category
    """

    response = openai.ChatCompletion.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    return json.loads(response["choices"][0]["message"]["content"])