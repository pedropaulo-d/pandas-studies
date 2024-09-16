# %%
import pandas as pd

# %%

df = pd.read_csv('../data/customers.csv', sep=';')
df
# %%
# Ordenado pela coluna Points
df.sort_values(by='Points', ascending=False) # Desc
df.sort_values(by='Points', ascending=True, inplace=True) # Asc

# %%

df.sort_values(by='Points', ascending=True, inplace=True)
df.rename(columns={"Name":"Nome", 'Points':'Pontos'}, inplace=True)
df

# %%

df = (df.sort_values(by=['Points', 'Name'], ascending=[False, True]).rename(columns={'Name':'Nome', 'Points':'Pontos'}))
df

# %%
