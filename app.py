from flask import Flask, render_template, request, jsonify
from langchain.prompts import PromptTemplate
import openai
import os
import time

secret_key = os.environ.get("openai_flask_bot_api")

app= Flask(__name__)

@app.route("/")
def home():
    return render_template('home.html')
@app.route("/index")
def index():
    return render_template('index.html')

