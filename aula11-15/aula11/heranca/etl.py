import pandas as pd

# Aqui eu estou definindo o "modelo", o esqueleto da classe para que ela possa ser implementada de maneira personalizada conforme necessidade, como acontece no classe class ETLCSV(ETLProcess):
class ETLProcess:
    def __init__(self, fonte_dados):
        self.fonte_dados = fonte_dados

    def extrair_dados(self):
        raise NotImplementedError("Método extrair_dados deve ser implementado nas classes filhas.")

    def transformar_dados(self, dados):
        raise NotImplementedError("Método transformar_dados deve ser implementado nas classes filhas.")

    def carregar_dados(self, dados_transformados):
        raise NotImplementedError("Método carregar_dados deve ser implementado nas classes filhas.")

    def executar_etl(self):
        dados_extraidos = self.extrair_dados()
        dados_transformados = self.transformar_dados(dados_extraidos)
        self.carregar_dados(dados_transformados)

# Aqui estou "implementando" a classe com os comportamentos necessários para CSV
class ETLCSV(ETLProcess):
    def extrair_dados(self):
        return pd.read_csv(self.fonte_dados)

    def transformar_dados(self, dados):
        # Exemplo simples de transformação: converter todas as letras em maiúsculas
        return dados.applymap(lambda x: x.upper() if isinstance(x, str) else x)

    def carregar_dados(self, dados_transformados):
        # Aqui você pode implementar a lógica para carregar os dados transformados para onde desejar
        print("Dados transformados:")
        print(dados_transformados)


# Inicialmente só tinha o ETLCSV, com uma nova necessidade, apenas venho e crio uma nova classe
class ETLExcel(ETLProcess):
    def __init__(self, fonte_dados):
        super().__init__(fonte_dados) # super -> Vou executar o mesmo que está definido na classe mãe
    
    def extrair_dados(self):
        print("all")
        return super().extrair_dados() # super -> Vou executar o mesmo que está definido na classe mãe

    def transformar_dados(self, dados):
        return "Dados transformados"


# Exemplo de uso
if __name__ == "__main__":
    fonte_csv = 'dados.csv'  # Substitua 'dados.csv' pelo caminho do seu arquivo CSV
    etl_csv = ETLCSV(fonte_csv)
    etl_csv.executar_etl()