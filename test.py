from calculo_das import calcular_das

aliq, das = calcular_das(12000, 250000, "III")

print(f"Alíquota efetiva: {aliq:.2%}")
print(f"Valor do DAS: R$ {das:,.2f}")
