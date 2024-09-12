# %%
import pandas as pd
# %%
"""
1. Converta a seguinte lista de dados para uma série pandas e obtenha:
- Média
- Desvio Padrão
- Máximo Valor

dados = [10, 20, 42, 9, 12, 35, 24, 10, 8, 14, 21]
"""
dados = [10, 20, 42, 9, 12, 35, 24, 10, 8, 14, 21]
series = pd.Series(dados)



# %%
estatistica = series.describe()
estatistica
# %%
print(f'Média: {estatistica['mean']:.3f}')
print(f'Desvio Padrão: {estatistica['std']:.3f}')
print(f'Máximo Valor: {estatistica['max']:.3f}')

# %%
"""
2. Converta o seguinte dicionárioo para DataFrame e obtenha:
- Sumário de cada coluna
- Média da coluna idade
- Último nome da coluna nome

dados = {'nome':['Téo', 'Nah', 'Napoleão'], 'idade':[31, 32, 14]}
"""
dados = {'nome':['Téo', 'Nah', 'Napoleão'], 'idade':[31, 32, 14]}

# %%
df = pd.DataFrame(dados)
# %%
df.columns
# %%
print(f'Sumario: {df.describe()}')
print(f'Média: {df['idade'].mean():.2f}')
print(f'Último nome da coluna nome: {df['nome'].iloc[-1]}')
# %%
