

from app.config import OPENAI_API_KEY
from app.retriever import get_retriever
from langchain_openai import ChatOpenAI

from langchain_classic.chains import create_retrieval_chain
from langchain_classic.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate

def create_rag():
    """
    Inicializa y configura la cadena RAG completa para INTECMIFA.
    Retorna el objeto rag_chain listo para ser invocado.
    """
    # 1. Obtener y configurar el recuperador de datos (Retriever)
    retriever = get_retriever()
    # Para cambiar los parámetros de búsqueda de forma segura en las versiones actuales,
    # se utiliza el método .search_kwargs directamente en el diccionario del objeto.
    retriever.search_kwargs = {"k": 3}

    # 2. Configurar el modelo de lenguaje de OpenAI (Actualizado a gpt-4o-mini)
    llm = ChatOpenAI(
        model="gpt-4o-mini", 
        api_key=OPENAI_API_KEY,
        temperature=0.2,
        #max_tokens=700
    )

    # 3. Estructurar el prompt del sistema y del usuario con la coma de separación obligatoria
    prompt = ChatPromptTemplate.from_messages([
        (
            "system",
      """ Eres el asistente virtual de INTECMIFA.

Tu objetivo es ayudar a los usuarios de manera amable y profesional.

Si el usuario realiza un saludo como "hola", "buenos días", "buenas tardes", "gracias", "adiós" o cualquier conversación casual, responde naturalmente como un asistente virtual.

Si la pregunta está relacionada con INTECMIFA, responde utilizando únicamente la información del contexto proporcionado.

Si el contexto no contiene la respuesta, responde:

"No encontré esa información en la base de conocimientos de INTECMIFA."

No inventes información ni hagas suposiciones.

Responde siempre en español.
Contexto:
{context}"""
        ), # <-- Coma de control para evitar el SyntaxWarning
        (
            "human", 
            "{input}"
        )
 ])
    # 4. Construir las cadenas jerárquicas del RAG
    documents_chain = create_stuff_documents_chain(llm, prompt)
    rag_chain = create_retrieval_chain(retriever, documents_chain)

    return rag_chain


# --- Bloque de prueba de ejecución ---
#if __name__ == "__main__":
    #print("Iniciando el sistema RAG de INTECMIFA...")

    # Construimos la cadena
   # mi_agente_rag = create_rag()
#while True:
   # preguntas = input("Ingrese su pregunta para INTECMIFA_Agent_IA: ")
   # if preguntas.lower() in ["salir", "exit", "quit"]:
    #    print("Saliendo del sistema RAG de INTECMIFA...")
    #   break
    # Obtener el retriever para probarlo
    #respuesta = mi_agente_rag.invoke( preguntas)
    #retriever = get_retriever()

    #docs = retriever.invoke(preguntas)


    # Ahora ejecutamos el RAG
   # respuesta = mi_agente_rag.invoke({"input": preguntas})

    # Obtener el retriever para probarlo
   #retriever = get_retriever()

    #docs = retriever.invoke(preguntas)

    # Ahora ejecutamos el RAG
   # respuesta = mi_agente_rag.invoke({"input": preguntas})

    #print("\n=== RESPUESTA RECIBIDA ===")
  #  print(preguntas)
   # print(respuesta["answer"])