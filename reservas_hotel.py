print()
print('SISTEMA DE RESERVAS DO HOTEL GUARULHOS DA MILLA')
print('Seja bem-vindo!')

#tipos de quartos
#valor de cada quarto

dados = {
'nomes':[],
'idades':[],
'quartos':['1. Simples','2. Duplo','3. Luxo'],
'quartos_escolhidos':[],
'valores':['', 100.00, 150.00, 250.00]
}

pessoas = int(input('Quantas pessoas irão se hospedar?'))
if pessoas == 1:
    dados['nomes'].append(input('Digite o nome da pessoa:'))
    dados['idades'].append(input('Digite a idade da pessoa:'))
    print('Escolha um quarto', dados['quartos'])
    dados['quartos_escolhidos'].append(dados['valores'][int(input('Número da escolha:'))])
    print('O valor do quarto escolhido é', dados['quartos_escolhidos'])
    
elif pessoas == 2:
    dados['nomes'].append(input('Digite o nome da primeira pessoa:'))
    dados['idades'].append(input('Digite a idade da primeira pessoa:'))
    dados['nomes'].append(input('Digite o nome da segunda pessoa:'))
    dados['idades'].append(input('Digite a idade da segunda pessoa:'))
    print('Escolha um quarto', dados['quartos'])
    dados['quartos_escolhidos'].append(dados['valores'][int(input('Número da escolha:'))])
    print('O valor do quarto escolhido é', dados['quartos_escolhidos'])
elif pessoas == 3:
    dados['nomes'].append(input('Digite o nome da primeira pessoa:'))
    dados['idades'].append(input('Digite a idade da primeira pessoa:'))
    dados['nomes'].append(input('Digite o nome da segunda pessoa:'))
    dados['idades'].append(input('Digite a idade da segunda pessoa:'))
    dados['nomes'].append(input('Digite o nome da terceira pessoa:'))
    dados['idades'].append(input('Digite a idade da terceira pessoa:'))
    print('Escolha um quarto', dados['quartos'])
    dados['quartos_escolhidos'].append(dados['valores'][int(input('Número da escolha:'))])
    print('O valor do quarto escolhido é', dados['quartos_escolhidos'])

dias = int(input('Quantos dias estará hospedado?'))
if dias == 1:
    print(dados['quartos_escolhidos'])
elif dias == 2:
    print(sum(dados['quartos_escolhidos']*2))
elif dias == 3:
    print(sum(dados['quartos_escolhidos']*3))

