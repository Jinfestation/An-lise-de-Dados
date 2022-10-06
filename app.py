from pdb import line_prefix
from tkinter.tix import COLUMN
import pandas as pd
# open the 6 sheets
lista_meses = ['janeiro', 'fevereiro',
               'março', 'abril', 'maio', 'junho']

for mes in lista_meses:

    tabela_vendas = pd.read_excel(f'{mes}.xlsx')
    if (tabela_vendas['Vendas'] > 55000).any():
        vendedor = tabela_vendas.loc[tabela_vendas['Vendas']
                                     > 55000, 'Vendedor'].values[0]
        vendas = tabela_vendas.loc[tabela_vendas['Vendas']
                                   > 55000, 'Vendas'].values[0]
        print(f'No mes de {mes} {vendedor} bateu a meta {vendas}')


# para cada arquivo
# Identificar quem vendeu mais de 55 mil
# Mandar SMS: Se for maior que 55 mil, sms com nome e mes de venda do vendedor
# Se for menor que 55 mil quanto falta
