import os
import sys
import google.generativeai as genai
from src.logger.logging import logger
from src.exception.exception import CustomException
from dotenv import load_dotenv

load_dotenv()

class ModelIngestion:
    def __init__(self):
        try:
            genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
            self.vision_model = genai.GenerativeModel('gemini-pro-vision')
            self.chat_model = genai.GenerativeModel('gemini-pro')
            logger.info("Gemini Models initialized successfully")
        except Exception as e:
            raise CustomException(e, sys)

    def get_vision_model(self):
        return self.vision_model

    def get_chat_model(self):
        return self.chat_model
