# Gráfico de Histograma

# Colunas justapostas para representar distribuição de frequencia em dados;
# No eixo horizontal temos os limites das classes de agrupamento;
# Frequencias x Intervalos.

import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import numpy as np

x = np.random.randn(1000)

plt.hist(x, bins = 10, color = 'lightseagreen', edgecolor = "teal")
plt.xlabel('Eixo x', size = 15)
plt.ylabel('Eixo y', size = 15)
plt.title('Gráfico de Linha', size = 15)
plt.show()
