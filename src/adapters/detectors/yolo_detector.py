from src.ports.plate_detector import PlateDetector
import cv2
from src.domain.models import BoundingBox, PlateDetection


class YoloDetector(PlateDetector):
    def __init__(self, model_path: str = "model/license_plate_detector.onnx", confidence_threshold: float = 0.4):
        self.model_path = model_path
        self.net = cv2.dnn.readNetFromONNX(self.model_path)
        self.confidence_threshold = confidence_threshold

    def detect(self, frame):
        blob = cv2.dnn.blobFromImage(frame, 1/255.0, (640, 640), swapRB=True, crop=False)
        self.net.setInput(blob)
        outputs = self.net.forward()

        preds = outputs[0]
        preds = preds.T

        boxes, confidences = [], []
        orig_h, orig_w = frame.shape[:2]

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

     


        


    
