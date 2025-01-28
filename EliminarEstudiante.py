import streamlit as st
import pandas as pd
import os

# Ruta del archivo Excel
DATA_PATH = "data/estudiantes.xlsx"

# Título de la página
st.title("❌ Eliminar Estudiante")

# Verificar si el archivo existe
if os.path.exists(DATA_PATH):
    df = pd.read_excel(DATA_PATH)

    # Seleccionar estudiante a eliminar
    estudiante_a_eliminar = st.selectbox("Selecciona un estudiante para eliminar", df["Nombre"])

    if st.button("Eliminar"):
        # Eliminar el estudiante
        df = df[df["Nombre"] != estudiante_a_eliminar]
        df.to_excel(DATA_PATH, index=False)
        st.success("✅ Estudiante eliminado exitosamente!")
else:
    st.warning("No hay estudiantes registrados aún.")
