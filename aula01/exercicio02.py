# Crie um programa onde o usuário digite dois valores e apareça a soma

"""
By default, when you don't specify the variable type, Python infers it based on the assigned value.

We can't do this if we want to sum numbers:
print(input("Digite um valor: ") + input("Digite outro valor: "))
"""

# We can code like this, without variables:
print(int(input("Digite um valor: ")) + int(input("Digite outro valor: ")))

#With variables:
numero1 = int(input("Digite um valor: "))
numero2 = int(input("Digite outro valor: "))
soma = numero1 + numero2
print(soma)

print(type(numero1))

#Tipos primitivos:

numero = 10 #int
numero_decimal = 20.32 #float
nome_de_usuario = "Vinícius" #str
booleano = True #bool