import streamlit as st
import pandas as pd
import os

# Ruta del archivo Excel
DATA_PATH = "data/estudiantes.xlsx"

# Título de la página
st.title("✏️ Editar Estudiante")

# Verificar si el archivo existe
if os.path.exists(DATA_PATH):
    df = pd.read_excel(DATA_PATH)

    # Verificar si hay estudiantes registrados
    if not df.empty:
        # Seleccionar estudiante a editar
        estudiante_a_editar = st.selectbox("Selecciona un estudiante para editar", df["Nombre"])

        # Obtener los datos del estudiante seleccionado
        estudiante = df[df["Nombre"] == estudiante_a_editar]

        if not estudiante.empty:
            estudiante = estudiante.iloc[0]

            # Formulario para editar
            with st.form("editar_estudiante"):
                nombre = st.text_input("Nombre", estudiante["Nombre"])
                edad = st.number_input("Edad", value=estudiante["Edad"])
                grado = st.selectbox("Grado", ["1ro", "2do", "3ro", "4to", "5to"], index=["1ro", "2do", "3ro", "4to", "5to"].index(estudiante["Grado"]))
                submit_button = st.form_submit_button("Actualizar")

                if submit_button:
                    # Actualizar los datos
                    df.loc[df["Nombre"] == estudiante_a_editar, ["Nombre", "Edad", "Grado"]] = [nombre, edad, grado]
                    df.to_excel(DATA_PATH, index=False)
                    st.success("✅ Estudiante actualizado exitosamente!")
        else:
            st.warning("No se encontró el estudiante seleccionado.")
    else:
        st.warning("No hay estudiantes registrados aún.")
else:
    st.warning("No hay estudiantes registrados aún.")
