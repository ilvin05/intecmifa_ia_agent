from langchain_chroma import Chroma
from langchain_openai import OpenAIEmbeddings
from app.config import OPENAI_API_KEY

def get_retriever():
    # Cargar la base vectorial desde el directorio "db"
    vectorstore = Chroma(persist_directory="db", embedding_function=OpenAIEmbeddings
    (model="text-embedding-3-small", api_key=OPENAI_API_KEY))
    retriever = vectorstore.as_retriever()
    return retriever
    
if __name__ == "__main__":
    # Crear un retriever a partir de la base vectorial
    retriever = get_retriever()
    print("Se ha creado el retriever a partir de la base vectorial")
   