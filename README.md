Calculadora DAS - Simples Nacional
Uma aplicação web feita com Python + Streamlit para calcular o valor do DAS (Documento de Arrecadação do Simples Nacional) de empresas enquadradas nos Anexos III, IV e V da LC 123/2006.



🚀 Funcionalidades
✅ Cálculo da alíquota efetiva e valor do DAS com base no faturamento e receita acumulada.
✅ Suporte aos Anexos III, IV e V com base nas faixas, alíquotas e parcelas a deduzir da LC 123/2006.
✅ Tratamento de retenção de ISS com cálculo ajustado.
✅ Visualização da distribuição dos tributos por percentual.
✅ Interface amigável e responsiva com Streamlit.
✅ Modularização com arquivos externos .json para fácil manutenção.

📁 Estrutura do Projeto
bash
Copiar
Editar
calculadora_das_completa/
├── main.py                      # Arquivo principal (interface Streamlit)
├── layout.py                    # Layout e exibição de cabeçalho/logo
├── calculo_das.py               # Funções de cálculo do DAS
├── tabelas_simples.json         # Tabelas de faixas, alíquotas e deduções
├── distribuicao_impostos.json  # Distribuição dos tributos por faixa e anexo
├── logo.png                     # Logo da aplicação
└── .streamlit/
    └── secrets.toml             # (opcional) credenciais
📊 Como funciona o cálculo
A fórmula utilizada segue o art. 18 da LC 123/2006:

java
Copiar
Editar
Alíquota efetiva = [(RBT12 x Alíquota nominal) - Parcela a deduzir] / RBT12
💡 RBT12 = Receita Bruta dos Últimos 12 Meses
💰 DAS = Faturamento do mês x Alíquota efetiva

🔧 Como rodar localmente
Clone o repositório:

bash
Copiar
Editar
git clone https://github.com/seu-usuario/calculadora-das.git
cd calculadora-das
Instale as dependências:

bash
Copiar
Editar
pip install streamlit
Rode o app:

bash
Copiar
Editar
streamlit run main.py
🌐 Deploy na Web
Você pode publicar seu app gratuitamente no Streamlit Cloud em poucos cliques.

🛠 Exemplo de entrada
Faturamento do mês: 25.000,00

Receita 12 meses: 250.000,00

Anexo: IV

ISS retido? ✅

Retorna:

Alíquota efetiva com ISS retido

Valor total do DAS

Distribuição dos impostos (IRPJ, CSLL, PIS, etc.)

👨‍💻 Autor
Desenvolvido por Miguel Mantoan Castellani
Projeto acadêmico e prático para automação contábil.

📄 Licença
Este projeto está licenciado sob a MIT License – fique à vontade para usar, melhorar e compartilhar.
