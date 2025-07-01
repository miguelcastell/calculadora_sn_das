import streamlit as st
import base64

import streamlit as st
import base64

def get_base64_of_bin_file(bin_file):
    with open(bin_file, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()

logo_base64 = get_base64_of_bin_file("logo.png")

html_code = f"""
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

st.markdown(html_code, unsafe_allow_html=True)


import streamlit as st
from calculo_das import calcular_das

usuario = st.secrets["DB_USERNAME"]
token = st.secrets["DB_TOKEN"]


st.set_page_config(page_title="Calculadora DAS", layout="centered")

# Função para renderizar cada aba
import re

def parse_numero_br(valor_str):
    """
    Converte '10.000,50' → 10000.50
    """
    valor_str = valor_str.strip()
    valor_str = valor_str.replace(".", "").replace(",", ".")
    return float(valor_str)


def render_aba(anexo_label):
    st.subheader(f"Simulação para o Anexo {anexo_label}")

    faturamento_input = st.text_input("Faturamento do mês (R$)", key=f"faturamento_{anexo_label}")
    receita_12m_input = st.text_input("Receita acumulada dos últimos 12 meses (R$)", key=f"rbt12_{anexo_label}")

    if st.button("Calcular", key=f"btn_{anexo_label}"):
        try:
            faturamento = parse_numero_br(faturamento_input)
            receita_12m = parse_numero_br(receita_12m_input)

            aliq, das, distribuicao = calcular_das(anexo_label, faturamento, receita_12m)
            st.success(f"✅ Alíquota efetiva: **{aliq:.2%}**")
            st.success(f"💰 Valor estimado do DAS: **R$ {das:,.2f}**")

            st.markdown("### 💡 Distribuição dos impostos:")
            for imposto, valor in distribuicao.items():
                st.write(f"**{imposto}**: R$ {valor:,.2f}")
        except ValueError:
            st.error("Digite valores numéricos válidos, ex: 10.000,00")
        except Exception as e:
            st.error(f"Erro inesperado: {str(e)}")

# Cria abas por anexo
aba_iii, aba_iv, aba_v = st.tabs(["Anexo III", "Anexo IV", "Anexo V"])
with aba_iii: render_aba("III")
with aba_iv: render_aba("IV")
with aba_v: render_aba("V")
