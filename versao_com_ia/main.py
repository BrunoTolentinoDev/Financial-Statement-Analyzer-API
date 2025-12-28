from fastapi import FastAPI, UploadFile, File
import csv
import io
import os
import re
from google import genai

GEMINI_API_KEY = "GEMINI_API_KEY"

client = genai.Client(api_key=GEMINI_API_KEY)
model = "gemini-1.5-flash"

app = FastAPI()

def limpar_valor(valor: str) -> float:
    # Ajusta o formato do dinheiro para conseguir somar
    valor = valor.replace("R$", "").replace(" ", "").replace(",", ".")
    return float(valor)

def categoria_fallback(descricao: str) -> str:
    # Regras simples caso a IA falhe
    desc = descricao.lower()

    if any(p in desc for p in ["uber", "99"]):
        return "Transporte"

    if any(p in desc for p in ["mcdonald", "cantina", "restaurante", "lanch"]):
        return "Alimentação"

    return "Outros"

def categorizar_com_ia(descricao: str) -> str:
    # pergunta para o ia qual a melhor categoria
    prompt = f"""
Classifique a despesa abaixo em UMA das categorias:
- Alimentação
- Transporte
- Moradia
- Lazer
- Saúde
- Outros

Responda apenas com o nome da categoria.

Despesa: "{descricao}"
"""

    try:
        response = client.models.generate_content(
            model=model,
            contents=prompt
        )

        categoria = response.text.strip()

        categorias_validas = [
            "Alimentação",
            "Transporte",
            "Moradia",
            "Lazer",
            "Saúde",
            "Outros"
        ]

        if categoria in categorias_validas:
            return categoria

        return categoria_fallback(descricao)

    except Exception:
        return categoria_fallback(descricao)

@app.post("/upload-extrato/")
async def upload_extrato(file: UploadFile = File(...)):
    # le o arquivo enviado pelo usuário
    conteudo = await file.read()
    texto = conteudo.decode("utf-8")

    reader = csv.DictReader(io.StringIO(texto))

    resumo = {
        "Alimentação": 0.0,
        "Transporte": 0.0,
        "Moradia": 0.0,
        "Lazer": 0.0,
        "Saúde": 0.0,
        "Outros": 0.0
    }

    detalhes = []

    for linha in reader:
        # pega a descrição e o valor de cada linha do CSV
        descricao = linha["Descricao"]
        valor = limpar_valor(linha["Valor"])

        # identifica a categoria usando a IA
        categoria = categorizar_com_ia(descricao)

        resumo[categoria] += valor

        detalhes.append({
            "descricao": descricao,
            "valor": valor,
            "categoria": categoria
        })

    # entrega o resultado final com o resumo e os itens
    return {
        "status": "sucesso",
        "resumo_gastos": resumo,
        "detalhamento": detalhes
    }