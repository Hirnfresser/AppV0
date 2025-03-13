# ====== Start Login Block ======
from utils.login_manager import LoginManager
LoginManager().go_to_login('Start.py')  
# ====== End Login Block ======

# ------------------------------------------------------------
# === RPI Grafik ===
import streamlit as st

st.title('RPI Verlauf')

data_df = st.session_state['data_df']
if data_df.empty:
    st.info('Keine RPI Daten vorhanden. Berechnen Sie Ihren RPI auf der Rechner_Unterseite.')
    st.stop()

# hematocrit over time
st.line_chart(data=data_df.set_index('timestamp')['hematocrit'], 
                use_container_width=True)
st.caption('Hämtokrit über Zeit (%)')

# reticulocytes over time 
st.line_chart(data=data_df.set_index('timestamp')['reticulocytes'],
                use_container_width=True)
st.caption('Retikulozyten über Zeit (%)')

# RPI over time
st.line_chart(data=data_df.set_index('timestamp')['ret_index'],
                use_container_width=True)
st.caption('RPI über Zeit')