from typing import List

# 1. Calcular média de valores em uma lista

def calcular_media(valores: List[float]) -> List[float]:
    return sum(valores) / len(valores)

print(calcular_media([10, 20, 30, 40]))

# ---------------------------------------------------- #

# 2. Filtrar dados acima de um limite

def filtrar_dados_acima_do_limite(valores: List[float], limite: float) -> List[float]:
    resultado: List[float] = []
    for x in valores:
        if x <= limite:
            resultado.append(x)
    return resultado

print(filtrar_dados_acima_do_limite([25.10, 56, 90, 150], 100))

# Usando list comprehension:

def filtrar_dados_acima_do_limite_list_comprehension(valores: List[float], limite: float) -> List[float]:
    return [x for x in valores if x <= limite]

print(filtrar_dados_acima_do_limite_list_comprehension([33.33, 75, 90, 150], 100))

# ---------------------------------------------------- #

# 3. Contar Valores Únicos em uma Lista

def contar_valores_unicos(lista: List[int]) -> int:
    return len(set(lista)) # set da lista vai remover os dados duplicados. Um set é não ordenado, sem dados duplicados e não indexável.

print(contar_valores_unicos([10, 20, 25, 25, 60]))
