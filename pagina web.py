import streamlit as st
import pandas as pd

# --- CONFIGURACIÓN DE LA PÁGINA ---
st.set_page_config(
    page_title="Asoc. Las Bendiciones",
    page_icon="🌿",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- ESTILOS CSS PERSONALIZADOS (OPCIONAL) ---
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
</style>
""", unsafe_allow_html=True)

# --- BARRA LATERAL (SIDEBAR) ---
with st.sidebar:
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
    st.markdown("<div class='bank-card'>"
                "<b>Banco Agrario de Colombia</b><br>"
                "Cuenta de Ahorros No.<br>"
                "<h3>416 223 006 894</h3>"
                "Oficina: Luruaco"
                "</div>", unsafe_allow_html=True)

# --- CONTENIDO PRINCIPAL ---

# Encabezado
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
# Crear etiquetas visuales para los valores
v_cols = st.columns(len(vals))
for i, v in enumerate(vals):
    v_cols[i].markdown(f"**{v}** 🌾")

st.write("---")

# SECCIÓN 2: INFORMACIÓN LEGAL
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
    
    st.markdown("#### 📑 Registro Tributario (RUT)")
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

# SECCIÓN 3: PLANEACIÓN ESTRATÉGICA 2026
st.header("📈 Planeación Estratégica 2026")

st.subheader("Objetivos")
st.markdown("**General:** Fortalecer la sostenibilidad económica, social y organizativa de la asociación campesina.")
st.markdown("**Específicos:** Mejorar ingresos, fortalecer gestión, acceder a mercados, incrementar productividad.")

# Estrategias en Tabs
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

# Tabla de Plan de Acción
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
st.write("• " + "\n• ".join(indicadores))

# Pie de página
st.write("---")
st.caption("© 2026 Asociación de Campesinos Agropecuarios Las Bendiciones | Luruaco, Atlántico")

