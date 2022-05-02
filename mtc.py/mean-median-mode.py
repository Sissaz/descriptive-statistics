# Calculando a Média

import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import numpy as np
import pandas as pd
from bokeh.sampledata.iris import flowers as dados

dados.shape

# (150, 5)
# 150 linhas e 5 colunas

-

dados.head(3)
# Plotagem da tabela com 3 linhas e as 5 colunas

-

med_sl = np.mean(dados['sepal_length'])
print(round(med_sl))
# Imprime a média arredondada para o comprimento da Sépala

-

type(dados)
# pandas.core.frame.DataFrame
# O tipo dessa estrutura de dados é do tipo DataFrame, presente na biblioteca Pandas.
# Com isso, consegue-se calcular a média diretamente, com:
np.mean(dados)

# sepal_length    5.843333
# sepal_width     3.057333
# petal_length    3.758000
# petal_width     1.199333

-

# Calculando a Mediana

mediana_sl = np.median(dados['sepal_length'])
mediana_sl

# 5.8

moda_sl = dados['sepal_length'].median()
moda_sl

# 5.8

-

# Calculando a Moda

median_sl = dados['sepal_length'].mode()
median_sl

# 5.0
