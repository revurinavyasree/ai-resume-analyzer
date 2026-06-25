import os
import json
from google import genai
from google.genai import types

# Get the API key from .env file
api_key = os.environ.get("GEMINI_API_KEY")

# Create the Gemini client only if we have a key
if api_key:
    client = genai.Client(api_key=api_key)
else:
    client = None


def ask_gemini(prompt):
    """Send a prompt to Gemini and get back a plain text answer."""
    if client is None:
        return None

    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )
        return response.text
    except Exception as e:
        print("Gemini error:", e)
        return None


def ask_gemini_json(prompt):
    """Send a prompt to Gemini and get back a JSON answer (as a dict)."""
    if client is None:
        return None

    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt,
            config=types.GenerateContentConfig(response_mime_type="application/json")
        )
        return json.loads(response.text)
    except Exception as e:
        print("Gemini error:", e)
        return None