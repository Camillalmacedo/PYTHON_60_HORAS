# print('EXERCÍCIO 1')
# numero = int(input('Digite um número  ->'))
# match numero % 2:
#     case 0:
#         print('O número informado é par')
#     case _:
#         print('O número informado é ímpar')
# print()
# print('EXERCÍCIO 2')
# numero = int(input('Digite outro número  ->'))
# match numero:
#     case x if x >0:
#         print('O número informado é positivo')
#     case x if x <0:
#         print('O número informado é negativo')
#     case 0:
#         print('O número informado é 0')
# print()
# print('EXERCÍCIO 3')
# x = input('Digite ou não uma palavra qualquer  ->')
# match x:
#     case '':
#         print('Vazio')
#     case _:
#         print('Preenchido')
        
# print()
# print('EXERCÍCIO 4')
# numero = int(input('Digite um número  ->'))

# match numero:
#     case x if x > 10:
#         print('maior que 10')
#     case x if x < 10:
#         print('menor que 10')
#     case _:
#         print('igual a 10')

print()
print('EXERCÍCIO 5')
idade = int(input('Digite uma idade  ->'))
match idade:
    case x if x <=12:
        print('criança')
    case x if x <=17:
        print('adolescente')
    case x if x <= 35:
        print('jovem')
    case x if x <=64:
        print('adulto')
    case _:
        print('idoso')