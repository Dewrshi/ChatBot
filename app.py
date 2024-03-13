from flask import Flask, render_template, request, jsonify

app= Flask(__name__)

@app.route("/")
def home():
    return render_template('home.html')
@app.route("/")
def index():
    return render_template('index.html')

