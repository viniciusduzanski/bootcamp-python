# Desenvolva uma calculadora simples que aceite duas entradas numéricas e um operador (+, -, *, /) do usuário. Use try-except para lidar com divisões por zero e entradas não numéricas. Utilize if-elif-else para realizar a operação matemática baseada no operador fornecido. Imprima o resultado ou uma mensagem de erro apropriada.

try:
    numero1 = int(input("Digite o primeiro número: "))
    numero2 = int(input("Digite o segundo número: "))
    operacao = input("Digite a operação a ser realizada, podendo ser +, -, * ou /: ")

    if operacao == '+':
        resultado = numero1 + numero2
    elif operacao == '-':
        resultado = numero1 - numero2
    elif operacao == '*':
        resultado = numero1 * numero2
    elif operacao == '/':
        resultado = numero1 / numero2
    else:
        print("Operador inválido")
    print(f"O resultado de {numero1} {operacao} {numero2} é: {resultado}")
except ValueError:
    print("Entrada inválida!")
    