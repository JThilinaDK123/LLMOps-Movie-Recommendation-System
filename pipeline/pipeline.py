from src.vectore_store import VectorStoreBuilder
from src.reccomender import MovieRecommender 
from config.config import GROQ_API_KEY, MODEL_NAME
from utils.logger import get_logger
from utils.custom_exception import CustomException

logger = get_logger(__name__)

class MovieRecommendationPipeline:
    def __init__(self, persist_dir: str = "chroma_db"):
        try:
            logger.info("Initializing Movie Recommendation Pipeline...")

            ## Build or load vector store
            vector_builder = VectorStoreBuilder(csv_path="", persist_dir=persist_dir)
            retriever = vector_builder.load_vector_store().as_retriever()

            ## Initialize recommender (manual LLM + retriever)
            self.recommender = MovieRecommender(retriever, GROQ_API_KEY, MODEL_NAME)

            logger.info("Pipeline initialized successfully ✅")

        except Exception as e:
            logger.error(f"Failed to initialize pipeline: {str(e)}")
            raise CustomException("Error during pipeline initialization", e)
        
    def recommend(self, query: str) -> str:
        try:
            logger.info(f"Received query: {query}")

            recommendation = self.recommender.get_recommendation(query)

            logger.info("Recommendation generated successfully ✅")
            return recommendation

        except Exception as e:
            logger.error(f"Failed to generate recommendation: {str(e)}")
            raise CustomException("Error during recommendation generation", e)
