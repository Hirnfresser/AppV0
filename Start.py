import streamlit as st
import pandas as pd

from utils.data_manager import DataManager #Anleitung Nummer 9 im moodle

# initialize the data manager
data_manager = DataManager(fs_protocol='webdav', fs_root_folder="Institution/BMLD_App_RPI_Rechner")  # switch drive 

# load the data from the persistent storage into the session state
data_manager.load_app_data(
    session_state_key='data_df', 
    file_name='data.csv', 
    initial_value = pd.DataFrame(), 
    parse_dates = ['timestamp']
    )

# === Initialize the login manager ===
from utils.login_manager import LoginManager

login_manager = LoginManager(data_manager) # initialize login manager
login_manager.login_register()  # opens login page


st.title("Retikulozytenproduktionsindex-Rechner")

st.markdown("Die RPI-Rechner-App ermöglicht die schnelle und präzise Berechnung des Retikulozytenproduktionsindex (RPI) zur Beurteilung der Knochenmarkaktivität. Durch die Eingabe von Hämatokrit und Retikulozytenwert erhalten medizinische Fachkräfte eine Einschätzung der erythropoetischen Aktivität.")
# !! WICHTIG: Eure Emails müssen in der App erscheinen!!

# Streamlit über den Text unten direkt in die App - cool
" Diese App wurde von folgenden Personen entwickelt: "
" - Sara Stettler (stettsar@zhaw.students.ch) "
" - Leah Cosslett (cossllea@zhaw.students.ch)"

if st.button('RPI-Rechner'):
    st.switch_page('pages/1_RPI-Rechner.py')
