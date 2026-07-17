from app.rag import create_rag
import streamlit as st
from PIL import Image

# Configuración de la página
st.set_page_config(
    page_title="INTECMIFA RAG",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)
#Cargamos el css
def load_css():
    with open("css/style.css") as css:
        st.markdown(f"<style>{css.read()}</style>", unsafe_allow_html=True)
load_css()    

#Agregamos las columnas
col1, col2 = st.columns([1,5])

#with col1:
    #st.image("assets/logo_intecmifa.jpeg", width=90)

with col2:
    st.markdown("""
    <div class="hero-text">

    <h1>INTECMIFA AI</h1>

    <p>Asistente Virtual Inteligente</p>

  

    </div>
    """,
unsafe_allow_html=True)

st.markdown("""
<div class="status-bar">

<div class="status-item">🟢 <strong>Sistema en línea</strong></div>

<div class="status-item">🤖 <strong>GPT-4o mini</strong></div>

<div class="status-item">📚 <strong>RAG Inteligente</strong></div>

<div class="status-item">⚡ <strong>Powered by ILDAEX AI Platform</strong></div>

</div>
""", unsafe_allow_html=True)

# Inicializar el sistema RAG
rag = create_rag()

if "messages" not in st.session_state:
    st.session_state.messages = []


# Historial del chat
if "messages" not in st.session_state:
    st.session_state.messages = []

# Mostrar mensajes anteriores
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if len(st.session_state.messages) == 0:
  
  st.markdown("""
<div class="welcome-card">

<h2>👋 ¡Bienvenido!</h2>

<p>
Soy el asistente virtual de <b>INTECMIFA</b>.
</p>

<p>Puedo ayudarte con:</p>

<ul>
    <li>📚 Cursos</li>
    <li>📝 Inscripciones</li>
    <li>📄 Requisitos</li>
    <li>⏰ Horarios</li>
    <li>📞 Información general</li>
</ul>

<p>
Escribe tu pregunta en el cuadro de texto para comenzar.
</p>

</div>
""", unsafe_allow_html=True)


# Entrada del usuario
pregunta = st.chat_input("Escribe tu pregunta aquí...")

if pregunta:

    # Mostrar mensaje del usuario
    st.session_state.messages.append({
        "role": "user",
        "content": pregunta
    })

    with st.chat_message("user"):
        st.markdown(pregunta)

    # Consultar el RAG
    with st.spinner("🤖 Analizando la información..."):

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