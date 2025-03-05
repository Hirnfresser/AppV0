import streamlit as st
import pandas as pd

st.title("Einführung App-Entwicklung mit Streamlit")

# !! WICHTIG: Eure Emails müssen in der App erscheinen!!

# Streamlit über den Text unten direkt in die App - cool
" Diese App wurde von folgenden Personen entwickelt: "
" - Sara Stettler (stettsar@zhaw.students.ch) "
" - Leah Cosslett (cossllea@zhaw.students.ch)"

if st.button('RPI-Rechner'):
    st.switch_page('pages/1_RPI-Rechner.py')