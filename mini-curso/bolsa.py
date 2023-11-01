import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick

dados_bancarios = yf.download(['ITUB4.SA', 'BBAS3.SA', 'SANB4.SA', 'BBDC4.SA', '^BVSP'],
                             start = "2010-01-01", end = "2022-04-30")['Adj Close']

lucro_bancos = pd.read_excel('/Users/felipesiqueira/develop/python/mini-curso/lucro_bancos.xlsx', index_col = "data")

dados_filtrados_2015 = dados_bancarios[dados_bancarios.index > "2015-01-01"]

itau = dados_bancarios['ITUB4.SA']
santander = dados_bancarios['SANB4.SA']
banco_do_brasil = dados_bancarios['BBAS3.SA']
bradesco = dados_bancarios['BBDC4.SA']
dados_mercado = dados_bancarios['^BVSP']

def retorno(lista):
    retorno = lista[-1]/lista[0] - 1
    
    return retorno

retorno_itau = retorno(lista = itau)
retorno_banco_brasil = retorno(lista = banco_do_brasil)
retorno_bradesco = retorno(lista = bradesco)
retorno_santander = retorno(lista = santander)
retorno_mercado = retorno(lista = dados_mercado)


df_retornos = pd.DataFrame(data = {'retornos': [retorno_itau, retorno_banco_brasil, 
                                   retorno_bradesco, retorno_santander, retorno_mercado]}, 
                           index = ["Itau", "Banco_do_Brasil", "Bradesco", "Santander", "Ibovespa"])

df_retornos['retornos'] = df_retornos['retornos'] * 100
df_retornos = df_retornos.sort_values(by = "retornos", ascending = False)

fig, ax = plt.subplots()

ax.bar(df_retornos.index , df_retornos['retornos'])
ax.yaxis.set_major_formatter(mtick.PercentFormatter())

plt.xticks(fontsize = 9)
plt.show()

var_lucro_bancos = lucro_bancos.iloc[-1]/lucro_bancos.iloc[0] - 1
var_lucro_bancos = var_lucro_bancos  * 100
var_lucro_bancos = var_lucro_bancos.sort_values(ascending = False)


fig2, ax2 = plt.subplots()

ax2.bar(var_lucro_bancos.index , var_lucro_bancos)
ax2.yaxis.set_major_formatter(mtick.PercentFormatter())

plt.xticks(fontsize = 9)

plt.show()