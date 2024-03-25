from flask import Flask, render_template, request, jsonify
import openai
import os
import requests
from bs4 import BeautifulSoup

# Set up OpenAI API
openai.api_key = os.environ.get("openai_flask_bot_api")

# Links array with relevant info
Links = [
    "https://www.linkedin.com/in/dewarshi-shukla-16072001/",
    "https://github.com/Dewrshi",
]

app = Flask(__name__)

# Function to extract information from the provided links based on the user's query
def extract_info(query):
    for link in Links:
        response = requests.get(link)
        soup = BeautifulSoup(response.content, 'html.parser')
        # Modify this part according to the structure of the page and the type of information you want to extract
        info = soup.find(text=query)
        if info:
            return info.strip()
    return None

# Function to generate prompt using the links and user message
def generate_prompt(message):
    # Extract information based on the user's message
    info = extract_info(message)
    if info:
        prompt = f"User: {message}\nInfo: {info}\n"
    else:
        return "Sorry Information is not available!"
    return prompt

# Function to get response from OpenAI API
def get_response(prompt):
    response = openai.Completion.create(
        engine="davinci",
        prompt=prompt,
        max_tokens=100,
    )
    return response.choices[0].text.strip()

@app.route("/")
def home():
    return render_template('home.html')

@app.route("/index")
def index():
    return render_template('index.html')

@app.route("/get_response", methods=["POST"])
def get_bot_response():
    # Get user's message from the request
    user_message = request.form.get("message")

    # Generate prompt using the user's message and the links
    prompt = generate_prompt(user_message)

    # Get response from OpenAI API
    bot_response = get_response(prompt)

    # Return bot's response as JSON
    return jsonify({"message": bot_response})

if __name__ == "__main__":
    app.run(debug=True)
