#from langchain_openia import OpenAIEmbeddings
from langchain_openai import OpenAIEmbeddings
from langchain_chroma import Chroma

from app.config import OPENAI_API_KEY
from app.loader import load_documents
from app.splitter import split_documents

#Creamos la funcion para crear la base vectorial
def create_vectorstore():
    #cargamos los documentos
    documentos = load_documents()

    #divimos los documentos
    documentos_divididos = split_documents(documentos)

    #creamos la base vectorial con Chroma y los embeddings de OpenAI
    embeddings = OpenAIEmbeddings(model="text-embedding-3-small", api_key=OPENAI_API_KEY)
    vectorstore = Chroma.from_documents(
        documents=documentos_divididos,
        embedding=embeddings,
        persist_directory="db"
    )   

    print("1. Cargando documentos...")
    documentos = load_documents()

    print("2. Dividiendo documentos...")
    documentos_divididos = split_documents(documentos)

    print("3. Creando embeddings...")
    embeddings = OpenAIEmbeddings(
    model="text-embedding-3-small",
    api_key=OPENAI_API_KEY
    )

    print("4. Creando Chroma...")
    vectorstore = Chroma.from_documents(
    documents=documentos_divididos,
    embedding=embeddings,
    persist_directory="db"
     )

    print("5. Base vectorial creada") 

   

    return vectorstore
if __name__ == "__main__":
    create_vectorstore()
  