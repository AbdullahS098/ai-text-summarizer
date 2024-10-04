import google.generativeai as genai
from time import time

# Configure the Gemini API (replace with your actual API key)
genai.configure(api_key='AIzaSyDG9a6Bfua3VCwcoPxQrmcvFbfyHsDGiN8')

# Rate limiting variables
RATE_LIMIT = 5  # Number of requests allowed per minute
request_times = []

def summarize_text(text, max_length=150):
    # Implement rate limiting
    current_time = time()
    request_times.append(current_time)
    request_times[:] = [t for t in request_times if current_time - t < 60]

    if len(request_times) > RATE_LIMIT:
        raise Exception("Rate limit exceeded. Please try again later.")

    try:
        model = genai.GenerativeModel('gemini-pro')
        prompt = f"Summarize the following text in about {max_length} words:\n\n{text}"
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        raise Exception(f"Error in text summarization: {str(e)}")