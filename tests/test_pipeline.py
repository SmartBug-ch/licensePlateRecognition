from src.ports.result_sink import ResultSink
from src.ports.plate_detector import PlateDetector
from src.ports.text_recognizer import TextRecognizer
from src.ports.image_source import ImageSource
from src.domain.models import PlateDetection
from src.application.pipeline import Pipeline


class FakeSource(ImageSource):
    def __init__(self):
        self.fake_data = ["image", None]
        self.counter = 0

    def get_next_frame(self):
        data = self.fake_data[self.counter]
        self.counter += 1
        return data

    def release(self):
        return print(f"release called")

class FakeDetector(PlateDetector):

    def __init__(self):
        self.result = None

    def detect(self, frame):
        self.result = PlateDetection(bbox=None, confidence=0.9, cropped_image=None)
        return [self.result]


class FakeRecognizer(TextRecognizer):
    def __init__(self):
        self.result = None

    def recognize(self, cropped_image):
        self.result = ("ZH 0213", 0.91)
        return self.result


class FakeSink(ResultSink):

    def __init__(self):
        self.isCalled = False

    def consume(self, result):
        self.isCalled = True




def test_Pipeline():
    fake_source = FakeSource()
    fake_detector = FakeDetector()
    fake_recognizer = FakeRecognizer()
    fake_sink = FakeSink()

    test_pipe = Pipeline(source=fake_source, recognizer=fake_recognizer, detector=fake_detector, sinks = [fake_sink])

    test_pipe.run()

    assert fake_detector.result == PlateDetection(bbox=None, confidence=0.9, cropped_image=None)
    assert fake_recognizer.result == ("ZH 0213", 0.91)
    assert fake_sink.isCalled

    
