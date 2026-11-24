from src.ports.plate_detector import PlateDetector
from src.domain.models import PlateDetection, BoundingBox
import cv2


class OpencvDetector(PlateDetector):

    def detect(self, frame):

        if frame is None: return []

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        sobelx = cv2.Sobel(gray, cv2.CV_32F, 1, 0, ksize=3)
        sobelx = cv2.convertScaleAbs(sobelx)

        kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (25,5))
        closed = cv2.morphologyEx(sobelx, cv2.MORPH_CLOSE, kernel)
        _, thresh = cv2.threshold(closed, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

        contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        detections = []
        for c in contours:
            x, y, w, h = cv2.boundingRect(c)
            aspect_ratio = w / float(h)
            area = w * h

            if 2.2 <= aspect_ratio <= 5.5 and 2000 <= area <= 60000:
                bbox = BoundingBox(x_min=x, y_min=y, x_max=x+w, y_max=y+h)
                cropped = frame[y:y+h, x:x+w]

                detections.append(PlateDetection(bbox=bbox, confidence=0.85, cropped_image=cropped
                                                 ))


        detections.sort(key=lambda d: d.bbox.area, reverse=True)        
        return detections





        
    

