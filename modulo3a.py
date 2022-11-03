lista_compras = ["maçãs", "leite", "arroz", "frango", "trigo"]
for x in lista_compras:
    print("Preciso comprar:", x)

print("O primeiro item que preciso comprar é:", lista_compras[1])
print("O segundo item que preciso comprar é:", lista_compras[0])

tamanho = len(lista_compras)
print("A lista de compras possui:", tamanho, "itens")

for i in range(len(lista_compras)):
    print("O elemento", i, "da lista é", lista_compras[i])
    print(lista_compras[i])

i = 0
while i < len(lista_compras):
    print("O elemento", i, "da lista é",lista_compras[i])
    i = i + 1

