from OralDiseaseClassifier.config.configuration import ConfigurationManager
from OralDiseaseClassifier.components.data_processing import DataLoader
from OralDiseaseClassifier import logger

STAGE_NAME = "Data Processing and Preparation"


class DataPreparingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        data_processing_config = config.get_data_processing_config()
        
        # print(data_processing_config)
        data_handler = DataLoader(root_dir=data_processing_config.data_dir, batch_size=32, train_split=0.9)
        dataset = data_handler.prepareDataset()
        train_dataset = data_handler.get_train_loader()
        val_dataset = data_handler.get_val_loader()

        
        return dataset, train_dataset, val_dataset
if __name__ == '__main__':
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = DataPreparingPipeline()
        dataset, train_dataset, val_dataset = obj.main()
        logger.info(
            f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e
