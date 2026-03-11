import random #criar aleatoriedade



maquina = ['','✂️','🪨','🧻'] #lista de ícones - 1 ->


escolha_maquina = random.choice(maquina[1:]) #escolha


id_maquina = maquina.index(escolha_maquina)#posicao dos indices da lista


minhas = ['','✂️','🪨','🧻']




print("Escolha '✂️ - 1' , '🪨 - 2, '🧻 - 3'")



minha_escolha = int(input('Escolha o objeto  ->'))


if minha_escolha == id_maquina:
    print('EMPATE😫😫😫😫😫!!!')
    print('Minha escolha -', minhas[minha_escolha])
    print('Escolha da máquina -', escolha_maquina)

elif id_maquina == 1 and minha_escolha == 3:
    print('VITÓRIA DA MÁQUINA😭😭😭😭😭!!!')
    print('Minha escolha -', minhas[minha_escolha])
    print('Escolha da máquina -', escolha_maquina)

elif id_maquina == 2 and minha_escolha == 1:
    print('VITÓRIA DA MÁQUINA😭😭😭😭😭!!!')
    print('Minha escolha -', minhas[minha_escolha])
    print('Escolha da máquina -', escolha_maquina)

elif id_maquina == 3 and minha_escolha == 2:
    print('VITÓRIA DA MÁQUINA😭😭😭😭😭!!!')
    print('Minha escolha -', minhas[minha_escolha])
    print('Escolha da máquina -', escolha_maquina)

elif id_maquina == 1 and minha_escolha == 2:
    print('SUA VITÓRIA🥰🥰🥰🥰🥰🥰!!!')
    print('Minha escolha -', minhas[minha_escolha])
    print('Escolha da máquina -', escolha_maquina)

elif id_maquina == 2 and minha_escolha == 3:
    print('SUA VITÓRIA🥰🥰🥰🥰🥰🥰!!!')
    print('Minha escolha -', minhas[minha_escolha])
    print('Escolha da máquina -', escolha_maquina)

elif id_maquina == 3 and minha_escolha == 1:
    print('SUA VITÓRIA🥰🥰🥰🥰🥰🥰!!!')
    print('Minha escolha -', minhas[minha_escolha])
    print('Escolha da máquina -', escolha_maquina)