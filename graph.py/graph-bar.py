# Gráfico de Colunas

# Servem para variáveis qualitativas;
# Formado por retângulos verticais;
# Comparam grandezas entre categorias;
# É principalmente usado para categorias com rotulos pequenos.

import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import seaborn as sns

y = [2, 5, 2, 7, 5, 1]
x = ['N1', 'N2', 'N3', 'N4', 'N5', 'N6']

x2 = ['Variável Um', 'Variável Dois', 'Variável Três', 'Variável Quatro', 'Variável Cinco', 'Variável Seis']

plt.bar(x, y, color = 'mediumseagreen')
plt.xlabel('Variável Eixo x', size = 15)
plt.ylabel('Categorias', size = 15)
plt.title('Gráfico de Barras', size = 15)
plt.show()

-

# Seaborn

import seaborn as sns

y = [2, 5, 2, 7, 5, 1]
x = ['N1', 'N2', 'N3', 'N4', 'N5', 'N6']

sns.barplot(x,y)
