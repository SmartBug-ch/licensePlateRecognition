from typing import Optional, Any
from src.ports.image_source import ImageSource
from src.ports.text_recognizer import TextRecognizer
from src.ports.plate_detector import PlateDetector
from src.ports.result_sink import ResultSink
from src.domain.models import PlateResult
from datetime import datetime


class Pipeline:

    def __init__(self, source: ImageSource, recognizer: TextRecognizer, detector: PlateDetector, sinks: Optional[list[ResultSink]] = None):
        self.source = source
        self.recognizer = recognizer
        self.detector = detector
        self.sinks = sinks if sinks is not None else []

    def add_sink(self, sink: ResultSink) -> None:
        self.sinks.append(sink)

    def run(self) -> None:
        try:
           while True:
               frame = self.source.get_next_frame()
               if frame is None:
                   break
               self.process_frame(frame)
        finally:
            self.source.release()




    def process_frame(self, frame: Any) -> list[PlateResult]:
        results = []
        
        plates = self.detector.detect(frame)
        for plate in plates:
            plate_raw = self.recognizer.recognize(plate.cropped_image)
            if (plate_raw):
                plate_str, conf = plate_raw
                if conf < 0.8:
                    continue
                
                results.append(PlateResult(plate_str, conf, plate.bbox, datetime.now()))

        for result in results:
            for sink in self.sinks:
                sink.consume(result)

        return results

            




        



