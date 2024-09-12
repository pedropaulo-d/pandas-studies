# %%
import pandas as pd

df_customers = pd.read_csv('../data/customers.csv', sep=';') # sep=';' indica o separador do arquivo csv
df_customers

# %%
df_customers.shape

# %%
df_customers.info(memory_usage='deep')

# %%
df_customers['Points'].describe()

# %%
df_customers['Points'].astype(int) # Converter o tipo de dado da coluna

# %%
df_customers['Points'].describe()

# %%
# Iterando os itens da lista para realizar a condição
notas = [4.5, 6, 7, 3.5]
for i in notas:
    if i > 5:
        print(i)

# %%
# Iterando os itens da lista para realizar a operação
notas_novas = []
for i in notas:
    notas_novas.append(i + 1)
notas_novas

# %%
# No Pandas, é feito uma operação vetorial.

# Retorna apenas as linhas com a condição True.
condicao = df_customers['Points'] > 1000
df_customers[condicao]

# %%
# Retorna apenas as linhas com a condição False.
condicao = df_customers['Points'] > 1000
df_customers[~condicao]

# %%
# Como retornar o usuario com o maior ponto? 1.0
maximo = df_customers['Points'].max()
condicao = df_customers['Points'] == maximo
df_customers[condicao]

# %%
# Como retornar o usuario com o maior ponto? 2.0
condicao = df_customers['Points'] == df_customers['Points'].max()
df_customers[condicao]

# %%
# Como retornar o usuario com o maior ponto? 3.0
df_customers[df_customers['Points'] == df_customers['Points'].max()]

# %%
# Como retornar o nome do usuario com o maior ponto? Utilizando iloc.
condicao = df_customers['Points'] == df_customers['Points'].max()
df_maior = df_customers[condicao]
df_maior['Name'].iloc[0]

# %%
# Como retornar os usuarios com pontos entre 1000 & 2000?
condicao = (df_customers['Points'] >= 1000) & (df_customers['Points'] <= 2000)
df_1000_2000 = df_customers[condicao]
df_1000_2000

# %%
# Se você for realizar um filtro para depois manipular os dados, FAÇA UM CÓPIA!
df_1000_2000 = df_customers[condicao].copy()
df_1000_2000 = df_1000_2000['Points'] + 1000
df_1000_2000

# %%
df_customers[condicao].describe()

# %%
# Como navegar pelas colunas no Pandas
df_customers[['UUID', 'Name']]

# %%
# Ordenando as colunas por odem alfabetica
columns = df_customers.columns.tolist()
columns.sort()
columns

# %%
df_customers = df_customers[columns]
df_customers

# %%
# Como renomear as colunas do DataFrame - Cria um DataFrame novo
df_customers = df_customers.rename(columns={
    'Name': 'Nome',
    'Points': 'Pontos'
})

df_customers

# %%
# Como renomear as colunas do DataFrame - Ele renomeia o MESMO DataFrame, sem criar um novo

df_customers.rename(columns={'UUID': 'ID'}, inplace=True)
df_customers

# %%
