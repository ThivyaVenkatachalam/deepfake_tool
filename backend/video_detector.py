# backend/video_detector.py
import cv2
import numpy as np
from backend.image_detector import ImageDetector
from backend.behavior import behavioral_analysis

class VideoDetector:
    def __init__(self):
        self.img_detector = ImageDetector()

    def detect(self, video_path):
        """
        Detect AI manipulation in video frames + behavioral analysis.
        """
        cap = cv2.VideoCapture(video_path)
        scores = []
        fps = int(cap.get(cv2.CAP_PROP_FPS)) or 1

        frame_id = 0
        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break

            # Analyze one frame per second
            if frame_id % fps == 0:
                cv2.imwrite("temp.jpg", frame)
                frame_score = self.img_detector.detect("temp.jpg")
                scores.append(frame_score)

            frame_id += 1

        cap.release()
        avg_score = round(np.mean(scores), 2) if scores else 0

        # Behavioral analysis
        behavior_result = behavioral_analysis(video_path)

        return {
            "score": avg_score,
            "behavior": behavior_result
        }
