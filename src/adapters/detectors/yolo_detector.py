from src.ports.plate_detector import PlateDetector
import cv2
from src.domain.models import BoundingBox, PlateDetection
import onnxruntime as ort
import numpy as np


class YoloDetector(PlateDetector):
    def __init__(self, model_path: str = "models/best.onnx", confidence_threshold: float = 0.4):
        self.model_path = model_path
        self.confidence_threshold = confidence_threshold
        self.session = ort.InferenceSession(self.model_path, providers=["CPUExecutionProvider"])
        self.input_name = self.session.get_inputs()[0].name

    def detect(self, frame):

        if frame is None: return []

        orig_h, orig_w = frame.shape[:2]

        image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        image = cv2.resize(image, (640, 640))
        image = image.astype(np.float32) / 255.0
        image = np.transpose(image, (2, 0, 1))   
        image = np.expand_dims(image, axis=0)

        outputs = self.session.run(None, {self.input_name: image})
        preds = outputs[0][0].T

        preds = outputs[0]
        preds = preds.T

        boxes, confidences = [], []
        
        for row in preds:
            confidence = row[4]
            if confidence < self.confidence_threshold:
                continue

            cx, cy, w, h = row[0], row[1], row[2], row[3]
            x = int((cx - w / 2) * orig_w / 640)
            y = int((cy - h / 2) * orig_h / 640)
            w = int(w * orig_w / 640)
            h = int(h * orig_h / 640)

            boxes.append([x, y, w, h])
            confidences.append(float(confidence)) 

        indices = cv2.dnn.NMSBoxes(boxes, confidences, self.confidence_threshold, 0.4)
        
        detections = []
        for i in indices:
            x, y, w, h = boxes[i]
            cropped = frame[max(0,y):y+h, max(0,x):x+w]
            bbox = BoundingBox(x_min=x, y_min=y, x_max=x+w, y_max=y+h)
            detections.append(PlateDetection(bbox=bbox, confidence=confidences[i], cropped_image=cropped))

        return detections