import streamlit as st
from calculo_das import calcular_das
from utils import parse_numero_br, formatar_moeda

def render_aba(anexo_label, atividade):
    st.header(f"Simples Nacional — Anexo {anexo_label}")
    st.markdown(f"**Atividade:** {atividade}")

    rbt12_input = st.text_input("Receita Bruta dos últimos 12 meses (RBT12)", key=f"rbt12_{anexo_label}")
    faturamento_mes_input = st.text_input("Faturamento do mês", key=f"faturamento_{anexo_label}")

    # Checkbox para ISS retido
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

            resultado = calcular_das(
                anexo=anexo_label,
                rbt12=rbt12,
                faturamento_mes=faturamento_mes
            )

            das = resultado["valor_das"]
            aliquota_efetiva = resultado["aliquota_efetiva"]
            faixa = resultado["faixa"]
            distribuicao = resultado["distribuicao"]

            st.markdown("---")
            st.subheader("Resultado")

            st.write(f"🧮 **Alíquota efetiva:** {aliquota_efetiva:.2f}%")
            st.write(f"📊 **Faixa:** {faixa}")
            st.write(f"💰 **Valor do DAS:** {formatar_moeda(das)}")

            if iss_retido and valor_iss_retido > 0:
                st.markdown("---")
                st.warning("💡 Como o ISS está retido, o valor será abatido do DAS.")
                valor_ajustado = das - valor_iss_retido
                valor_ajustado = max(valor_ajustado, 0)
                st.success(f"💸 DAS a pagar com retenção de R$ {valor_iss_retido:,.2f}: **{formatar_moeda(valor_ajustado)}**")

            st.markdown("---")
            st.subheader("Distribuição dos Tributos:")

            for imposto, valor in distribuicao.items():
                st.write(f"• {imposto}: {formatar_moeda(valor)}")

        except ValueError:
            st.error("🚫 Por favor, digite valores válidos em RBT12 e Faturamento do mês.")

