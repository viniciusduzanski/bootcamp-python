import json

# Sem tipagem:
idade = 30
altura = 1.75
nome = "Alice"
is_estudante = True

# Com tipagem (Type Hint):
idade: int = 30
altura: float = 1.75
nome: str = "Alice"
estudante: bool = True

# Atenção:

idade = input("Digite sua idade: ")
print(type(idade))

idade_tipada: int = input("Digite sua idade: ")
print(type(idade_tipada))

# Hint na realidade é uma dica, não quer dizer que ele deixou a variável como int no exemplo acima.


# ------------------------------ LISTAS ------------------------------ #

produto: str = "sapato"
produto_2: str = "camiseta"
produto_3: str = "videogame"

produtos: list = []

produtos.append(produto) # Adiciona esse item na lista
produtos.append(produto_2)
produtos.append(produto_3)
produtos.pop() # Retira o último produto da lista porque não especifiquei o índice dentro do pop, o pop é mais performático
produtos.remove(produto_2) # Retira especificando

print(produtos)

# ------------------------------ DICIONÁRIOS ------------------------------ #

lista = ["Sapato", 39, 10.38, True]

# Criando um dicionário
produto_01 = {
    "nome": "Sapato",
    "quantidade": 39,
    "preco": 10.38,
    "disponibilidade": True
}

# Criando outro dicionário
produto_02 = {
    "nome": "Televisao",
    "quantidade": 10,
    "preco": 300.50,
    "disponibilidade": False
}

carrinho: list = []
carrinho.append(produto_01) # Adicionando o dicionário produto_01 na lista
carrinho.append(produto_02) # Adicionando o dicionário produto_02 na lista

print(carrinho) # Vou ter uma lista de dicionários

# Convertendo para JSON

carrinho_json = json.dumps(carrinho)
print(carrinho_json)

# Note que uma das diferenças é que na lista é True e no JSON é true