import pandas as pd

df = pd.read_csv('aula11-15/aula12/exemplo.csv')

df_filtrado = df[df['estado'] == 'SP'] # Criando um novo DataFrame com os dados do estado SP

print(df_filtrado)
