import librosa
import numpy as np

class AudioDetector:
    def detect(self, path):
        y, sr = librosa.load(path)
        flatness = np.mean(librosa.feature.spectral_flatness(y=y))

        score = (1 - flatness) * 100
        return round(score, 2)
