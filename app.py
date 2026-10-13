import streamlit as st
from google import genai

# Configuración de la página
st.set_page_config(page_title="ClassTrack - Asistente Académico", layout="wide")

# Inicialización segura del cliente utilizando st.secrets
try:
    client = genai.Client(api_key=st.secrets["GEMINI_API_KEY"])
except Exception as e:
    st.error("⚠️ Error de configuración: No se encontró la clave GEMINI_API_KEY en los secretos de Streamlit.")
    st.stop()

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

# Interfaz Principal
st.title("📚 ClassTrack")
st.markdown("Tu copiloto inteligente para la gestión y creación de instrumentos pedagógicos.")

# Menú lateral para seleccionar el módulo
modulo = st.sidebar.selectbox(
    "Selecciona un módulo",
    ["Planificador de Clases", "Creación de Actividades", "Generador de Rúbricas", "Quizzes Interactivos"]
)

st.markdown("---")

if modulo == "Planificador de Clases":
    st.subheader("📝 Planificador de Clases Inteligente")
    tema = st.text_input("Tema o contenido de la clase:")
    nivel = st.selectbox("Nivel / Curso:", ["Enseñanza Básica", "Enseñanza Media", "Educación Superior"])
    
    if st.button("Generar Planificación") and tema:
        prompt = f"Crea una planificación de clase detallada sobre '{tema}' dirigida a un nivel de {nivel}, incluyendo objetivo, inicio, desarrollo y cierre."
        with st.spinner("Generando planificación..."):
            resultado = generar_respuesta_segura(prompt)
            if resultado:
                st.markdown(resultado)

elif modulo == "Creación de Actividades":
    st.subheader("🛠️ Creador de Actividades Pedagógicas")
    objetivo = st.text_input("¿Qué objetivo de aprendizaje deseas trabajar?")
    
    if st.button("Crear Actividad") and objetivo:
        prompt = f"Diseña una actividad práctica e innovadora para los estudiantes enfocada en el siguiente objetivo: '{objetivo}'."
        with st.spinner("Diseñando actividad..."):
            resultado = generar_respuesta_segura(prompt)
            if resultado:
                st.markdown(resultado)

elif modulo == "Generador de Rúbricas":
    st.subheader("📊 Generador de Rúbricas de Evaluación")
    criterio = st.text_input("¿Qué se va a evaluar? (Ej: Exposición oral, Ensayo, Maqueta):")
    
    if st.button("Generar Rúbrica") and criterio:
        prompt = f"Genera una tabla de rúbrica de evaluación clara y estructurada para: '{criterio}' con niveles de logro (Excelente, Bueno, Suficiente, Insuficiente)."
        with st.spinner("Construyendo rúbrica..."):
            resultado = generar_respuesta_segura(prompt)
            if resultado:
                st.markdown(resultado)

elif modulo == "Quizzes Interactivos":
    st.subheader("❓ Generador de Quizzes")
    materia = st.text_input("Materia o tema para el quiz:")
    
    if st.button("Crear Quiz") and materia:
        prompt = f"Crea un quiz de 5 preguntas de selección múltiple sobre '{materia}' indicando sus respectivas respuestas correctas al final."
        with st.spinner("Elaborando quiz..."):
            resultado = generar_respuesta_segura(prompt)
            if resultado:
                st.markdown(resultado)
