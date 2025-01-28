import streamlit as st
import pandas as pd
import os

# Ruta del archivo Excel
DATA_PATH = "data/estudiantes.xlsx"

# Título de la página
st.title("📋 Ver Estudiantes")

# Verificar si el archivo existe
if os.path.exists(DATA_PATH):
    df = pd.read_excel(DATA_PATH)
    st.dataframe(df)
else:
    st.warning("No hay estudiantes registrados aún.")
