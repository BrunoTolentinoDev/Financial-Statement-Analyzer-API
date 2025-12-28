📊 Analisador de Extrato Bancário – FastAPI (com e sem IA)

Este projeto é uma API em Python usando FastAPI que recebe um extrato bancário em CSV e retorna um resumo dos gastos por categoria.

A ideia principal é mostrar duas formas de resolver o mesmo problema:

uma abordagem tradicional, baseada em regras

uma abordagem moderna, utilizando Inteligência Artificial como apoio

📁 Estrutura do Projeto (revisada)

Estrutura simples e clara, pensada para facilitar a leitura de quem avalia o repositório:

Sem-IA/
└── main.py

Com-IA/
└── main.py

Cada pasta representa uma abordagem diferente para o mesmo problema.

🔹 Versão Sem IA (Regras Fixas)

Nesta versão, a categorização das despesas é feita por regras manuais, usando palavras-chave presentes na descrição.

Exemplos:

UBER → Transporte

IFOOD / MCDONALDS → Alimentação

NETFLIX → Lazer

Qualquer outro caso → Outros

Pontos fortes:

Código simples e direto

Fácil de entender e manter

Resultado previsível

Limitação:

Pouco flexível para descrições novas ou inesperadas

🤖 Versão Com IA (Gemini)

Nesta versão, a API utiliza Inteligência Artificial (Gemini) para interpretar a descrição da despesa e definir a categoria mais adequada.

A IA não é usada como “mágica”, mas sim de forma controlada:

prompt claro e objetivo

validação da resposta retornada

regras de fallback caso a IA falhe

Resultado:

Mais flexibilidade

Melhor adaptação a descrições reais de extratos bancários

Uso consciente de IA, sem perder controle da lógica

📄 Formato do Arquivo CSV

O arquivo enviado para a API deve seguir este padrão:

Descricao,Valor
Uber,R$13
McDonalds,R$81
Cantina do Lucas,R$89
99Pop,R$26

▶️ Como Executar o Projeto

Instalar dependências:

Versão Sem IA
pip install fastapi uvicorn pandas

Versão Com IA
pip install fastapi uvicorn google-generativeai

Executar a aplicação:
uvicorn main:app --reload

Acessar no navegador:
http://127.0.0.1:8000/docs

🎯 Objetivo do Projeto

Este projeto foi desenvolvido para praticar e demonstrar:

construção de APIs com FastAPI

processamento de arquivos CSV

organização e clareza de código

uso responsável de Inteligência Artificial em aplicações reais
