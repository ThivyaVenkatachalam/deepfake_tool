# backend/tts.py
import pyttsx3
import threading

engine = pyttsx3.init()

def speak(text):
    """
    Speak text using pyttsx3 in a separate thread to avoid Streamlit RuntimeError.
    """
    def run_speech():
        engine.say(text)
        engine.runAndWait()
    
    # Run in a separate thread
    thread = threading.Thread(target=run_speech)
    thread.start()
