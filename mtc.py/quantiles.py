# Calculo das Separatrizes

import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import numpy as np
import pandas as pd
from bokeh.sampledata.iris import flowers as dados

dados.head(3)


# Primeiro Quartil (25% dos dados)
Q1 = np.quantile(dados['sepal_length'], 0.25)
Q1
# 5.1


# Segundo Quartil (Mediana, 50% dos dados)
P50 = np.quantile(dados['sepal_length'], 0.50)
P50
# 5.8


# Terceiro Quartil (75% dos dados)
Q3 = np.quantile(dados['sepal_length'], 0.75)
Q3
# 6.4


P10 = np.quantile(dados['sepal_length'], 0.10)
P10
# 4.8
