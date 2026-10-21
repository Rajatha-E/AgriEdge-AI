import time
import cv2
import numpy as np
import os
from vision import DiseaseClassifier

print("Initializing AI Model...")
# Initialize the classifier (ensure your 'model' folder is in the same directory)
classifier = DiseaseClassifier()

print("Loading test image...")
# Create a dummy image for testing if you don't have one handy
image_path = 'test_image.jpg'
if not os.path.exists(image_path):
    dummy_img = np.random.randint(0, 255, (224, 224, 3), dtype=np.uint8)
    cv2.imwrite(image_path, dummy_img)

frame = cv2.imread(image_path)

if frame is None:
    print("Error: Could not read image.")
else:
    print("Running Inference with TTA (Test-Time Augmentation)...")
    
    # Start the timer
    start_time = time.perf_counter()
    
    # Run the prediction using YOUR actual class method
    results = classifier.predict(frame)
    
    # Stop the timer
    end_time = time.perf_counter()
    
    # Calculate milliseconds
    time_ms = (end_time - start_time) * 1000
    
    print("\n----------------------------------------")
    print("TOP 3 PREDICTIONS:")
    for res in results:
        print(f" - {res['disease_class']}: {res['confidence']*100:.2f}%")
    print("----------------------------------------")
    print(f"TOTAL INFERENCE TIME: {time_ms:.2f} milliseconds")
    print("----------------------------------------\n")