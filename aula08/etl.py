import pandas as pd
import os
import glob

# Uma função de extract que lê e consolida os JSONs

def extrair_dados_e_consolidar(pasta: str) -> pd.DataFrame:
    arquivos_json = glob.glob(os.path.join(pasta, '*.json')) # Vai criar uma lista de tudo que tem de JSON nesse diretório de pasta
    df_list = [pd.read_json(arquivo) for arquivo in arquivos_json] # Vai ler cada arquivo JSON e criar uma lista de DataFrames
    # A linha abaixo vai concatenar os DataFrames. Ex: Dataframe1 com 100 linhas, Dataframe2 com 200 linhas, vai gerar um novo DataFrame único com 300 linhas
    df_total = pd.concat(df_list, ignore_index=True) # O ignore_index vai ignorar os índices originais e criar novos sequenciais (0, 1, 2...)
    return df_total


# Uma função que transforma

def calcular_kpi_de_total_de_vendas(df: pd.DataFrame) -> pd.DataFrame:
    df["Total"] = df["Quantidade"] * df["Venda"] # Aqui eu vou criar uma nova coluna chamada Total que é resultado da multiplicação
    return df


# Uma função que dá load em csv ou parquet

def carregar_dados(df: pd.DataFrame, formato_de_saida: list):
    """
    Parâmetro que vai ser ou "csv" ou "parquet" ou "os dois"
    """
    for formato in formato_de_saida:
        if formato == 'csv':
            df.to_csv("dados.csv")

        if formato == 'parquet':
            df.to_parquet("dados.parquet")


def pipeline_calcular_kpi_de_vendas_consolidado(pasta: str, formato_de_saida: list):
    data_frame = extrair_dados_e_consolidar(pasta)
    data_frame_calculado = calcular_kpi_de_total_de_vendas(data_frame) # Aqui já estou com a coluna Total adicionado no meu DataFrame
    carregar_dados(data_frame_calculado, formato_de_saida)
