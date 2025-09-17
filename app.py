# app.py
from flask import Flask, request, jsonify
import cohere
import os
from sensors import sensor_module
from outputs import device_control

app = Flask(__name__)

# Initialize Cohere client
co = cohere.Client(os.getenv("COHERE_API_KEY"))

@app.route("/chat", methods=["POST"])
def chat():
    try:
        data = request.json
        message = data.get("message", "").strip()

        # Cohere reasoning/chat
        if message.lower().startswith("cohere,"):
            try:
                response = co.chat(model="command-a-03-2025", message=message)
                return jsonify({"reply": response.text})
            except Exception as e:
                return jsonify({"error": f"Cohere error: {str(e)}"}), 500

        # Automation commands
        if "turn on light" in message.lower():
            return jsonify({"reply": device_control.turn_on_light()})
        elif "turn off light" in message.lower():
            return jsonify({"reply": device_control.turn_off_light()})
        elif "status" in message.lower():
            temp = sensor_module.get_temperature()
            ldr = sensor_module.get_ldr()
            return jsonify({"reply": f"{device_control.get_status()}, Temp: {temp}, LDR: {ldr}"})
        else:
            return jsonify({"reply": "🤖 Command not recognized by automation"})

    except Exception as e:
        return jsonify({"error": f"Server error: {str(e)}"}), 500

if __name__ == "__main__":
    app.run(debug=True)
