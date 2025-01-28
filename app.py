import streamlit as st

# Configuración de la página
st.set_page_config(
    page_title="Gestión de Estudiantes",
    page_icon="🏫",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Título de la aplicación
st.title("🏫 Gestión de Estudiantes")
st.markdown("Bienvenido a la aplicación de gestión de estudiantes. Selecciona una opción del menú lateral.")

# Menú lateral
st.sidebar.title("Menú")
st.sidebar.markdown("Selecciona la operación que deseas realizar:")

# Enlaces a las páginas
st.sidebar.page_link("app.py", label="🏠 Inicio")
st.sidebar.page_link("pages/1_📝_Registrar_Estudiante.py", label="📝 Registrar Estudiante")
st.sidebar.page_link("pages/2_📋_Ver_Estudiantes.py", label="📋 Ver Estudiantes")
st.sidebar.page_link("pages/3_✏️_Editar_Estudiante.py", label="✏️ Editar Estudiante")
st.sidebar.page_link("pages/4_❌_Eliminar_Estudiante.py", label="❌ Eliminar Estudiante")
