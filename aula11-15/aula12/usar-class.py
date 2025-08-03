from src.interface.classes.csv_class import CsvProcessor

arquivo_csv = "aula11-15/aula12/exemplo.csv"
filtro = "estado"
limite = "SP"

arquivo_csv_processado = CsvProcessor(arquivo_csv)
arquivo_csv_processado.carregar_csv()
print(arquivo_csv_processado.filtrar_por(['estado', 'preço'], ['SP', '10,50']))