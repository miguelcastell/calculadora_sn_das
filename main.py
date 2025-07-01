import streamlit as st
from calculo_das import calcular_das

# 🔧 Funções utilitárias incorporadas (não precisa mais do utils.py)
def parse_numero_br(s: str) -> float:
    """
    Converte string no formato brasileiro '1.234,56' para float 1234.56
    """
    s = s.replace('.', '').replace(',', '.').strip()
    return float(s)

def formatar_moeda(valor: float) -> str:
    """
    Formata um número float no estilo 'R$ 1.234,56'
    """
    return f"R$ {valor:,.2f}".replace(',', 'X').replace('.', ',').replace('X', '.')

# 🧮 Função principal da aba
def render_aba(anexo_label: str, atividade: str):
    st.header(f"Simples Nacional — Anexo {anexo_label}")
    st.markdown(f"**Atividade:** {atividade}")

    rbt12_input = st.text_input("Receita Bruta últimos 12 meses", key=f"rbt12_{anexo_label}")
    faturamento_mes_input = st.text_input("Faturamento do mês", key=f"faturamento_{anexo_label}")

    # 🔘 Checkbox e campo de ISS Retido
    iss_retido = st.checkbox("Possui ISS Retido?", key=f"iss_retido_{anexo_label}")
    valor_iss_retido = 0.0
    if iss_retido:
        valor_iss_retido_input = st.text_input("Valor do ISS retido (R$)", key=f"valor_iss_{anexo_label}")
        if valor_iss_retido_input:
            try:
                valor_iss_retido = parse_numero_br(valor_iss_retido_input)
            except ValueError:
                st.error("Digite um valor válido para o ISS retido.")

    if rbt12_input and faturamento_mes_input:
        try:
            rbt12 = parse_numero_br(rbt12_input)
            faturamento_mes = parse_numero_br(faturamento_mes_input)

            resultado = calcular_das(anexo=anexo_label, rbt12=rbt12, faturamento_mes=faturamento_mes)

            das = resultado["valor_das"]
            st.markdown("---")
            st.write(f"**Alíquota efetiva:** {resultado['aliquota_efetiva']:.2f}%")
            st.write(f"**Faixa atingida (R$ ≤):** {resultado['faixa']:,}")
            st.write(f"**Valor do DAS:** {formatar_moeda(das)}")

            if iss_retido and valor_iss_retido > 0:
                st.markdown("---")
                st.warning("💡 ISS retido será abatido do DAS.")
                ajustado = das - valor_iss_retido
                ajustado = max(0, ajustado)
                st.success(f"💸 DAS após retenção: **{formatar_moeda(ajustado)}**")

            st.markdown("---")
            st.subheader("Distribuição dos Tributos")
            for imp, val in resultado["distribuicao"].items():
                st.write(f"• {imp}: {formatar_moeda(val)}")

        except ValueError:
            st.error("🚫 Informe valores válidos em RBT12 e faturamento.")
