📊 Analisador de Extrato Bancário (com e sem IA)

API desenvolvida em Python com FastAPI que recebe um extrato bancário em formato CSV e gera um resumo de gastos por categoria.

O projeto apresenta duas abordagens para resolver o mesmo problema:
uma baseada em regras fixas e outra utilizando Inteligência Artificial (Gemini).

📁 Estrutura do Projeto

Sem-IA/
  └── main.py

Com-IA/
  └── main.py

🔹 Versão Sem IA

Nesta versão, a categorização é feita por meio de regras manuais, utilizando palavras-chave presentes na descrição da despesa.

Exemplos de categorização:

UBER → Transporte
IFOOD / MCDONALDS → Alimentação
NETFLIX → Lazer
Outros → Outros

✅ Simples, rápido e previsível
❌ Pouco flexível para novas descrições

🤖 Versão Com IA

Nesta versão, a categorização é feita utilizando o Gemini (IA), que analisa a descrição da despesa e retorna a categoria mais adequada.

Estratégia utilizada:

Prompt bem definido

Validação da resposta da IA

Regras de fallback em caso de erro ou resposta inválida

✅ Mais flexível e inteligente
A IA é utilizada como apoio, não como lógica principal

📄 Formato do CSV

Descricao,Valor
Uber,R$13
McDonalds,R$81
Cantina do Lucas,R$89
99Pop,R$26

▶️ Como Rodar o Projeto

Instalar as dependências

Sem IA
pip install fastapi uvicorn pandas

Com IA
pip install fastapi uvicorn google-generativeai

🚀 Executar a API

uvicorn main:app --reload

🌐 Acessar a documentação

http://127.0.0.1:8000/docs

🎯 Objetivo do Projeto

Projeto desenvolvido com foco em:

FastAPI

Processamento de arquivos CSV

Boas práticas de backend

Uso consciente de Inteligência Artificial em aplicações reais
