# %%
import pandas as pd

df_products = pd.read_csv('../data/products.csv', sep=';', 
                            names=['ID', 'Name', 'Description'],
                            )
df_products

# %%
df_products.rename(columns={'Name': 'Nome',
                            'Description': 'Descrição'}, 
                            inplace=True
                            )
df_products

# %%
