📊 Analisador de Extrato Bancário (com e sem IA)

API em Python com FastAPI que recebe um extrato bancário em CSV e gera um resumo de gastos por categoria.

O projeto possui duas abordagens para resolver o mesmo problema:
uma usando regras fixas e outra utilizando Inteligência Artificial (Gemini).

📁 Estrutura

Sem-IA/
main.py

Com-IA/
main.py

  Versão Sem IA

A categorização é feita com regras manuais, usando palavras-chave.

Exemplos:

UBER → Transporte

IFOOD / MCDONALDS → Alimentação

NETFLIX → Lazer

Outros → Outros

✅ Simples, rápido e previsível
❌ Pouco flexível para novas descrições

 Versão Com IA

A categorização é feita com Gemini (IA) a partir da descrição da despesa.

Prompt bem definido

Validação da resposta da IA

Regras de fallback em caso de erro

✅ Mais flexível e inteligente
  A IA é usada como apoio, não como lógica principal

 Formato do CSV

Descricao,Valor
UBER VIAGEM,R$ 25,90
MCDONALDS,R$ 42,50

 Como rodar

Instalar dependências:

Sem IA
pip install fastapi uvicorn pandas

Com IA
pip install fastapi uvicorn google-generativeai

Rodar a API:
uvicorn main:app --reload

Acessar:
http://127.0.0.1:8000/docs

🎯 Objetivo

Projeto focado em:

FastAPI

Processamento de CSV

Boas práticas de backend

Uso consciente de IA em aplicações reais
