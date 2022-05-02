# Listas:

lista = []
# Lista em branco.

-

carros = ['Clio', 'Gol', 'Celta']
carros[0]
# 'Clio'

-

# Adicionar itens:
carros = ['Clio', 'Gol', 'Celta']
carros.append('Fox')
carros[3]
# 'Fox'

-

# Remover itens pelo nome:
carros = ['Clio', 'Gol', 'Celta']
carros.remove('Gol')
carros
# ['Clio', 'Celta']

-

# Remover itens pela posição:
carros = ['Clio', 'Gol', 'Celta']
carros.pop(0)
carros
# ['Gol', 'Celta']

-

# Contar itens na lista:
carros = ['Clio', 'Gol', 'Celta']
len(carros)
# 3

-

# Contar itens na lista pelo nome:
carros = ['Clio', 'Gol', 'Celta']
carros.count('Clio')
# 1

-

# Contar a posiçao do item pelo nome:
carros = ['Clio', 'Gol', 'Celta']
carros.index('Celta')
# 2

-

# Slice da lista:
carros = ['Clio', 'Gol', 'Celta']
carros[0:2]
# ['Clio', 'Gol']
# 0 representa o inicio e o 2 representa a quantidade de itens que irá retornar.