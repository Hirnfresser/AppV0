import streamlit as st
from functions.rpi_rechner import calculate_reticulocyte_index
from utils.data_manager import DataManager

login_manager = LoginManager(data_manager) # initialize login manager
login_manager.login_register()  # opens login page

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
    if result == 1.0:
        st.success(f"Der berechnete Retikulozytenproduktionsindex beträgt: {result:.2f}\n\nDies entspricht dem Normalfall", icon="✅")
    else:
        st.info(f"Der berechnete Retikulozytenproduktionsindex beträgt: {result:.2f}")
        

    result_dict = {
    'reticulocytes': reticulocytes,
    'hematocrit': hematocrit,
    'ret_index': result  # Assuming 'result' is the computed reticulocyte index
}   
    # update data in session state and save to persistent storage
    DataManager().append_record(session_state_key='data_df', record_dict=result_dict)  



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

if st.button('Startseite'):
    st.switch_page('Start.py')