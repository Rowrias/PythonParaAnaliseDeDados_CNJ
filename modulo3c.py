lista_compras = [] #uma lista vazia
item = input("Digite um item ou sair: ")
while item != "sair":
    lista_compras.append(item)
    item = input("Digite um item ou sair: ")
    
for it in lista_compras:
    print(it)