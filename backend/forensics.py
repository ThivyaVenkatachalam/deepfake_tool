import hashlib
import os

def file_fingerprint(path):
    with open(path, "rb") as f:
        file_hash = hashlib.sha256(f.read()).hexdigest()

    size_kb = round(os.path.getsize(path) / 1024, 2)

    return {
        "hash": file_hash,
        "size_kb": size_kb,
        "note": "Hash generated for legal verification"
    }

def forensic_flags(media_type, score):
    flags = []

    if score > 60:
        flags.append("High probability of AI-generated content")

    if media_type == "image":
        flags.append("Possible AI texture artifacts detected")
        flags.append("Image metadata inconsistencies found")

    elif media_type == "video":
        flags.append("Temporal facial inconsistency detected")
        flags.append("Lighting mismatch across video frames")

    elif media_type == "audio":
        flags.append("Synthetic frequency cut-offs detected")

    return flags
