import streamlit as st
import random
from google import genai

# Configuración de la página
st.set_page_config(
    page_title="ClassTrack - Chile",
    page_icon="🇨🇱",
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
        background-color: #1e3a8a;
        color: white;
        padding: 0.5rem 1rem;
    }
    .stButton>button:hover {
        background-color: #1e40af;
    }
    </style>
""", unsafe_allow_html=True)

# ==============================================================================
# 🔐 SISTEMA DE DOBLE IA (BALANCEO DE CLAVES) Y CONTEXTO MINEDUC CHILE
# ==============================================================================

# Inicialización segura de dos clientes con claves distintas desde los secretos de Streamlit
try:
    client_principal = genai.Client(api_key=st.secrets["GEMINI_API_KEY_1"])
except Exception:
    client_principal = None

try:
    client_respaldo = genai.Client(api_key=st.secrets["GEMINI_API_KEY_2"])
except Exception:
    client_respaldo = None

# Base de conocimiento embebida basada en el Currículum Nacional del MINEDUC
CONTEXTO_MINEDUC_CHILE = """
Eres un asistente experto para el aula chilena de ClassTrack. Tus respuestas deben alinearse estrictamente a:
1. Las Bases Curriculares vigentes del MINEDUC (Decreto 433, Decreto 439 y actualizaciones de Educación Parvularia a Media).
2. Los textos escolares oficiales distribuidos por el gobierno de Chile en años recientes.
3. El Decreto 83 y criterios DUA (Diseño Universal para el Aprendizaje) para la diversificación de la enseñanza.
4. El Programa de Integración Escolar (PIE) y orientaciones técnicas vigentes.
Usa terminología pedagógica formal chilena (Objetivos de Aprendizaje OA, Indicadores de evaluación, Tickets de salida, etc.).
"""

def motor_masivo_chile(modulo, entrada, nivel_curso=""):
    """Motor autónomo masivo adaptado al Currículum Nacional del MINEDUC de Chile con respuestas extensas y profundas."""
    e_low = entrada.lower()
    
    # --- MÓDULO PIE / INCLUSIÓN (Independiente) ---
    if modulo == "Módulo PIE / Inclusión":
        return f"""### 🤝 Módulo Especializado PIE (Programa de Integración Escolar - Chile)
**Foco de Adecuación Curricular:** `{entrada}` | **Nivel:** `{nivel_curso}`

---

#### 📋 Plan de Diversificación y Apoyo Metodológico (Decreto 83 / DUA)
* **Evaluación de Barreras (BAP):** Identificación rigurosa de obstáculos para el aprendizaje y la participación en torno a `{entrada}`.
* **Adecuación en el Acceso y los Materiales:**
  - Incorporación de apoyos visuales directos, esquemas estructurados y glosario de términos clave de los textos del MINEDUC.
  - Fraccionamiento de las instrucciones complejas en secuencias cortas de ejecución guiada para optimizar la memoria de trabajo.
* **Adecuación en la Metodología:**
  - Uso de material concreto y estaciones de trabajo multisensoriales.
  - Asignación de tiempos flexibles y andamiaje directo por parte del docente durante los primeros minutos de la actividad.
* **Evaluación Diferenciada Sugerida:**
  - Validation de saberes mediante demostración oral, esquemas conceptuales o proyectos prácticos supervisados, resguardando los Objetivos de Aprendizaje (OA) priorizados.
