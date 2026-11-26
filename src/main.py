import yaml
from src.adapters.sources.folder_source import FolderSource
from src.adapters.sinks.console_sink import ConsoleSink
from src.adapters.sinks.csv_sink import CsvSink
from src.adapters.detectors.opencv_detector import OpencvDetector
from src.adapters.ocr.tesseract_ocr import TesseractOcr
from src.application.pipeline import Pipeline
from src.adapters.sources.picamera_source import PicameraSource
from src.adapters.detectors.yolo_detector import YoloDetector
from src.adapters.ocr.rapid_ocr import RapidOcr

def main():

    with open("config.yaml") as f:
        config = yaml.safe_load(f)

        source = get_source(config)
        sinks = get_sinks(config)
        detector = get_detector(config)
        ocr = get_ocr(config) # wo gebe ich das zur Pipeline dazu? the fuck

        pipeline = Pipeline(source=source, detector=detector, sinks=sinks, recognizer=ocr)

        pipeline.run()

    

def get_source(config):
    source = config["source"]["type"]
    if source == "folder": return FolderSource(path=config["source"]["path"])
    if source == "picam": return PicameraSource()

def get_sinks(config):
    sinks_raw = config["sinks"]
    sinks = []
    for sink in sinks_raw:
        if sink == "console": sinks.append(ConsoleSink())
        if sink == "csv": sinks.append(CsvSink())
    return sinks

def get_detector(config):
    detector = config["detector"]["type"]
    if detector == "opencv": return OpencvDetector()
    if detector == "yolo": return YoloDetector()

def get_ocr(config):
    ocr = config["ocr"]["type"]
    if ocr == "tesseract": return TesseractOcr()
    if ocr == "opencv": return NotImplemented
    if ocr == "rapidocr": return RapidOcr()

if __name__ == "__main__":
    main()
