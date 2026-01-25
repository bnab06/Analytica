import streamlit as st
from core.assay import assay_engine

def render():
    st.write("Assay Tablets UI")
    assay_engine.calculate()