from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    return jsonify({
        "endpoints": {
            "/chat": "POST JSON {\"message\": \"your text\"} to chat with AI",
            "/command": "POST JSON {\"command\": \"turn_on_fan\"} to control device",
            "/debug_env": "GET to check if environment variables are loaded"
        },
        "message": "✅ Voice Assistant API is running!"
    })

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    message = data.get("message", "")
    return jsonify({"reply": f"You said: {message}"})

@app.route("/command", methods=["POST"])
def command():
    data = request.get_json()
    cmd = data.get("command", "")
    return jsonify({"status": f"Command {cmd} received"})

@app.route("/debug_env", methods=["GET"])
def debug_env():
    import os
    return jsonify(dict(os.environ))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
