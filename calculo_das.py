import json

# Carrega os dados
with open("distribuicao_impostos.json", "r") as f:
    distribuicao = json.load(f)

with open("tabelas_simples.json", "r") as f:
    tabelas_simples = json.load(f)


def encontrar_faixa(anexo: str, rbt12: float):
    for faixa in tabelas_simples[anexo]:
        if rbt12 <= faixa["limite_superior"]:
            return faixa
    raise ValueError("Receita bruta ultrapassa o limite do Simples Nacional.")


def calcular_das(anexo: str, receita_bruta: float, rbt12: float):
    anexo = anexo.upper()
    faixa = encontrar_faixa(anexo, rbt12)
    
    # Cálculo da alíquota efetiva
    aliq_efetiva = ((rbt12 * faixa["aliquota"]) - faixa["parcela_deduzir"]) / rbt12
    
    valor_das = receita_bruta * aliq_efetiva

    faixa_num = faixa["faixa"]
    distribuicao_faixa = distribuicao[anexo][str(faixa_num)]
    
    valores_por_imposto = {
        imposto: valor_das * percentual
        for imposto, percentual in distribuicao_faixa.items()
    }

    return aliq_efetiva, valor_das, valores_por_imposto
