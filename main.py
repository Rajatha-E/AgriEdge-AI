import cv2
import time
import os
import json
from datetime import datetime
from flask import Flask, render_template, Response, jsonify, send_from_directory, request
import numpy as np

import config
from camera import Camera
from vision import DiseaseClassifier
from sensors import SensorReader
from fertilizer import FertilizerRecommender, calculate_dosage_table
from pesticide_map import get_disease_info

app = Flask(__name__)
camera = Camera()
classifier = DiseaseClassifier()
sensors = SensorReader()
fert_recommender = FertilizerRecommender()

HISTORY_FILE = "history.json"

def save_to_history(data):
    """Saves the analysis result to a local JSON file."""
    history = []
    if os.path.exists(HISTORY_FILE):
        with open(HISTORY_FILE, "r") as f:
            try:
                history = json.load(f)
            except json.JSONDecodeError:
                history = []
    
    # Add timestamp and insert at the beginning (newest first)
    data["timestamp"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    history.insert(0, data)
    
    # Keep only the last 20 records to save space
    history = history[:20]
    
    with open(HISTORY_FILE, "w") as f:
        json.dump(history, f, indent=4)

def process_frame(frame):
    if not os.path.exists("captures"):
        os.makedirs("captures")
    filename = f"captures/leaf_{datetime.now().strftime('%Y%m%d_%H%M%S')}.jpg"
    cv2.imwrite(filename, frame)

    start_time = time.perf_counter()
    top3 = classifier.predict(frame)
    inference_time_ms = round((time.perf_counter() - start_time) * 1000, 1)
    
    top1_class = top3[0]["disease_class"]
    disease_info = get_disease_info(top1_class)
    
    sensor_data = sensors.read_sensors()
    
    fert_type = fert_recommender.recommend(
        sensor_data["n"], sensor_data["p"], sensor_data["k"], 
        sensor_data["temp"], sensor_data["humidity"]
    )
    dosage_table = calculate_dosage_table(
        fert_type, sensor_data["n"], sensor_data["p"], sensor_data["k"]
    )

    result_data = {
        "status": "success",
        "image_url": f"/{filename}",
        "predictions": top3,
        "disease_info": disease_info,
        "sensors": sensor_data,
        "fertilizer": fert_type.replace("_", " "),
        "dosage_table": dosage_table,
        "inference_time_ms": inference_time_ms
    }

    # Save to history file
    save_to_history(result_data)
    
    return result_data

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/video_feed')
def video_feed():
    def generate():
        while True:
            frame = camera.capture()
            if frame is not None:
                ret, buffer = cv2.imencode('.jpg', frame)
                if ret:
                    yield (b'--frame\r\n'
                           b'Content-Type: image/jpeg\r\n\r\n' + buffer.tobytes() + b'\r\n')
            else:
                time.sleep(0.1)
    return Response(generate(), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/api/analyze', methods=['POST'])
def analyze():
    frame = camera.capture()
    if frame is None:
        return jsonify({"status": "error", "message": "Camera not available"})
    return jsonify(process_frame(frame))

@app.route('/api/analyze_upload', methods=['POST'])
def analyze_upload():
    if 'file' not in request.files:
        return jsonify({"status": "error", "message": "No file uploaded"})
    file = request.files['file']
    if file.filename == '':
        return jsonify({"status": "error", "message": "No selected file"})
        
    file_bytes = np.frombuffer(file.read(), np.uint8)
    frame = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)
    
    if frame is None:
        return jsonify({"status": "error", "message": "Invalid image format"})
        
    return jsonify(process_frame(frame))

@app.route('/api/history', methods=['GET'])
def get_history():
    if os.path.exists(HISTORY_FILE):
        with open(HISTORY_FILE, "r") as f:
            try:
                return jsonify(json.load(f))
            except:
                return jsonify([])
    return jsonify([])

@app.route('/captures/<filename>')
def serve_capture(filename):
    return send_from_directory("captures", filename)

if __name__ == '__main__':
    print(f"[main] Dashboard running at http://localhost:{config.FLASK_PORT}")
    app.run(host=config.FLASK_HOST, port=config.FLASK_PORT, debug=False)