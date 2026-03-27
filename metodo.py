import random


def atividade1():
    x  =  random.randint(5,10)
    return x

def atividade2():
    x  =  random.randint(1,10)
    y  =  random.randint(1,10)
    z  =  random.randint(1,10)
    return x, y, z

def atividade3():
    x = list(range(10,31))
    return random.choice(x)

def atividade4():
    x = list(range(1,11))
    x.reverse()
    for i in x:
        print(i)
    print('Fogo!')

def atividade5():
    x = input(int('Digite um número inteiro positivo-->'))
    
