from OralDiseaseClassifier import logger
from OralDiseaseClassifier.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from OralDiseaseClassifier.pipeline.stage_02_data_processing import DataPreparingPipeline
# from src.OralDiseaseClassifier.pipeline.stage_03_model_training import ModelTrainingPipeline
# from OralDiseaseClassifier.pipeline.stage_04_model_evaluation import EvaluationPipeline

# STAGE_NAME = "Data Ingestation"

# try:
#     logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
#     obj = DataIngestionTrainingPipeline()
#     obj.main()
#     logger.info(
#         f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")

# except Exception as e:
#     logger.exception(e)
#     raise e

STAGE_NAME = "Data Processing and Preparation"

try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    obj = DataPreparingPipeline()
    dataset, train_dataset, val_dataset = obj.main()
    logger.info(
        f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e

