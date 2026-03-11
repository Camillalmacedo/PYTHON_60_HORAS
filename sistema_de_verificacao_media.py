print('SISTEMA DE VERIFICAÇÃO DE MÉDIA')

nome = input ('Digite o nome do aluno:')

print('Digite as notas do aluno', nome)
n1 = float(input('Digite a primeira nota:'))
n2 = float(input('Digite a segunda nota:'))
n3 = float(input('Digite a terceira nota:'))
print("***" * 15)
print('Média do aluno(a)', nome)
media = (n1 + n2 + n3) / 3
print(media)

aprovado = media >= 7
recuperação = media >= 5 and media < 7
reprovado = media < 5

print(f'''
SITUAÇÃO DO ALUNO(A) {nome}
Aprovado? - {aprovado}
Reprovado? - {reprovado}
Recuperação? - {recuperação}
''')