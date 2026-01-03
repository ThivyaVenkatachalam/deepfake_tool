import cv2
import numpy as np

def generate_heatmap(image_path):
    img = cv2.imread(image_path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    heatmap = cv2.applyColorMap(gray, cv2.COLORMAP_JET)
    blended = cv2.addWeighted(img, 0.6, heatmap, 0.4, 0)
    return blended