"""

    # --- BANCOS DE CONOCIMIENTO AMPLIOS AL CURRÍCULUM CHILENO ---
    if any(k in e_low for k in ["limite", "derivada", "calculo", "integral", "infinitesimal"]):
        area = "Cálculo Infinitesimal (Matemática - Educación Media / Superior)"
        enfoque = "rigor analítico, tasas de cambio instantáneo y modelamiento de funciones"
        banco_quizzes = [
            ("¿Cuál es el valor del límite $\\lim_{x \\to 2} (3x^2 - 5)$?", ["A) 7 *(Correcta)*", "B) 6", "C) 11", "D) 1"]),
            ("¿Cuál es la derivada de la función polinómica $f(x) = 4x^3 - 2x + 5$?", ["A) $12x^2 - 2$ *(Correcta)*", "B) $12x^3 - 2$", "C) $4x^2 - 2$", "D) $12x - 2$"]),
            ("¿Qué representa geométricamente la derivada de una función en un punto dado?", ["A) El área bajo la curva", "B) La pendiente de la recta tangente a la curva en ese punto *(Correcta)*", "C) La intersección con el eje vertical", "D) El límite superior del dominio"]),
            ("Al evaluar el límite $\\lim_{x \\to 0} \\frac{\\sin(x)}{x}$, ¿qué valor notable se obtiene?", ["A) 0", "B) 1 *(Correcta)*", "C) Infinito", "D) No existe"]),
            ("¿Cuál es la regla de derivación aplicable al producto de dos funciones $f(x) \\cdot g(x)$?", ["A) $f'(x) \\cdot g'(x)$", "B) $f'(x)g(x) + f(x)g'(x)$ *(Correcta)*", "C) $\\frac{f'(x)}{g'(x)}$", "D) $f(x)g(x) - f'(x)g'(x)$"]),
            ("¿Cuál es la integral indefinida de la función constante $f(x) = k$?", ["A) $k + C$ *(Correcta)*", "B) $0$", "C) $kx^2 + C$", "D) $1 + C$"]),
            ("¿Qué indica el Teorema Fundamental del Cálculo?", ["A) La relación inversa entre la derivación y la integración *(Correcta)*", "B) Que toda función tiene infinitas asíntotas", "C) Cómo calcular el volumen de una esfera perfecta", "D) Que el límite de una suma es cero"]),
            ("¿Cuál es la derivada de la función exponencial natural $f(x) = e^{2x}$?", ["A) $e^{2x}$", "B) $2e^{2x}$ *(Correcta)*", "C) $2x e^{x}$", "D) $\\frac{1}{2}e^{2x}$"]),
            ("¿En qué punto una función derivable presenta un punto crítico?", ["A) Donde su primera derivada es cero o no está definida *(Correcta)*", "B) Donde el valor de $x$ es estrictamente negativo", "C) En la intersección con el eje y", "D) Cuando la función es constante"]),
            ("¿Cuál es el límite cuando $x$ tiende a infinito de $\\frac{1}{x}$?", ["A) Infinito", "B) 0 *(Correcta)*", "C) 1", "D) No está definido"])
        ]
    elif any(k in e_low for k in ["algebra", "matematica", "ecuacion", "funcion", "geometria", "numeros"]):
        area = "Matemáticas (Currículum Nacional MINEDUC Chile)"
        enfoque = "resolución de problemas, pensamiento crítico y modelamiento algebraico"
        banco_quizzes = [
            ("Dada la función lineal $f(x) = 2x + 3$, ¿cuál es el valor de $f(4)$?", ["A) 5", "B) 11 *(Correcta)*", "C) 8", "D) 14"]),
            ("Al despejar la incógnita en la ecuación lineal $3x - 6 = 12$, el valor de $x$ es:", ["A) 2", "B) 4", "C) 6 *(Correcta)*", "D) 8"]),
            ("¿Cuál es la representación gráfica principal de una función cuadrática $ax^2 + bx + c$?", ["A) Una línea recta", "B) Una parábola *(Correcta)*", "C) Una circunferencia", "D) Una hipérbola"]),
            ("¿Qué representa la pendiente 'm' en la ecuación de la recta $y = mx + b$?", ["A) La tasa de cambio y la inclinación de la recta *(Correcta)*", "B) El punto de corte con el eje vertical", "C) Una constante nula", "D) El radio"]),
            ("¿Cuál es el valor del discriminante en una ecuación cuadrática que tiene dos soluciones reales distintas?", ["A) Menor que cero ($\\Delta < 0$)", "B) Mayor que cero ($\\Delta > 0$) *(Correcta)*", "C) Exactamente igual a cero ($\\Delta = 0$)", "D) Indeterminado"]),
            ("¿Cómo se expresa en lenguaje algebraico 'el doble de un número disminuido en cinco unidades'?", ["A) $2x - 5$ *(Correcta)*", "B) $2(x - 5)$", "C) $x^2 - 5$", "D) $5 - 2x$"]),
            ("¿Cuál es el resultado de simplificar la expresión $(x^2 - 9) / (x - 3)$ para $x \\neq 3$?", ["A) $x + 3$ *(Correcta)*", "B) $x - 3$", "C) 9", "D) 1"]),
            ("En un triángulo rectángulo, si los catetos miden 3 cm y 4 cm, ¿cuánto mide la hipotenusa?", ["A) 5 cm *(Correcta)*", "B) 7 cm", "C) 12 cm", "D) 25 cm"]),
            ("¿Cuál es la suma de los ángulos interiores de cualquier triángulo plano?", ["A) 90°", "B) 180° *(Correcta)*", "C) 360°", "D) 270°"]),
            ("¿Qué probabilidad hay de obtener un número par al lanzar un dado común de 6 caras?", ["A) 1/6", "B) 1/2 *(Correcta)*", "C) 1/3", "D) 2/3"])
        ]
    elif any(k in e_low for k in ["salud", "bienestar", "nutricion", "ejercicio", "fisica", "anatomia", "prevencion"]):
        area = "Salud, Bienestar y Educación Física (MINEDUC)"
        enfoque = "promoción de vida activa, autocuidado, prevención de riesgos y salud integral"
        banco_quizzes = [
            ("¿Cuál es un beneficio principal de mantener una rutina de ejercicio cardiovascular regular?", ["A) Disminución de la capacidad pulmonar", "B) Mejora de la salud cardíaca, circulación y reducción del estrés *(Correcta)*", "C) Aumento del sedentarismo", "D) Pérdida total de masa ósea"]),
            ("¿Qué grupo de nutrientes cumple la función plástica o reparadora en el organismo humano?", ["A) Las proteínas *(Correcta)*", "B) Las vitaminas complejas", "C) El agua destilada", "D) Los lípidos saturados"]),
            ("¿Qué se entiende por salud integral según la Organización Mundial de la Salud (OMS)?", ["A) La ausencia absoluta de cualquier enfermedad física", "B) Un estado de completo bienestar físico, mental y social *(Correcta)*", "C) Únicamente el bienestar psicológico individual", "D) No tener dolencias menores"]),
            ("¿Cuál es la principal función de los carbohidratos en la dieta diaria?", ["A) Aportar energía rápida y eficiente para las actividades celulares y físicas *(Correcta)*", "B) Aislar los órganos internos del frío", "C) Regular la coagulación de la sangre", "D) Sintetizar ADN"]),
            ("¿Qué medida preventiva es fundamental antes de realizar actividad física intensa?", ["A) Consumir bebidas azucaradas en exceso", "B) Realizar un calentamiento muscular y articular adecuado *(Correcta)*", "C) Dormir inmediatamente después", "D) Evitar la hidratación"]),
            ("¿Qué rol cumple la hidratación en el cuerpo humano durante el esfuerzo físico?", ["A) Regula la temperatura corporal y transporta nutrientes *(Correcta)*", "B) Bloquea el metabolismo", "C) Eleva la fatiga muscular", "D) Aumenta la deshidratación"]),
            ("¿Cuál de los siguientes hábitos promueve una correcta salud mental en el ámbito escolar?", ["A) El aislamiento social prolongado", "B) El descanso adecuado, la comunicación asertiva y el manejo de pausas activas *(Correcta)*", "C) La privación voluntaria de sueño", "D) Acumular altos niveles de estrés"]),
            ("¿Qué son las enfermedades no transmisibles (ENT)?", ["A) Infecciones virales de contagio rápido en el aula", "B) Afecciones crónicas como problemas cardiovasculares o diabetes asociadas al estilo de vida *(Correcta)*", "C) Lesiones deportivas accidentales", "D) Enfermedades de transmisión escolar"]),
            ("¿Por qué es importante el consumo de fibra dietética en la alimentación?", ["A) Favorece el tránsito intestinal y regula los niveles de glucosa en sangre *(Correcta)*", "B) Produce obesidad mórbida", "C) Detiene la digestión", "D) Sustituye al agua"]),
            ("¿Cuál es una estrategia clave de primeros auxilios ante una contusión o esguince leve?", ["A) Aplicar calor directo y masajear con fuerza", "B) Aplicar protocolo RICE (Reposo, Hielo, Compresión y Elevación) *(Correcta)*", "C) Continuar corriendo sin parar", "D) Ignorar el dolor"])
        ]
    elif any(k in e_low for k in ["quimica", "estequiometria", "mole", "acido", "reaccion", "atomos", "enlace", "biologia", "celula", "ecosistema", "fotosintesis", "fisica"]):
        area = "Ciencias Naturales (Biología, Física y Química - MINEDUC)"
        enfoque = "indagación científica, experimentación, análisis de variables y comprensión del entorno natural"
        banco_quizzes = [
            ("¿Cuál es la unidad fundamental estructural y funcional de todos los seres vivos?", ["A) El átomo", "B) La célula *(Correcta)*", "C) La molécula de agua", "D) El tejido adiposo"]),
            ("¿Qué organelo celular es responsable de la respiración celular y producción de ATP?", ["A) El ribosoma", "B) La mitocondria *(Correcta)*", "C) El aparato de Golgi", "D) La pared conocer"]),
            ("¿Qué proceso realizan las plantas para transformar dióxido de carbono y agua en glucosa y oxígeno?", ["A) Fermentación láctica", "B) Fotosíntesis *(Correcta)*", "C) Transpiración pasiva", "D) Ciclo de Krebs"]),
            ("¿Cuántos gramos equivalen teóricamente a 1 mol de átomos de Carbono-12?", ["A) 6.022 × 10²³ gramos", "B) 12 gramos *(Correcta)*", "C) 22.4 gramos", "D) 1 gramo"]),
            ("¿Qué indica el coeficiente estequiométrico en una ecuación química balanceada?", ["A) La proporción en moles de las sustancias participantes *(Correcta)*", "B) La temperatura exacta", "C) El color de la solución", "D) La velocidad de reacción"]),
            ("¿Cuál es la primera ley de Newton o principio de inercia?", ["A) Todo cuerpo persevera en su estado de reposo o movimiento rectilíneo uniforme a menos que se aplique una fuerza neta *(Correcta)*", "B) La fuerza es igual a masa por aceleración", "C) A toda acción siempre opone una reacción igual", "D) La energía se destruye"]),
            ("¿Qué tipo de enlace químico se forma por la transferencia de electrones entre un metal y un no metal?", ["A) Enlace covalente", "B) Enlace iónico *(Correcta)*", "C) Enlace metálico puro", "D) Puentes de hidrógeno"]),
            ("¿Cuál es la función principal de los glóbulos rojos en la sangre humana?", ["A) Combatir infecciones bacterianas", "B) Transportar oxígeno desde los pulmones a los tejidos corporales *(Correcta)*", "C) Coagular heridas abiertas", "D) Regular los anticuerpos"]),
            ("¿Qué ley física explica la conservación de la energía mecánica en un sistema aislado?", ["A) Primera Ley de la Termodinámica *(Correcta)*", "B) Ley de gravedad universal", "C) Principio de Arquímedes", "D) Ley de Ohm"]),
            ("¿Qué estructura del sistema nervioso central controla el equilibrio y la coordinación motora fina?", ["A) El bulbo raquídeo", "B) El cerebelo *(Correcta)*", "C) El hipotálamo", "D) La corteza visual"])
        ]
    elif any(k in e_low for k in ["libro", "novela", "cuento", "literatura", "cortazar", "texto", "poesia", "narrativa"]):
        area = "Lengua y Literatura (Currículum Nacional MINEDUC)"
        enfoque = "deconstrucción de textos, análisis hermenéutico, estética y pensamiento crítico"
        banco_quizzes = [
            ("¿Qué técnica narrativa caracteriza las obras de Julio Cortázar en cuanto al tiempo?", ["A) Linealidad estricta y cronológica", "B) Ruptura temporal, saltos y exploración de la subjetividad y conciencia *(Correcta)*", "C) Ausencia total de descripciones temporales", "D) Estilo estrictamente periodístico"]),
            ("En el análisis crítico de un texto literario, ¿qué busca primordialmente el lector?", ["A) Memorizar la fecha exacta de edición", "B) Interpretar las intenciones estéticas, simbolismos y subtextos del autor *(Correcta)*", "C) Contar el número exacto de párrafos", "D) Ignorar el contexto histórico"]),
            ("¿Qué elemento define principalmente a una novela frente a un cuento corto?", ["A) La complejidad de su trama, múltiples subtramas y desarrollo profundo de personajes *(Correcta)*", "B) La obligatoriedad de tener rima métrica", "C) El uso exclusivo de diálogos directos", "D) Su extensión menor a dos páginas"]),
            ("¿A qué se refiere el concepto de 'narrador omnisciente' en una obra literaria?", ["A) Un personaje secundario que cuenta su propia vivencia", "B) Una voz narrativa que lo conoce todo, incluidos los pensamientos íntimos de los personajes *(Correcta)*", "C) Un observador externo neutral que no sabe nada", "D) Un diálogo coral entre actores"]),
            ("¿Cuál es la función principal de las figuras literarias (como la metáfora o la hipérbole) en la poesía?", ["A) Confundir al lector deliberadamente", "B) Embellecer el lenguaje y evocar múltiples capas de significado y emoción *(Correcta)*", "C) Aportar rigor matemático estricto", "D) Describir fichas técnicas"]),
            ("¿Qué caracteriza a un texto argumentativo?", ["A) Narrar una historia de ficción fantástica", "B) Defender una tesis o postura mediante argumentos lógicos y evidencias para persuadir *(Correcta)*", "C) Dar instrucciones de uso paso a paso", "D) Expresar sentimientos íntimos mediante versos"]),
            ("¿Cuál es el propósito de los textos normativos o instructivos?", ["A) Regular conductas o guiar en la realización de un procedimiento paso a paso *(Correcta)*", "B) Entretener con anécdotas", "C) Criticar la política actual", "D) Analizar la métrica poética"]),
            ("¿Qué es la cohesión textual?", ["A) La propiedad gramatical que asegura la conexión formal y lingüística entre las oraciones y párrafos *(Correcta)*", "B) El tema central del libro", "C) La cantidad de capítulos", "D) El año de publicación"]),
            ("¿A qué género literario pertenece una obra destinada a ser representada por actores en un escenario?", ["A) Género lírico", "B) Género dramático o teatral *(Correcta)*", "C) Género épico-narrativo", "D) Ensayo ensayístico"]),
            ("¿Qué rol cumple el contexto de producción de una obra literaria?", ["A) Ninguno, la obra existe aislada", "B) Aporta luces sobre las circunstancias históricas, sociales y culturales que rodearon al autor *(Correcta)*", "C) Define el color de la portada", "D) Establece el precio comercial"])
        ]
    else:
        area = "Desarrollo Curricular Multidisciplinario (MINEDUC)"
        enfoque = f"transferencia de saberes, resolución de problemas sistémicos y análisis de {entrada}"
        banco_quizzes = [
            (f"¿Cuál es el objetivo principal al abordar la temática de {entrada}?", ["A) Aislar los componentes teóricos", "B) Comprender su impacto sistémico y aplicación práctica en el entorno *(Correcta)*", "C) Memorizar datos sin contexto", "D) Descartar el análisis"]),
            (f"¿Qué metodología resulta más efectiva para trabajar {entrada}?", ["A) Clases pasivas unidireccionales", "B) Aprendizaje basado en resolución de desafíos prácticos y colaboración *(Correcta)*", "C) Lectura monótona sin pausa", "D) Exclusión total de la práctica"]),
            (f"¿Cómo se valida el logro de aprendizaje respecto a {entrada}?", ["A) Mediante evaluación formativa, rúbricas y transferencia a escenarios reales *(Correcta)*", "B) Repitiendo conceptos al azar", "C) Evitando toda evaluación", "D) Copiando respuestas"]),
            (f"¿Qué habilidad del siglo XXI se fomenta al estudiar {entrada}?", ["A) El pensamiento crítico y la resolución colaborativa de problemas *(Correcta)*", "B) El aislamiento cognitivo", "C) La memorización pasiva", "D) La repetición mecánica"]),
            (f"¿Por qué es relevante contextualizar {entrada} en el aula chilena?", ["A) Porque permite conectar el saber teórico con la realidad sociocultural del estudiante *(Correcta)*", "B) Para cumplir un trámite administrativo", "C) No tiene relevancia alguna", "D) Para dificultar la enseñanza"]),
            (f"¿Qué rol cumple el docente como mediador frente a {entrada}?", ["A) Guiar, facilitar y estructurar el andamiaje cognitivo del estudiante *(Correcta)*", "B) Dar las respuestas sin explicar", "C) Observar en silencio", "D) Evitar que los alumnos participen"]),
            (f"¿Cuál es el papel de la metacognición en este proceso?", ["A) Reflexionar sobre el propio aprendizaje y cómo se resolvió el problema *(Correcta)*", "B) Olvidar lo aprendido", "C) Evaluar al profesor", "D) Memorizar fechas"]),
            (f"¿Qué recurso didáctico potencia mejor este contenido?", ["A) Organizadores gráficos y estudios de caso prácticos *(Correcta)*", "B) Un texto sin formato", "C) Silencio absoluto en el aula", "D) Ningún recurso"]),
            (f"¿Cómo se relacionan los Objetivos de Aprendizaje (OA) con este tema?", ["A) Guían la ruta pedagógica asegurando el estándar ministerial esperado *(Correcta)*", "B) Son independientes de la clase", "C) Limitan la creatividad", "D) No aplican"]),
            (f"¿Qué indicador demuestra dominio avanzado en esta área?", ["A) La capacidad de argumentar, transferir y crear soluciones originales ante nuevos desafíos *(Correcta)*", "B) Copiar definiciones", "C) Entregar la prueba tarde", "D) No participar"])
        ]

    # Generación de variables combinatorias profundas
    verbos = ["Analizar profundamente", "Deconstructivamente examinar", "Sistematizar los principios de", "Modelar escenarios sobre", "Evaluar cuantitativa y cualitativamente"]
    metodologias = ["Aprendizaje Basado en Retos (ABR)", "Aula Invertida (Flipped Classroom)", "Enseñanza por Indagación", "Socioconstructivismo Aplicado"]
    v = random.choice(verbos)
    m = random.choice(metodologias)

    if modulo == "Planificador de Clases":
        return f"""### 📝 Planificación Académica Curricular MINEDUC ({area})
