import os
import google.generativeai as genai
from dotenv import load_dotenv

# Load .env file
load_dotenv()

def init_gemini():
    api_key = os.getenv("GEMINI_API_KEY")
    if api_key:
        genai.configure(api_key=api_key)
        print("Gemini initialized using API key from .env")
        return genai.GenerativeModel("gemini-2.5-flash")

    print("No API key found. Using mock fallback.")
    return None


model = init_gemini()


def generate_script(product, audience, tone):
    prompt = f"""
    Write a 30-second advertisement script using the structure:
    HOOK → BODY → CTA.

    Product: {product}
    Target audience: {audience}
    Tone: {tone}

    Also include a short 'Visual Hook' suggestion.
    """

    # REAL MODEL RESPONSE
    if model:
        try:
            response = model.generate_content(prompt)
            return response.text
        except Exception as e:
            print("LLM error:", e)

    # FALLBACK
    return f"""
HOOK: The camera zooms dramatically into a jar of {product}.

BODY: In a {tone.lower()} tone, the narrator explains why {audience} love this product.

CTA: “Try {product} today — experience the flavour explosion!”

Visual Hook: Close-up of the product opening.
"""


def extract_visual_hook(script):
    if "Visual Hook" in script:
        return script.split("Visual Hook")[1].replace(":", "").strip()

    return "Close-up of product with dramatic lighting."
