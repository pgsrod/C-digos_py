# import numpy as np - numpy mais rápido que o pandas
# import matplotlib.pyplot as pyplot  
# import seaborn
# import plotly
# from sklearn import 

# criar 20 pedidos 

import pandas as pd 
import random  

produtos = ['Computador', 'Monitor', 'Mouse', 'Caixa de som', 'Teclado', 'Fone']

dados = {
    'Produto': [random.choice(produtos) for _ in range(20)], 
    'Preco': [random.randint(100,5000) for _ in range (20)], 
    'Quantidade' : [random. randint(1,10) for _ in range (20)]
    }

df = pd.DataFrame(dados) 
# head() -> mostra 'n' primeiras linhas
# tail() -> mostra 'n' ultimas linhas
# padrão() -> 5 linhas
print(df.head())

# para saber informações do tipo
print (df.info()) 

print(30*'-')
print(30*'-')

print (df.describe())

# noção de coluna para tratar
print(df.shape)

# quando precisa saber das colunas
print(df.columns)

# imprimir 1 coluna
print(df['Produto'])
# imprimir 2 ou mais colunas
print (df[['Produto','Preco']])

# filtrar o dataframe
df_filtrado = df[df['Quantidade']>5]
print(df_filtrado)

print(30*'-')

print('Multiplicação Vetorial')

# criar uma coluna
df['preco_final'] = df['Preco'] * df['Quantidade']
print(df.head())

# dá os nomes das colunas e o tipo de cada uma
print(df.dtypes)
# para exportar 
df.to_csv('base_criada.csv', index=False)