import random

print('MEGASENA!')

numeros = list (range(1,61))

quantos_numeros_deaposta = int(input('A partir de 6:'))

if quantos_numeros_deaposta == 6:


    n1 = random.choice(numeros)
    n2 = random.choice(numeros)
    n3 = random.choice(numeros)
    n4 = random.choice(numeros)
    n5 = random.choice(numeros)
    n6 = random.choice(numeros)

    lista_maquina = [n1, n2, n3, n4, n5, n6]
    print(lista_maquina)

m1 = int(input('Escolha de 1 à 60:'))
m2 = int(input('Escolha de 1 à 60:'))
m3 = int(input('Escolha de 1 à 60:'))
m4 = int(input('Escolha de 1 à 60:'))
m5 = int(input('Escolha de 1 à 60:'))
m6 = int(input('Escolha de 1 à 60:'))

if m1 in lista_maquina and m2 in lista_maquina and m3 in lista_maquina and m4 in lista_maquina and m5 in lista_maquina and m6 in lista_maquina:
    print(lista_maquina)
    print('GANHOU A MEGASENA!')
elif m1 in lista_maquina or m2 in lista_maquina or m3 in lista_maquina or m4 in lista_maquina or m5 in lista_maquina or m6 in lista_maquina:
    minha = [m1 and m2 and m3 and m4 and m5 and m6 in lista_maquina]
    print('Parabéns esses são os seus')
    