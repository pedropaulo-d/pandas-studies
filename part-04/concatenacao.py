# %%
import pandas as pd
import os
# %%

def import_etl(path:str):

    name = path.split('/')[-1].split('.')[0]

    df = (
        pd.read_csv(path, sep=';')
            .rename(columns={'valor': name})
            .set_index(['cod', 'nome', 'período'])
    )

    return df
# %%

path = '../data/ipea/'
files = os.listdir(path)
# %%

dfs = []
for data in files:
    dfs.append(import_etl(path+data))

# %%
dfs
# %%


df_consolidado = pd.concat(dfs, axis=1)
df_consolidado
# %%

df_consolidado.to_csv('../data/ipea_consolidado.csv')
# %%
