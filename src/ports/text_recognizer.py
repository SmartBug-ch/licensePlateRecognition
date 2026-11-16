from abc import ABC, abstractmethod
from typing import Any, Optional


class TextRecognizer(ABC):

    @abstractmethod
    def recognize(self, cropped_image: Any) -> Optional[tuple[str, float]]:
        """
            gives back none or the teyt on the plate with the confidence
        """
