# Implementação do algoritmo de ordenação por seleção
lista = [64, 34, 25, 12, 22, 11, 90]

def ordenar_lista_de_numeros(numeros: list) -> list:
    lista_numeros = numeros.copy()
    
    for i in range(len(lista_numeros)):
        for j in range(i+1, len(lista_numeros)):
            if lista_numeros[i] > lista_numeros[j]:
                lista_numeros[i], lista_numeros[j] = lista_numeros[j], lista_numeros[i]
                
    return lista_numeros

# Ordenando a lista
nova_lista = ordenar_lista_de_numeros(lista)

# Aqui eu desenvolvi um módulo, posso reutilizar ele. Vamos usar na classe data_science.py

# Trabalhando com parâmetros com valores default:
def saudacao(nome: str, idade: int = 30) -> str:
    return f"Olá, {nome}, você tem {idade} anos."

# Se eu não enviar um valor para idade, ela vai ser considerada como 30.