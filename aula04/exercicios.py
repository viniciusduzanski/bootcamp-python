from typing import Dict, Any

# Crie uma lista com os números de 1 a 10 e use um loop para imprimir cada número elevado ao quadrado.

numeros: list = []
for numero in range(1, 11):
    numeros.append(numero ** 2)

print(numeros)


# Dada a lista ["Python", "Java", "C++", "JavaScript"], remova o item "C++" e adicione "Ruby".

linguagens: list = ["Python", "Java", "C++", "JavaScript"]
linguagens.pop(2) # Irá remover C++
linguagens.append("Ruby")

print(linguagens)


# Crie um dicionário para armazenar informações de um livro, incluindo título, autor e ano de publicação. Imprima cada informação.

livro: Dict[str, Any] = {
    "Título": "Game of Thrones",
    "Autor": "Estagiário",
    "Ano": 2005
}

livro_01: dict[str, Any] = { # Se eu usar o dict minúsculo, eu não preciso usar a lib typing, pois o dict é nativo após o Python 3.9
    "Título": "Game of Thrones",
    "Autor": "Estagiário",
    "Ano": 2005
}

livro_02: Dict[str, Any] = {
    "Título": "Jogos Vorazes",
    "Autor": "Teste",
    "Ano": 2010
}


print(livro["Título"]) # Vai imprimir Game of Thrones

lista_de_elementos: list = livro.items() # Criar uma LISTA já preenchida com os dados do meu DICIONÁRIO
for elemento in livro:
    print(elemento)


# Lista de dicionários
lista_de_livros = []
lista_de_livros.append(livro_01)
lista_de_livros.append(livro_02)
print(lista_de_livros)

# Dicionário de dicionário
lista_de_livros_usando_dict: dict = {
    "livro_01": {
    "Título": "Game of Thrones",
    "Autor": "Estagiário",
    "Ano": 2005},
    
    "livro_02": {
    "Título": "Jogos Vorazes",
    "Autor": "Teste",
    "Ano": 2010}
}

# Quando trabalhamos com APIs, geralmente trabalhamos com dicionário de dicionário

print(lista_de_livros_usando_dict["livro_01"]) # Imprimir todo o primeiro dicionário


print(lista_de_livros_usando_dict["livro_01"]["Título"]) # Imprimir somente o Título do Livro 01
