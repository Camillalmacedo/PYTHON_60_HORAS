import statistics
print('Escolha sua nova empresa a partir de dados obtidos dos salários!')
    
def estatistica():    
#  while True:
    empresa1 = [1000,6000,1200,8000,1400]

    empresa2 = [5000,4000,3000,2000,7000]

    empresa3 = [1200,1300,8000,3000,15000]

    empresa4 = [1400,1750,2000,4500,5900]

    print('Opção 1',empresa1)

    print('Opção 2',empresa2)

    print('Opção 3',empresa3)

    print('Opção 4',empresa4)



    escolha = input(f'''
    Deseja verificar um dos tópicos abaixo?
                    
    Média salarial
    Moda salarial
    Mediana dos salários
    Desvio Padrão
                    
    sim ou não?
    -->''')

    if(escolha) == 'sim':
        opcaoescolhida = input(f'''
    Escolha a opção de análise de dados:
    1 - Média
    2 - Moda
    3 - Mediana
    4 - Desvio Padrão
    -->''')
        if(opcaoescolhida) == '1': #média
            escolhaempresa = input('Escolha aqui o número da empresa-->')
            if escolhaempresa == '1':
                media = statistics.mean(empresa1)
                print(media)
            elif escolhaempresa == '2':
                media = statistics.mean(empresa2)
                print(media)
            elif escolhaempresa == '3':
                media = statistics.mean(empresa3)
                print(media)
            elif escolhaempresa == '4':
                media = statistics.mean(empresa4)
                print(media)


        if(opcaoescolhida) == '2': #moda
            escolhaempresa = input('Escolha aqui o número da empresa-->')
            if escolhaempresa == '1':
                moda = statistics.mode(empresa1)
                print(moda)
            elif escolhaempresa == '2':
                moda = statistics.mode(empresa2)
                print(moda)
            elif escolhaempresa == '3':
                moda = statistics.mode(empresa3)
                print(moda)
            elif escolhaempresa == '4':
                moda = statistics.mode(empresa4)
                print(moda)



        if(opcaoescolhida) == '3': #mediana
            escolhaempresa = input('Escolha aqui o número da empresa-->')
            if escolhaempresa == '1':
                mediana = statistics.median(empresa1)
                print(mediana)
            elif escolhaempresa == '2':
                mediana = statistics.median(empresa2)
                print(mediana)
            elif escolhaempresa == '3':
                mediana = statistics.median(empresa3)
                print(mediana)
            elif escolhaempresa == '4':
                mediana = statistics.median(empresa4)
                print(mediana)




        if(opcaoescolhida) == '4': #desvio
            escolhaempresa = input('Escolha aqui o número da empresa-->')
            if escolhaempresa == '1':
                desvio = statistics.stdev(empresa1)
                print(desvio)
            elif escolhaempresa == '2':
                desvio = statistics.stdev(empresa2)
                print(desvio)
            elif escolhaempresa == '3':
                desvio = statistics.stdev(empresa3)
                print(desvio)
            elif escolhaempresa == '4':
                desvio = statistics.stdev(empresa4)
                print(desvio)



    else:
        print('Clique enter para sair da navegação.')

estatistica()