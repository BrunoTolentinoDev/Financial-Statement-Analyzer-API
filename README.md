# Financial Statement Analyzer API

Este projeto foi criado para automatizar a análise de demonstrações financeiras, organizando dados contábeis de forma clara e fácil de interpretar. A ideia é simplificar a leitura de balanços e demonstrativos financeiros, tornando as análises mais ágeis e objetivas.

##  Estrutura do Projeto

- versao_sem_ia  
  Análise financeira baseada em cálculos matemáticos e regras de negócio determinísticas, priorizando precisão e validação objetiva dos dados.

- versao_com_ia  
  Análise financeira utilizando inteligência artificial para interpretar textos financeiros, identificar padrões em balanços e gerar insights sobre a saúde financeira da empresa.

##  Funcionalidades

- Processamento de Balanço Patrimonial  
- Processamento de DRE  
- Cálculo de indicadores financeiros  
- Organização e padronização dos dados  
- Geração de insights financeiros (versão com IA)

##  Tecnologias e Ferramentas

- Linguagem: Python  
- Inteligência Artificial: API de modelo de linguagem  
- Controle de Versão: Git / GitHub  
- Bibliotecas Python para processamento de dados e execução de servidor backend

##  Como Executar o Projeto

git clone https://github.com/BrunoTolentinoDev/Financial-Statement-Analyzer-API.git

cd Financial-Statement-Analyzer-API

python -m venv venv

venv\Scripts\activate

pip install -r requirements.txt

setx OPENAI_API_KEY "sua_chave_de_api_aqui"

cd versao_sem_ia
python main.py

cd versao_com_ia
python main.py

##  Observações

- A versão sem IA utiliza apenas regras de negócio e cálculos financeiros.
- A versão com IA depende da configuração correta da chave de API.
- O projeto pode ser expandido para integração com banco de dados ou frontend.

Desenvolvido por Bruno Tolentino  
GitHub: https://github.com/BrunoTolentinoDev
