import os  # <- Make sure this is at the top
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return "Voice Assistant Server Running"

@app.route("/process", methods=["POST"])
def process_audio():
    data = request.json
    text = data.get("text", "")
    response = f"Processed: {text}"
    return jsonify({
        "reply": response,
        "command": "turn_on_light"
    })

if __name__ == "__main__":
    # Use environment PORT on Render
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 10000)))
