from utils import helpers
import streamlit as st

def calculate_reticulocyte_index(reticulocytes, hematocrit, normal_hematocrit=45, timezone='Europe/Zurich'):
    result = (reticulocytes * hematocrit) / normal_hematocrit
    if result == 1.0:
        st.success(f"Der berechnete Retikulozytenproduktionsindex beträgt: {result:.2f}\n\nDies entspricht dem Normalfall", icon="✅")
    else:
         st.info(f"Der berechnete Retikulozytenproduktionsindex beträgt: {result:.2f}")
        
    result_dict = {
        'timestamp': helpers.ch_now(),
        'reticulocytes': reticulocytes,
        'hematocrit': hematocrit,
        'ret_index': result}
    
    return result_dict
    