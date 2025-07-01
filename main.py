import streamlit as st
from layout import render_header
from calculo_das import calcular_das

st.set_page_config(page_title="Calculadora DAS", layout="centered")
render_header()

usuario = st.secrets["DB_USERNAME"]
token = st.secrets["DB_TOKEN"]

def parse_numero_br(valor_str):
    valor_str = valor_str.strip().replace(".", "").replace(",", ".")
    return float(valor_str)

def render_aba(anexo_label):
    st.subheader(f"Simulação para o Anexo {anexo_label}")

    faturamento_input = st.text_input("Faturamento do mês (R$)", key=f"faturamento_{anexo_label}")
    receita_12m_input = st.text_input("Receita acumulada dos últimos 12 meses (R$)", key=f"rbt12_{anexo_label}")
    
    possui_iss_retido = st.checkbox("Possui ISS retido?", key=f"iss_retido_{anexo_label}")

    if st.button("Calcular", key=f"btn_{anexo_label}"):
        try:
            faturamento = parse_numero_br(faturamento_input)
            receita_12m = parse_numero_br(receita_12m_input)

            aliq, das, distribuicao = calcular_das(anexo_label, faturamento, receita_12m)

            if possui_iss_retido:
                try:
                    pd = distribuicao.get("PD", 0)
                    aliq_efetiva_iss = (receita_12m * aliq - pd) / receita_12m
                    st.success(f"✅ Alíquota efetiva com ISS retido: **{aliq_efetiva_iss:.4%}**")
                except ZeroDivisionError:
                    st.error("❌ Receita dos últimos 12 meses não pode ser zero.")
            else:
                st.success(f"✅ Alíquota efetiva: **{aliq:.2%}**")
                st.success(f"💰 Valor estimado do DAS: **R$ {das:,.2f}**")

            st.markdown("### 💡 Distribuição dos impostos:")
            for imposto, valor in distribuicao.items():
                st.write(f"**{imposto}**: R$ {valor:,.2f}")

        except ValueError:
            st.error("❌ Digite valores numéricos válidos. Ex: 10.000,00")
        except Exception as e:
            st.error(f"Erro inesperado: {str(e)}")

aba_iii, aba_iv, aba_v = st.tabs(["Anexo III", "Anexo IV", "Anexo V"])
with aba_iii: render_aba("III")
with aba_iv: render_aba("IV")
with aba_v: render_aba("V")
