# backend/detector.py
from backend.image_detector import ImageDetector
from backend.audio_detector import AudioDetector
from backend.video_detector import VideoDetector
from backend.url_detector import check_url
from backend.explainer import explain

img_detector = ImageDetector()
aud_detector = AudioDetector()
vid_detector = VideoDetector()

def analyze(path, media_type):
    """
    Main function to analyze any media type.
    Returns result dict for app display, report, and TTS.
    """
    result = {}

    if media_type == "image":
        score = img_detector.detect(path)
        result["score"] = score
        result["verdict"] = "🔴 High Risk" if score > 60 else "⚠️ Suspicious" if score > 40 else "✅ Safe"

    elif media_type == "audio":
        score = aud_detector.detect(path)
        result["score"] = score
        result["verdict"] = "🔴 High Risk" if score > 60 else "⚠️ Suspicious" if score > 40 else "✅ Safe"

    elif media_type == "video":
        video_result = vid_detector.detect(path)
        score = video_result["score"]
        result["score"] = score
        result["verdict"] = "🔴 High Risk" if score > 60 else "⚠️ Suspicious" if score > 40 else "✅ Safe"
        result["behavior"] = video_result["behavior"]

    elif media_type == "url":
        is_safe, flags = check_url(path)
        result["score"] = 100 if is_safe else 30
        result["verdict"] = "✅ Safe" if is_safe else "🔴 High Risk"
        result["flags"] = flags

    result["media_type"] = media_type
    result["why"] = explain(media_type, result["score"])
    return result
