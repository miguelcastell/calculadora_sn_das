# 📊 CALCULADORA DE DAS - SIMPLES NACIONAL

Sistema em Python com interface Streamlit para calcular o valor do DAS (Documento de Arrecadação do Simples Nacional), considerando todas as faixas, anexos e partilhas por imposto, com base na legislação vigente (LC 123/2006).

---

## ⚙️ FUNCIONALIDADES

✅ Cálculo da **alíquota efetiva** com base na receita bruta dos últimos 12 meses  
✅ Cálculo do **valor do DAS** mensal  
✅ Exibição da **faixa tributária** correta  
✅ Distribuição do DAS por **IRPJ, CSLL, COFINS, PIS, CPP e ISS**  
✅ Seleção de **Anexo III, IV ou V**  
✅ Interface interativa com **Streamlit**  
✅ Tabelas externas em **.json** (modular e editável)

---

## 🗂 ESTRUTURA DO PROJETO

```
📁 seu_projeto/
├── main.py                     # Interface com Streamlit
├── calculo_das.py              # Lógica de cálculo
├── tabelas_simples.json        # Tabelas com faixas e alíquotas
├── distribuicao_impostos.json # Percentual de cada imposto por faixa/anexo
├── README.md                   # Este arquivo
```

---

## ▶️ COMO EXECUTAR

1. Instale as dependências:
```bash
pip install streamlit
```

2. Rode o sistema:
```bash
streamlit run main.py
```

---

## 📈 EXEMPLO DE USO

> Receita dos últimos 12 meses: R$ 280.000,00  
> Receita do mês: R$ 12.000,00  
> Anexo: **III**

**Saída esperada**:
- Alíquota efetiva: **11,09%**
- Valor do DAS: **R$ 1.330,80**
- Distribuição:
  - IRPJ: R$ 46,58
  - CSLL: R$ 46,58
  - COFINS: R$ 167,98
  - ...

---

## 📚 BASE LEGAL

- Lei Complementar 123/2006
- Tabelas do Simples Nacional vigentes desde **01/01/2018**
- Alíquotas e percentuais extraídos diretamente da legislação

---

## 💼 APLICÁVEL PARA

- Escritórios de contabilidade
- Profissionais autônomos e MEIs no Simples
- Estudantes de Contabilidade e Programação
- Empresas que desejam simular a carga tributária do Simples

---

## 🧠 IDEIAS FUTURAS

- Upload de planilhas Excel com receitas mês a mês  
- Exportação em PDF ou CSV  
- Adição de Anexo I e II  
- Simulação de exclusão do Simples  
- Análise gráfica da carga tributária por faixa

---

## 🤝 AUTORIA

Feito com 💻 por **Miguel Mantoan Castellani**  
🚀 Transformando Contabilidade com Tecnologia

---
