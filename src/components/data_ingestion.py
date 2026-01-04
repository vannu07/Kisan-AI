import os
import sys
from src.logger.logging import logger
from src.exception.exception import CustomException
from src.utils.common import create_directories
from dataclasses import dataclass
from pathlib import Path
from werkzeug.utils import secure_filename

@dataclass
class DataIngestionConfig:
    root_dir: Path = Path("artifacts/raw_data")
    upload_folder: Path = Path("static/uploads")

class DataIngestion:
    def __init__(self):
        self.config = DataIngestionConfig()
        create_directories([self.config.root_dir, self.config.upload_folder])

    def save_uploaded_file(self, file):
        try:
            filename = secure_filename(file.filename)
            file_path = os.path.join(self.config.upload_folder, filename)
            file.save(file_path)
            
            # Also save to artifacts for raw data versioning
            artifact_path = os.path.join(self.config.root_dir, filename)
            # In a real scenario we might copy or move, here we save again or copy
            # Since file is a stream, we saved it once. Let's just use the static path for now
            # or copy it.
            import shutil
            shutil.copy(file_path, artifact_path)
            
            logger.info(f"File saved at {file_path} and {artifact_path}")
            return file_path
        except Exception as e:
            raise CustomException(e, sys)
