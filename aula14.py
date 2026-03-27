import os


# Exercício 1: Criar e ler um Arquivo

# Criar um arquivo  "with"
with open('novo_diretorio', 'w') as novo_arquivo:
    os.mkdir('novo_arquivo')
with open('exemplo.txt', 'r') as arquivo:
    conteúdo = arquivo.read()
    print(conteúdo)

# Exemplo 2: Cria um Diretório

with os.scandir('c:/Users/aluno/Desktop/aula12/') as entrada:
      for arquivo in entrada:
         print(f'Diretório encontrado: {arquivo.name}')

# Exercício 3: Renomear um Diretório
os.rename('arquivo.txt', 'novo_nome.txt')


# Exercício 4:  Listar Arquivos em um Diretório
with os.scandir('meu_diretorio') as entrada:
    for arquivo in entrada:
        if arquivo.is_file():
            print(f'Arquivo encontrado: {arquivo.name}')

# Exemplo de como visualizar o nome dos arquivos do diretório
import os
with os.scandir('C:/caminho da pasta(barra ao contrário)') as entrada:
    for arquivo in entrada:
         if arquivo.is_file():
             print(f'Arquivo encontrado: {arquivo.name}')



with os.scandir('C:/Users/aluno/Downloads/teste') as entrada :
       for n in entrada: 
           if 'teste.txt':
               with open('C:/Users/aluno/Downloads/teste/teste.txt', 'r')  as t:
                    content = t.read()

# Exercício 5:  Copiar Arquivos em um Diretório
import shutil
shutil.copytree('original', 'nome da copia')
# serve para pastas -> diretórios

# Exercício 6:  Remover
import shutil
shutil.rmtree('c:/Users/aluno/Desktop/aula12/')