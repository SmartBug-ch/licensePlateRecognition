from abc import ABC, abstractmethod
from typing import Optional, Any
from src.domain.models import PlateDetection


class PlateDetector(ABC):

    @abstractmethod
    def detect(self, frame: Any) -> list[PlateDetection]:
        """
            detect function, can return empty list []
        """


    

