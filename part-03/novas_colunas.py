# %%
import pandas as pd
import numpy as np
# %%
df = pd.read_csv('../data/customers.csv', sep=';')
df
# %%
df['Points_double'] = df['Points'] * 2
df
# %%
df['Points_ratio'] = df['Points_double'] / df['Points']
df# %%

# %%
df['Costante'] = 1
df
# %%
df['Points_log'] = np.log(df['Points'])
df
# %%
def get_first(nome:str):
    return nome.split('_')[0]

# %%
df['Name_First'] = df['Name'].apply(get_first)
df
# %%
df['Name'].apply( lambda x: x.upper().split('_')[0])
# %%
def intervalo_pontos(pontos):
    if pontos < 2500:
        return 'Baixo'
    elif pontos < 3500:
        return 'Medio'
    else:
        return 'Alto'

df['Faia_Pontos'] = df['Points'].apply(intervalo_pontos)
df
# %%
