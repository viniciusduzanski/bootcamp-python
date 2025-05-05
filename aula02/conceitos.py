"""
Tipos de dados:
Inteiros (int): Representam números inteiros.
Ponto Flutuante (float): Representam números reais.
Strings (str): Representam sequências de caracteres.
Booleanos (bool): Representam valores verdadeiros (True) ou falsos (False).

1. Inteiros (int)
Métodos e operações:
+ (adição)
- (subtração)
* (multiplicação)
// (divisão inteira)
% (módulo - resto da divisão)

2. Números de Ponto Flutuante (float)
Métodos e operações:
+ (adição)
- (subtração)
* (multiplicação)
/ (divisão)
** (potenciação)

3. Strings (str)
Métodos e operações:
.upper() (converte para maiúsculas)
.lower() (converte para minúsculas)
.strip() (remove espaços em branco no início e no final)
.split(sep) (divide a string em uma lista, utilizando sep como delimitador)
+ (concatenação de strings)

4. Booleanos (bool)
Operações lógicas:
and (E lógico)
or (OU lógico)
not (NÃO lógico)
== (igualdade)
!= (diferença)
"""

nome_aluno = "Vinícius"

# Verificando o tipo da variável
print(type(nome_aluno))
print(type("Vinícius"))

# Converter para maiúsculas
print(nome_aluno.upper())

# Converter para minúsculas
print(nome_aluno.lower())

# Remover os espaços em branco no começo e no final da string
nome_com_espacos = "   Teste com espaços   "
print(nome_aluno.strip())

# Dividir a string com um delimitador, vai criar uma lista com o resultado
nome_delimitador = "viniciusduzanski@gmail.com"
print(nome_delimitador.split("@"))


# Exemplo com TypeError

try:
    resultado = len(3) # Exception porque len é um método para strings
    print(resultado)
except TypeError as e:
    print(e)
else:
    print("Tudo ocorreu bem")
finally:
    print("O finally sempre será executado")


# isistance

numero = int(input("Insira um número: "))
if isinstance(numero, int): # Verifica se minha variável numero é do tipo int
    print("A variável é um inteiro")
else:
    print("A variável não é um inteiro")

# if, else, elif

IDADE_MINIMA_PARA_DIRIGIR = 18
IDADE_PARA_TIRAR_CARTEIRA = 18

if IDADE_MINIMA_PARA_DIRIGIR < 18:
    print("Não pode dirigir")
elif IDADE_PARA_TIRAR_CARTEIRA == 18:
    print("Pode tirar a carteira esse ano")
else:
    print("Pode dirigir")
