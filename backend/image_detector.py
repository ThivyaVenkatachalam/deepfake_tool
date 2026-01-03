import torch
from torchvision import models, transforms
from PIL import Image
import numpy as np

class ImageDetector:
    def __init__(self):
        self.model = models.resnet50(weights="DEFAULT")
        self.model.fc = torch.nn.Linear(2048, 1)
        self.model.eval()

        self.transform = transforms.Compose([
            transforms.Resize((224, 224)),
            transforms.ToTensor(),
        ])

    def detect(self, path):
        img = Image.open(path).convert("RGB")
        x = self.transform(img).unsqueeze(0)

        with torch.no_grad():
            score = torch.sigmoid(self.model(x)).item()

        return round(score * 100, 2)
