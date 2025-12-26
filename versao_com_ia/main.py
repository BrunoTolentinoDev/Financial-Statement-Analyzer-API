import pandas as pd
from fastapi import FastAPI, UploadFile, File, HTTPException
from io import StringIO
import google.generativeai as genai
import os

# API para analisar extratos bancários e categorizar gastos usando IA
app = FastAPI(
    title="API de Análise de Gastos",
    description="API para processar extratos bancários e categorizar gastos usando IA (Gemini)",
    version="1.0.0"
)

# le a chave da API do Gemini a partir da variável de ambiente
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# Impede a aplicação de rodar sem a chave configurada
if not GEMINI_API_KEY:
    raise RuntimeError(
        "Variável de ambiente GEMINI_API_KEY não encontrada. "
        "Configure sua chave da API do Gemini antes de rodar."
    )

# Configura o acesso à API do Gemini
genai.configure(api_key=GEMINI_API_KEY)

# modelo de IA usado para classificar os gastos
model = genai.GenerativeModel("gemini-1.5-flash")

# Categorias que a IA pode retornar
CATEGORIAS_PERMITIDAS = [
    "Transporte",
    "Alimentação",
    "Moradia",
    "Lazer",
    "Compras",
    "Saúde",
    "Outros"
]

# Usa a IA para identificar a categoria do gasto pela descrição
def categorizar_com_ia(descricao: str) -> str:
    # Prompt simples enviado para a IA
    prompt = f"""
Classifique o gasto abaixo em apenas UMA das categorias:
{", ".join(CATEGORIAS_PERMITIDAS)}

Gasto: "{descricao}"

Responda SOMENTE with o nome da categoria.
"""

    try:
        response = model.generate_content(prompt)
        categoria = response.text.strip()

        # Garante que a resposta seja uma categoria válida
        if categoria not in CATEGORIAS_PERMITIDAS:
            return "Outros"

        return categoria

    except Exception:
        # Se a IA falhar, classifica como "Outros"
        return "Outros"

# Processa o extrato bancário enviado pelo usuário
def processar_extrato(conteudo_csv: str) -> dict:
    try:
        df = pd.read_csv(StringIO(conteudo_csv))
    except Exception:
        raise ValueError("Erro ao ler o arquivo CSV")

    # Verifica se o CSV tem as colunas necessárias
    if "Descricao" not in df.columns or "Valor" not in df.columns:
        raise ValueError("Colunas obrigatórias: Descricao, Valor")

    try:
        # Remove símbolos e converte os valores para número
        df["Valor"] = (
            df["Valor"]
            .replace("[R$,]", "", regex=True)
            .astype(float)
        )
    except Exception:
        raise ValueError("Valores inválidos na coluna 'Valor'")

    # Classifica cada gasto usando a IA
    df["Categoria"] = df["Descricao"].apply(categorizar_com_ia)

    # soma os valores por categoria
    return df.groupby("Categoria")["Valor"].sum().to_dict()

# Endpoint para upload do extrato bancário
@app.post("/upload-extrato/")
async def upload_extrato(file: UploadFile = File(...)):
    # verifica se o arquivo enviado é CSV
    if not file.filename.lower().endswith(".csv"):
        raise HTTPException(
            status_code=400,
            detail="Envie um arquivo no formato CSV"
        )

    # Lê o conteúdo do arquivo
    conteudo = await file.read()

    try:
        resumo = processar_extrato(conteudo.decode("utf-8"))
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

    # retorna o resumo dos gastos
    return {
        "status": "sucesso",
        "resumo_gastos": resumo
    }
