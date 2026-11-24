import pytesseract
from src.ports.text_recognizer import TextRecognizer
import cv2


class TesseractOcr(TextRecognizer):

    def recognize(self, cropped_image):
        
        if cropped_image is None: return None

        return self.text_extract(self.pre_processing(cropped_image))

    def pre_processing(self, frame):

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        blur = cv2.GaussianBlur(gray, (5,5), 0)
        _, thresh = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

        return thresh

    def text_extract(self, frame):

        config = "--psm 7 -c tessedit_char_whitelist=ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
        raw_text = pytesseract.image_to_string(frame, config=config)
        text = raw_text.strip()

        if not text: return None
        return (text, 0.90)
        