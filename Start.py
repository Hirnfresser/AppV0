import streamlit as st
import pandas as pd

st.title("Retikulozytenproduktionsindex-Rechner")

st.markdown("Die RPI-Rechner-App ermöglicht die schnelle und präzise Berechnung des Retikulozytenproduktionsindex (RPI) zur Beurteilung der Knochenmarkaktivität. Durch die Eingabe von Hämatokrit und Retikulozytenwert erhalten medizinische Fachkräfte eine Einschätzung der erythropoetischen Aktivität.")
# !! WICHTIG: Eure Emails müssen in der App erscheinen!!

# Streamlit über den Text unten direkt in die App - cool
" Diese App wurde von folgenden Personen entwickelt: "
" - Sara Stettler (stettsar@zhaw.students.ch) "
" - Leah Cosslett (cossllea@zhaw.students.ch)"

if st.button('RPI-Rechner'):
    st.switch_page('pages/1_RPI-Rechner.py')
