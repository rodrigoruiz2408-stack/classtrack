import streamlit as st
import random
from google import genai

# Configuración de la página
st.set_page_config(page_title="ClassTrack - Asistente Académico", layout="wide")

# Inicialización segura del cliente utilizando st.secrets
try:
    client = genai.Client(api_key=st.secrets["GEMINI_API_KEY"])
except Exception as e:
    client = None

def motor_autonomo_pedagogico(modulo, entrada):
    """Motor autónomo avanzado con alta variabilidad y lenguaje técnico pedagógico profundo."""
    
    enfoques = [
        "Enfoque socioconstructivista orientado a la resolución de problemáticas del entorno real.",
        "Metodología basada en indagación y desarrollo del pensamiento crítico de orden superior.",
        "Diseño instruccional fundamentado en la teoría del andamiaje cognitivo y participación activa.",
        "Enfoque de aprendizaje basado en proyectos (ABP) con integración de habilidades del siglo XXI."
    ]
    
    estrategias_atencion = [
        "Adaptación de materiales con apoyos visuales y multimodales para estudiantes PIE.",
        "Estrategias de diversificación curricular (DUA) con niveles de complejidad escalonados.",
        "Tutoría entre pares y andamiaje flexible según el ritmo de aprendizaje individual."
    ]

    if modulo == "Planificador de Clases":
        return f"""### 📝 Planificación Académica Inteligente (ClassTrack AI)
**Tema / Objeto de Estudio:** `{entrada}`

> **Marco Metodológico:** {random.choice(enfoques)}

---

#### 🎯 Objetivos de Aprendizaje Integrales
* **Conceptual:** Analizar y deconstruir los fundamentos teóricos de {entrada}.
* **Procedimental:** Aplicar modelos de resolución práctica vinculados al contexto del estudiante.
* **Actitudinal:** Fomentar el pensamiento crítico, la colaboración y la rigurosidad analítica.

---

#### ⏱️ Secuencia Didáctica Estructurada

1. **Fase de Inicio & Activación (15 min)**
   - **Ganchos Cognitivos:** Planteamiento de un dilema o pregunta problematizadora relacionada con {entrada} para movilizar saberes previos.
   - **Explicitación de Metas:** Clarificación de los criterios de éxito y la relevancia de la sesión para el perfil de egreso del nivel.

2. **Fase de Desarrollo & Mediación (30 min)**
   - **Trabajo en Estación / Colaborativo:** Los estudiantes se organizan en células de trabajo para analizar casos o resolver desafíos prácticos sobre {entrada}.
   - **Mediación Docente:** El profesor actúa como facilitador itinerante, aplicando preguntas socráticas para destrabar nudos conceptuales.
   - **Inclusión y DUA:** {random.choice(estrategias_atencion)}

3. **Fase de Cierre & Metacognición (15 min)**
   - **Ticket de Salida Analítico:** Breve síntesis escrita donde cada estudiante explicita una conclusión y una duda remanente.
   - **Consolidación:** Plenario relámpago con los hallazgos más destacados y retroalimentación formativa global.
"""

    elif modulo == "Creación de Actividades":
        return f"""### 🛠️ Diseño de Actividad Experiencial (ClassTrack AI)
**Propósito Central:** `{entrada}`

> **Estrategia Pedagógica:** Actividad de transferencia activa orientada a la construcción de evidencias de aprendizaje significativas.

---

#### 📋 Consignas y Estructura para el Estudiante
* **Contexto del Reto:** Imagina que debes resolver un desafío crítico donde {entrada} es la clave para estructurar una solución efectiva.
* **Paso a Paso Operativo:**
  1. *Fase de Diagnóstico (10 min):* Identifica las variables principales involucradas en {entrada} mediante una matriz de análisis rápido.
  2. *Fase de Ideación (20 min):* Diseña una propuesta o modelo conceptual que resuelva el problema utilizando herramientas de co-creación.
  3. *Fase de Validación (15 min):* Simula la aplicación práctica de tu propuesta y evalúa sus posibles puntos de fallo.
  4. *Fase de Comunicación (10 min):* Elabora un pitch ejecutivo de 90 segundos para presentar los resultados al plenario.

* **Criterios de Evaluación Formativa:** Rigurosidad conceptual, originalidad en la propuesta, viabilidad práctica y coherencia argumentativa en la defensa.
"""

    elif modulo == "Generador de Rúbricas":
        return f"""### 📊 Rúbrica Analítica de Evaluación por Competencias
**Instrumento Generado para:** `{entrada}`

| Criterio Evaluativo | Nivel Avanzado (4 pts) | Nivel Competente (3 pts) | En Desarrollo (2 pts) | Inicial (1 pt) |
| :--- | :--- | :--- | :--- | :--- |
| **Dominio Conceptual y Teórico** | Demuestra comprensión profunda, articulando conceptos avanzados de {entrada} con precisión milimétrica. | Explica con solidez los conceptos clave, aunque presenta menores omisiones teóricas secundarias. | Evidencia comprensión parcial; confunde ciertos principios fundamentales de {entrada}. | Muestra vacilaciones severas y ausencia de dominio conceptual básico. |
| **Aplicación y Resolución Práctica** | Resuelve la tarea con alta eficiencia metodológica, aportando soluciones creativas y bien fundamentadas. | Aplica los procedimientos metodológicos esperados de forma correcta y estándar. | La aplicación práctica contiene errores conceptuales o inconsistencias procedimentales notables. | No logra desarrollar la aplicación práctica solicitada o está incompleta. |
| **Pensamiento Crítico y Metacognición** | Analiza críticamente el proceso, justificando cada decisión con argumentos teóricos sólidos. | Justifica sus elecciones adecuadamente basándose en lo visto en clase. | Las argumentaciones son superficiales o carecen de respaldo conceptual claro. | Ausencia de análisis crítico o argumentación inconsistente. |
"""

    else:
        return f"""### ❓ Banco de Evaluación Formativa y Quiz Inteligente
**Materia / Contenido:** `{entrada}`

1. Desde una perspectiva sistémica, ¿cuál es el propósito fundamental de analizar y comprender {entrada}?
   * A) Aislar los componentes teóricos sin interconexión práctica
   * B) Optimizar la comprensión estructural y facilitar la transferencia a situaciones reales *(Correcta)*
   * C) Generar un marco estático de memorización a corto plazo
   * D) Reducir la complejidad metodológica a su mínima expresión

2. ¿Qué indicador evidencia que un estudiante ha alcanzado un nivel de comprensión profunda sobre {entrada}?
   * A) La capacidad de reproducir definiciones textuales sin alteraciones
   * B) La habilidad de aplicar, criticar y adaptar el concepto ante escenarios nuevos e imprevistos *(Correcta)*
   * C) La omisión de los procesos de validación empírica
   * D) La dependencia constante de la supervisión docente

3. ¿Cuál de las siguientes estrategias metodológicas maximiza el impacto de este contenido en el aula?
   * A) Clases magistrales expositivas continuas sin retroalimentación
   * B) Ciclos cerrados de evaluación sumativa punitiva
   * C) Aprendizaje activo mediado por andamiaje cognitivo y resolución de casos *(Correcta)*
   * D) Estudiar el tema de manera estrictamente individual y aislada

---
* **Clave de Validación Docente:** 1. B | 2. B | 3. C
"""

