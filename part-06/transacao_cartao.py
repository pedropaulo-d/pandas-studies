# %%

import pandas as pd
from dateutil.relativedelta import relativedelta

# %%

df = pd.read_excel('../data/faturas.xlsx')
df
# %%

df['dtTransaction'] = pd.to_datetime(df['dtTransaction'], format='%d-%m-%Y')
# %%
def fatia_parcela(row):
    return [row['Valor'] / row['Parcelas'] for i in range(row['Parcelas'])]

df['ValorParcela'] = df.apply(fatia_parcela, axis=1)

df
# %%
df_fatura = df.explode('ValorParcela')
df_fatura
# %%

df_fatura = df_fatura.drop(['Valor', 'Parcelas'], axis=1)

df_fatura
# %%

df_fatura['Months_add'] = df_fatura.groupby('idTransaction')['dtTransaction'].rank('first').astype(int)
df_fatura
# %%

def add_months(row):
    new_date = row['dtTransaction'] + relativedelta(months=row['Months_add'])
    dt_str = f'{new_date.year}-{new_date.month:02}'
    return dt_str

df_fatura['DtFatura'] = df_fatura.apply(add_months, axis=1)
df_fatura
# %%

df_fatura_mes = (
    df_fatura.groupby(['idCliente', 'DtFatura'])['ValorParcela']
    .sum()
    .reset_index()
)

df_fatura_mes
# %%

df_fatura_mes = df_fatura_mes.pivot_table(
    columns='DtFatura',
    index='idCliente',
    values='ValorParcela'
).fillna(0)


df_fatura_mes
# %%
