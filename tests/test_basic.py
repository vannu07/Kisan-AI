import unittest
from unittest.mock import patch, MagicMock
import sys
import os
import json

# Add project root to path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Mock the expensive/external dependencies BEFORE importing app
# This prevents actual initialization of Gemini/Mongo during import if they are instantiated at module level
with patch('src.pipeline.prediction_pipeline.PredictionPipeline') as MockPipeline, \
     patch('src.components.data_ingestion.DataIngestion') as MockDataIngestion, \
     patch('src.database.mongodb.MongoDBClient') as MockMongoDB:
    
    from app import app

class TestKisanAI(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_home_page(self):
        """Test that the home page loads."""
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'KisanAI', response.data)

    def test_scan_page(self):
        """Test that the scan page loads."""
        response = self.app.get('/scan.html')
        self.assertEqual(response.status_code, 200)

    def test_recommendation_crop_route(self):
        """Test the crop recommendation API."""
        # We need to mock the pred_pipeline instance in api.routes
        # Since api.routes is already imported by app, we need to patch the instance *inside* api.routes
        with patch('api.routes.pred_pipeline') as mock_pipeline:
            mock_pipeline.recommend_crop.return_value = "Recommended Crop: Wheat"
            
            data = {
                'N': 90, 'P': 42, 'K': 43,
                'temperature': 20, 'humidity': 80,
                'ph': 6.5, 'rainfall': 200
            }
            
            response = self.app.post('/api/recommend/crop', 
                                     data=json.dumps(data),
                                     content_type='application/json')
            
            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.json['success'], True)
            self.assertEqual(response.json['recommendation'], "Recommended Crop: Wheat")

    def test_recommendation_fertilizer_route(self):
        """Test the fertilizer recommendation API."""
        with patch('api.routes.pred_pipeline') as mock_pipeline:
            mock_pipeline.recommend_fertilizer.return_value = "Recommended Fertilizer: Urea"
            
            data = {
                'soil_type': 'Clay', 'crop': 'Rice',
                'N': 50, 'P': 20, 'K': 20
            }
            
            response = self.app.post('/api/recommend/fertilizer', 
                                     data=json.dumps(data),
                                     content_type='application/json')
            
            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.json['success'], True)
            self.assertEqual(response.json['recommendation'], "Recommended Fertilizer: Urea")

if __name__ == '__main__':
    unittest.main()
