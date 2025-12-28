# 📊 Analisador de Extrato Bancário – FastAPI (com e sem IA)

&nbsp;

Este projeto é uma API em Python usando FastAPI que recebe um extrato bancário em CSV e retorna um resumo dos gastos por categoria.

&nbsp;

A ideia principal é mostrar duas formas de resolver o mesmo problema: uma abordagem tradicional (regras) e uma moderna (IA).

&nbsp;

---

&nbsp;

## 📁 Estrutura do Projeto

&nbsp;

Estrutura simples e clara, pensada para facilitar a leitura:

- **versao_sem_ia/** -> main.py
- **versao_com_ia/** -> main.py

&nbsp;

---

&nbsp;

## 🔹 Versão Sem IA (Regras Fixas)

&nbsp;

Nesta versão, a categorização das despesas é feita por regras manuais, usando palavras-chave.

**Exemplos:**
- UBER → Transporte
- IFOOD / MCDONALDS → Alimentação
- NETFLIX → Lazer

&nbsp;

**Pontos fortes:** Simples, direto e resultado previsível.

&nbsp;

---

&nbsp;

## 🤖 Versão Com IA (Gemini)

&nbsp;

A API utiliza Inteligência Artificial para interpretar a descrição e definir a categoria mais adequada.

&nbsp;

**Destaques:**
- Prompt claro e objetivo.
- Validação da resposta retornada.
- Regras de fallback (segurança) caso a IA falhe.

&nbsp;

---

&nbsp;

## 📄 Formato do Arquivo CSV

&nbsp;

O arquivo enviado deve seguir este padrão:

`Descricao,Valor`  
`Uber,13.00`  
`McDonalds,81.00`

&nbsp;

---

&nbsp;

## ▶️ Como Executar o Projeto

&nbsp;

**1. Instalar dependências:**
```bash
pip install fastapi uvicorn pandas google-generativeai
