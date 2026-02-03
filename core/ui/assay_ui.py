import streamlit as st
from core.assay import assay_capsules_ui, assay_tablets_ui

def render():
    st.title("Assay")
    choix = st.selectbox("Formulation", ["Capsules", "Tablets"])
    if choix == "Capsules":
        assay_capsules_ui.render()
    else:
        assay_tablets_ui.render()