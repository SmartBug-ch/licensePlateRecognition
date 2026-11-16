from abc import ABC, abstractmethod
from typing import Optional, Any

class ImageSource(ABC):

    @abstractmethod
    def get_next_frame(self) -> Optional[Any]:
        """
            To get the next frame from source
        """

    @abstractmethod
    def release(self) -> None:
        """
            To release resource for power reasons, so that the cam doesnt run while programm not running
        """
