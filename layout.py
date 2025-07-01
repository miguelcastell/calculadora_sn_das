import streamlit as st
import base64

def get_base64_of_bin_file(bin_file):
    with open(bin_file, "rb") as f:
        return base64.b64encode(f.read()).decode()

def render_header():
    logo_base64 = get_base64_of_bin_file("logo.png")
    html = f"""
    <style>
        .header-container {{
            display: flex;
            flex-direction: column;
            align-items: center;
            padding: 40px 0;
            border-bottom: 1px solid #eee;
        }}
        .header-container img {{
            height: 160px;
            margin-bottom: 20px;
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
    st.markdown(html, unsafe_allow_html=True)
