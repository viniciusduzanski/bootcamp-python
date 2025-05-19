import csv

caminho_do_arquivo: str = "aula04/exemplo.csv"

arquivo_csv: list = []

with open(file=caminho_do_arquivo, mode="r", encoding='utf-8') as arquivo:
    leitor_csv: csv.DictReader = csv.DictReader(arquivo) # Vai ler e retorna cada linha como um dicionário
    
    for linha in leitor_csv:
        arquivo_csv.append(linha) # Para cada linha do dicionário, adicione na minha lista. Com isso, vamos ter uma lista de dicionários

print(arquivo_csv)
