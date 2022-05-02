# Gráfico de Linhas

# Indicado para representar séries temporais.

import matplotlib.pyplot as plt
import matplotlib.colors as mcolors

y = [6, 8, 3, 1, 9]

x1 = [1, 2, 3, 4, 5]

x = ['seg', 'ter', 'qua', 'qui', 'sex']

plt.plot(x, y, 'o-', color = 'lightseagreen')
plt.xlabel('Eixo x', size = 15)
plt.ylabel('Eixo y', size = 15)
plt.title('Gráfico de Linha', size = 15)
plt.show()
