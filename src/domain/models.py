from datetime import datetime
from typing import Any, Optional
from dataclasses import dataclass


@dataclass(frozen=True)
class BoundingBox:
    x_min: int
    x_max: int
    y_min: int
    y_max: int


    @property 
    def width(self) -> int:
        return (self.x_max - self.x_min)

    @property
    def height(self) -> int:
        return (self.y_max - self.y_min)

    @property
    def area(self) -> int:
        return (self.width * self.height)


@dataclass(frozen=True)
class PlateDetection:
    bbox: BoundingBox
    confidence: float
    cropped_image: Optional[Any] = None

@dataclass(frozen=True)
class PlateResult:
    text: str
    confidence: float
    bbox: BoundingBox
    timestamp: datetime
