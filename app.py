from flask import Flask, request, jsonify
import os

# Import sensor + output functions
from sensors import sensors
from outputs import outputs

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    return jsonify({
        "endpoints": {
            "/chat": "POST JSON {\"message\": \"your text\"} to chat with AI",
            "/command": "POST JSON {\"command\": \"turn_on_fan\"} to control device",
            "/debug_env": "GET to check if environment variables are loaded",
            "/sensors": "GET to read all sensor values"
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

    if cmd == "turn_on_fan":
        outputs.fan_on()
        return jsonify({"status": "Fan turned on"})
    elif cmd == "turn_off_fan":
        outputs.fan_off()
        return jsonify({"status": "Fan turned off"})
    elif cmd == "turn_on_led":
        outputs.led_on()
        return jsonify({"status": "LED turned on"})
    elif cmd == "turn_off_led":
        outputs.led_off()
        return jsonify({"status": "LED turned off"})
    elif cmd == "relay_on":
        outputs.relay_on()
        return jsonify({"status": "Relay activated"})
    elif cmd == "relay_off":
        outputs.relay_off()
        return jsonify({"status": "Relay deactivated"})
    else:
        return jsonify({"error": f"Unknown command: {cmd}"}), 400

@app.route("/sensors", methods=["GET"])
def sensors_data():
    return jsonify({
        "temperature": sensors.read_temperature(),
        "humidity": sensors.read_humidity(),
        "ldr": sensors.read_ldr()
    })

@app.route("/debug_env", methods=["GET"])
def debug_env():
    return jsonify(dict(os.environ))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
