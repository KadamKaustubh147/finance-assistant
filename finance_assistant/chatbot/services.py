import google.generativeai as genai

from decouple import config
from markdown2 import markdown as mark_html


genai.configure(api_key=config("GEMINI_API_KEY"))
model = genai.GenerativeModel("gemini-1.5-flash")


def response_ai(question):
    response = model.generate_content(question)
    return mark_html(response.text)

print(response_ai("Hello"))