from dotenv import load_dotenv
import os

# Cargamos las variables de entorno desde el archivo .env
load_dotenv()

# Obtenemos la clave de OpenAI desde las variables de entorno
OPENAI_API_KEY = os.getenv("Openai_key")
