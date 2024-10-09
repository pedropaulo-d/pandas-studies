# %%
import pandas as pd

df = pd.read_csv('../data/ipea_consolidado.csv')
df
# %%

df = df.set_index(['cod', 'nome', 'período'])

# %%
df_stack = df.stack().reset_index().rename(columns={
    'level_3': 'tipo_homicidio', 0: 'quantidade'
    })

# %%

df_unstack = df_stack.set_index(
    ['cod', 'nome', 'período', 'tipo_homicidio']
    ).unstack().reset_index()

homicidios = df_unstack['quantidade'].columns.tolist()
homicidios
# %%
df_unstack.columns = ['cod', 'nome', 'periodo'] + homicidios
df_unstack
# %%
