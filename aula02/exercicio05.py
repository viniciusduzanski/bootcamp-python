# Crie um script que solicite ao usuário uma lista de números separados por vírgula. O programa deve converter a string de entrada em uma lista de números inteiros. Utilize try-except para tratar a conversão de cada número e validar que cada elemento da lista convertida é um inteiro. Se a conversão falhar ou um elemento não for um inteiro, imprima uma mensagem de erro. Se a conversão for bem-sucedida para todos os elementos, imprima a lista de inteiros.

entrada_lista = input("Digite uma lista de números separados por vírgula: ")
numeros_str = entrada_lista.split(",") # O split separa e automaticamente coloca em uma lista
numeros_int = []

try:
    for numero in numeros_str:
        numeros_int.append(int(numero.strip()))
    print("Lista de inteiros: ", numeros_int)
except ValueError:
    print("Certifique-se se os números são inteiros!")