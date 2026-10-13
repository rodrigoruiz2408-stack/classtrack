import streamlit as st
from google import genai

st.set_page_config(page_title="ClassTrack", layout="wide")

# Configuración del cliente de Gemini
client = genai.Client(api_key=st.secrets["GEMINI_API_KEY"])
def generar_respuesta_segura(prompt_texto):
    try:
        response = client.models.generate_content(model='gemini-2.5-flash', contents=prompt_texto)
        return response.text
    except Exception as e:
        if "503" in str(e) or "UNAVAILABLE" in str(e) or "429" in str(e) or "RESOURCE_EXHAUSTED" in str(e):
            st.warning("⚠️ Límite de la API alcanzado o alta demanda. Por favor, intenta de nuevo en unos momentos.")
        else:
            st.error(f"Ocurrió un error inesperado: {e}")
        return None

st.title("📚 ClassTrack")
st.write("Bienvenido a ClassTrack, tu asistente para la gestión académica.")

# Ejemplo de uso de la función
prompt_usuario = st.text_input("Escribe una consulta para la IA:")
if prompt_usuario:
    respuesta = generar_respuesta_segura(prompt_usuario)
    if respuesta:
        st.write(respuesta)
