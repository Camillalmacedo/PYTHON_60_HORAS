print()
print('EXERCÍCIO 1')
númeroa = int(input('DIGITE UM VALOR INTEIRO  ->'))
if númeroa > 0:
    print('O número informado é positivo.')
elif númeroa < 0:
    print('O número informado é negativo.')
else:
    print('O número não é negativo nem positivo, pois é igual a 0.')

print()
print('EXERCÍCIO 2')
idade = int(input('Idade  ->'))

if idade >= 18:
    print('Pode votar.')
else:
    print('Não pode votar.')

print()
print('EXERCÍCIO 3')
numerob = int(input('Digite um número qualquer  ->'))
if numerob % 2 == 0:
    print('O número informado é par.')
else:
    print('O número informado é ímpar.')

print()
print('EXERCÍCIO 4')
print('Abaixo digite 3 valores para cada lado de um triângulo:')
lado1 = int(input('Lado 1  ->'))
lado2 = int(input('Lado 2  ->'))
lado3 = int(input('Lado 3  ->'))

if lado1 == lado2 == lado3:
    print('O triângulo informado é equilátero.')
elif lado1 == lado2 != lado3:
    print('O triângulo informado é isósceles.')
elif lado1 == lado3 != lado2:
    print('O triângulo informado é isósceles.')
elif lado2 == lado3 != lado1:
    print('O triângulo informado é isósceles.')
else:
    print('O triângulo informado é escaleno.')

print()
print('EXERCÍCIO 5')
numeroc = int(input('Digite um número inteiro  ->'))
if numeroc % 5 == 0 and numeroc % 7 == 0:
    print('O número informado é múltiplo de 5 e 7.')
else: 
    print('O número informado não é múltiplo de 5 e 7.')

print()
print('EXERCÍCIO 6')
numerod = int(input('Digite um valor positivo ou negativo  ->'))
if numerod > 10:
    print('O numero informado é positivo e maior que 10.')
else:
    print('O número informado não se encaixa nas quaificações: ser positivo e maior que 10.')

print()
print('EXERCÍCIO 7')
numeroe = int(input('Digie um número  ->'))
if numeroe % 3 == 0 or numeroe % 5 == 0:
    print('O número é divisível por 3 ou por 5.')
else:
    print('O número não é divivível nem por 3 nem por 5')