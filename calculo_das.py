def calcular_das_completo(anexo, faturamento, rbt12):
    from tabelas import tabelas_simples, distribuicao

    tabela = tabelas_simples[anexo]
    for faixa in tabela:
        if rbt12 <= faixa["limite"]:
            aliquota = faixa["aliquota"] / 100
            deducao = faixa["deducao"]
            break

    aliq_efetiva = ((faturamento * aliquota) - deducao) / faturamento
    das = faturamento * aliq_efetiva

    partilha = distribuicao[anexo]
    dist = {imposto: round(das * perc, 2) for imposto, perc in partilha.items() if imposto != "PD"}

    return aliq_efetiva, das, dist


def calcular_totais_contabeis(das, distribuicao, iss_retido):
    iss_distribuido = distribuicao.get("ISS", 0)
    iss_final = iss_retido
    das_sem_iss = das - iss_distribuido
    total_pago = das_sem_iss + iss_final

    return {
        "das_total": round(das, 2),
        "iss_distribuido": round(iss_distribuido, 2),
        "iss_retido": round(iss_retido, 2),
        "das_sem_iss": round(das_sem_iss, 2),
        "total_contabil": round(total_pago, 2)
    }
