import cv2
from src.adapters.detectors.opencv_detector import OpencvDetector


def test_detector_finds_plate():
    test_image = cv2.imread("sample_images/test_image.jpg")
    test_detector = OpencvDetector()
    detections = test_detector.detect(test_image)

    # wenn man was sehen will ( aber achtung anderer Test schlägt dan fehl)
    
    # for i in range(len(detections)):
    #     cv2.imwrite(f"sample_images/candidate_{i}.jpg", detections[i].cropped_image)

    assert len(detections) >= 1
    assert detections[0].bbox.width > 100