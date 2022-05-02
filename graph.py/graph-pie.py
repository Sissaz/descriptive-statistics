# Gráfico de Setores (Pizza)

# Divide um círculo em setores proporcionais às frequencias observadas nas categorias;
# Indicado para comparar valor da categoria especifica com o total;
# Principal utilização se dá com um pequeno número de categoria.

import matplotlib.pyplot as plt
import matplotlib.colors as mcolors

y = [2, 5, 2, 7, 5, 1]
x = ['N1', 'N2', 'N3', 'N4', 'N5', 'N6']

plt.pie(y, labels=x, radius=1)
plt.show()
