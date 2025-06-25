from etl import *

path_arquivo = "aula07/vendas.csv"

lista_de_produtos = ler_csv(path_arquivo) # Retorna uma lista
produtos_nao_entregues = filtrar_produtos_nao_entregues(lista_de_produtos) # Pego a lista e passo para esse método
valor_dos_produtos_nao_entregues = somar_valores_dos_produtos(produtos_nao_entregues)
print(valor_dos_produtos_nao_entregues)
