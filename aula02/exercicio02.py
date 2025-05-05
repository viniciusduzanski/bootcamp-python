# Crie um programa que verifica se uma palavra ou frase é um palíndromo (lê-se igualmente de trás para frente, desconsiderando espaços e pontuações). Utilize try-except para garantir que a entrada seja uma string. Dica: Utilize a função isinstance() para verificar o tipo da entrada.

entrada = input("Digite uma palavra ou frase: ")

if isinstance(entrada.isalpha, str): # isalpha retorna se toda a entrada contém apenas letras e espaços
    formatado = entrada.replace(" ", "").lower()
    if formatado == formatado[::-1]:
        print("É um palíndromo.")
    else:
        print("Não é um palíndromo")
else:
    print("Insira uma entrada válida, sendo palavra ou frase")