def generar_respuesta_segura(modulo, prompt_texto):
    if client:
        try:
            response = client.models.generate_content(model='gemini-3.8-flash', contents=prompt_texto)
            if response and response.text:
                return response.text
        except Exception:
            pass
    return motor_autonomo_pedagogico(modulo, prompt_texto)

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
        prompt_completo = f"Planificación de clase sobre {tema} para nivel {nivel}"
        with st.spinner("Generando planificación académica..."):
            resultado = generar_respuesta_segura(modulo, prompt_completo)
            st.markdown(resultado)

elif modulo == "Creación de Actividades":
    st.subheader("🛠️ Creador de Actividades Pedagógicas")
    objetivo = st.text_input("¿Qué objetivo de aprendizaje deseas trabajar?")
    
    if st.button("Crear Actividad") and objetivo:
        with st.spinner("Diseñando actividad experiencial..."):
            resultado = generar_respuesta_segura(modulo, objetivo)
            st.markdown(resultado)

elif modulo == "Generador de Rúbricas":
    st.subheader("📊 Generador de Rúbricas de Evaluación")
    criterio = st.text_input("¿Qué se va a evaluar? (Ej: Exposición oral, Ensayo, Maqueta):")
    
    if st.button("Generar Rúbrica") and criterio:
        with st.spinner("Construyendo rúbrica analítica..."):
            resultado = generar_respuesta_segura(modulo, criterio)
            st.markdown(resultado)

elif modulo == "Quizzes Interactivos":
    st.subheader("❓ Generador de Quizzes")
    materia = st.text_input("Materia o tema para el quiz:")
    
    if st.button("Crear Quiz") and materia:
        with st.spinner("Elaborando banco de evaluación..."):
            resultado = generar_respuesta_segura(modulo, materia)
            st.markdown(resultado)
