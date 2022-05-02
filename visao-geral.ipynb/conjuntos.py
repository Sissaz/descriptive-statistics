# Conjuntos (Set)

lista = [1,2,3,4,5]
c = set(lista)
type(c)
# set

-

c.add(55)
c
# {1, 2, 3, 4, 5, 55}

-

# Numeros em comum
c1 = set([1,2,3,4])
c2 = set((1,2,88))
c1.intersection(c2)
# {1, 2}

-

# Uniao
c1.union(c2)
# {1, 2, 3, 4, 88}

-

8 in c1
# False

-

2 in c1
# True