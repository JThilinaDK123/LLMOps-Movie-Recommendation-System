from src.data_loader_Processing import DataLoaderProcessing
from src.vectore_store import VectorStoreBuilder
from dotenv import load_dotenv
from utils.logger import get_logger
from utils.custom_exception import CustomException

load_dotenv()

logger = get_logger(__name__)

def main():
    try:
        logger.info("Starting to build pipeline...")

        loader = DataLoaderProcessing("data/movies.csv" , "data/movies_updated.csv")
        processed_csv = loader.load_data()

        logger.info("Data loaded and processed...")

        vector_builder = VectorStoreBuilder(processed_csv)
        vector_builder.create_vector_store()

        logger.info("Vector store Built successfully....")

        logger.info("Pipeline built successfully....")
    except Exception as e:
            logger.error(f"Failed to execute pipeline {str(e)}")
            raise CustomException("Error during pipeline " , e)
    
if __name__=="__main__":
     main()
