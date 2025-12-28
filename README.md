# 📊 Analisador de Extrato Bancário – FastAPI (com e sem IA)


Este projeto é uma API em Python usando FastAPI que recebe um extrato bancário em CSV e retorna um resumo dos gastos por categoria.


A ideia principal é mostrar duas formas de resolver o mesmo problema: uma abordagem tradicional (regras) e uma moderna (IA).


---


### 📁 Estrutura do Projeto


Estrutura simples e clara, pensada para facilitar a leitura:


- **versao_sem_ia/** -> main.py
- **versao_com_ia/** -> main.py


---


### 🔹 Versão Sem IA (Regras Fixas)


Nesta versão, a categorização das despesas é feita por regras manuais, usando palavras-chave.


**Exemplos:**
- UBER → Transporte
- IFOOD / MCDONALDS → Alimentação
- NETFLIX → Lazer


**Pontos fortes:** Simples, direto e resultado previsível.


---


### 🤖 Versão Com IA (Gemini)


A API utiliza Inteligência Artificial para interpretar a descrição e definir a categoria mais adequada.


**Destaques:**
- Prompt claro e objetivo.
- Validação da resposta retornada.
- Regras de fallback (segurança) caso a IA falhe.


---


### 📄 Formato do Arquivo CSV


O arquivo enviado deve seguir este padrão:


`Descricao,Valor`
`Uber,13.00`
`McDonalds,81.00`


---


### ▶️ Como Executar o Projeto


**1. Instalar dependências:**

`pip install fastapi uvicorn pandas google-generativeai`


**2. Executar a aplicação:**

`uvicorn main:app --reload`


**3. Acessar no navegador:**

`http://127.0.0.1:8000/docs`


---


### 🎯 Objetivo do Projeto


Desenvolvido para demonstrar construção de APIs, processamento de dados e uso responsável de IA.
