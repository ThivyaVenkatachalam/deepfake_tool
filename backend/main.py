from fastapi import FastAPI, UploadFile, File
import shutil
import os
from backend.detector import Detector
from backend.database import save_result

app = FastAPI(title="VeriShield AI API")

detector = Detector()

@app.post("/analyze/")
async def analyze(file: UploadFile = File(...)):
    temp_path = f"temp_{file.filename}"
    with open(temp_path, "wb") as f:
        shutil.copyfileobj(file.file, f)

    if file.content_type.startswith("image"):
        res = detector.analyze(temp_path, "image")
    elif file.content_type.startswith("audio"):
        res = detector.analyze(temp_path, "audio")
    elif file.content_type.startswith("video"):
        res = detector.analyze(temp_path, "video")
    else:
        os.remove(temp_path)
        return {"error": "Unsupported file"}

    save_result(file.filename, res["verdict"], res["score"])
    os.remove(temp_path)
    return res
