"""
Importamos la librería pathlib
para trabajar con rutas de archivos
"""
from langchain_community.document_loaders import PyPDFLoader
from pathlib import Path


def load_documents():
    # Le indicamos la ruta de la carpeta que queremos verificar
    ruta = Path("data")

    # Hacemos la verificación de la existencia de la carpeta
    print(ruta.exists())

    # Mostramos la lista de archivos PDF
    print(list(ruta.glob("*.pdf")))

    # Lista donde almacenaremos todos los documentos
    todos_los_documentos = []

    # Recorremos todos los archivos PDF
    for archivo in ruta.glob("*.pdf"):
        # Cargamos el archivo PDF
        loader = PyPDFLoader(str(archivo))

        # Obtenemos los documentos del PDF
        documentos = loader.load()

        # Agregamos los documentos a la lista general
        todos_los_documentos.extend(documentos)

        print(
            f"Se han cargado {len(documentos)} documentos del archivo {archivo.name}"
        )

    print(
        f"Se han cargado un total de {len(todos_los_documentos)} documentos"
    )

    return todos_los_documentos


if __name__ == "__main__":
    documentos = load_documents()