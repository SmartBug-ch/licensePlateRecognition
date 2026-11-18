from src.ports.result_sink import ResultSink
from datetime import datetime
from src.domain.models import PlateResult

class ConsoleSink(ResultSink):

    def consume(self, result: PlateResult) -> None:
       
       print(f"{result.timestamp.strftime("%Y-%m-%d %H:%M:%S")} detected: {result.text}, with confidence: {result.confidence}") 