import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

# Configure the AI with your API Key
genai.configure(api_key = os.getenv("GEMINI_API_KEY"))

def generate_readme_text(code_context: str, notes: str = "") -> str:
    if not code_context:
        return "No code context provided."
    
    model = genai.GenerativeModel('gemini-2.5-flash')

    # Building the prompt
    prompt = f"""
    You are an expert developer and technical writer. 
    Your task is to generate a professional README.md file for the project code provided below.

    --- USER NOTES ---
    {notes}

    --- CODE CONTEXT ---
    {code_context}

    --- INSTRUCTIONS ---
    1. Analyze the file structure and code to understand what the project does.
    2. Write a clear Title and Description.
    3. Include a 'Features' section.
    4. Include a 'Installation' and 'Usage' section based on the code (look for requirements.txt, package.json, etc).
    5. Output ONLY raw Markdown code. Do not wrap it in markdown blocks (```markdown). Also, do not include any emojis.
    """

    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"AI Error: {str(e)}"