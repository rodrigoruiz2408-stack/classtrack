import streamlit as st
import random
from google import genai

# Configuración de la página
st.set_page_config(
    page_title="ClassTrack",
    page_icon="📚",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Estilos CSS profesionales
st.markdown("""
    <style>
    .main { background-color: #f8fafc; }
    .stButton>button {
        width: 100%;
        border-radius: 8px;
        font-weight: 600;
        background-color: #2563eb;
        color: white;
        padding: 0.5rem 1rem;
    }
    .stButton>button:hover {
        background-color: #1d4ed8;
    }
    .card {
        background: white;
        padding: 20px;
        border-radius: 10px;
        border: 1px solid #e2e8f0;
        box-shadow: 0 1px 3px rgba(0,0,0,0.05);
    }
    </style>
""", unsafe_allow_html=True)

# Inicialización segura del cliente utilizando st.secrets
try:
    client = genai.Client(api_key=st.secrets["GEMINI_API_KEY"])
except Exception as e:
    client = None

def motor_masivo_extremo(modulo, entrada, nivel_curso=""):
    """Motor algorítmico masivo de alta capacidad con múltiples bases de conocimiento especializadas."""
    e_low = entrada.lower()
    
    # --- MÓDULO PIE / INCLUSIÓN (Independiente) ---
    if modulo == "Módulo PIE / Inclusión":
        banco_pie = [
            ("Adecuación Curricular Grado 1 (Acceso)", "Implementación de soportes visuales directos, pictogramas y glosario de términos clave previo al abordaje de la unidad."),
            ("Adecuación Curricular Grado 2 (Proceso)", "Fraccionamiento de instrucciones complejas en secuencias de 3 pasos cortos, uso de organizadores gráficos y tiempo extendido en un 30%."),
            ("Adecuación Curricular Grado 3 (Evaluación)", "Evaluación diversificada (DUA) permitiendo demostración oral, esquemática o mediante proyectos prácticos supervisados en lugar de pruebas escritas masivas."),
            ("Apoyo Multisensorial Específico", "Uso de material manipulable, regletas lógicas y diseño de estaciones de aprendizaje con bajo estímulo distractores.")
        ]
        estrategia, desc = random.choice(banco_pie)
        return f"""### 🤝 Módulo Especializado PIE (Integración Escolar)
**Foco de Adecuación:** `{entrada}` | **Nivel:** `{nivel_curso}`

---

#### 📋 Plan de Diversificación y Apoyo (DUA)
* **Estrategia Seleccionada:** `{estrategia}`
* **Descripción Operativa:** {desc}
* **Mediación Docente Sugerida:**
  1. *Anticipación y Anclaje:* Conectar el contenido nuevo con experiencias concretas del estudiante.
  2. *Acompañamiento Gradual:* Reducir la carga cognitiva inicial mediante andamiaje directo los primeros minutos.
  3. *Validación Formativa:* Evaluar progreso mediante hitos parciales y refuerzo positivo constante.
"""

    # --- BANCOS DE CONOCIMIENTO TÉCNICO MASIVO PARA OTROS MÓDULOS ---
    if any(k in e_low for k in ["limite", "derivada", "calculo", "integral", "limites", "infinitesimal"]):
        area = "Cálculo Infinitesimal y Análisis Real"
        enfoque = "rigor analítico, tasas de cambio instantáneo y modelamiento de funciones"
        banco_quizzes = [
            ("¿Cuál es el valor del límite $\\lim_{x \\to 2} (3x^2 - 5)$?", ["A) 7 *(Correcta)*", "B) 6", "C) 11", "D) 1"]),
            ("¿Cuál es la derivada de la función polinómica $f(x) = 4x^3 - 2x + 5$?", ["A) $12x^2 - 2$ *(Correcta)*", "B) $12x^3 - 2$", "C) $4x^2 - 2$", "D) $12x - 2$"]),
            ("¿Qué representa geométricamente la derivada de una función en un punto dado?", ["A) El área bajo la curva", "B) La pendiente de la recta tangente a la curva en ese punto *(Correcta)*", "C) La intersección con el eje vertical", "D) El límite superior del dominio"]),
            ("Al evaluar el límite $\\lim_{x \\to 0} \\frac{\\sin(x)}{x}$, ¿qué valor notable se obtiene?", ["A) 0", "B) 1 *(Correcta)*", "C) Infinito", "D) No existe"]),
            ("¿Cuál es la regla de derivación aplicable al producto de dos funciones derivables $f(x) \\cdot g(x)$?", ["A) $f'(x) \\cdot g'(x)$", "B) $f'(x)g(x) + f(x)g'(x)$ *(Correcta)*", "C) $\\frac{f'(x)}{g'(x)}$", "D) $f(x)g(x) - f'(x)g'(x)$"])
        ]
    elif any(k in e_low for k in ["algebra", "matematica", "ecuacion", "numeros", "geometria", "funciones", "polinomio"]):
        area = "Álgebra y Razonamiento Lógico-Matemático"
        enfoque = "abstracción formal, modelamiento cuantitativo y resolución de sistemas"
        banco_quizzes = [
            ("Dada la función lineal $f(x) = 2x + 3$, ¿cuál es el valor de $f(4)$?", ["A) 5", "B) 11 *(Correcta)*", "C) 8", "D) 14"]),
            ("Al despejar la incógnita en la ecuación lineal $3x - 6 = 12$, el valor de $x$ es:", ["A) 2", "B) 4", "C) 6 *(Correcta)*", "D) 8"]),
            ("¿Cuál es la representación gráfica principal de una función cuadrática $ax^2 + bx + c$?", ["A) Una línea recta", "B) Una parábola *(Correcta)*", "C) Una circunferencia", "D) Una hipérbola"]),
            ("¿Qué representa la pendiente 'm' en la ecuación de la recta $y = mx + b$?", ["A) La tasa de cambio y la inclinación de la recta *(Correcta)*", "B) El punto de corte con el eje vertical", "C) Una constante nula", "D) El radio de curvatura"]),
            ("Al resolver un sistema de ecuaciones lineales de 2x2, ¿qué indica una solución única?", ["A) Que las rectas son paralelas", "B) Que las rectas se intersecan en un único punto exacto *(Correcta)*", "C) Que las rectas son coincidentes", "D) Que no hay variables"])
        ]
    elif any(k in e_low for k in ["quimica", "estequiometria", "mole", "acido", "reaccion", "atomos", "enlace"]):
        area = "Química y Estequiometría Avanzada"
        enfoque = "análisis cuantitativo de reacciones, balance atómico y comportamiento molar"
        banco_quizzes = [
            ("¿Cuántos gramos equivalen teóricamente a 1 mol de átomos de Carbono-12?", ["A) 6.022 × 10²³ gramos", "B) 12 gramos *(Correcta)*", "C) 22.4 gramos", "D) 1 gramo"]),
            ("¿Qué indica el coeficiente estequiométrico en una reacción química balanceada?", ["A) La proporción en moles de las sustancias participantes *(Correcta)*", "B) La temperatura exacta de fusión", "C) El color de la solución resultante", "D) La velocidad en segundos"])
        ]
    elif any(k in e_low for k in ["libro", "novela", "cuento", "literatura", "cortazar", "texto", "poesia", "narrativa"]):
        area = "Literatura y Hermenéutica Crítica"
        enfoque = "deconstrucción de textos, análisis de tiempos narrativos y contexto estético"
        banco_quizzes = [
            ("¿Qué técnica narrativa caracteriza las obras de Julio Cortázar en cuanto al tiempo?", ["A) Linealidad estricta", "B) Ruptura temporal, saltos y exploración de la conciencia *(Correcta)*", "C) Ausencia de descripciones", "D) Estilo periodístico"]),
            ("En el análisis crítico de un texto literario, ¿qué busca primordialmente el hermeneuta?", ["A) Memorizar la fecha de edición", "B) Interpretar las intenciones estéticas, simbolismos y subtextos del autor *(Correcta)*", "C) Contar el número exacto de párrafos", "D) Ignorar el contexto histórico"])
        ]
    else:
        area = "Desarrollo Curricular Multidisciplinario"
        enfoque = f"transferencia de saberes, resolución de problemas sistémicos y análisis de {entrada}"
        banco_quizzes = [
            (f"¿Cuál es el objetivo principal al abordar la temática de {entrada}?", ["A) Aislar los componentes teóricos", "B) Comprender su impacto sistémico y aplicación práctica *(Correcta)*", "C) Memorizar datos sin contexto", "D) Descartar el análisis"]),
            (f"¿Qué metodología resulta más efectiva para trabajar {entrada}?", ["A) Clases pasivas unidireccionales", "B) Aprendizaje basado en resolución de desafíos prácticos y colaboración *(Correcta)*", "C) Lectura monótona sin pausa", "D) Exclusión total de la práctica"])
        ]

    # Generación de variables combinatorias profundas
    verbos = ["Analizar profundamente", "Deconstructivamente examinar", "Sistematizar los principios de", "Modelar escenarios sobre", "Evaluar cuantitativa y cualitativamente"]
    metodologias = ["Aprendizaje Basado en Retos (ABR)", "Aula Invertida (Flipped Classroom)", "Enseñanza por Indagación", "Socioconstructivismo Aplicado"]
    v = random.choice(verbos)
    m = random.choice(metodologias)

    if modulo == "Planificador de Clases":
        return f"""### 📝 Planificación Académica Avanzada ({area})
**Tema Principal:** `{entrada}` | **Nivel:** `{nivel_curso}`

---

#### 🎯 Ejes Orientadores
* **Propósito Central:** {v} `{entrada}` aplicando los fundamentos de {area}.
* **Metodología Base:** {m}, orientada al desarrollo de {enfoque}.

---

#### ⏱️ Secuencia Didáctica Estructurada en 3 Fases
1. **Fase de Activación y Saberes Previos (15 min):** Planteamiento de un dilema detonante, pregunta problematizadora o ejercicio práctico vinculado directamente a `{entrada}`.
2. **Fase de Desarrollo, Mediación y Práctica (30 min):** 
   - Exposición conceptual breve y estructurada.
   - Resolución guiada de ejemplos y ejercicios de alta complejidad en la pizarra.
   - Trabajo colaborativo en células con asignación de roles operativos.
3. **Fase de Cierre y Metacognición (15 min):** 
   - Ticket de salida con resolución relámpago de un ejercicio clave.
   - Plenario de conclusiones y retroalimentación formativa global.
"""

    elif modulo == "Creación de Actividades":
        return f"""### 🛠️ Creador de Experiencias Prácticas ({area})
**Reto Asignado:** `{entrada}`

* **Dinámica Metodológica:** Basada en **{m}**.
* **Estructura Paso a Paso para el Estudiante:**
  1. *Fase de Diagnóstico y Análisis (10 min):* Revisar las premisas teóricas o datos iniciales de `{entrada}`.
  2. *Fase de Ejecución y Modelamiento (25 min):* Aplicar fórmulas, procedimientos analíticos o esquemas propios de {enfoque}.
  3. *Fase de Comprobación Cruzada (10 min):* Confrontar los resultados obtenidos frente al modelo esperado.
  4. *Fase de Plenario y Defensa (5 min):* Socializar las conclusiones ante el grupo curso mediante argumentos sólidos.
* **Criterio de Éxito:** Rigurosidad metodológica, precisión en los procedimientos y claridad expositiva.
"""

    elif modulo == "Generador de Rúbricas":
        return f"""### 📊 Rúbrica Analítica de Evaluación ({area})
**Instrumento Generado para:** `{entrada}`

| Criterio Evaluativo | Nivel Avanzado (4 pts) | Nivel Competente (3 pts) | En Desarrollo (2 pts) | Inicial (1 pt) |
| :--- | :--- | :--- | :--- | :--- |
| **Dominio Conceptual / Técnico** | Domina con precisión absoluta los fundamentos y fórmulas de `{entrada}`. | Explica y aplica correctamente los conceptos clave con menores omisiones. | Comprende parcialmente; comete errores operativos frecuentes. | Muestra vacilaciones severas y carencia de dominio básico. |
| **Resolución Práctica o Analítica** | Resuelve los ejercicios aplicando {enfoque} con rigor y exactitud. | Aplica los procedimientos metodológicos esperados de forma estándar. | La resolución contiene errores notables en el desarrollo o cálculo. | No logra desarrollar la tarea solicitada o está incompleta. |
| **Pensamiento Crítico y Rigor** | Justifica cada paso del proceso con argumentos sólidos y consistentes. | Justifica adecuadamente sus elecciones metodológicas. | Argumentación superficial o carente de sustento técnico claro. | Ausencia de análisis o justificación lógica. |
"""

    else:
        sample_q = random.sample(banco_quizzes, min(3, len(banco_quizzes)))
        preguntas_format = ""
        clase_resp = []
        for idx, (q, opts) in enumerate(sample_q, 1):
            preguntas_format += f"{idx}. {q}\n   * {opts[0]}\n   * {opts[1]}\n   * {opts[2]}\n   * {opts[3]}\n\n"
            correcta_letra = "A"
            for opt in opts:
                if "*(Correcta)*" in opt:
                    correcta_letra = opt[0]
            clase_resp.append(f"{idx}. {correcta_letra}")

        return f"""### ❓ Banco de Evaluación Formativa y Quiz Técnico ({area})
**Tema Evaluado:** `{entrada}`

{preguntas_format}
---
* **Clave de Validación Docente:** {" | ".join(clase_resp)}
"""

def generar_respuesta_segura(modulo, prompt_texto, nivel=""):
    if client and modulo != "Módulo PIE / Inclusión":
        try:
            response = client.models.generate_content(model='gemini-3.8-flash', contents=prompt_texto)
            if response and response.text:
                return response.text
        except Exception:
            pass
    return motor_masivo_extremo(modulo, prompt_texto, nivel)

# --- INTERFAZ DE USUARIO PRINCIPAL ---
st.title("📚 ClassTrack")
st.markdown("Plataforma pedagógica inteligente para la gestión curricular, cálculo, materias y soporte inclusivo.")
st.markdown("---")

# Menú lateral organizado
st.sidebar.markdown("### 🎛️ Panel de Navegación")
modulo = st.sidebar.radio(
    "Selecciona una herramienta:",
    ["Planificador de Clases", "Creación de Actividades", "Generador de Rúbricas", "Quizzes Interactivos", "Módulo PIE / Inclusión"]
)

st.sidebar.markdown("---")
st.sidebar.info("💡 **Estado del Sistema:** Motor autónomo extendido y optimizado para presentaciones en vivo.")

# Renderizado modular independiente
if modulo == "Módulo PIE / Inclusión":
    st.subheader("🤝 Módulo Especializado PIE (Integración Escolar)")
    st.markdown("Herramienta independiente dentro de la plataforma para diseñar adecuaciones curriculares y estrategias orientadas a la diversidad funcional.")
    
    col1, col2 = st.columns(2)
    with col1:
        tema_pie = st.text_input("Tema o dificultad a adaptar (Ej: Discalculia en ecuaciones, Comprensión lectora):")
    with col2:
        nivel_pie = st.selectbox("Nivel Educativo:", ["Enseñanza Básica", "Enseñanza Media", "Educación Superior"])
    
    if st.button("Generar Adaptación Curricular PIE") and tema_pie:
        with st.spinner("Construyendo adecuación inclusiva..."):
            resultado = generar_respuesta_segura(modulo, tema_pie, nivel_pie)
            st.markdown(resultado)

elif modulo == "Planificador de Clases":
    st.subheader("📝 Planificador Académico Inteligente")
    st.markdown("Estructura clases dinámicas basadas en objetivos, secuencias y criterios de éxito.")
    
    col1, col2 = st.columns(2)
    with col1:
        tema = st.text_input("Tema o contenido (Ej: Límites y derivadas, Álgebra, Estequiometría):")
    with col2:
        nivel = st.selectbox("Nivel / Curso:", ["Enseñanza Básica", "Enseñanza Media", "Educación Superior"])
    
    if st.button("Generar Planificación Completa") and tema:
        prompt_completo = f"Planificación de clase sobre {tema} para nivel {nivel}"
        with st.spinner("Generando planificación avanzada..."):
            resultado = generar_respuesta_segura(modulo, prompt_completo, nivel)
            st.markdown(resultado)

elif modulo == "Creación de Actividades":
    st.subheader("🛠️ Creador de Experiencias Prácticas")
    st.markdown("Diseña retos y dinámicas de transferencia activa para los estudiantes.")
    
    objetivo = st.text_input("¿Qué objetivo o contenido deseas trabajar en la actividad?")
    
    if st.button("Diseñar Actividad Experiencial") and objetivo:
        with st.spinner("Construyendo consignas y pasos..."):
            resultado = generar_respuesta_segura(modulo, objetivo)
            st.markdown(resultado)

elif modulo == "Generador de Rúbricas":
    st.subheader("📊 Generador de Rúbricas Analíticas")
    st.markdown("Crea instrumentos de evaluación estructurados por niveles de logro y competencias.")
    
    criterio = st.text_input("¿Qué se va a evaluar? (Ej: Límites y derivadas, Ensayo crítico, Maqueta):")
    
    if st.button("Generar Rúbrica de Evaluación") and criterio:
        with st.spinner("Construyendo matriz analítica..."):
            resultado = generar_respuesta_segura(modulo, criterio)
            st.markdown(resultado)

elif modulo == "Quizzes Interactivos":
    st.subheader("❓ Generador de Quizzes Técnicos")
    st.markdown("Genera bancos de evaluación con preguntas de selección múltiple, alternativas y clave de respuestas.")
    
    materia = st.text_input("Materia o tema para el quiz (Ej: Límites y derivadas, Estequiometría, Álgebra):")
    
    if st.button("Generar Banco de Preguntas") and materia:
        with st.spinner("Elaborando quiz técnico..."):
            resultado = generar_respuesta_segura(modulo, materia)
            st.markdown(resultado)