**Tema Principal:** `{entrada}` | **Nivel:** `{nivel_curso}`

---

#### 🎯 Ejes Orientadores y Objetivos (OA)
* **Propósito Central:** {v} `{entrada}` aplicando los fundamentos y estándares del área de {area}.
* **Metodología Base:** {m}, orientada al desarrollo de {enfoque}.

---

#### ⏱️ Secuencia Didáctica Estructurada en 3 Fases (Formato MINEDUC)
1. **Fase de Inicio (15 min):** 
   - Activación de conocimientos previos mediante preguntas detonantes ancladas a los textos escolares oficiales de Chile.
   - Presentación clara del Objetivo de Aprendizaje (OA) y los criterios de éxito esperados.
2. **Fase de Desarrollo y Mediación (30 min):** 
   - Exposición conceptual estructurada y modelaje docente paso a paso.
   - Trabajo colaborativo en equipos para la resolución de guías prácticas o estudios de caso.
   - Monitoreo itinerante y apoyo focalizado para asegurar la comprensión de todos los estudiantes.
3. **Fase de Cierre y Metacognición (15 min):** 
   - Aplicación de un **Ticket de Salida** con un desafío breve de validación conceptual.
   - Plenario de síntesis y retroalimentación formativa global a cargo del profesor.
"""

    elif modulo == "Creación de Actividades":
        return f"""### 🛠️ Creador de Experiencias Prácticas ({area})
