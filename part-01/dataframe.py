# %%
import pandas as pd

# %%
data = {
    'nome':['teo', 'nah', 'lara', 'maria'],
    'sobrenome':['calvo', 'ataide', 'calvo', 'calvo'],
    'idade': [31, 32, 31, 2]
}

data
# %%
df = pd.DataFrame(data)
df
# %%
print(df.iloc[0])

print(df['idade'].iloc[0])

print(df['sobrenome'].iloc[0])

print(type(df['sobrenome'].iloc[0]))

# %%
print(df.index) # Index do dataframe
print('-='*40)

print(df.columns) # Nomes das colunas do dataframe
print('-='*40)

print(df.info(memory_usage='deep')) # Informações sobre o dataframe
print('-='*40) 

print(df.dtypes) # Tipos dos dados de cada coluna
print('-='*40)

print(df.describe()) # Aplicar estatisticas para todas as colunas númericas

# %%
