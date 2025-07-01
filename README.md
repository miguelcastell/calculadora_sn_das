📊 Calculadora de DAS - Simples Nacional
Projeto em Python com interface Streamlit que calcula:

✅ Alíquota efetiva com base na receita bruta dos últimos 12 meses

✅ Valor do DAS do mês

✅ Distribuição por imposto (IRPJ, CSLL, COFINS, PIS, CPP, ISS)

✅ Cálculo separado por Anexo (III, IV e V)

🛠 Tecnologias
Python 3.10+

Streamlit

JSON (para tabelas de alíquotas e partilhas)

Pandas (opcional, se quiser importar Excel no futuro)

🗂 Estrutura
bash
Copiar
Editar
📁 seu_projeto/
├── main.py                     # Interface Streamlit (front-end)
├── calculo_das.py              # Funções de cálculo (back-end)
├── tabelas_simples.json        # Faixas, alíquotas e parcelas a deduzir
├── distribuicao_impostos.json # Percentuais por imposto (por anexo e faixa)
├── README.md                   # Este arquivo
▶️ Como rodar
bash
Copiar
Editar
pip install streamlit
streamlit run main.py
🧠 Como funciona
O usuário seleciona o anexo (III, IV ou V)

Informa:

Receita bruta acumulada dos últimos 12 meses

Faturamento do mês atual

O sistema calcula:

Faixa correta

Alíquota efetiva

Valor do DAS

Distribuição do DAS por tributo

📌 Observações
Baseado nas regras da LC 123/2006 (vigentes desde 01/01/2018)

Os dados de faixas e percentuais são carregados dinamicamente via .json

Pode ser estendido facilmente para Anexo I e II

💼 Ideal para
Escritórios contábeis

MEIs e pequenas empresas no Simples

Estudantes de Contabilidade e Programação

👨‍💻 Autor
Desenvolvido por Miguel Mantoan Castellani
Projeto acadêmico e prático para automação contábil.

📄 Licença
Este projeto está licenciado sob a MIT License – fique à vontade para usar, melhorar e compartilhar.
