# Escreva um programa que solicite ao usuário para digitar um número. Utilize try-except para assegurar que a entrada seja numérica e utilize if-elif-else para classificar o número como "positivo", "negativo" ou "zero". Adicionalmente, identifique se o número é "par" ou "ímpar".

try:
    numero = int(input("Digite um número: "))
    if numero > 0:
        print("O número é positivo")
    elif numero < 0:
        print("O número é negativo")
    else:
        print("O número é zero")
    
    if numero % 2 == 0:
        print("O número é par")
    else:
        print("O número é impar")
except ValueError:
    print("Entrada inválida!")