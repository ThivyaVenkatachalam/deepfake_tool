# backend/explainer.py

def explain(media_type, score):
    """
    Human-readable explanation for Grandma Mode
    """
    if media_type == "image":
        if score > 60:
            return "The image shows unnatural textures and missing camera information, which is common in AI-generated images."
        elif score > 40:
            return "The image has some suspicious patterns, but manipulation is not certain."
        else:
            return "The image structure and metadata appear consistent."

    if media_type == "audio":
        if score > 60:
            return "The audio contains unnatural frequency patterns often found in synthetic or cloned voices."
        elif score > 40:
            return "The audio shows some irregularities and should be verified."
        else:
            return "The audio appears natural and consistent."

    if media_type == "video":
        if score > 60:
            return "The video shows inconsistent facial movements and lighting, which are signs of deepfake manipulation."
        elif score > 40:
            return "The video has minor inconsistencies and should be treated with caution."
        else:
            return "The video appears visually consistent."

    if media_type == "url":
        if score > 60:
            return "The website uses common scam keywords and unsafe patterns."
        elif score > 40:
            return "The website has some suspicious characteristics."
        else:
            return "The website appears to be safe."

    return "Analysis completed."


def spoken_message(result):
    """
    Convert the analysis result dict into a spoken-friendly message.
    """
    verdict = result.get("verdict", "Unknown verdict")
    score = result.get("score", 0)
    media_type = result.get("media_type", "content")  # optional, if you store it

    # Use the explain function for the "why"
    explanation = explain(media_type, score)

    # Combine into a full spoken message
    message = (
        f"Analysis complete. Verdict: {verdict}. "
        f"Trust Score: {score} percent. "
        f"Explanation: {explanation}"
    )
    return message