**Reto Asignado:** `{entrada}`

* **Dinámica Metodológica:** Basada en **{m}** (Alineada al Currículum Nacional).
* **Estructura Paso a Paso para el Estudiante:**
  1. *Fase de Diagnóstico y Análisis (10 min):* Revisión de premisas, lectura de fuentes o análisis de datos iniciales sobre `{entrada}`.
  2. *Fase de Ejecución y Modelamiento (25 min):* Aplicación de procedimientos analíticos, experimentales o de razonamiento propios de {enfoque}.
  3. *Fase de Comprobación Cruzada (10 min):* Validación de resultados obtenidos frente a los criterios esperados.
  4. *Fase de Plenario y Defensa (5 min):* Socialización de conclusiones ante el curso mediante argumentos sólidos.
* **Criterios de Éxito:** Rigurosidad procedimental, precisión analítica y claridad en la comunicación de resultados.
"""

    elif modulo == "Generador de Rúbricas":
        return f"""### 📊 Rúbrica Analítica de Evaluación Oficial ({area})
**Instrumento Generado para:** `{entrada}`

| Criterio Evaluativo | Nivel Avanzado (4 pts) | Nivel Competente (3 pts) | En Desarrollo (2 pts) | Inicial (1 pt) |
| :--- | :--- | :--- | :--- | :--- |
| **Dominio Conceptual y Técnico** | Domina con absoluta precisión los fundamentos, conceptos y normativas de `{entrada}`. | Explica y aplica correctamente los conceptos clave con menores omisiones. | Comprende parcialmente; comete errores operativos o conceptuales frecuentes. | Muestra vacilaciones severas y carencia de dominio básico. |
| **Resolución Práctica o Analítica** | Resuelve los desafíos aplicando {enfoque} con rigor, exactitud y autonomía. | Aplica los procedimientos metodológicos esperados de forma estándar y correcta. | La resolución contiene errores notables en el desarrollo, cálculo o argumentación. | No logra desarrollar la tarea solicitada o está incompleta. |
| **Pensamiento Crítico y Rigor** | Justifica cada paso del proceso con argumentos sólidos, evidencias y consistencia lógica. | Justifica adecuadamente sus elecciones metodológicas y teóricas. | Argumentación superficial o carente de sustento técnico claro. | Ausencia absoluta de análisis, justificación o coherencia lógica. |
"""

    else:
        sample_q = random.sample(banco_quizzes, min(10, len(banco_quizzes)))
        preguntas_format = ""
        clase_resp = []
        
        for idx, (q, opts) in enumerate(sample_q, 1):
            opciones_texto = ""
            for opt in opts:
                opciones_texto += f"   * {opt}\n"
                
            preguntas_format += f"{idx}. {q}\n{opciones_texto}\n"
            
            correcta_letra = "A"
            for opt in opts:
                if "*(Correcta)*" in opt or "(Correcta)" in opt:
                    correcta_letra = opt
            clase_resp.append(f"{idx}. {correcta_letra}")

        return f"""### ❓ Banco de Evaluación Formativa y Quiz Extendido ({area})
