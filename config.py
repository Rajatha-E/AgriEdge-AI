"""
Central configuration for the leaf disease + fertilizer recommendation app.

Switch HARDWARE_MODE to change between:
    "laptop"    — laptop webcam, simulated sensors, full TensorFlow
    "pi"        — Pi Camera Module v2, real sensors, tflite-runtime
"""

# ============================================================
# HARDWARE MODE
# ============================================================
HARDWARE_MODE = "laptop"     # change to "pi" when deployed on Raspberry Pi


# ============================================================
# PATHS — model and metadata files
# ============================================================
# On the laptop (today):
MODEL_DIR_LAPTOP = r"D:\smart_agri\pi_app\model"

# On the Pi (tomorrow), uncomment and use this instead:
# MODEL_DIR_PI = "/home/pi/smart_agri/model"

MODEL_DIR = MODEL_DIR_LAPTOP if HARDWARE_MODE == "laptop" else MODEL_DIR_PI

DISEASE_MODEL_PATH = f"{MODEL_DIR}/mobilenetv2_int8.tflite"
DISEASE_CLASSES_PATH = f"{MODEL_DIR}/classes.json"
FERT_MODEL_PATH = f"{MODEL_DIR}/fert_model.pkl"
FERT_CLASSES_PATH = f"{MODEL_DIR}/fert_classes.json"
FERT_FEATURES_PATH = f"{MODEL_DIR}/fert_features.json"


# ============================================================
# CAMERA
# ============================================================
CAMERA_INDEX = 0                 # laptop webcam index (0 = default)
CAMERA_WIDTH = 640
CAMERA_HEIGHT = 480
FRAME_INTERVAL_SECONDS = 1.0     # how often to run inference (not every frame)


# ============================================================
# SENSORS
# ============================================================
SENSOR_READ_INTERVAL = 5.0       # seconds between sensor reads
SENSOR_SIMULATION_CYCLE = True   # cycle through 6 predefined scenarios


# ============================================================
# WEB SERVER
# ============================================================
FLASK_HOST = "0.0.0.0"
FLASK_PORT = 5000