valor_1 = 10
valor_2 = 15

valor_3 = 25
valor_4 = 50


# Estrutura básica de uma função:
def soma(valor1_para_somar: float, valor2_para_somar: float) -> float:
    """
    Uma função simples de soma de valores do tipo float que retorna float
    """
    resultado_da_soma = valor1_para_somar + valor2_para_somar
    return resultado_da_soma

resultado_primeira_soma = soma(valor_1, valor_2)
resultado_segunda_soma = soma(valor_3, valor_4)

print(resultado_primeira_soma)
print(resultado_segunda_soma)

# Utilizando valor padrão de argumento:
# Vai usar 10 para o argumento valor2_para_somar caso nenhum valor seja passado na chamada da função
def soma_argumento_padrao(valor1_para_somar: float, valor2_para_somar: float = 10) -> float:
    """
    Uma função simples de soma de valores do tipo float que retorna float
    """
    resultado_da_soma = valor1_para_somar + valor2_para_somar
    return resultado_da_soma

resultado1 = soma_argumento_padrao(valor_3) # Aqui ele vai usar o valor padrão 10 para o segundo valor
print(resultado1)
