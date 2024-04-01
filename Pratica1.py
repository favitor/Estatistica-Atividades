#Importando bibliotecas necessarias para rodar o programa
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import PercentFormatter
import numpy as np



#Criando a tabela, aqui chamados de dataframe
dados = [
	['F1', 'Bahia', 48.000, 26, 20],
	['F2', 'Pernambuco', 37.000, 19, 30],
	['F3', 'Pernambuco', 25.000, 14, 22],
	['F4', 'Bahia', 18.000,	12,	32],
	['F5', 'Pernambuco', 17.000, 8,	44],
	['F6', 'Pernambuco', 39.000, 21, 2],
	['F7', 'Pernambuco', 51.000, 30, 17],
	['F8', 'Rio de Janeiro', 45.000, 14, 25],
	['F9', 'Rio de Janeiro', 31.000, 15, 25],
	['F10', 'Rio de Janeiro', 26.000, 13, 19]
]


df = pd.DataFrame(dados, columns=['Filial', 'Estado', 'Receita Mensal(milhões)', 'Nº de Funcionário', 'Projeção de clientes em %'])
print(df)