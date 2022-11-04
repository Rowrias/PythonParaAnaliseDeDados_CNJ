# Modulo 3
# 1 - Listas

lista_compras = ["maças", "leite", "arroz", "frango"]

# Iterando
for item in lista_compras:
    print("Preciso comprar:", item)

# Acesso por índice
print("O primeiro item que preciso comprar é:", lista_compras[0])
print("O terceiro item que preciso comprar é:", lista_compras[2])

#Qual o tamanho da lista?
tamanho = len(lista_compras)
print("A lista de compras possui:", tamanho, "itens")

# Outra forma de iterar
for i in range(len(lista_compras)):
    print("O elemento", i, "da lista é", lista_compras[i])

i = 0
while i < len(lista_compras):
    print("O elemento", i, "da lista é", lista_compras[i])
    i = i + 1

# Itervalos
lista_compras = ["maças", "leite", "arroz", "frango", "macarrão"]
sublista = lista_compras[1:4]
for item in sublista:
    print(item)

print("Outra forma")
for item in lista_compras[2:5]:
    print(item)

# Alterando
lista_compras = ["maçãs", "leite", "arroz", "frango"]
lista_compras[1] = "açúcar"
lista_compras[3] = "feijão"
for item in lista_compras:
    print(item)

# 2 - Funções de listas ( docs.python.org/pt-br/3/tutorial/datastructures.html )
# Índices e contagens
lista_compras = ["maçãs", "leite", "arroz", "frango", "leite", "trigo"]

qtde_vezes = lista_compras.count("leite") #Quantas vezes "leite aparece na lista?
idx = lista_compras.index("leite")        #Qual o primeiro índice de "leite" na lista?

print("Quantidade:", qtde_vezes)
print("Primeiro idx:", idx)

#Ordenando
lista_compras = ["maçãs", "leite", "arroz", "frango", "trigo"]
for item in lista_compras:
    print(item)
print("Ordenado Crescente")
lista_compras.sort()
for item in lista_compras:
    print(item)
print("Ordenado Decrescente")
lista_compras.sort(reverse = True)
for item in lista_compras:
    print(item)

#Excluindo por índice
lista_compras = ["maçãs", "leite", "arroz", "frango", "trigo"]
del lista_compras[1]
print("Excluindo o leite da lista:")
for item in lista_compras:
    print(item)

#Excluindo por valor
lista_compras = ["maçãs", "leite", "arroz", "frango", "trigo"]
lista_compras.remove("arroz") # Remove o primeiro elemento com o conteúdo especificado
lista_compras.pop()           # Remove o ultimo elemento
print("Excluindo por valor:")
for item in lista_compras:
    print(item)

#Inserindo
lista_compras = ["maçãs", "leite", "arroz", "frango", "trigo"]
lista_compras.insert(2, "feijão") #Insere o item na posição
lista_compras.append("tomate")    #Insere o item no final
print("Inserindo:")
print(lista_compras)

#Exemplo completo
lista_compras = [] #uma lista vazia
print("\nExemplo completo:")
item = input("Digite um item ou sair: ")
while item != "sair":
    lista_compras.append(item)
    item = input("Digite um item ou sair: ")
print(lista_compras)
for it in lista_compras:
    print(it)
