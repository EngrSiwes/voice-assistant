# Mock output module for controlling devices

device_state = {"light": "off", "fan": "off", "temperature": 30, "ldr": 200}

def turn_on_light():
    device_state["light"] = "on"
    return "✅ Light turned ON"

def turn_off_light():
    device_state["light"] = "off"
    return "✅ Light turned OFF"

def get_status():
    return f"Light: {device_state['light']}, Fan: {device_state['fan']}, Temp: {device_state['temperature']}, LDR: {device_state['ldr']}"
