import pandas as pd
from utils.data_manager import DataManager
from utils.login_manager import LoginManager

# initialize the data manager
data_manager = DataManager(fs_protocol='webdav', fs_root_folder="Institution/BMLD_App_RPI_Rechner")  # switch drive 

# load the data from the persistent storage into the session state
data_manager.load_user_data(
    session_state_key='data_df', 
    file_name='data.csv', 
    initial_value = pd.DataFrame(),
    parse_dates = ['timestamp']
    )

# initialize the login manager
login_manager = LoginManager(data_manager)
login_manager.login_register()  # open login/register page

import streamlit as st

st.title("Retikulozytenproduktionsindex-Rechner")

st.markdown("Die RPI-Rechner-App ermöglicht die schnelle und präzise Berechnung des Retikulozytenproduktionsindex (RPI) zur Beurteilung der Knochenmarkaktivität. Durch die Eingabe von Hämatokrit und Retikulozytenwert erhalten medizinische Fachkräfte eine Einschätzung der erythropoetischen Aktivität.")
# !! WICHTIG: Eure Emails müssen in der App erscheinen!!

# Streamlit über den Text unten direkt in die App - cool
" Diese App wurde von folgenden Personen entwickelt: "
" - Sara Stettler (stettsar@zhaw.students.ch) "
" - Leah Cosslett (cossllea@zhaw.students.ch)"

col1, col2, col3 = st.columns(3)

with col1:
    if st.button('Zum Rechner'):
        st.switch_page('pages/1_RPI-Rechner.py')
with col2:
    if st.button('Zu den Daten'):
        st.switch_page('pages/2_RPI-Daten.py')
with col3:
    if st.button('Zu der Grafik'):
        st.switch_page('pages/3_RPI-Statistik.py')

