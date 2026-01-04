import sys
from src.logger.logging import logger
from src.exception.exception import CustomException
from PIL import Image

class DataTransformation:
    def __init__(self):
        pass

    def transform_image(self, image_path):
        """
        Prepares image for Gemini API (if needed).
        Gemini accepts PIL images or bytes.
        This step validates and opens the image.
        """
        try:
            img = Image.open(image_path)
            logger.info(f"Image loaded and transformed: {image_path}")
            return img
        except Exception as e:
            raise CustomException(e, sys)
