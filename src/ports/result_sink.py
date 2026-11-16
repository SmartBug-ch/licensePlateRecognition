from abc import abstractmethod, ABC
from typing import Any, Optional
from src.domain.models import PlateResult

class ResultSink(ABC):

    @abstractmethod
    def consume(self, result: PlateResult) -> None:
        """
            consumes the result and ports it to the given output Format
        """
