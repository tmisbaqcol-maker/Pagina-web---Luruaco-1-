import streamlit as st
import pandas as pd
import base64

# --- CONFIGURACIÓN DE LA PÁGINA ---
st.set_page_config(
    page_title="Asoc. Las Bendiciones",
    page_icon="🌿",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- FUNCIÓN PARA CARGAR IMÁGENES LOCALES EN BASE64 ---
def img_to_base64(img_path):
    try:
        with open(img_path, "rb") as f:
            return base64.b64encode(f.read()).decode()
    except FileNotFoundError:
        return None

# --- ESTILOS CSS PERSONALIZADOS ---
st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        color: #2e7d32;
        font-weight: bold;
    }
    .sub-header {
        color: #555;
        font-size: 1.2rem;
    }
    .card {
        background-color: #f1f8e9;
        padding: 20px;
        border-radius: 10px;
        border-left: 5px solid #2e7d32;
        margin-bottom: 10px;
    }
    .bank-card {
        background-color: #e8f5e9;
        padding: 15px;
        border-radius: 10px;
        text-align: center;
    }
    .foto-caption {
        text-align: center;
        color: #555;
        font-style: italic;
        font-size: 0.9rem;
        margin-top: 5px;
    }
</style>
""", unsafe_allow_html=True)

# --- RUTAS DE IMÁGENES ---
# Todos estos archivos deben estar en la MISMA carpeta que este script
LOGO_PATH = "Captura_de_pantalla_2026-02-18_003923.png"
FOTOS = [
    {
        "path": "WhatsApp_Image_2026-02-17_at_12_06_06_PM.jpeg",
        "caption": "Cultivos de cúrcuma en etapa de crecimiento"
    },
    {
        "path": "WhatsApp_Image_2026-02-17_at_12_09_15_PM.jpeg",
        "caption": "Asociado trabajando en el cultivo"
    },
    {
        "path": "WhatsApp_Image_2026-02-17_at_12_15_48_PM.jpeg",
        "caption": "Cosecha de cúrcuma — producción enero 2025"
    },
]

# --- BARRA LATERAL (SIDEBAR) ---
with st.sidebar:
    logo_b64 = img_to_base64(LOGO_PATH)
    if logo_b64:
        st.markdown(
            f"<div style='text-align:center; margin-bottom:15px;'>"
            f"<img src='data:image/png;base64,{logo_b64}' style='max-width:90%; border-radius:10px;'>"
            f"</div>",
            unsafe_allow_html=True
        )
    else:
        st.image("https://via.placeholder.com/300x100?text=LOGO+LAS+BENDICIONES", use_column_width=True)

    st.title("Contacto y Recursos")

    st.markdown("### 📞 Información")
    st.write("**Representante Legal:**")
    st.write("Luis Eduardo Sierra Ramírez")
    st.caption("CC. 72.224.810")
    st.write("📧 eduardoluissierra2020@gmail.com")
    st.write("📍 Luruaco, Atlántico")

    st.divider()

    st.markdown("### 🏦 Cuenta Bancaria")
    st.markdown(
        "<div class='bank-card'>"
        "<b>Banco Agrario de Colombia</b><br>"
        "Cuenta de Ahorros No.<br>"
        "<h3>416 223 006 894</h3>"
        "Oficina: Luruaco"
        "</div>",
        unsafe_allow_html=True
    )

# --- CONTENIDO PRINCIPAL ---

# Encabezado con logo
logo_b64_main = img_to_base64(LOGO_PATH)
if logo_b64_main:
    col_logo, col_titulo = st.columns([1, 4])
    with col_logo:
        st.markdown(
            f"<div style='display:flex; align-items:center; height:100%;'>"
            f"<img src='data:image/png;base64,{logo_b64_main}' style='width:140px; border-radius:10px;'>"
            f"</div>",
            unsafe_allow_html=True
        )
    with col_titulo:
        st.markdown('<p class="main-header">ASOCIACIÓN DE CAMPESINOS AGROPECUARIOS LAS BENDICIONES</p>', unsafe_allow_html=True)
        st.markdown('<p class="sub-header">NIT: 901.698.986-0 | Luruaco, Atlántico, Colombia</p>', unsafe_allow_html=True)
else:
    st.markdown('<p class="main-header">ASOCIACIÓN DE CAMPESINOS AGROPECUARIOS LAS BENDICIONES</p>', unsafe_allow_html=True)
    st.markdown('<p class="sub-header">NIT: 901.698.986-0 | Luruaco, Atlántico, Colombia</p>', unsafe_allow_html=True)

st.write("---")

# SECCIÓN 1: NOSOTROS
st.header("🌱 Nosotros")
col1, col2 = st.columns(2)
with col1:
    st.subheader("Misión")
    st.info("Representar y fortalecer a los campesinos asociados mediante la producción sostenible, la comercialización justa y el desarrollo social y económico de sus familias.")
with col2:
    st.subheader("Visión")
    st.success("Ser una asociación campesina sólida, reconocida por su producción de calidad, su organización democrática y su impacto positivo en el desarrollo rural de la Región.")

st.subheader("Valores")
vals = ["Solidaridad", "Trabajo colectivo", "Transparencia", "Sostenibilidad", "Compromiso social"]
v_cols = st.columns(len(vals))
for i, v in enumerate(vals):
    v_cols[i].markdown(f"**{v}** 🌾")

st.write("---")

# SECCIÓN 2: GALERÍA FOTOGRÁFICA
st.header("📸 Nuestro Trabajo en el Campo")

cols_foto = st.columns(3)
for i, foto in enumerate(FOTOS):
    b64 = img_to_base64(foto["path"])
    with cols_foto[i]:
        if b64:
            st.markdown(
                f"<img src='data:image/jpeg;base64,{b64}' "
                f"style='width:100%; border-radius:12px; object-fit:cover; height:280px; "
                f"box-shadow: 0 4px 8px rgba(0,0,0,0.15);'>",
                unsafe_allow_html=True
            )
            st.markdown(f"<p class='foto-caption'>{foto['caption']}</p>", unsafe_allow_html=True)
        else:
            st.warning(f"Imagen no encontrada: {foto['path']}")

st.write("---")

# SECCIÓN 3: INFORMACIÓN LEGAL
st.header("📜 Información Legal y Cumplimiento")

legal_col1, legal_col2 = st.columns(2)

with legal_col1:
    st.markdown("#### 📋 Datos de la Asociación")
    st.markdown("""
    - **Nombre:** Asociación de Campesinos Agropecuarios Las Bendiciones
    - **NIT:** 901.698.986-0
    - **Dirección:** Calle 17 #20-27 / CR 24 17 15
    - **Municipio:** Luruaco, Atlántico
    - **Teléfono:** 3145311578
    """)

    st.markdown("#### 🔑 Registro Tributario (RUT)")
    st.caption("Fecha de inscripción: 30 de marzo de 2023")
    st.write("Responsabilidades: Impuesto Renta, Retención en la fuente, Obligación facturar, Informante de exogena.")

with legal_col2:
    st.markdown("#### 👤 Representante Legal")
    st.markdown("""
    - **Nombre:** Luis Eduardo Sierra Ramírez
    - **C.C.:** 72.224.810
    - **Vigencia Cédula Rural:**
      - Del 04 Marzo 2025 al 04 Marzo 2027
    """)

    st.markdown("#### ⚖️ Cumplimiento Normativo")
    st.success("✅ **Alcaldía Municipal de Luruaco:** Certificación cumplimiento Ley 2219 de 2022. (Sep 2025)")
    st.success("✅ **Procuraduría General:** No registra sanciones ni inhabilidades vigentes. (Ene 2026)")

st.write("---")

# SECCIÓN 4: PLANEACIÓN ESTRATÉGICA 2026
st.header("📈 Planeación Estratégica 2026")

st.subheader("Objetivos")
st.markdown("**General:** Fortalecer la sostenibilidad económica, social y organizativa de la asociación campesina.")
st.markdown("**Específicos:** Mejorar ingresos, fortalecer gestión, acceder a mercados, incrementar productividad.")

st.subheader("Líneas Estratégicas")
tab1, tab2, tab3, tab4 = st.tabs(["🌱 Productivas", "🛒 Comerciales", "🤝 Organizacionales", "💰 Financieras"])

with tab1:
    st.write("- Capacitación técnica en cultivos y buenas prácticas.")
    st.write("- Producción planificada según demanda.")
    st.write("- Uso compartido de maquinaria e insumos.")

with tab2:
    st.write("- Venta directa (ferias campesinas, mercados locales).")
    st.write("- Eliminación de intermediarios.")
    st.write("- Creación de marca colectiva.")

with tab3:
    st.write("- Fortalecer la junta directiva.")
    st.write("- Reglamentos claros de funcionamiento.")
    st.write("- Formación en liderazgo campesino.")

with tab4:
    st.write("- Fondo común de ahorro.")
    st.write("- Gestión de créditos rurales.")
    st.write("- Acceso a proyectos y convocatorias.")

# Tabla Plan de Acción
st.subheader("Plan de Acción")
data_plan = {
    'Actividad': ['Capacitación agrícola', 'Creación de marca', 'Feria campesina', 'Fondo de ahorro'],
    'Responsable': ['Junta directiva', 'Comité comercial', 'Asociación', 'Tesorería'],
    'Tiempo': ['6 meses', '4 meses', 'Permanente', '3 meses'],
    'Recursos': ['Apoyo institucional', 'Diseñador / aliados', 'Productos', 'Aportes asociados']
}
df_plan = pd.DataFrame(data_plan)
st.dataframe(df_plan, use_container_width=True, hide_index=True)

# Indicadores
st.subheader("Indicadores de Seguimiento")
indicadores = [
    "Incremento del ingreso promedio de los asociados",
    "Número de nuevos mercados alcanzados",
    "Nivel de participación en reuniones",
    "Producción vendida directamente"
]
for ind in indicadores:
    st.write(f"• {ind}")

# Pie de página
st.write("---")
st.caption("© 2026 Asociación de Campesinos Agropecuarios Las Bendiciones | Luruaco, Atlántico")
