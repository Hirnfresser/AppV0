# ====== Start Login Block ======
from utils.login_manager import LoginManager
LoginManager().go_to_login('Start.py') 
# ====== End Login Block ======

import streamlit as st
from functions.rpi_rechner import calculate_reticulocyte_index
from utils.data_manager import DataManager

# Streamlit App
st.title("🩸Retikulozytenproduktionsindex-Rechner")

st.write("Dieser Rechner bestimmt den Retikulozytenproduktionsindex zur Bewertung der Erythropoese-Aktivität.")

# Formular für Benutzereingaben
with st.form(key='input_form'):
    reticulocytes = st.number_input("Retikulozytenzahl (%):", min_value=0.0, max_value=100.0, value=1.0, step=0.1)
    hematocrit = st.number_input("Hämatokrit-Wert (%):", min_value=0.0, max_value=100.0, value=40.0, step=0.1)
    submit_button = st.form_submit_button(label="Berechnen")

if submit_button:
    result = calculate_reticulocyte_index(reticulocytes, hematocrit)

 # --- Save RPI data ---
    from utils.data_manager import DataManager
    DataManager().append_record(session_state_key='data_df', record_dict=result)  # update data in session state and storage


st.write("Hinweis: Bitte beachten Sie, dass die Normwerte abweichen können und der Rechner keine medizinische Beratung ersetzt!")


st.feedback("stars")

st.markdown(
    """
    <style>
    .stApp {
        background: linear-gradient(to bottom, #FFCCCC, #FFFFFF);
        background-attachment: fixed;
    }
    </style>
    """,
    unsafe_allow_html=True
)

col1, col2, col3 = st.columns(3)

with col1:
    if st.button('Zur Startseite'):
        st.switch_page('Start.py')

with col2:
    if st.button('Zur Daten-Tabelle'):
        st.switch_page('pages/2_RPI-Daten.py')

with col3:
    if st.button('Zur Grafik'):
        st.switch_page('pages/3_RPI-Statistik.py')