import streamlit as st
from streamlit_drawable_canvas import st_canvas

# ==========================================
# CONFIGURACIÓN DE PÁGINA Y ESTILOS PASTEL
# ==========================================
st.set_page_config(
    page_title="Lienzo Mágico de Fábulas 🎨✨",
    page_icon="🦄",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Estilos CSS con paleta pastel, bordes suavizados y fuentes amigables
st.markdown("""
<style>
    /* Fondo general cálido y suave */
    .stApp {
        background-color: #FFFDF9;
    }
    
    /* Banner Narrativo */
    .magic-header {
        background: linear-gradient(135deg, #FFD1DC 0%, #FCE1E4 40%, #E2F0CB 100%);
        padding: 2rem;
        border-radius: 24px;
        color: #4A4A4A;
        text-align: center;
        margin-bottom: 2rem;
        box-shadow: 0 8px 20px rgba(255, 209, 220, 0.4);
    }
    
    .magic-header h1 {
        color: #6B4E71 !important;
        font-weight: 800;
        font-size: 2.3rem;
        margin-bottom: 0.5rem;
    }
    
    .magic-header p {
        color: #555555;
        font-size: 1.15rem;
        margin: 0;
    }

    /* Ajuste para tarjetas e inputs */
    div[data-testid="stSidebar"] {
        background-color: #FAF0CA !important;
        border-right: 2px dashed #F4ACB7;
    }

    /* Subtítulos de la barra lateral */
    .sidebar-title {
        color: #6B4E71;
        font-weight: 700;
        font-size: 1.1rem;
        margin-top: 1rem;
    }
</style>
""", unsafe_allow_html=True)

# ==========================================
# BARRA LATERAL: LA VARITA Y LOS PINCELES
# ==========================================
with st.sidebar:
    st.image(
        "https://images.unsplash.com/photo-1513364776144-60967b0f800f?auto=format&fit=crop&w=400&q=80",
        width=260
    )
    st.markdown("## 🧙‍♂️️ Taller del Cuentacuentos")
    st.caption("¡Ayuda al Duende Ilustrador a darle vida al bosque encantado de la fábula!")

    st.markdown("---")

    # Mapeo de herramientas a nombres mágicos amigables
    st.markdown('<p class="sidebar-title">🪄 Herramienta de Creación</p>', unsafe_allow_html=True)
    tool_options = {
        "✏️ Trazo Libre (Pincel Volador)": "freedraw",
        "📏 Línea Recta (Puente de Hada)": "line",
        "🔲 Cuadrado (Caja de Tesoros)": "rect",
        "🟡 Círculo (Sol y Soles)": "circle",
        "✋ Mover o Girar Dibujos": "transform",
        "🔹 Puntos de Estrellas": "point"
    }
    
    selected_tool_label = st.selectbox(
        "Elige qué quieres dibujar:",
        list(tool_options.keys())
    )
    drawing_mode = tool_options[selected_tool_label]

    st.markdown('<p class="sidebar-title">🎨 Colores de Cuento</p>', unsafe_allow_html=True)
    
    col_stroke, col_bg = st.columns(2)
    with col_stroke:
        # Color pastelito por defecto: Rosa Hada
        stroke_color = st.color_picker("Color del Pincel", "#FFB7B2")
    
    with col_bg:
        # Color pastelito por defecto: Fondo Menta Suave
        bg_color = st.color_picker("Color del Papel", "#E2F0CB")

    st.markdown('<p class="sidebar-title">✏️ Grosor del Pincel</p>', unsafe_allow_html=True)
    stroke_width = st.slider("¿Qué tan grueso quieres el trazo?", 2, 40, 12)

    st.markdown('<p class="sidebar-title">📐 Tamaño del Papel Mágico</p>', unsafe_allow_html=True)
    canvas_width = st.slider("Ancho del Papel", 400, 800, 650, 50)
    canvas_height = st.slider("Alto del Papel", 300, 600, 420, 50)

# ==========================================
# BANNER PRINCIPAL Y NARRATIVA
# ==========================================
st.markdown("""
<div class="magic-header">
    <h1>Lienzo Mágico de las Fábulas 🦄🎨</h1>
    <p>Había una vez un conejo curioso que necesitaba un bosque de colores... ¡Dibuja el camino de la historia!</p>
</div>
""", unsafe_allow_html=True)

# Layout para centrar el lienzo de dibujo
col_canvas, col_info = st.columns([2.5, 1], gap="medium")

with col_canvas:
    st.subheader("🖼️ Tu Papel Mágico")
    
    # Creación del componente Canvas con relleno semitransparente pastel
    canvas_result = st_canvas(
        fill_color="rgba(255, 223, 186, 0.4)",  # Naranja durazno suave
        stroke_width=stroke_width,
        stroke_color=stroke_color,
        background_color=bg_color,
        height=canvas_height,
        width=canvas_width,
        drawing_mode=drawing_mode,
        key=f"kid_canvas_{canvas_width}_{canvas_height}",
    )

with col_info:
    st.subheader("📖 La Fábula del Día")
    
    st.info("""
    **Capítulo 1: El Gran Árbol**
    
    *"El conejo Simón quiere encontrar la bellota dorada. ¿Puedes dibujarle unas flores pastel o un sol brillante para iluminar su camino?"*
    """)
    
    st.markdown("---")
    
    st.markdown("### 🌟 Estado del Dibujo")
    if canvas_result.json_data is not None:
        objects_count = len(canvas_result.json_data["objects"])
        st.metric(label="Objetos Mágicos Creados", value=f"{objects_count} ✨")
        if objects_count > 5:
            st.success("¡Tu dibujo está cobrando vida! La fábula se ve hermosa. 🦊🌸")
    else:
        st.caption("Usa tu pincel para empezar a crear la historia.")

st.caption("💡 Tip Mágico: Si quieres cambiar el tamaño del lienzo o empezar de nuevo, ajusta las medidas en la barra lateral.")
