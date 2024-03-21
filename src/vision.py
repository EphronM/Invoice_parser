from dotenv import load_dotenv
import os
import google.generativeai as genai



load_dotenv()  # take environment variables from .env.



genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))


def get_gemini_response(input,image,prompt):
    model = genai.GenerativeModel('gemini-pro-vision')
    response = model.generate_content([input,image[0],prompt])
    return response.text


