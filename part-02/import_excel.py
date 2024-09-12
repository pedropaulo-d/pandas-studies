# %%
import pandas as pd
df_excel = pd.read_excel('../data/transactions.xlsx')
df_excel
# %%
df_excel.head()
# %%
df_excel.tail()
# %%
colunas = ['UUID', 'Points', 'IdCustomer', 'DtTransaction']

df_excel = df_excel[colunas]
df_excel
# %%
df_excel.info(memory_usage='deep')
# %%
