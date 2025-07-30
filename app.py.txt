from flask import Flask, request, jsonify
from openai import OpenAI
from gtts import gTTS
import os

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return "Voice Assistant Server Running"

@app.route("/process", methods=["POST"])
def process_audio():
    return jsonify({"status": "working..."})

if __name__ == "__main__":
    app.run(debug=True)
