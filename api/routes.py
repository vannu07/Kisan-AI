from flask import Blueprint, request, jsonify, current_app
from src.logger.logging import logger
import os

api_bp = Blueprint('api', __name__)

# Lazy initialization to prevent crashes on cold starts
_pred_pipeline = None
_data_ingestion = None
_mongo_client = None

def get_prediction_pipeline():
    """Lazy load prediction pipeline"""
    global _pred_pipeline
    if _pred_pipeline is None:
        from src.pipeline.prediction_pipeline import PredictionPipeline
        _pred_pipeline = PredictionPipeline()
    return _pred_pipeline

def get_data_ingestion():
    """Lazy load data ingestion"""
    global _data_ingestion
    if _data_ingestion is None:
        from src.components.data_ingestion import DataIngestion
        _data_ingestion = DataIngestion()
    return _data_ingestion

def get_mongo_client():
    """Lazy load MongoDB client"""
    global _mongo_client
    if _mongo_client is None:
        from src.database.mongodb import MongoDBClient
        _mongo_client = MongoDBClient()
    return _mongo_client

@api_bp.route('/recommend/crop', methods=['POST'])
def recommend_crop():
    try:
        data = request.json
        pred_pipeline = get_prediction_pipeline()
        result = pred_pipeline.recommend_crop(data)
        return jsonify({"success": True, "recommendation": result})
    except Exception as e:
        logger.error("Error in /recommend/crop", exc_info=True)
        return jsonify({"error": "An internal error has occurred. Please try again later."}), 500

@api_bp.route('/recommend/fertilizer', methods=['POST'])
def recommend_fertilizer():
    try:
        data = request.json
        pred_pipeline = get_prediction_pipeline()
        result = pred_pipeline.recommend_fertilizer(data)
        return jsonify({"success": True, "recommendation": result})
    except Exception as e:
        logger.error("Error in /recommend/fertilizer", exc_info=True)
        return jsonify({"error": "An internal error has occurred. Please try again later."}), 500

@api_bp.route('/scan', methods=['POST'])
def scan_crop():
    try:
        if 'file' not in request.files:
            return jsonify({"error": "No file part"}), 400
        
        file = request.files['file']
        if file.filename == '':
            return jsonify({"error": "No selected file"}), 400

        # 1. Save File
        data_ingestion = get_data_ingestion()
        file_path = data_ingestion.save_uploaded_file(file)
        
        # 2. Run Prediction Pipeline
        pred_pipeline = get_prediction_pipeline()
        result = pred_pipeline.predict_disease(file_path)
        
        return jsonify({"success": True, "analysis": result})
        
    except Exception as e:
        logger.error("Error in /scan", exc_info=True)
        return jsonify({"error": "An internal error has occurred. Please try again later."}), 500

@api_bp.route('/chat', methods=['POST'])
def chat_advisor():
    try:
        data = request.json
        query = data.get('query')
        
        if not query:
            return jsonify({"error": "No query provided"}), 400
            
        # Run Chat Pipeline
        pred_pipeline = get_prediction_pipeline()
        response = pred_pipeline.chat_with_advisor(query)
        
        return jsonify({"success": True, "response": response})
        
    except Exception as e:
        logger.error(f"Error in /chat: {str(e)}")
        return jsonify({"error": "An internal error occurred while processing your request."}), 500

@api_bp.route('/history', methods=['GET'])
def get_history():
    try:
        user_id = request.args.get('user_id')
        if not user_id:
            # If no user_id, return empty list or all records (depending on logic). 
            # For now, let's require user_id or return all if admin.
            # But based on user request "history of user", we should filter.
            pass

        query = {"user_id": user_id} if user_id else {}
        mongo_client = get_mongo_client()
        records = mongo_client.get_records("scan_history", query)
        
        # Convert ObjectId to str for JSON serialization
        for record in records:
            record['_id'] = str(record['_id'])
        return jsonify({"success": True, "history": records})
    except Exception as e:
        logger.error(f"Error in /history: {str(e)}")
        return jsonify({"error": str(e)}), 500

@api_bp.route('/auth/signup', methods=['POST'])
def signup():
    try:
        data = request.json
        email = data.get('email')
        password = data.get('password')
        name = data.get('name')

        if not email or not password:
            return jsonify({"error": "Email and password are required"}), 400

        # Check if user exists
        mongo_client = get_mongo_client()
        existing_user = mongo_client.find_one("users", {"email": email})
        if existing_user:
            return jsonify({"error": "User already exists"}), 409

        user_id = mongo_client.insert_record("users", {
            "email": email, 
            "password": password, # In production, hash this!
            "name": name
        })

        return jsonify({"success": True, "user_id": str(user_id), "message": "User created successfully"})
    except Exception as e:
        logger.error(f"Error in /signup: {str(e)}")
        return jsonify({"error": str(e)}), 500

@api_bp.route('/auth/login', methods=['POST'])
def login():
    try:
        data = request.json
        email = data.get('email')
        password = data.get('password')

        if not email or not password:
            return jsonify({"error": "Email and password are required"}), 400

        mongo_client = get_mongo_client()
        user = mongo_client.find_one("users", {"email": email, "password": password})
        if not user:
            return jsonify({"error": "Invalid credentials"}), 401

        return jsonify({"success": True, "user_id": str(user['_id']), "name": user.get('name')})
    except Exception as e:
        logger.error(f"Error in /login: {str(e)}")
        return jsonify({"error": "An internal error occurred while processing your request."}), 500

@api_bp.route('/profile', methods=['GET', 'POST'])
def profile():
    try:
        mongo_client = get_mongo_client()
        
        if request.method == 'POST':
            data = request.json
            user_id = data.get('user_id')
            if not user_id:
                return jsonify({"error": "User ID is required"}), 400
            
            profile_data = {
                "user_id": user_id,
                "location": data.get('location'),
                "farm_size": data.get('farm_size'),
                "crops": data.get('crops'),
                "name": data.get('name') # Update name if provided
            }
            
            # Check if profile exists
            existing_profile = mongo_client.find_one("profiles", {"user_id": user_id})
            if existing_profile:
                mongo_client.update_record("profiles", {"user_id": user_id}, profile_data)
            else:
                mongo_client.insert_record("profiles", profile_data)
                
            return jsonify({"success": True, "message": "Profile saved successfully"})
            
        else: # GET
            user_id = request.args.get('user_id')
            if not user_id:
                return jsonify({"error": "User ID is required"}), 400
                
            profile = mongo_client.find_one("profiles", {"user_id": user_id})
            if not profile:
                return jsonify({"error": "Profile not found"}), 404
                
            if '_id' in profile:
                profile['_id'] = str(profile['_id'])
                
            return jsonify(profile)
            
    except Exception as e:
        logger.error(f"Error in /profile: {str(e)}")
        return jsonify({"error": "An internal error occurred while processing your request."}), 500
