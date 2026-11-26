from rapidocr_onnxruntime import RapidOCR
from src.ports.text_recognizer import TextRecognizer


class RapidOcr (TextRecognizer):

    def __init__(self):
        self.ocr = RapidOCR()

    def recognize(self, cropped_image):

        if cropped_image.size == 0: return None
        result, _ = self.ocr(cropped_image)

        if not result: return None

        
        texts = []
        confidences = []

        for res in result:
            text = res[1]
            confidence = float(res[2])

            if confidence < 0.6:
                continue

            texts.append(text)
            confidences.append(confidence)

        if not texts:
            return None

        full_text = " ".join(texts).strip()
        avg_confidence = sum(confidences) / len(confidences)
            

        return (full_text, avg_confidence)


            
            