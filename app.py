import streamlit as st
import random
from google import genai

# Configuración de la página
st.set_page_config(page_title="ClassTrack - Asistente Académico & PIE", layout="wide")

# Inicialización segura del cliente utilizando st.secrets
try:
    client = genai.Client(api_key=st.secrets["GEMINI_API_KEY"])
except Exception as e:
    client = None

def motor_masivo_avanzado(modulo, entrada):
    """Motor autónomo ampliado con alta variabilidad, razonamiento pedagógico profundo y enfoque PIE."""
    entrada_lower = entrada.lower()
    
    # 1. Detección automática del área de estudio
    if any(k in entrada_lower for k in ["algebra", "matematica", "ecuacion", "numeros", "calculo", "geometria", "aritmetica", "funciones"]):
        area = "Matemáticas y Razonamiento Lógico"
        enfoque = "abstracción formal, modelamiento cuantitativo y rigor analítico"
        quizzes = [
            ("Dada la función $f(x) = 2x + 3$, ¿cuál es el valor de $f(4)$?", ["A) 5", "B) 11 *(Correcta)*", "C) 8", "D) 14"]),
            ("Al despejar la incógnita en la ecuación lineal $3x - 6 = 12$, el valor de $x$ es:", ["A) 2", "B) 4", "C) 6 *(Correcta)*", "D) 8"]),
            ("¿Cuál es la representación gráfica principal de una función cuadrática de la forma $ax^2 + bx + c$?", ["A) Una línea recta", "B) Una parábola *(Correcta)*", "C) Una circunferencia", "D) Una hipérbola"]),
            ("¿Qué representa la pendiente 'm' en la ecuación de la recta $y = mx + b$?", ["A) La inclinación y tasa de cambio de la variable", "B) El punto de corte con el eje vertical", "C) Una constante nula", "D) El valor absoluto del radio"]),
            ("Si resolvemos el sistema de ecuaciones con dos incógnitas, ¿qué significa hallar la solución?", ["A) Encontrar el punto de intersección de ambas rectas", "B) Multiplicar los coeficientes al azar", "C) Anular las variables", "D) Calcular el área bajo la curva"]),
            ("¿Cuál es el resultado de simplificar la expresión algebraica $(x^2 - 9) / (x - 3)$ para $x \\neq 3$?", ["A) $x + 3$ *(Correcta)*", "B) $x - 3$", "C) $9$", "D) $x^2$"]),
            ("En una progresión aritmética, ¿cómo se define la diferencia común?", ["A) Restando un término menos su antecedente inmediato *(Correcta)*", "B) Multiplicando todos los factores", "C) Dividiendo el límite superior", "D) Elevando al cuadrado"])
        ]
    elif any(k in entrada_lower for k in ["libro", "novela", "cuento", "literatura", "cortazar", "texto", "poesia", "autor", "narrativa"]):
        area = "Literatura y Hermenéutica Crítica"
        enfoque = "deconstrucción de textos, análisis de tiempos narrativos y contexto estético"
        quizzes = [
            ("¿Qué técnica narrativa caracteriza frecuentemente las obras de Julio Cortázar en cuanto al tiempo?", ["A) Linealidad estricta", "B) Ruptura temporal, saltos y exploración de la conciencia *(Correcta)*", "C) Ausencia de descripciones", "D) Estilo periodístico"]),
            ("En el análisis hermenéutico de un texto literario, ¿qué busca primordialmente el lector crítico?", ["A) Memorizar la fecha", "B) Interpretar las intenciones estéticas y subtextos del autor *(Correcta)*", "C) Contar páginas", "D) Ignorar el contexto"]),
            ("¿Qué elemento define principalmente a una novela frente a un cuento corto?", ["A) La complejidad de su trama, subtramas y desarrollo profundo de personajes *(Correcta)*", "B) La obligatoriedad de rima", "C) Uso exclusivo de diálogos", "D) Extensión menor a dos páginas"]),
            ("¿A qué se refiere el concepto de 'narrador omnisciente'?", ["A) Un personaje que cuenta su propia historia en primera persona", "B) Una voz que lo conoce todo, incluidos los pensamientos íntimos de los personajes *(Correcta)*", "C) Un observador externo neutral sin información", "D) Un diálogo coral entre varios actores"]),
            ("¿Cuál es la función principal de las figuras retóricas en la poesía?", ["A) Confundir al lector deliberadamente", "B) Embellecer el lenguaje y evocar múltiples capas de significado y emoción *(Correcta)*", "C) Aportar rigor matemático al texto", "D) Describir fichas técnicas"])
        ]
    elif any(k in entrada_lower for k in ["ciencia", "fisica", "quimica", "biologia", "celula", "ecosistema", "atomos", "energia"]):
        area = "Ciencias Naturales y Experimentación"
        enfoque = "observación empírica, formulación de hipótesis y validación de variables"
        quizzes = [
            ("¿Cuál es la unidad fundamental estructural y funcional de los seres vivos?", ["A) El átomo", "B) La célula *(Correcta)*", "C) La molécula de agua", "D) El tejido adiposo"]),
            ("En el método científico, ¿qué paso sigue inmediatamente después de formular una hipótesis?", ["A) La experimentación y recolección de datos *(Correcta)*", "B) La publicación del libro", "C) Concluir sin pruebas", "D) Descartar la observación"]),
            ("¿Qué ley física explica la conservación de la energía en un sistema aislado?", ["A) Primera Ley de la Termodinámica *(Correcta)*", "B) Ley de la gravedad", "C) Principio de Arquímedes", "D) Ley de Ohm"]),
            ("¿Cuál es la función principal de los cloroplastos en las células vegetales?", ["A) Realizar la respiración celular", "B) Llevar a cabo la fotosíntesis capturando energía lumínica *(Correcta)*", "C) Almacenar material genético principal", "D) Sintetizar lípidos complejos"])
        ]
    else:
        area = "Desarrollo Curricular Multidisciplinario"
        enfoque = f"transferencia de saberes, resolución de problemas y análisis de {entrada}"
        quizzes = [
            (f"¿Cuál es el objetivo principal al abordar la temática de {entrada}?", ["A) Aislar componentes", "B) Comprender su impacto sistémico y aplicación práctica *(Correcta)*", "C) Memorizar datos", "D) Descartar análisis"]),
            (f"¿Qué metodología resulta más efectiva para trabajar {entrada}?", ["A) Clases pasivas", "B) Aprendizaje basado en resolución de desafíos prácticos *(Correcta)*", "C) Lectura monótona", "D) Exclusión de práctica"]),
            (f"¿Cómo se valida el dominio sobre {entrada}?", ["A) Mediante evaluación formativa y transferencia a escenarios reales *(Correcta)*", "B) Repitiendo conceptos", "C) Evitando evaluación", "D) Copiando respuestas"])
        ]

    # 2. Bancos masivos de variabilidad y razonamiento PIE
    verbos = ["Analizar profundamente", "Deconstruir de forma crítica", "Sistematizar los principios de", "Modelar escenarios sobre", "Evaluar el impacto de"]
    metodologias = ["Aprendizaje Basado en Retos (ABR)", "Aula Invertida (Flipped Classroom)", "Enseñanza por Indagación", "Socioconstructivismo Aplicado"]
    estrategias_pie = [
        "Apoyos visuales estructurados (pictogramas y organizadores gráficos) para estudiantes con necesidades de procesamiento visual.",
        "Fraccionamiento de consignas complejas en pasos secuenciales cortos para potenciar la memoria de trabajo.",
        "Uso de material concreto y andamiaje físico/digital adaptado para estudiantes con diversidad funcional.",
        "Flexibilización temporal y validación de respuestas a través de medios orales o multimodales (Diseño Universal de Aprendizaje - DUA)."
    ]

    v = random.choice(verbos)
    m = random.choice(metodologias)
    pie = random.choice(estrategias_pie)

    if modulo == "Planificador de Clases":
        return f"""### 📝 Planificación Académica Inclusiva (ClassTrack AI & PIE)
**Categoría Detectada:** `{area}`
**Objeto de Estudio:** `{entrada}`

---

#### 🎯 Ejes Orientadores y Diversificación
* **Propósito Central:** {v} `{entrada}` integrando los principios del área de {area}.
* **Metodología Base:** {m}, orientada a la participación universal.
* **Adecuación Curricular PIE / NEE:** 
  - *Estrategia de Apoyo:* {pie}
  - *Criterio de Evaluación Diferenciada:* Foco en el progreso cualitativo y la aplicación funcional del concepto por sobre la memorización estricta.

---

#### ⏱️ Secuencia Didáctica Estructurada (7 Momentos Clave)
1. **Activación Multisensorial (10 min):** Presentación del tema mediante activadores visuales y preguntas detonantes ancladas a experiencias cotidianas.
2. **Modelaje Docente Explicativo (15 min):** Demostración guiada paso a paso, asegurando verificación de comprensión en tiempo real.
3. **Trabajo Colaborativo en Células (20 min):** Resolución de desafíos en equipos heterogéneos con roles asignados.
4. **Adecuación y Andamiaje PIE (15 min):** Espacio de mediación focalizada y apoyo diversificado para estudiantes que requieran refuerzo en la consigna.
5. **Puesta en Común y Plenario (10 min):** Socialización de soluciones y contraste de hipótesis grupales.
6. **Consolidación Conceptual (10 min):** Síntesis esquemática a cargo del docente destacando las ideas fuerza.
7. **Cierre Metacognitivo (10 min):** Ticket de salida flexible (escrito, oral o gráfico) para autoevaluar el proceso de aprendizaje.
"""

    elif modulo == "Creación de Actividades":
        return f"""### 🛠️ Creador de Actividades Accesibles y Experienciales ({area})
**Reto Asignado:** `{entrada}`

* **Enfoque Metodológico:** Basado en **{m}** con adecuación universal DUA.
* **Estrategia PIE para Diversidad Funcional:** {pie}

* **Paso a Paso Operativo para el Estudiante:**
  1. *Fase de Contextualización (10 min):* Explorar los conceptos clave de `{entrada}` apoyándose en organizadores gráficos.
  2. *Fase de Desarrollo Práctico (25 min):* Ejecutar la tarea resolviendo los nodos críticos con apoyo de plantillas de guía estructurada.
  3. *Fase de Contrastación (15 min):* Revisar los resultados utilizando pautas de autocorrección paso a paso.
  4. *Fase de Comunicación Multimodal (10 min):* Presentar las conclusiones mediante soportes flexibles (oral, escrito o esquemático).

* **Criterio de Éxito Inclusivo:** Valoración del esfuerzo procedimental, razonamiento lógico y creatividad en la solución por sobre el formato estricto de entrega.
"""

    elif modulo == "Generador de Rúbricas":
        return f"""### 📊 Rúbrica Analítica de Evaluación Inclusiva ({area})
**Instrumento Adaptado para:** `{entrada}`

| Criterio Evaluativo | Nivel Avanzado (4 pts) | Nivel Competente (3 pts) | En Desarrollo / Con Apoyo (2 pts) | Inicial (1 pt) |
| :--- | :--- | :--- | :--- | :--- |
| **Dominio Conceptual y Comprensión** | Domina con precisión los conceptos clave de `{entrada}` y los explica con claridad. | Explica correctamente los fundamentos teóricos con menores omisiones. | Comprende los conceptos centrales con apoyo de andamiaje o adaptaciones visuales. | Muestra dificultades severas incluso con apoyos especializados. |
| **Aplicación y Resolución Práctica** | Resuelve la tarea aplicando {enfoque} con autonomía y rigor metodológico. | Aplica los procedimientos esperados de forma estándar y correcta. | Resuelve la tarea utilizando plantillas de apoyo, guías paso a paso o mediación docente. | No logra desarrollar la aplicación práctica solicitada. |
| **Razonamiento y Participación PIE** | Contribuye activamente al trabajo colaborativo, aportando soluciones creativas. | Participa cumpliendo responsablemente con su rol asignado en el equipo. | Participa activamente en las dinámicas adaptadas según su plan de apoyo individual. | No participa de manera efectiva en las actividades del grupo. |
"""

    else:
        # Seleccionar aleatoriamente 3 o 4 preguntas del banco correspondiente
        sample_q = random.sample(quizzes, min(4, len(quizzes)))
        
        preguntas_format = ""
        clase_resp = []
        for idx, (q, opts) in enumerate(sample_q, 1):
            preguntas_format += f"{idx}. {q}\n   * {opts[0]}\n   * {opts[1]}\n   * {opts[2]}\n   * {opts[3]}\n\n"
            # Extraer la letra de la respuesta correcta de la cadena "(Correcta)"
            correcta_letra = "B"
            for opt in opts:
                if "*(Correcta)*" in opt:
                    correcta_letra = opt[0]
            clase_resp.append(f"{idx}. {correcta_letra}")

        return f"""### ❓ Banco de Evaluación Formativa Inclusiva y Quiz Adaptado ({area})
**Tema de Evaluación:** `{entrada}`
* **Nota PIE:** Este instrumento incluye opciones con lectura clara y adaptaciones de formato para facilitar el acceso cognitivo.

{preguntas_format}
---
* **Clave de Validación Docente / PIE:** {" | ".join(clase_resp)}
"""

