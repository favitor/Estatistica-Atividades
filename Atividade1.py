#Importando bibliotecas necessarias para rodar o programa
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import PercentFormatter
import numpy as np


#Dados da tabela da atividade e  'dtype' defini o tipo dos dados, nesse caso numeros reais
dados = pd.array(data=[0.0, 0.9, 9.8, 9.3, 3.0, 6.0, 5.2,
6.4, 9.4, 7.4, 6.4, 9.4, 0.8, 0.8,
3.8, 9.4, 8.4, 2.0, 3.2, 2.2, 5.2,
1.8, 6.9, 9.9, 10.0, 8.8, 2.1, 5.4, 4.4, 5.1], dtype=float)



#Historigrama de Fequência Absoluta
plt.title('Distribuição de notas de avaliação do serviço de telemarketing')
plt.xlabel('Notas')
plt.ylabel('Frequência Absoluta')
plt.hist(dados, 5, rwidth=0.9)#Aqui o 5 é o numero de classes, já o rwidth é o tamanho das barras
plt.show()



#Historigrama de Fequência Absoluta
fig = plt.figure()
ax = fig.add_subplot(111)
ax.hist(dados, edgecolor='black', weights=np.ones_like(dados)* 100 / len(dados))
ax.yaxis.set_major_formatter(PercentFormatter())
plt.show()
#
#istograma de frequências absolutas e um histograma de frequências relativas