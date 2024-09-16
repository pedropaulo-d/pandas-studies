# %%
import pandas as pd
# %%
data = {
    'Nome': ['Teo', 'Nah', 'Maria', 'Nah', 'Lara', 'Teo'],
    'Idade': [32, 33, 2, 33, 31, 32],
    'updated_at': [1, 2, 3, 1, 2, 3]
}

df = pd.DataFrame(data)
df
# %%
df = (df.sort_values(by='updated_at', ascending=False).drop_duplicates(subset=['Nome', 'Idade'], keep='first'))
df

# %%

df = pd.read_excel('../data/transactions.xlsx')
df

# %%
df_last = (df.sort_values('DtTransaction', ascending=False).drop_duplicates(subset='IdCustomer', keep='first'))
df_last.head()

# %%
df_last['IdCustomer'].nunique()

# %%

condicao = df['IdCustomer'] == '5f8fcbe0-6014-43f8-8b83-38cf2f4887b3'
df[condicao]

# %%
df_last[df_last['IdCustomer'] == '5f8fcbe0-6014-43f8-8b83-38cf2f4887b3']

# %%
df = pd.read_csv('../data/customers.csv', sep=';')
df
# %%
df.dtypes
# %%
df['Points'].astype('str')
# %%
