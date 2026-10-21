import random
import time
import config

# Uncomment this when you move to the Pi tomorrow:
# import serial

class SensorReader:
    def __init__(self):
        self.mode = config.HARDWARE_MODE
        if self.mode == "pi":
            # Tomorrow, change 'COM3' to your Arduino port (e.g., '/dev/ttyUSB0' on Pi)
            pass
            # self.arduino = serial.Serial('COM3', 9600, timeout=1)

    def read_sensors(self):
        if self.mode == "laptop":
            # Simulate realistic NPK values fluctuating slightly
            return {
                "n": round(random.uniform(20.0, 80.0), 1),
                "p": round(random.uniform(10.0, 50.0), 1),
                "k": round(random.uniform(15.0, 60.0), 1),
                "temp": round(random.uniform(22.0, 32.0), 1),
                "humidity": round(random.uniform(40.0, 70.0), 1)
            }
        else:
            # HARDWARE MODE: Read from Arduino
            # data = self.arduino.readline().decode('utf-8').strip().split(',')
            # return {"n": float(data[0]), "p": float(data[1]), "k": float(data[2]), "temp": float(data[3]), "humidity": float(data[4])}
            return {"n": 0, "p": 0, "k": 0, "temp": 0, "humidity": 0}