import streamlit as st
from layout import exibir_logo_centralizada
from calculo_das import calcular_das

st.set_page_config(page_title="Calculadora DAS", layout="centered")
exibir_logo_centralizada()

# ✅ Fonte customizada
st.markdown(
    """
    <style>
    html, body, [class*="css"] {
        font-family: 'Segoe UI', sans-serif;
        font-size: 16px;
    }
    </style>
    """,
    unsafe_allow_html=True
)


def parse_numero_br(valor_str):
    valor_str = valor_str.strip().replace(".", "").replace(",", ".")
    return float(valor_str)


def render_aba(anexo_label):
    st.subheader(f"Simulação para o Anexo {anexo_label}")

    faturamento_input = st.text_input("Faturamento do mês (R$)", key=f"faturamento_{anexo_label}")
    receita_12m_input = st.text_input("Receita acumulada dos últimos 12 meses (R$)", key=f"rbt12_{anexo_label}")

    exibir_retencao = anexo_label in ["III", "IV"]
    valor_iss_retido_input = "0"

    if exibir_retencao:
        iss_retido = st.checkbox("Possui ISS Retido?", key=f"iss_retido_{anexo_label}")
        if iss_retido:
            valor_iss_retido_input = st.text_input(
                "Valor do ISS retido (R$)",
                key=f"valor_iss_{anexo_label}"
            )
    else:
        iss_retido = False

    if st.button("Calcular", key=f"btn_{anexo_label}"):
        try:
            faturamento = parse_numero_br(faturamento_input)
            receita_12m = parse_numero_br(receita_12m_input)

            aliq, das, distribuicao = calcular_das(anexo_label, faturamento, receita_12m)

            st.success(f"✅ Alíquota efetiva: **{aliq:.2%}**")
            st.success(f"💰 Valor estimado do DAS (sem considerar retenções): **R$ {das:,.2f}**")

            st.markdown("### 💡 Distribuição dos impostos:")
            for imposto, valor in distribuicao.items():
                if imposto != "PD":
                    st.write(f"**{imposto}**: R$ {valor:,.2f}")

            if iss_retido and valor_iss_retido_input.strip():
                valor_iss_retido = parse_numero_br(valor_iss_retido_input)
                if valor_iss_retido > 0:
                    st.markdown("---")
                    st.warning("💡 O ISS informado como retido será subtraído do valor do DAS.")

                    iss_distribuido = distribuicao.get("ISS", 0)
                    valor_iss_retido = min(valor_iss_retido, iss_distribuido)

                    das_com_retencao = das - valor_iss_retido
                    das_com_retencao = max(das_com_retencao, 0.0)
                    total_pago = das_com_retencao + valor_iss_retido

                    st.markdown("### 🧾 Resumo do cálculo com retenção de ISS")
                    st.write(f"💰 **Valor total do DAS (cheio)**: R$ {das:,.2f}")
                    st.write(f"🧾 **ISS Retido (ajustado)**: R$ {valor_iss_retido:,.2f}")
                    st.write(f"✅ **DAS a pagar (guia)**: R$ {das_com_retencao:,.2f}")

                    # Estilo condicional
                    if das_com_retencao < das:
                        cor = "#28a745"  # verde
                        texto = "✅ Economia gerada pela retenção de ISS 💸"
                    else:
                        cor = "#dc3545"  # vermelho
                        texto = "⚠️ Sem economia com retenção de ISS"

                    st.markdown(
                        f"""
                        <div style='
                            background-color:{cor}10;
                            padding: 1rem;
                            border-left: 5px solid {cor};
                            border-radius: 0.5rem;
                            margin-top: 1rem;
                        '>
                            <p style='color:{cor}; margin:0; font-weight: bold;'>{texto}</p>
                            <p style='margin:0; font-size: 1.2rem; font-weight: bold;'>
                                📊 Total de tributos pagos pela empresa: R$ {total_pago:,.2f}
                            </p>
                        </div>
                        """,
                        unsafe_allow_html=True
                    )

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
