import streamlit as st
from layout import exibir_logo_centralizada
from calculo_das import calcular_das_completo, calcular_totais_contabeis

st.set_page_config(page_title="Calculadora DAS", layout="centered")
exibir_logo_centralizada()

st.markdown("""
    <style>
    html, body, [class*="css"] {
        font-family: 'Segoe UI', sans-serif;
        font-size: 16px;
    }
    </style>
""", unsafe_allow_html=True)

def parse_numero_br(valor_str):
    valor_str = valor_str.strip().replace(".", "").replace(",", ".")
    return float(valor_str)

def render_aba(anexo):
    st.subheader(f"Simulação para o Anexo {anexo}")

    faturamento_input = st.text_input("Faturamento do mês (R$)", key=f"faturamento_{anexo}")
    receita_12m_input = st.text_input("Receita acumulada dos últimos 12 meses (R$)", key=f"rbt12_{anexo}")

    exibir_retencao = anexo in ["III", "IV"]
    valor_iss_retido_input = "0"

    if exibir_retencao:
        iss_retido = st.checkbox("Possui ISS Retido?", key=f"iss_retido_{anexo}")
        if iss_retido:
            valor_iss_retido_input = st.text_input("Valor do ISS retido (R$)", key=f"valor_iss_{anexo}")
    else:
        iss_retido = False

    if st.button("Calcular", key=f"btn_{anexo}"):
        try:
            faturamento = parse_numero_br(faturamento_input)
            receita_12m = parse_numero_br(receita_12m_input)
            valor_iss_retido = parse_numero_br(valor_iss_retido_input) if iss_retido else 0.0

            aliq, das, distribuicao = calcular_das_completo(anexo, faturamento, receita_12m)
            totais = calcular_totais_contabeis(das, distribuicao, valor_iss_retido)

            st.success(f"Alíquota efetiva: **{aliq:.2%}**")
            st.success(f"DAS calculado sobre o faturamento: **R$ {totais['das_total']:,.2f}**")

            st.markdown("### Distribuição estimada dos impostos:")
            for imposto, valor in distribuicao.items():
                if imposto != "PD":
                    st.write(f"**{imposto}**: R$ {valor:,.2f}")

            if iss_retido and valor_iss_retido > 0:
                st.markdown("---")
                st.warning("O ISS informado como retido será considerado no total contábil.")

                cor = "#28a745" if totais['das_sem_iss'] + totais['iss_retido'] < totais['das_total'] else "#dc3545"
                texto = "✅ Economia gerada pela retenção de ISS 💸" if cor == "#28a745" else "⚠️ Sem economia com retenção de ISS"

                st.markdown(f"""
                    ### Resumo contábil com retenção de ISS
                    - **DAS cheio:** R$ {totais['das_total']:,.2f}
                    - **ISS Retido (ajustado):** R$ {totais['iss_retido']:,.2f}
                    - **DAS sem o ISS:** R$ {totais['das_sem_iss']:,.2f}
                """)

                st.markdown(f"""
                    <div style='
                        background-color:{cor}10;
                        padding: 1rem;
                        border-left: 5px solid {cor};
                        border-radius: 0.5rem;
                        margin-top: 1rem;'>
                        <p style='color:{cor}; margin:0; font-weight: bold;'>{texto}</p>
                        <p style='margin:0; font-size: 1.2rem; font-weight: bold;'>
                            Total de tributos pagos pela empresa: R$ {totais['total_contabil']:,.2f}
                        </p>
                    </div>
                """, unsafe_allow_html=True)

        except ValueError:
            st.error("Digite valores numéricos válidos, ex: 10.000,00")
        except Exception as e:
            st.error(f"Erro inesperado: {str(e)}")

# Criar abas para os anexos
aba_iii, aba_iv, aba_v = st.tabs(["Anexo III", "Anexo IV", "Anexo V"])
with aba_iii:
    render_aba("III")
with aba_iv:
    render_aba("IV")
with aba_v:
    render_aba("V")
