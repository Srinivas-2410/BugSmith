import os
import google.generativeai as genai
from dotenv import load_dotenv
load_dotenv()

# Configure Gemini
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-1.5-flash")

def generate_bug_report(description, severity, environment):
    prompt = f"""
Act like a QA assistant. A tester reports the bug:
"{description}"

Generate a detailed bug report including:
1. Steps to reproduce
2. Probable bug category (UI, Backend, Logic, Performance, etc.)
3. Suspected code component (if possible)
4. Severity: {severity}
5. Environment: {environment}
    """

    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Error generating report: {str(e)}"
