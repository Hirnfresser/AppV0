# ====== Start Login Block ======
from utils.login_manager import LoginManager
LoginManager().go_to_login('Start.py')  
# ====== End Login Block ======

# ------------------------------------------------------------
# Here starts the actual app, which was developed previously
import streamlit as st

st.title('RPI Werte')

data_df = st.session_state['data_df']
if data_df.empty:
    st.info('Keine RPI Daten vorhanden. Berechnen Sie Ihren RPI auf der Rechner-Unterseite.')
    st.stop()

# Sort dataframe by timestamp
data_df = data_df.sort_values('timestamp', ascending=False)

# Display table
st.dataframe(data_df)

col1, col2, col3 = st.columns(3)

with col1: 
    if st.button('Zur Startseite'):
        st.switch_page('Start.py')
with col2:
    if st.button('Zum Rechner'):
        st.switch_page('pages/1_RPI-Rechner.py')
with col3:
    if st.button('Zu der Grafik'):
        st.switch_page('pages/3_RPI-Statistik.py')