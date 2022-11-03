lista_compras= ['1', '2', '3']

cond = True
while(cond):
    item = input("Você deseja incluir, remover, substituir ou sair da lista de compras?\nSe deseja incluir aperte 'i', se deseja remover aperte 'r', se deseja substituir aperte 's' e se deseja sair aperte 'q': ")
    if (item == 'q'):
        cond = False
    elif (item == 'i'):
        item = input("Qual item deseja colocar?: ")
        lista_compras.append(item)
        for x in lista_compras:
            print(list(x))
    elif (item == 'r'):
        item = input("Qual item deseja remover?: ")
        lista_compras.remove(item)
        for list in lista_compras:
            print(list)
    elif (item == 's'):
        item = input("Qual item deseja substituir?: ")
        lista_compras.remove(item)
        item = input("Qual item deseja colocar?: ")
        lista_compras.insert(item)
