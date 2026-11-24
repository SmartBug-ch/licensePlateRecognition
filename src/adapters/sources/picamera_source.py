from src.ports.image_source import ImageSource
from typing import Optional, Any
try:
    from picam2 import Picamera2
except ImportError:
    Picamera2 = None


class PicameraSource(ImageSource):
    def __init__(self, resolution: tuple[int, int] = (1280, 720)):
        if Picamera2 is None:
            raise RuntimeError("Picamera2 ist nicht installiert, Bitte nur auf Raspberry Pi aktivieren")
        self.camera = Picamera2()
        config = self.camera.create_preview_configuration(main={"size": resolution, "format": "BGR888"})
        self.camera.configure(config)
        self.camera.start()




        
    def get_next_frame(self):
        return self.camera.capture_array()
    
    def release(self):
        self.camera.stop()
        self.camera.close()
    