from src.ports.result_sink import ResultSink
from src.domain.models import PlateResult
import os
import csv


class CsvSink(ResultSink):

    def __init__(self, path: str = "plates.csv"):
        self.path = path

        file_exists = os.path.exists(self.path)

        if not file_exists:
        
            with open(self.path, mode="w", newline="", encoding="utf-8") as f:
                writer = csv.writer(f)
                writer.writerow(["Date", "Plate Number", "Confidence"])
                    

    def consume(self, result: PlateResult) -> None:
        with open(self.path, mode="a", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow([result.timestamp.strftime("%Y-%m-%d %H:%M:%S"), result.text, result.confidence])
        