**Tema Evaluado:** `{entrada}`
*(Instrumento diseñado con estándares ministeriales)*

{preguntas_format}
---
* **Clave de Validación Docente:** {" | ".join(clase_resp)}
"""

# --- ESCUDO DE CACHÉ PARA EVITAR SATURAR LA API DE GOOGLE ---
@st.cache_data(show_spinner=False)
def llamar_api_gemini_con_cache(prompt_enriquecido):
    """Hace la consulta a Google de forma segura e inteligente alternando las llaves."""
    if client_principal:
        try:
            response = client_principal.models.generate_content(
                model='gemini-1.5-flash',
                contents=prompt_enriquecido
            )
            if response and response.text:
                return response.text
        except Exception as e_principal:
            print(f"IA Principal agotada o limitada: {e_principal}. Activando respaldo...")
            if client_respaldo:
                try:
                    response_respaldo = client_respaldo.models.generate_content(
                        model='gemini-1.5-flash',
                        contents=prompt_enriquecido
                    )
                    if response_respaldo and response_respaldo.text:
                        return response_respaldo.text
                except Exception as e_respaldo:
                    print(f"IA de Respaldo también falló: {e_respaldo}")
                    pass
    return None

def generar_respuesta_segura(modulo, prompt_texto, nivel=""):
    if modulo == "Módulo PIE / Inclusión":
        return motor_masivo_chile(modulo, prompt_texto, nivel)
    
    prompt_enriquecido = f"{CONTEXTO_MINEDUC_CHILE}\n\n[Módulo: {modulo} | Nivel: {nivel}]\nPregunta del docente: {prompt_texto}"
    
    resultado_ia = llamar_api_gemini_con_cache(prompt_enriquecido)
    if resultado_ia:
        return resultado_ia
        
    return motor_masivo_chile(modulo, prompt_texto, nivel)

# --- INTERFAZ DE USUARIO PRINCIPAL ---
st.title("📚 ClassTrack")
st.markdown("Plataforma pedagógica inteligente para profesores chilenos (Currículum MINEDUC, Cálculo, Salud, Ciencias, Humanidades e Inclusión).")
st.markdown("---")

st.sidebar.markdown("### 🎛️ Panel de Navegación")
modulo = st.sidebar.radio(
    "Selecciona una herramienta:",
    ["Planificador de Clases", "Creación de Actividades", "Generador de Rúbricas", "Quizzes Interactivos", "Módulo PIE / Inclusión"]
)
st.sidebar.markdown("---")
st.sidebar.info("🇨🇱 **Estado:** Motor autónomo optimizado con bases curriculares de Chile y quizes extendidos de 10 preguntas.")

if modulo == "Módulo PIE / Inclusión":
    st.subheader("🤝 Módulo Especializado PIE (Integración Escolar - Chile)")
    st.markdown("Diseña adecuaciones curriculares bajo el Decreto 83 y DUA orientadas a la diversidad funcional.")
    col1, col2 = st.columns(2)
    with col1:
        tema_pie = st.text_input("Tema, dificultad o déficit a adaptar (Ej: Discalculia en ecuaciones, Comprensión lectora):")
    with col2:
        nivel_pie = st.selectbox("Nivel Educativo:", ["Educación Básica", "Educación Media", "Educación Superior"])
    if st.button("Generar Adecuación Curricular PIE") and tema_pie:
        with st.spinner("Construyendo adecuación inclusiva oficial..."):
            resultado = generar_respuesta_segura(modulo, tema_pie, nivel_pie)
            st.markdown(resultado)

elif modulo == "Planificador de Clases":
    st.subheader("📝 Planificador Académico Curricular")
    st.markdown("Estructura clases dinámicas basadas en las Bases Curriculares de Chile.")
    col1, col2 = st.columns(2)
    with col1:
        tema = st.text_input("Tema o contenido (Ej: Límites y derivadas, Hábitos de vida saludable, Estequiometría):")
    with col2:
        nivel = st.selectbox("Nivel / Curso:", ["7° Básico", "8° Básico", "1° Medio", "2° Medio", "3° Medio", "4° Medio"])
    if st.button("Generar Planificación Completa") and tema:
        prompt_completo = f"Planificación curricular chilena sobre {tema} para nivel {nivel}"
        with st.spinner("Generando planificación avanzada..."):
            resultado = generar_respuesta_segura(modulo, prompt_completo, nivel)
            st.markdown(resultado)

elif modulo == "Creación de Actividades":
    st.subheader("🛠️ Creador de Experiencias Prácticas")
    st.markdown("Diseña retos y dinámicas de transferencia activa alineadas al aula chilena.")
    objetivo = st.text_input("¿Qué objetivo o contenido deseas trabajar en la actividad?")
    if st.button("Diseñar Actividad Experiencial") and objetivo:
        with st.spinner("Construyendo consignas y pasos..."):
            resultado = generar_respuesta_segura(modulo, objetivo)
            st.markdown(resultado)

elif modulo == "Generador de Rúbricas":
    st.subheader("📊 Generador de Rúbricas Analíticas")
    st.markdown("Crea instrumentos de evaluación estructurados por niveles de logro ministeriales.")
    criterio = st.text_input("¿Qué se va a evaluar? (Ej: Límites y derivadas, Plan de salud nutricional, Ensayo):")
    if st.button("Generar Rúbrica de Evaluación") and criterio:
        with st.spinner("Construyendo matriz analítica..."):
            resultado = generar_respuesta_segura(modulo, criterio)
            st.markdown(resultado)

elif modulo == "Quizzes Interactivos":
    st.subheader("❓ Generador de Quizzes Extendidos (10 Preguntas)")
    st.markdown("Genera bancos de evaluación masivos con 10 preguntas de selección múltiple basadas en los textos escolares del MINEDUC.")
    materia = st.text_input("Materia o tema para el quiz (Ej: Límites y derivadas, Hábitos de vida saludable, Álgebra, Célula):")
    if st.button("Generar Banco de 10 Preguntas") and materia:
        with st.spinner("Elaborando quiz técnico extendido..."):
            resultado = generar_respuesta_segura(modulo, materia)
            st.markdown(resultado)
