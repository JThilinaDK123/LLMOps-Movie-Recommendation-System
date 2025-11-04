from langchain_groq import ChatGroq
from src.prompt_template import get_movie_prompt

class MovieRecommender:
    def __init__(self, retriever, api_key: str, model_name: str):
        self.retriever = retriever
        self.llm = ChatGroq(api_key=api_key, model=model_name, temperature=0)
        self.prompt_template = get_movie_prompt()

    def get_recommendation(self, query: str):
        try:
            docs = self.retriever.invoke(query)
        except Exception:
            docs = self.retriever.invoke({"question": query})

        context = "\n".join([d.page_content for d in docs])
        prompt = self.prompt_template.format(context=context, question=query)
        response = self.llm.invoke(prompt)
        return response.content

