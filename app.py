import streamlit as st
from google import genai

st.set_page_config(
    page_title="ClassTrack - Asistente Pedagógico AI",
    page_icon="📚",
    layout="wide"
)

st.markdown("""
    <style>
    .main-header { font-size: 2.2rem; color: #1E3A8A; font-weight: 700; }
    .sub-header { font-size: 1.2rem; color: #4B5563; }
    </style>
""", unsafe_allow_html=True)

client = genai.Client(api_key="AQ.Ab8RN6KYYxhTrQRG7VBmWXVfKjiAZDf0CbP2Rug0j1ooJ4bM3A")

st.sidebar.image("https://img.icons8.com/color/96/class.png", width=80)
st.sidebar.title("ClassTrack Navigation")
modulo = st.sidebar.radio(
    "Selecciona un Módulo:",
    ["Planificador de Clases", "Creación de Actividades", "Rúbricas de Evaluación", "Quizzes Interactivos", "Inclusión PIE"]
)

st.sidebar.markdown("---")
st.sidebar.info("💡 Sistema conectado y listo para la presentación.")

def generar_respuesta_segura(prompt_texto):
    try:
       response = client.models.generate_content(model='gemini-2.5-flash', contents=prompt_texto)
        return response.text
    except Exception as e:
        if "503" in str(e) or "UNAVAILABLE" in str(e):
            st.warning("⚠️ Los servidores de IA están experimentando alta demanda en este momento. Por favor, dale al botón de nuevo en unos segundos.")
        else:
            st.error(f"Ocurrió un error inesperado: {e}")
        return None

if modulo == "Planificador de Clases":
    st.markdown('<p class="main-header">📋 Planificador de Clases Inteligente</p>', unsafe_allow_html=True)
    st.markdown('<p class="sub-header">Genera planificaciones curriculares alineadas y detalladas en segundos.</p>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    with col1:
        materia = st.text_input("Asignatura / Materia", "Matemáticas")
        nivel = st.text_input("Nivel / Curso", "1° Medio")
    with col2:
        unidad = st.text_input("Unidad o Tema Central", "Álgebra y Funciones")
        tiempo = st.selectbox("Duración de la clase", ["45 minutos", "90 minutos", "Doble bloque"])

    objetivo = st.text_area("Objetivo de Aprendizaje (OA) o meta de la clase")

    if st.button("Generar Planificación Completa", type="primary"):
        if objetivo:
            with st.spinner("Diseñando la planificación pedagógica..."):
                prompt = f"Actúa como un experto curricular. Diseña una planificación de clase detallada para la asignatura de {materia}, nivel {nivel}, unidad {unidad}, duración {tiempo}. Objetivo de aprendizaje: {objetivo}. Incluye inicio, desarrollo, cierre y evaluación formativa."
                resultado = generar_respuesta_segura(prompt)
                if resultado:
                    st.markdown("---")
                    st.markdown(resultado)
        else:
            st.warning("Por favor, ingresa un objetivo de aprendizaje.")

elif modulo == "Creación de Actividades":
    st.markdown('<p class="main-header">✨ Creación de Actividades Dinámicas</p>', unsafe_allow_html=True)
    tema_act = st.text_input("¿Sobre qué contenido o tema necesitas una actividad?")
    if st.button("Generar Actividad"):
        with st.spinner("Creando dinámica..."):
            prompt = f"Diseña una actividad de aprendizaje práctica, innovadora y atractiva para estudiantes sobre el tema: {tema_act}."
            resultado = generar_respuesta_segura(prompt)
            if resultado:
                st.markdown(resultado)

elif modulo == "Rúbricas de Evaluación":
    st.markdown('<p class="main-header">📊 Generador de Rúbricas</p>', unsafe_allow_html=True)
    criterio = st.text_input("Trabajo o proyecto a evaluar")
    if st.button("Generar Rúbrica"):
        with st.spinner("Construyendo tabla de evaluación..."):
            prompt = f"Genera una rúbrica de evaluación detallada en formato de tabla Markdown con 4 niveles de desempeño para: {criterio}."
            resultado = generar_respuesta_segura(prompt)
            if resultado:
                st.markdown(resultado)

elif modulo == "Quizzes Interactivos":
    st.markdown('<p class="main-header">❓ Quizzes y Evaluaciones Cortas</p>', unsafe_allow_html=True)
    tema_quiz = st.text_input("Materia o contenido para el quiz")
    if st.button("Crear Quiz"):
        with st.spinner("Elaborando preguntas..."):
            prompt = f"Crea un quiz de 5 preguntas de opción múltiple con sus respectivas respuestas correctas sobre: {tema_quiz}."
            resultado = generar_respuesta_segura(prompt)
            if resultado:
                st.markdown(resultado)

elif modulo == "Inclusión PIE":
    st.markdown('<p class="main-header">🤝 Adaptaciones Curriculares PIE</p>', unsafe_allow_html=True)
    necesidad = st.text_input("Tipo de NEE o desafío de aprendizaje (ej. TEA, Dislexia, TDAH)")
    actividad_base = st.text_area("Actividad original de la clase")
    if st.button("Generar Adaptación"):
        with st.spinner("Adaptando recursos..."):
            prompt = f"Adapta la siguiente actividad considerando estrategias para estudiantes con {necesidad}. Actividad base: {actividad_base}"
            resultado = generar_respuesta_segura(prompt)
            if resultado:
                st.markdown(resultado)