def generar_respuesta_segura(modulo, prompt_texto):
    if client:
        try:
            response = client.models.generate_content(model='gemini-3.8-flash', contents=prompt_texto)
            if response and response.text:
                return response.text
        except Exception:
            pass
    return motor_masivo_avanzado(modulo, prompt_texto)

# Interfaz Principal
st.title("📚 ClassTrack AI & PIE")
st.markdown("Tu asistente pedagógico inteligente especializado en gestión curricular, diversificación y apoyo a la integración escolar.")

# Menú lateral para seleccionar el módulo
modulo = st.sidebar.selectbox(
    "Selecciona un módulo",
    ["Planificador de Clases", "Creación de Actividades", "Generador de Rúbricas", "Quizzes Interactivos"]
)

st.markdown("---")

if modulo == "Planificador de Clases":
    st.subheader("📝 Planificador de Clases Inclusivo (Enfoque PIE)")
    tema = st.text_input("Tema o contenido (Ej: Álgebra, Cortázar, Fotosíntesis, Ecosistemas):")
    nivel = st.selectbox("Nivel / Curso:", ["Enseñanza Básica", "Enseñanza Media", "Educación Superior"])
    
    if st.button("Generar Planificación Inclusiva") and tema:
        prompt_completo = f"Planificación de clase inclusiva sobre {tema} para nivel {nivel} con enfoque PIE"
        with st.spinner("Generando planificación académica avanzada..."):
            resultado = generar_respuesta_segura(modulo, prompt_completo)
            st.markdown(resultado)

