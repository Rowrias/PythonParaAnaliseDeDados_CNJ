from ast import Del


arq = open("modulo5a.txt", "a")
lista_compras= ['maça', 'abacaxi', 'pera']

cond = True
while(cond):
    item = input("Você deseja incluir, remover, substituir ou sair da lista de compras?\nSe deseja incluir aperte 'i', se deseja remover aperte 'r', se deseja substituir aperte 's' e se deseja sair aperte 'q': ")
    if (item == 'q'):
        cond = False
    elif (item == 'i'):
        item = input("Qual item deseja colocar?: ")
        lista_compras.append(item)
        arq = open("modulo5a.txt", "a")
        arq.write(str(item))
        arq.write(';')
        arq.write('\n')
        arq.close()
        for x in lista_compras:
            print(x)
        
    elif (item == 'r'):
        item = input("Qual item deseja remover?: ")
        lista_compras.remove(item)
        arq = open("modulo5a.txt", "a")
        arq.Del(str(item))
        arq.Del(';')
        arq.Del('\n')
        arq.close()
        for list in lista_compras:            
            print(list)
            
    elif (item == 's'):
        item = input("Qual item deseja substituir?: ")
        lista_compras.remove(item)
        item = input("Qual item deseja colocar?: ")
        lista_compras.insert(item)


