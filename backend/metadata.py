from PIL import Image

def extract_metadata(path):
    try:
        img = Image.open(path)
        data = img.info
        return {
            "present": bool(data),
            "count": len(data),
            "message": "Metadata present" if data else "Metadata missing"
        }
    except:
        return {"present": False, "count": 0, "message": "No metadata"}
