import pandas as pd

class CsvProcessor:
    def __init__(self, file_path: str):
        self.file_path = file_path
        self.df = None # Quero que o DataFrame fique salvo na minha classe, quero que sempre seja associado a essa classe, para eu não ter que ficar transitando entre uma função e outra
        self.df_filtrado = None

    
    def carregar_csv(self): # Se eu recebo o self, eu recebo tudo que já foi inicializado no método init
        self.df = pd.read_csv(self.file_path)
        
    
    def filtrar_por(self, colunas: [], atributos: []):
        if len(colunas) != len(atributos):
            raise ValueError("Não tem o mesmo número de colunas e atributos")
        
        if len(colunas) == 0:
            return self.df
        
        coluna_atual = colunas[0]
        atributo_atual = atributos[0]

        df_filtrado = self.df[self.df[coluna_atual] == atributo_atual]
        
        if len(colunas) == 1: # Estou no meu último filtro, não preciso chamar novamente a função pois o filtro já foi aplicado no comando acima
            return df_filtrado
        else:
            return self.filtrar_por(colunas[1:], atributos[1:]) # Recursividade, vou passar como parâmetro já da posição 1

        self.df_filtrado = self.df[self.df[coluna] == atributo] # Aqui eu estou atribuindo a um "atributo" da minha classe. Então qualquer operação que eu fizer após executar esse método, vai ser feita no DataFrame filtrado
        return self.df_filtrado


    """ def sub_filtro(self, coluna, atributo):
        return self.df_filtrado[self.df_filtrado[coluna] == atributo]
    
        

arquivo_csv = "aula11-15/aula12/exemplo.csv"
filtro = "estado"
limite = "SP"

arquivo_csv_processado = CsvProcessor(arquivo_csv)
arquivo_csv_processado.carregar_csv()
print(arquivo_csv_processado.filtrar_por(filtro, limite)) # Aqui eu usei o método filtrar com o estado SP. A partir dessa execução desse método, o DataFrame da minha classe só vai ter SP
print(arquivo_csv_processado.sub_filtro("preço", "10,50")) # Como na linha anterior eu filtrei só pelo SP, aqui eu vou ter só SP no meu DataFrame e vou filtrar pelo preço
 """
