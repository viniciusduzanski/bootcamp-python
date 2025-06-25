from etl import *

path_arquivo = "aula07/vendas.csv"

lista_de_produtos = ler_csv(path_arquivo) # Retorna uma lista
produtos_nao_entregues = filtrar_produtos_nao_entregues(lista_de_produtos) # Pego a lista e passo para esse método
print(produtos_nao_entregues)
