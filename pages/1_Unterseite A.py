import streamlit as st

st.title("Retikulozytenindex-Rechner")

st.write("Diese Seite ist eine Unterseite der Startseite.")

import streamlit as st

def calculate_reticulocyte_index(reticulocytes, hematocrit, normal_hematocrit=45):
    """
    Berechnet den Retikulozytenindex.
    :param reticulocytes: Retikulozytenzahl in %
    :param hematocrit: Patientenspezifischer Hämatokrit-Wert in %
    :param normal_hematocrit: Normaler Hämatokrit-Wert (Standard: 45%)
    :return: Retikulozytenindex
    """
    return (reticulocytes * hematocrit / normal_hematocrit)

# Streamlit App
st.title("Retikulozytenindex-Rechner")

st.write("Dieser Rechner bestimmt den Retikulozytenindex zur Bewertung der Knochenmarkaktivität.")

# Benutzereingaben
reticulocytes = st.number_input("Retikulozytenzahl (%):", min_value=0.0, max_value=100.0, value=1.0, step=0.1)
hematocrit = st.number_input("Hämatokrit-Wert (%):", min_value=0.0, max_value=100.0, value=40.0, step=0.1)

if st.button("Berechnen"):
    ret_index = calculate_reticulocyte_index(reticulocytes, hematocrit)
    st.success(f"Der berechnete Retikulozytenindex beträgt: {ret_index:.2f}")

st.write("Hinweis: Ein Wert über 2 zeigt eine gesteigerte Erythropoese an, während ein Wert unter 2 eine unzureichende Knochenmarkreaktion anzeigt.")
