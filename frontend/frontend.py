from app.rag import create_rag
import streamlit as st

# Configuración de la página
st.set_page_config(
    page_title="INTECMIFA RAG",
    page_icon="🤖",
    layout="wide"
)

st.title("INTECMIFA Agente IA")
st.subheader("Asistente Virtual Inteligente de INTECMIFA")
st.caption("Powered by ILDAEX")

# Inicializar el sistema RAG
rag = create_rag()
with st.sidebar:
    #st.image("frontend/assets/intecmifa_logo.png", width=140)
    st.markdown("INTECMIFA")
    st.success("🟢Sistema Activo")
    st.divider()
    st.button("💬Nuevo Chat", key="new_chat", on_click=lambda: st.session_state.messages.clear())
    st.button("📄Documento")
    st.button("📊Estado")
    st.button("⚙️Configuración")
    st.divider()
    st.caption("powered by ILDAEX")
    st.markdown("ILDAEX AI PLATFORM")

# Historial del chat
if "messages" not in st.session_state:
    st.session_state.messages = []

# Mostrar mensajes anteriores
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Entrada del usuario
pregunta = st.chat_input("Ingrese su pregunta para INTECMIFA_Agent_IA:")

if pregunta:

    # Mostrar mensaje del usuario
    st.session_state.messages.append({
        "role": "user",
        "content": pregunta
    })

    with st.chat_message("user"):
        st.markdown(pregunta)

    # Consultar el RAG
    respuesta = rag.invoke({
        "input": pregunta
    })

    # (Opcional) Mostrar la respuesta completa para depuración
    # st.write(respuesta)

    # Obtener únicamente la respuesta final
    respuesta_final = respuesta.get(
        "answer",
        "No se encontró una respuesta."
    )

    # Mostrar respuesta del asistente
    with st.chat_message("assistant"):
        st.markdown(respuesta_final)

    # Guardar respuesta en el historial
    st.session_state.messages.append({
        "role": "assistant",
        "content": respuesta_final
    })