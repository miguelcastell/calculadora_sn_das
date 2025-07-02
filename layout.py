import streamlit as st
import base64

def carregar_logo(logo_path="logo.png"):
    with open(logo_path, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()

def exibir_logo_centralizada():
    logo_base64 = carregar_logo()

    html_code = f"""
    <style>
        .header-container {{
            display: flex;
            flex-direction: column;
            align-items: center;
            padding: 20px 0;
            border-bottom: 1px solid #eee;
        }}
        .header-container img {{
            height: 80px;
            margin-bottom: 10px;
        }}
        .header-container h1 {{
            margin: 0;
            font-size: 2.5rem;
            font-weight: 700;
            color: #333;
            text-align: center;
        }}
    </style>

    <div class="header-container">
        <img src="data:image/png;base64,{logo_base64}" alt="Logo" />
        <h1>Calculadora de DAS - Simples Nacional</h1>
    </div>
    """

    st.markdown(html_code, unsafe_allow_html=True)
