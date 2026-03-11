
print()
print('E-COMMERCE DA MILLA')
print('Sejam bem-vindos!')
print()

carrinho = [] #lista vazia
valores = [] #lista vazia

ecommerce ={ #o dicionário foi aberto

#colocar os produtos que tenho:
'shampoo': 30,
'condicionador': 25,


}#fechei o dicionário


produto_escolhido = input('Deseja comprar um shampoo ou condicionador?')


carrinho.append(produto_escolhido)
valores.append(ecommerce[produto_escolhido])

print('Em seu carrinho há o produto', carrinho)
print('O valor é de',valores)