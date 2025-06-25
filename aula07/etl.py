import csv

path_arquivo = "aula07/vendas.csv"

def ler_csv(nome_do_arquivo_csv: str) -> list[dict]:
    """
    Função que lê um arquivo csv e retorna uma lista de dicionários
    """
    lista = []
    with open(nome_do_arquivo_csv, mode="r", encoding='utf-8') as arquivo:
        leitor = csv.DictReader(arquivo)
        for linha in leitor:
            lista.append(linha)
    return lista


def filtrar_produtos_nao_entregues(lista: list[dict]) -> list[dict]:
    """
    Função que filtra produtos onde entrega = False
    """
    lista_com_produtos_filtrados = []
    for produto in lista:
        if produto.get("entregue") == "False": # Na lista de dicionários, estou pegando a chave 'entregue' e comparando se é True
            lista_com_produtos_filtrados.append(produto)
    return lista_com_produtos_filtrados


def somar_valores_dos_produtos(lista_com_produtos_filtrados: list[dict]) -> float:
    """
    Soma todos os valores dos produtos que estão na lista
    """
    valor_total = 0
    for produto in lista_com_produtos_filtrados:
        valor_total += float(produto.get("price")) # Preciso fazer o casting porque sempre que eu usar csv.DictReader(arquivo) ele vai ler como string, independente se no csv está como número
    return valor_total
