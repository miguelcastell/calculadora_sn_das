import streamlit as st
from layout import render_header
from calculo_das import calcular_das

# --- Page Configuration ---
# Sets basic page configurations like title and layout.
st.set_page_config(page_title="Calculadora DAS", layout="centered")
# Displays a logo in the sidebar.
st.sidebar.image("logo.png", width=150)

# Renders a custom header for the application (defined in layout.py).
render_header()

# --- Secret Management (Placeholders) ---
# Accesses secrets (like database credentials) for potential future use.
# These are typically configured outside the code for security.
usuario = st.secrets["DB_USERNAME"]
token = st.secrets["DB_TOKEN"]

# --- Utility Function ---
# Parses a Brazilian formatted number string (e.g., "10.000,00") into a float.
def parse_numero_br(valor_str):
    valor_str = valor_str.strip().replace(".", "").replace(",", ".")
    return float(valor_str)

# --- Main Render Function for Each Annex Tab ---
# This function creates the UI and logic for each "Anexo" tab.
def render_aba(anexo_label):
    st.subheader(f"Simulação para o Anexo {anexo_label}")

    # Input fields for monthly revenue and accumulated revenue over 12 months.
    # 'key' is crucial for Streamlit to uniquely identify widgets across tabs.
    faturamento_input = st.text_input("Faturamento do mês (R$)", key=f"faturamento_{anexo_label}")
    receita_12m_input = st.text_input("Receita acumulada dos últimos 12 meses (R$)", key=f"rbt12_{anexo_label}")
    
    # Checkbox to indicate if ISS (Service Tax) was withheld.
    possui_iss_retido = st.checkbox("Possui ISS retido?", key=f"iss_retido_{anexo_label}")

    # Button to trigger the calculation.
    if st.button("Calcular", key=f"btn_{anexo_label}"):
        try:
            # Parse input strings to float numbers.
            faturamento = parse_numero_br(faturamento_input)
            receita_12m = parse_numero_br(receita_12m_input)

            # Calls the external function to calculate DAS (defined in calculo_das.py).
            aliq, das, distribuicao = calcular_das(anexo_label, faturamento, receita_12m)

            # --- Displaying Results ---
            if possui_iss_retido:
                try:
                    # Calculates effective rate considering ISS withheld.
                    pd = distribuicao.get("PD", 0) # Gets 'PD' (presumably PIS/COFINS/IRPJ/CSLL portion) from distribution.
                    aliq_efetiva_iss = (receita_12m * aliq - pd) / receita_12m
                    st.success(f"✅ Alíquota efetiva com ISS retido: **{aliq_efetiva_iss:.4%}**")
                except ZeroDivisionError:
                    st.error("❌ Receita dos últimos 12 meses não pode ser zero.")
            else:
                # Displays the standard effective tax rate and estimated DAS value.
                st.success(f"✅ Alíquota efetiva: **{aliq:.2%}**")
                st.success(f"💰 Valor estimado do DAS: **R$ {das:,.2f}**")

            # Displays the breakdown of taxes.
            st.markdown("### 💡 Distribuição dos impostos:")
            for imposto, valor in distribuicao.items():
                st.write(f"**{imposto}**: R$ {valor:,.2f}")

        except ValueError:
            # Error handling for invalid numeric input.
            st.error("❌ Digite valores numéricos válidos. Ex: 10.000,00")
        except Exception as e:
            # General error handling for any unexpected issues.
            st.error(f"Erro inesperado: {str(e)}")

# --- Tab Creation ---
# Creates three tabs for different "Anexos".
aba_iii, aba_iv, aba_v = st.tabs(["Anexo III", "Anexo IV", "Anexo V"])
# Renders the content for each tab by calling the render_aba function.
with aba_iii: render_aba("III")
with aba_iv: render_aba("IV")
with aba_v: render_aba("V")
