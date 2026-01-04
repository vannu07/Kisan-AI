import sys
from src.logger.logging import logger
from src.exception.exception import CustomException
from src.components.data_transformation import DataTransformation
from src.components.model_ingestion import ModelIngestion
from src.database.mongodb import MongoDBClient
import datetime

class PredictionPipeline:
    def __init__(self):
        self.data_transformation = DataTransformation()
        self.model_ingestion = ModelIngestion()
        self.mongo_client = MongoDBClient()

    def predict_disease(self, image_path):
        try:
            # 1. Transform Image
            img = self.data_transformation.transform_image(image_path)
            
            # 2. Get Model
            model = self.model_ingestion.get_vision_model()
            
            # 3. Generate Prediction
            prompt = """
            Analyze this crop image. 
            1. Identify the crop.
            2. Detect any disease or issue.
            3. Provide Treatment.
            4. Provide Prevention.
            Format the output as JSON with keys: 'disease_name', 'severity', 'treatment', 'prevention', 'confidence'.
            If healthy, state 'Healthy' in disease_name.
            """
            response = model.generate_content([prompt, img])
            result_text = response.text
            
            # 4. Save to History (MongoDB)
            record = {
                "type": "scan",
                "image_path": image_path,
                "result": result_text,
                "timestamp": datetime.datetime.now()
            }
            self.mongo_client.insert_record("scan_history", record)
            
            return result_text
            
        except Exception as e:
            raise CustomException(e, sys)

    def chat_with_advisor(self, query):
        try:
            # 1. Get Chat Model
            model = self.model_ingestion.get_chat_model()
            
            # 2. Generate Response
            prompt = f"You are an expert agriculture advisor named KisanAI. Answer this farmer's question: {query}"
            response = model.generate_content(prompt)
            answer = response.text
            
            # 3. Save Chat to MongoDB
            record = {
                "type": "chat",
                "user_query": query,
                "ai_response": answer,
                "timestamp": datetime.datetime.now()
            }
            self.mongo_client.insert_record("chat_history", record)
            
            return answer
            
        except Exception as e:
            raise CustomException(e, sys)

    def recommend_crop(self, data):
        try:
            model = self.model_ingestion.get_chat_model()
            prompt = f"""
            You are KisanAI, an expert agricultural advisor. 
            Based on the following conditions, recommend suitable crops:
            Nitrogen: {data.get('N')}
            Phosphorous: {data.get('P')}
            Potassium: {data.get('K')}
            Temperature: {data.get('temperature')} C
            Humidity: {data.get('humidity')} %
            PH: {data.get('ph')}
            Rainfall: {data.get('rainfall')} mm
            
            Provide a detailed recommendation in JSON format with keys: 'recommended_crops' (list), 'reasoning', 'farming_tips'.
            """
            response = model.generate_content(prompt)
            return response.text
        except Exception as e:
            raise CustomException(e, sys)

    def recommend_fertilizer(self, data):
        try:
            model = self.model_ingestion.get_chat_model()
            prompt = f"""
            You are KisanAI, an expert agricultural advisor. 
            Based on the following soil details and crop, recommend a fertilizer:
            Soil Type: {data.get('soil_type')}
            Crop: {data.get('crop')}
            Nitrogen: {data.get('N')}
            Phosphorous: {data.get('P')}
            Potassium: {data.get('K')}
            
            Provide a recommendation in JSON format with keys: 'fertilizer_name', 'application_method', 'dosage', 'precautions'.
            """
            response = model.generate_content(prompt)
            return response.text
        except Exception as e:
            raise CustomException(e, sys)
