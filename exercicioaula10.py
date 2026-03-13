#1 - Faça um programa, utilizando ***while***, que mostre na tela os números de 0 a 1000.

# print()
# c = 0
# while c <=1000:
#     print(c)
#     c=c+1
    


# print()
# nomes = []
# while len(nomes) <=10:
#     nomes.append(input('DIGITE UM NOME  ->'))
# print(nomes)








print()
print('ATIVIDADE 2')
sistema = {
'acesso': {
'senha' : 'farofa',
'nome' : 'teacher Milla'
},

'português':[],
'matemática': [],
'ciências': []
}
print('PORTAL DOS PROFESSORES')

for chances in range(3):
    senha  =  input('Digite sua senha: ')
    if senha == sistema['acesso']['senha']:
        print('Bem-vindo(a) ', sistema['acesso']['nome'])
        print(f'''Escolha uma matéria: 
            1 - Português | 2 - Matemática | 3 - Ciências''')
        materia = input('Sua escolha: ')
        if materia == '1':
            sistema['português'].append(float(input('Digite a nota que o aluno tirou na prova: ')))
            sistema['português'].append(float(input('Digite a nota que o aluno tirou no seminário: ')))
            sabermedia = input('Deseja saber a média do aluno? ')
            if sabermedia == 'sim':
                mediaportugues = sum(sistema['português'])
                print(mediaportugues*0.5)
                break
                
            elif sabermedia == 'não':
                print('tá bom então👌')
                suaresposta = input('Deseja escolher outra matéria?')
                if suaresposta == 'sim':
                    print(f'''Escolha uma matéria: 
            1 - Português | 2 - Matemática | 3 - Ciências''')
                elif suaresposta == 'não':
                    print('tá bom então👌')
                    break

       
            

        if materia == '2':
            sistema['matemática'].append(float(input('Digite a nota que o aluno tirou na prova: ')))
            sistema['matemática'].append(float(input('Digite a nota que o aluno tirou no seminário: ')))
            sabermedia = input('Deseja saber a média do aluno? ')
            if sabermedia == 'sim':
                mediamatematica = sum(sistema['matemática'])
                print(mediamatematica*0.5)
                break

            elif sabermedia == 'não':
                print('tá bom então👌')
                suaresposta = input('Deseja escolher outra matéria?')
                if suaresposta == 'sim':
                    print(f'''Escolha uma matéria: 
            1 - Português | 2 - Matemática | 3 - Ciências''')
        materia = input('Sua escolha: ')



        if materia == '3':
            sistema['ciências'].append(float(input('Digite a nota que o aluno tirou na prova: ')))
            sistema['ciências'].append(float(input('Digite a nota que o aluno tirou no seminário: ')))
            sabermedia = input('Deseja saber a média do aluno? ')
            if sabermedia == 'sim':
                mediaciências = sum(sistema['ciências'])
                print(mediaciências*0.5)
                break

            elif sabermedia == 'não':
                print('tá bom então👌')
                suaresposta = input('Deseja escolher outra matéria?')
                if suaresposta == 'sim':
                    print(f'''Escolha uma matéria: 
            1 - Português | 2 - Matemática | 3 - Ciências''')
        materia = input('Sua escolha: ')
                
                   


    else:
        print('Senha incorreta. Tente novamente.')    

else:
    print('Senha incorreta. Acesso bloqueado.')




       
input('Enter para SAIR ')



