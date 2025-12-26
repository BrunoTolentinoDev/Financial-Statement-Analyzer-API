import pandas as pd
from fastapi import FastAPI, UploadFile, File, HTTPException

# inicializa a aplicação FastAPI
app = FastAPI()

# dicionário que mapeia palavras chave para categorias de gastos
CATEGORIAS = {
    'UBER': 'Transporte',
    'IFOOD': 'Alimentação',
    'MCDONALDS': 'Alimentação',
    'NETFLIX': 'Lazer',
    'AMAZON': 'Compras'
}

def processar_extrato(caminho_arquivo: str) -> dict:
    """
    Lê um arquivo CSV de extrato bancário, categoriza os gastos
    com base em regras (dicionário) e retorna o total por categoria.
    """
    # lê o arquivo CSV usando pandas
    df = pd.read_csv(caminho_arquivo)

    # Verifica se o arquivo possui as colunas obrigatórias
    if 'Descricao' not in df.columns or 'Valor' not in df.columns:
        raise ValueError("Arquivo inválido. Colunas esperadas: Descricao, Valor")

    # Remove símbolos  e converte os valores para float
    df['Valor'] = df['Valor'].replace('[R$,]', '', regex=True).astype(float)

    def categorizar(descricao):
        """
        Recebe a descrição da transação e retorna a categoria correspondente
        com base nas palavras-chave definidas no dicionário.
        """
        descricao = str(descricao).upper()
        for chave, categoria in CATEGORIAS.items():
            if chave in descricao:
                return categoria
        return 'Outros'

    # Aplica a função de categorização em cada descrição do extrato
    df['Categoria'] = df['Descricao'].apply(categorizar)

    # Agrupa os valores por categoria e retorna um dicionário
    return df.groupby('Categoria')['Valor'].sum().to_dict()

@app.post("/upload-extrato/")
async def upload_file(file: UploadFile = File(...)):
    """
    Endpoint que recebe um arquivo CSV do usuário,
    processa o extrato e retorna o resumo dos gastos.
    """
    # Valida se o arquivo enviado é do tipo CSV
    if not file.filename.endswith('.csv'):
        raise HTTPException(status_code=400, detail="Envie um arquivo CSV")

    # Salva o arquivo temporariamente no servidor
    with open("temp.csv", "wb") as f:
        f.write(await file.read())

    # Processa o extrato bancário
    dados = processar_extrato("temp.csv")

    # Retorna o resultado da categorização
    return {
        "status": "sucesso",
        "resumo_gastos": dados
    }
