import os
import pymongo
import json
from src.logger.logging import logger
from src.exception.exception import CustomException
import sys
from dotenv import load_dotenv
from bson import ObjectId

load_dotenv()

class MongoDBClient:
    def __init__(self):
        self.use_local = False
        # Use /tmp in serverless environments
        self.local_db_path = "/tmp/local_db.json" if os.environ.get('VERCEL') else "local_db.json"
        
        try:
            mongo_url = os.getenv("MONGODB_URL")
            if not mongo_url or "your_mongodb_atlas" in mongo_url:
                raise Exception("MongoDB URL not configured")
                
            self.client = pymongo.MongoClient(mongo_url)
            self.db_name = "kisanai_db"
            self.db = self.client[self.db_name]
            logger.info(f"Connected to MongoDB Atlas: {self.db_name}")
        except Exception as e:
            logger.warning(f"MongoDB connection failed or not configured: {str(e)}. Switching to local JSON storage.")
            self.use_local = True
            self._init_local_db()

    def _init_local_db(self):
        if not os.path.exists(self.local_db_path):
            with open(self.local_db_path, 'w') as f:
                json.dump({"users": [], "profiles": [], "scan_history": []}, f)

    def _read_local_db(self):
        with open(self.local_db_path, 'r') as f:
            return json.load(f)

    def _write_local_db(self, data):
        with open(self.local_db_path, 'w') as f:
            json.dump(data, f, indent=4)

    def insert_record(self, collection_name, record):
        try:
            if self.use_local:
                data = self._read_local_db()
                if collection_name not in data:
                    data[collection_name] = []
                
                # Simulate ObjectId for local storage
                if '_id' not in record:
                    record['_id'] = str(ObjectId())
                
                data[collection_name].append(record)
                self._write_local_db(data)
                logger.info(f"Inserted record into local {collection_name}")
                return record['_id']
            else:
                collection = self.db[collection_name]
                result = collection.insert_one(record)
                logger.info(f"Inserted record into {collection_name}")
                return result.inserted_id
        except Exception as e:
            raise CustomException(e, sys)

    def get_records(self, collection_name, query=None):
        try:
            if self.use_local:
                data = self._read_local_db()
                records = data.get(collection_name, [])
                if query:
                    filtered_records = []
                    for record in records:
                        match = True
                        for k, v in query.items():
                            if record.get(k) != v:
                                match = False
                                break
                        if match:
                            filtered_records.append(record)
                    return filtered_records
                return records
            else:
                collection = self.db[collection_name]
                if query:
                    records = list(collection.find(query))
                else:
                    records = list(collection.find())
                logger.info(f"Fetched {len(records)} records from {collection_name}")
                return records
        except Exception as e:
            raise CustomException(e, sys)

    def find_one(self, collection_name, query):
        try:
            records = self.get_records(collection_name, query)
            return records[0] if records else None
        except Exception as e:
            raise CustomException(e, sys)

    def update_record(self, collection_name, query, update_data):
        try:
            if self.use_local:
                data = self._read_local_db()
                records = data.get(collection_name, [])
                updated = False
                for record in records:
                    match = True
                    for k, v in query.items():
                        if record.get(k) != v:
                            match = False
                            break
                    if match:
                        record.update(update_data)
                        updated = True
                if updated:
                    self._write_local_db(data)
                return updated
            else:
                collection = self.db[collection_name]
                result = collection.update_one(query, {"$set": update_data})
                return result.modified_count > 0
        except Exception as e:
            raise CustomException(e, sys)
