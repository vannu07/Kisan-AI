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
            api_key = os.getenv("GEMINI_API_KEY")
            if not api_key:
                raise ValueError("GEMINI_API_KEY environment variable is not set. Please add it to your .env file.")
            
            genai.configure(api_key=api_key)
            
            # Use gemini-1.5-flash which supports both vision and text
            # gemini-pro and gemini-pro-vision are deprecated
            self.vision_model = genai.GenerativeModel('gemini-1.5-flash')
            self.chat_model = genai.GenerativeModel('gemini-1.5-flash')
            
            logger.info("Gemini Models initialized successfully with gemini-1.5-flash")
        except Exception as e:
            logger.error(f"Failed to initialize Gemini models: {str(e)}")
            raise CustomException(e, sys)

    def get_vision_model(self):
        return self.vision_model

    def get_chat_model(self):
        return self.chat_model
