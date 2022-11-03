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
