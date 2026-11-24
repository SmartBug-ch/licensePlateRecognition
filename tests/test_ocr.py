from src.adapters.ocr.tesseract_ocr import TesseractOcr
import numpy as np


def test_recognize_returns_none_on_empty():
    ocr = TesseractOcr()
    result = ocr.recognize(None)

    assert result is None


    


def test_pre_processing_create_binary_image():
    orc = TesseractOcr()
    img = np.zeros((50,100,3), dtype=np.uint8)
    thresh = orc.pre_processing(img)

    assert len(thresh.shape) == 2


def test_recognize_extracts_text_with_mock(monkeypatch):
    ocr = TesseractOcr()

    monkeypatch.setattr(
        "pytesseract.image_to_string",
        lambda frame, config=None: " TANDOORI\n  "
    )

    dummy_plate = np.zeros((50,200,3), dtype=np.uint8)
    result = ocr.recognize(dummy_plate)

    assert result == ("TANDOORI", 0.90)