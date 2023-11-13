import yfinance as yf
import datetime as dt
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy.optimize import minimize
import matplotlib.ticker as mtick

lista_acoes = ["WEGE3", "LREN3", "VALE3", "PETR4", "EQTL3", "EGIE3"]
lista_acoes = [acao + ".SA" for acao in lista_acoes]

precos = yf.download(lista_acoes, start = "2015-01-01", end = "2022-12-31")['Adj Close']

retornos = precos.pct_change().apply(lambda x: np.log(1+x)).dropna()
media_retornos = retornos.mean()
matriz_cov = retornos.cov()

numero_carteiras = 1000
tabela_retornos_esperados = np.zeros(numero_carteiras)
tabela_volatilidade_esperada = np.zeros(numero_carteiras)
tabela_sharpe = np.zeros(numero_carteiras)
tabela_pesos = np.zeros((numero_carteiras, len(lista_acoes)))

for k in range(numero_carteiras):
  pesos = np.random.random(len(lista_acoes))
  pesos = pesos/np.sum(pesos)
  tabela_pesos[k, :] = pesos

  tabela_retornos_esperados[k] = np.sum(media_retornos * pesos * 252)
  tabela_volatilidade_esperada[k] = np.sqrt(np.dot(pesos.T, np.dot(matriz_cov*252, pesos)))

  tabela_sharpe[k] = tabela_retornos_esperados[k]/tabela_volatilidade_esperada[k]

indice_do_sharpe_maxio = tabela_sharpe.argmax()
tabela_pesos[indice_do_sharpe_maxio]

tabela_retornos_esperados_arit = np.exp(tabela_retornos_esperados) - 1
eixo_y_fronteira_eficiente = np.linspace(tabela_retornos_esperados_arit.min(),
                                         tabela_retornos_esperados_arit.max(), 50)

def pegando_retorno(peso_teste):
  peso_teste = np.array(peso_teste)
  retorno = np.sum(media_retornos * peso_teste) * 252
  retorno = np.exp(retorno) - 1

  return retorno

def checando_soma_pesos(peso_teste):
  return np.sum(peso_teste) - 1

def pegando_vol(peso_teste):
  peso_teste = np.array(peso_teste)
  vol = np.sqrt(np.dot(peso_teste.T, np.dot(matriz_cov * 252, peso_teste)))

  return vol

peso_inicial = [1/len(lista_acoes)] * len(lista_acoes)
limites = tuple([(0, 1) for ativo in lista_acoes])

eixo_x_fronteira_eficiente = []

for retorno_possivel in eixo_y_fronteira_eficiente:
  #vamos pegar a melhor volatilidade para cada retorno possível

  restricoes = ({'type': 'eq', 'fun': checando_soma_pesos},
                {'type': 'eq', 'fun': lambda w: pegando_retorno(w) - retorno_possivel})
  
  result = minimize(pegando_vol, peso_inicial, method='SLSQP', bounds=limites,
                    constraints=restricoes)
  eixo_x_fronteira_eficiente.append(result['fun'])

  fig, ax = plt.subplots()

ax.scatter(tabela_volatilidade_esperada, tabela_retornos_esperados_arit, c = tabela_sharpe)
plt.xlabel("Volatilidade esperada")
plt.ylabel("Retorno esperado")
ax.scatter(tabela_volatilidade_esperada[indice_do_sharpe_maxio], 
            tabela_retornos_esperados_arit[indice_do_sharpe_maxio], c = "red")
ax.plot(eixo_x_fronteira_eficiente, eixo_y_fronteira_eficiente)
ax.yaxis.set_major_formatter(mtick.PercentFormatter(1.0))
ax.xaxis.set_major_formatter(mtick.PercentFormatter(1.0))

plt.show()