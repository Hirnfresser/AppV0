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
st.title("Retikulozytenproduktionsindex-Rechner")

st.write("Dieser Rechner bestimmt den Retikulozytenproduktionsindex zur Bewertung der Erythropoese-Aktivität.")

# Formular für Benutzereingaben
with st.form(key='input_form'):
    reticulocytes = st.number_input("Retikulozytenzahl (%):", min_value=0.0, max_value=100.0, value=1.0, step=0.1)
    hematocrit = st.number_input("Hämatokrit-Wert (%):", min_value=0.0, max_value=100.0, value=40.0, step=0.1)
    submit_button = st.form_submit_button(label="Berechnen")

if submit_button:
    ret_index = calculate_reticulocyte_index(reticulocytes, hematocrit)
    if ret_index == 1.0:
        st.success(f"Der berechnete Retikulozytenproduktionsindex beträgt: {ret_index:.2f}\n\nDies entspricht dem Normalfall", icon="✅")
    else:
        st.info(f"Der berechnete Retikulozytenproduktionsindex beträgt: {ret_index:.2f}")

st.write("Hinweis: Bitte beachten Sie, dass dieser Rechner nur eine grobe Schätzung darstellt und keine medizinische Beratung ersetzt")


st.feedback("stars")

st.markdown(
    """
    <style>
    .stApp {
        background: linear-gradient(to bottom, #FFFFFF, #FFCCCC);
        background-attachment: fixed;
    }
    </style>
    """,
    unsafe_allow_html=True
)