
# Importamos los modulos a utilizar
from app.loader import load_documents
from langchain_text_splitters import RecursiveCharacterTextSplitter

def split_documents(documentos):
    # Creamos el divisor de texto
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=300,
        chunk_overlap=30
    )
    # Dividimos los documentos
    return splitter.split_documents(documentos)



if __name__ == "__main__":
    documentos = load_documents()
    # Dividimos los documentos
    documentos_divididos = split_documents(documentos)
    print(f"Se han dividido un total de {len(documentos_divididos)} documentos")