import random

def read_temperature():
    # Replace with actual temperature sensor read code
    return round(25 + random.uniform(-2, 2), 2)

def read_humidity():
    # Replace with actual humidity sensor read code
    return round(60 + random.uniform(-5, 5), 2)

def read_ldr():
    # Replace with ADC read for LDR sensor
    return random.randint(200, 800)
