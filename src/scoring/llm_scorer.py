import os
from google import genai
from dotenv import load_dotenv

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

SYSTEM_PROMPT = """
You are a strict customer support quality auditor.

Evaluate the conversation on:
1. Empathy (1-5)
2. Compliance with policy (1-5)
3. Resolution effectiveness (1-5)

Return STRICT JSON only:
{
  "empathy_score": number,
  "compliance_score": number,
  "resolution_score": number,
  "summary": "brief explanation"
}
"""

def score_conversation(text):
    response = client.models.generate_content(
        model="gemini-flash-latest",
        contents=text,
        config={
            "system_instruction": SYSTEM_PROMPT,
            "temperature": 0
        }
    )

    return response.text