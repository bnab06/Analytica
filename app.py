import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

import streamlit as st
from core.ui import (
    assay_ui,
    content_uniformity_ui,
    dissolution_ui,
    water_content_ui,
    density_ui,
    lod_ui,
    method_validation_ui,
    cleaning_validation_ui,
    admin_ui,
    pdf_report
)

st.set_page_config(page_title="Analytica", layout="wide")

st.sidebar.title("Analytica")
st.sidebar.caption("Powered by: BnB")

module = st.sidebar.selectbox("Select Module", [
    "Assay",
    "Content Uniformity",
    "Dissolution",
    "Water Content",
    "Density",
    "Loss on Drying (LOD)",
    "Method Validation",
    "Cleaning Validation"
])

if module == "Assay":
    assay_ui.render()
elif module == "Content Uniformity":
    content_uniformity_ui.render()
elif module == "Dissolution":
    dissolution_ui.render()
elif module == "Water Content":
    water_content_ui.render()
elif module == "Density":
    density_ui.render()
elif module == "Loss on Drying (LOD)":
    lod_ui.render()
elif module == "Method Validation":
    method_validation_ui.render()
elif module == "Cleaning Validation":
    cleaning_validation_ui.render()