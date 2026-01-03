# backend/behavior.py
import cv2
import random

def behavioral_analysis(video_path):
    """
    Simulated behavioral biometrics for video:
    - Blink rate (synthetic)
    - Micro-expression irregularities
    """
    cap = cv2.VideoCapture(video_path)
    fps = int(cap.get(cv2.CAP_PROP_FPS)) or 1
    frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT)) or 1

    duration_sec = frame_count // fps

    # Simulated blink rate
    blink_rate = random.randint(3, 15)
    if blink_rate < 6:
        status = "Abnormally low blink rate (synthetic indicator)"
    elif blink_rate > 14:
        status = "Abnormally high blink rate (synthetic indicator)"
    else:
        status = "Normal blinking pattern"

    cap.release()
    return {
        "blink_rate": blink_rate,
        "status": status,
        "duration_sec": duration_sec
    }
