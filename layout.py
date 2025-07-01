import streamlit as st
import base64
import os

def carregar_logo():
    logo_path = "logo.png"
    if os.path.exists(logo_path):
        with open(logo_path, "rb") as f:
            return base64.b64encode(f.read()).decode("utf-8")
    return None

def render_header():
    logo_base64 = carregar_logo()
    if logo_base64:
        st.markdown(
            f'<div style="text-align: center;"><img src="data:image/png;base64,{logo_base64}" width="200"></div>',
            unsafe_allow_html=True
        )
    st.title("Calculadora do Simples Nacional")
    st.markdown("---")
