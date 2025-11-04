# from langchain.chains import RetrievalQA
# from langchain_groq import ChatGroq
# from src.prompt_template import get_movie_prompt

# class MovieRecommender:
#     def __init__(self, retriever, api_key:str, model_name:str):
#         self.llm = ChatGroq(api_key = api_key, model = model_name, temperature = 0)
#         self.prompt = get_movie_prompt()

#         self.qa_chain = RetrievalQA.from_chain_type(
#             llm = self.llm,
#             chain_type = "stuff",
#             retriever = retriever,
#             return_source_documents = True,
#             chain_type_kwargs = {"prompt":self.prompt}
#         )

#     def get_recommendation(self,query:str):
#         result = self.qa_chain({"query":query})
#         return result['result']
    

# from langchain_groq import ChatGroq
# from src.prompt_template import get_movie_prompt

# class MovieRecommender:
#     def __init__(self, retriever, api_key: str, model_name: str):
#         self.retriever = retriever
#         self.llm = ChatGroq(api_key=api_key, model=model_name, temperature=0)
#         self.prompt_template = get_movie_prompt()

#     def get_recommendation(self, query: str):
#         # Step 1: Retrieve top docs
#         docs = self.retriever.get_relevant_documents(query)
#         context = "\n".join([d.page_content for d in docs])

#         # Step 2: Format prompt manually
#         prompt = self.prompt_template.format(context=context, query=query)

#         # Step 3: Call Groq LLM directly
#         response = self.llm.invoke(prompt)
#         return response.content


from langchain_groq import ChatGroq
from src.prompt_template import get_movie_prompt

class MovieRecommender:
    def __init__(self, retriever, api_key: str, model_name: str):
        self.retriever = retriever
        self.llm = ChatGroq(api_key=api_key, model=model_name, temperature=0)
        self.prompt_template = get_movie_prompt()

    def get_recommendation(self, query: str):
        # Step 1: Retrieve relevant docs
        # docs = self.retriever.get_relevant_documents(query)
        try:
            # docs = self.retriever.get_relevant_documents(query)
            docs = self.retriever.invoke(query)
        except Exception:
            # docs = self.retriever.get_relevant_documents({"question": query})
            docs = self.retriever.invoke({"question": query})

        context = "\n".join([d.page_content for d in docs])
        prompt = self.prompt_template.format(context=context, question=query)
        response = self.llm.invoke(prompt)
        return response.content

