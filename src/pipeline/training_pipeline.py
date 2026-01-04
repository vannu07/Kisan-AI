from src.components.model_trainer import ModelTrainer
from src.logger.logging import logger

class TrainingPipeline:
    def __init__(self):
        pass

    def run_pipeline(self):
        logger.info("Starting Training Pipeline")
        trainer = ModelTrainer()
        trainer.initiate_model_training()
        logger.info("Training Pipeline Completed")

if __name__ == "__main__":
    pipeline = TrainingPipeline()
    pipeline.run_pipeline()
