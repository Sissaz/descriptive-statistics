# Funções

def soma(a,b):
    som = a+b
    return som
soma(5,9)

# 14

-

def subtrair(a,b):
    sub = a - b
    return sub
subtrair(10,8)

# 2

-

def nomeIdade(nome, idade):
    resp = (f"O nome é {nome} e a idade é {idade} anos.")
    return resp
nomeIdade("Pedro", 70)

#{'O nome é Pedro e a idade é 70 anos.'}

-

def subSoma(x,y):
    sub = subtrair(x,y)
    som = soma(x,y)
    return (f"Subtração = {sub} e Soma = {som}.")
subSoma(6,7)

# 'Subtração = -1 e Soma = 13.'