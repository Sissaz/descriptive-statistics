# Medidas de Tendência Central

# Indicam um ponto em torno do qual se concentram os dados;
# Medidas descritivas para resumir dados;
# Se calculadas a partir de dados populacionais, temos PARÂMETROS;
# Se calculadas a partir de dados amostrais, temos ESTIMADORES ou ESTATÍSTICAS;
# Estatísticas: Média, Moda, Mediana, Percentis.

# Notações das Estatísticas:

# Para Parâmetros:
# Número de Elementos: N
# Média: μ
# Variância: σ²
# Desvio Padrão: σ

# Para Estimadores:
# Número de Elementos: n
# Média: x̅
# Variância: S²
# Desvio Padrão: S

-

import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import numpy as np
import pandas as pd
from bokeh.sampledata.iris import flowers as dados

type(dados)
# pandas.core.frame.DataFrame

dados.describe()

# Quando os dados forem do tipo DataFrame, pode-se utilizar a função dados.describe() para obter informações, como:

# sepal_length	sepal_width	petal_length	petal_width
# count	150.000000	150.000000	150.000000	150.000000
# mean	5.843333	3.057333	3.758000	1.199333
# std	0.828066	0.435866	1.765298	0.762238
# min	4.300000	2.000000	1.000000	0.100000
# 25%	5.100000	2.800000	1.600000	0.300000
# 50%	5.800000	3.000000	4.350000	1.300000
# 75%	6.400000	3.300000	5.100000	1.800000
# max	7.900000	4.400000	6.900000	2.500000