elif modulo == "Creación de Actividades":
    st.subheader("🛠️ Creador de Actividades Accesibles y DUA")
    objetivo = st.text_input("¿Qué objetivo o contenido deseas trabajar?")
    
    if st.button("Crear Actividad Inclusiva") and objetivo:
        with st.spinner("Diseñando actividad con adaptaciones..."):
            resultado = generar_respuesta_segura(modulo, objetivo)
            st.markdown(resultado)

elif modulo == "Generador de Rúbricas":
    st.subheader("📊 Generador de Rúbricas de Evaluación Diferenciada")
    criterio = st.text_input("¿Qué se va a evaluar? (Ej: Ecuaciones, Análisis literario, Maqueta):")
    
    if st.button("Generar Rúbrica PIE") and criterio:
        with st.spinner("Construyendo rúbrica analítica inclusiva..."):
            resultado = generar_respuesta_segura(modulo, criterio)
            st.markdown(resultado)

elif modulo == "Quizzes Interactivos":
    st.subheader("❓ Generador de Quizzes Adaptados")
    materia = st.text_input("Materia o tema para el quiz:")
    
    if st.button("Crear Quiz Accesible") and materia:
        with st.spinner("Elaborando banco de evaluación formativa..."):
            resultado = generar_respuesta_segura(modulo, materia)
            st.markdown(resultado)
