import random

class sensors:
    @staticmethod
    def read_temperature():
        # Replace with real sensor code
        return round(25 + random.uniform(-2, 2), 2)

    @staticmethod
    def read_humidity():
        # Replace with real sensor code
        return round(60 + random.uniform(-5, 5), 2)

    @staticmethod
    def read_ldr():
        # Replace with real sensor code
        return random.randint(200, 800)
