# import streamlit as st
# from pipeline.pipeline import MovieRecommendationPipeline
# from dotenv import load_dotenv

# st.set_page_config(page_title="Movie Recommender", layout="wide")
# load_dotenv()

# @st.cache_resource
# def init_pipeline():
#     return MovieRecommendationPipeline()

# pipeline = init_pipeline()

# st.title("🎬 Movie Recommender System")
# query = st.text_input("Enter your movie preferences (e.g., emotional drama with strong female lead, sci-fi adventure, romantic comedy):")

# if query:
#     with st.spinner("Fetching personalized movie recommendations..."):
#         response = pipeline.recommend(query)
#         st.markdown("### 🎥 Recommendations")
#         st.write(response)



import streamlit as st
from pipeline.pipeline import MovieRecommendationPipeline
from dotenv import load_dotenv

st.set_page_config(page_title="Movie Recommender", layout="wide")

load_dotenv()

@st.cache_resource
def init_pipeline():
    """Initialize the Movie Recommendation pipeline."""
    return MovieRecommendationPipeline()

pipeline = init_pipeline()

st.title("🎬 Movie Recommender System")
st.markdown("Get personalized movie recommendations powered by LLMs and contextual search!")

query = st.text_input(
    "Enter your movie preferences (e.g., emotional drama with strong female lead, sci-fi adventure, romantic comedy):"
)

if query:
    with st.spinner("🔍 Fetching personalized movie recommendations..."):
        try:
            recommendations = pipeline.recommend(query)
            st.markdown("### 🎥 Recommendations")
            st.write(recommendations)
        except Exception as e:
            st.error(f"An error occurred: {e}")
