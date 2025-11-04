from langchain_text_splitters import CharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_community.document_loaders.csv_loader import CSVLoader
from langchain_community.embeddings import HuggingFaceEmbeddings
from tqdm import tqdm
from dotenv import load_dotenv

load_dotenv()

class VectorStoreBuilder:
    def __init__(self, csv_path: str, persist_dir: str = "chroma_db"):
        self.csv_path = csv_path
        self.persist_dir = persist_dir
        self.embedding = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

    def create_vector_store(self):
        loader = CSVLoader(
            file_path=self.csv_path,
            encoding="utf-8",
            metadata_columns=[]
        )

        data = loader.load()
        print("Data loaded from CSV file.")

        splitter = CharacterTextSplitter(
            chunk_size=1000,
            chunk_overlap=0
        )

        texts = splitter.split_documents(data)
        print(f"Total document chunks: {len(texts)}")

        db = None
        batch_size = 5000

        for i in tqdm(range(0, len(texts), batch_size), desc="Building Chroma Vector Store"):
            batch = texts[i:i + batch_size]
            if db is None:
                db = Chroma.from_documents(
                    batch,
                    self.embedding,
                    persist_directory=self.persist_dir
                )
            else:
                db.add_documents(batch)

        db.persist()
        print(f"Vector store created and saved at: {self.persist_dir}")

    def load_vector_store(self):
        return Chroma(
            persist_directory=self.persist_dir,
            embedding_function=self.embedding
        )
