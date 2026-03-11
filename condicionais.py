idade = int(input('Idade:'))
carteira_motorista = input('Possui CNH?')
if idade >= 18 and carteira_motorista == 'sim' :
    print('Pode dirigir')
elif idade >= 18 and carteira_motorista == 'não':
    print('Não pode dirigir')
    print('Tire a carteira no site clicando aqui...')

else:
    print('Não pode dirigir')



if idade >= 18:
    if carteira_motorista == 'sim':
        print('Pode dirigir')
