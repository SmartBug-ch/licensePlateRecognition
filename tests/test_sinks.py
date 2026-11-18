from src.adapters.sinks.csv_sink import CsvSink
import csv
from src.domain.models import PlateResult
from datetime import datetime


def test_csv_sink_and_path(tmp_path):


    test_file = str(tmp_path/"test_plates.csv")
    sink = CsvSink(test_file)
    test_result = PlateResult( text = "AG 0112", confidence = 0.95, bbox = None, timestamp = datetime.now())


    sink.consume(test_result)

    with open(test_file) as f:
        lines = f.readlines()
        assert len(lines) == 2
        assert "AG 0112" in lines[1]


