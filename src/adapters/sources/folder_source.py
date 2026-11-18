from src.ports.image_source import ImageSource
import os
import cv2

class FolderSource(ImageSource):
    def __init__(self, path: str = "what to insert"):
        self.path = path
        self.counter = 0
        self.image_files = []

        if not os.path.exists(self.path):
            raise FileNotFoundError(f"file nicht gefunden: {self.path}")

        valid_extensions = (".jpg", ".jpeg", ".png", ".bmp")
        files = os.listdir(self.path)

        for file in files:
            if file.lower().endswith(valid_extensions):
                self.image_files.append(os.path.join(self.path, file))



    def get_next_frame(self):
        if self.counter >= len(self.image_files):
            return None
        
        frame = cv2.imread(self.image_files[self.counter])
        self.counter += 1
        return frame


    
    def release(self):
        pass