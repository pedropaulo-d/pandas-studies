# %%
import pandas as pd
# %%
idades = [30, 42, 90, 34]

media = sum(idades) / len(idades)

total = 0
for i in idades:
    total += (media - i)**2

variancia = total / (len(idades) - 1)
print(f"Python - Idades: {idades}\nPython - Média: {media}\nPython - Variancia: {variancia}")

# %%
series_idades = pd.Series(idades)
series_idades

# %%
print(f'Pandas - Idades: {series_idades}')
print(f'Pandas - Média: {series_idades.mean()}')
print(f'Pandas - Variancia: {series_idades.var()}')
print(f'Pandas - Mediana: {series_idades.median()}')


# %%
series_idades.describe()
# %%
series_idades.shape # Quantas linhas o objeto Series tem
# %%
idades[0]
# %%
series_idades[0]

# %%
series_idades.iloc[0] # Garantido que vai pegar pela posição

# %%
series_idades.loc[2] # Garantido que vai pegar pelo índice

# %%
series_idades.name = 'idades'
series_idades
# %%
