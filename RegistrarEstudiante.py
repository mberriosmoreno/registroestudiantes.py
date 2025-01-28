import streamlit as st
import pandas as pd
import os

# Ruta del archivo Excel
DATA_PATH = "data/estudiantes.xlsx"

# Título de la página
st.title("📝 Registrar Estudiante")

# Formulario para registrar un estudiante
with st.form("registrar_estudiante"):
    nombre = st.text_input("Nombre del Estudiante")
    edad = st.number_input("Edad", min_value=1, max_value=100)
    grado = st.selectbox("Grado", ["1ro", "2do", "3ro", "4to", "5to"])
    submit_button = st.form_submit_button("Registrar")

    if submit_button:
        # Verificar si el archivo ya existe
        if os.path.exists(DATA_PATH):
            df = pd.read_excel(DATA_PATH)
        else:
            df = pd.DataFrame(columns=["Nombre", "Edad", "Grado"])

        # Agregar el nuevo estudiante
        nuevo_estudiante = {"Nombre": nombre, "Edad": edad, "Grado": grado}
        df = df.append(nuevo_estudiante, ignore_index=True)

        # Guardar el archivo
        df.to_excel(DATA_PATH, index=False)
        st.success("✅ Estudiante registrado exitosamente!")
