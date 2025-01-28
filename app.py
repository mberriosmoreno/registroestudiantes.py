import streamlit as st

# Menú lateral
st.sidebar.title("Menú")
st.sidebar.markdown("Selecciona la operación que deseas realizar:")

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

