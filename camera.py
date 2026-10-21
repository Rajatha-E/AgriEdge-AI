"""
Camera abstraction — works with laptop webcam or Pi Camera Module v2.
"""
import time
import numpy as np

from config import HARDWARE_MODE, CAMERA_INDEX, CAMERA_WIDTH, CAMERA_HEIGHT


class Camera:
    def __init__(self):
        self.mode = HARDWARE_MODE
        self.cap = None
        self._init_camera()

    def _init_camera(self):
        if self.mode == "pi":
            try:
                from picamera2 import Picamera2
                self.cap = Picamera2()
                cfg = self.cap.create_preview_configuration(
                    main={"size": (CAMERA_WIDTH, CAMERA_HEIGHT)}
                )
                self.cap.configure(cfg)
                self.cap.start()
                time.sleep(2)   # let camera warm up
                print("[camera] Pi Camera initialized")
            except Exception as e:
                print(f"[camera] Pi Camera failed: {e}")
                print("[camera] Falling back to OpenCV webcam")
                self.mode = "laptop"
                self._init_opencv()
        else:
            self._init_opencv()

    def _init_opencv(self):
        import cv2
        self.cap = cv2.VideoCapture(CAMERA_INDEX)
        if not self.cap.isOpened():
            raise RuntimeError("Could not open webcam")
        self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, CAMERA_WIDTH)
        self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, CAMERA_HEIGHT)
        print("[camera] OpenCV webcam initialized")

    def capture(self):
        """Return a BGR numpy array (H, W, 3), or None on failure."""
        if self.mode == "pi":
            frame = self.cap.capture_array()          # RGB
            import cv2
            return cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
        else:
            ok, frame = self.cap.read()
            return frame if ok else None

    def release(self):
        try:
            if self.mode == "pi":
                self.cap.stop()
            else:
                self.cap.release()
        except Exception:
            pass