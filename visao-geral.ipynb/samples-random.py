# Amostragem Random

# Importar:
import random
import numpy as np

-

x = random.random()
print(x)

# 0.6187932948481972

-

y = []
for i in range(100):
    y.append(random.random())
y

-

nomes = ['Lucas', 'Marcos', 'Thiago', 'Roberto', 'Bianca', 'Erika']
random.choice(nomes)

# 'Thiago'

-

# Aleatorizar a Lista:

random.shuffle(nomes)
nomes

# ['Thiago', 'Erika', 'Lucas', 'Roberto', 'Bianca', 'Marcos']

-

# Obter valores de amostras de forma aleatoria:

random.sample(nomes, 3)
# ['Marcos', 'Lucas', 'Thiago']


