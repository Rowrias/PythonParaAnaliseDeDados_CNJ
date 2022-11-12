# Modulo 4 
# Dicionário

#Dicionários se parecem com listas, mas são mais versáteis.
L1 = ["a", "b", "c"]
print(list(enumerate(L1)))

Dic = {"chave1": "valor1", "chave2": "valor2"}
print(Dic["chave2"])
# adicionando
Dic["k3"] = "x"
print(Dic)
# alterando
Dic["k3"] = "valor3"
print(Dic)
# removendo
Dic.pop("chave1")
print(Dic)
# removendo último elemento
Dic.popitem()
print(Dic)
# outra forma de remover
Dic = {"chave2": "valor2", "k3": "valor3"}
del Dic["k3"]
print(Dic)

# Remover dicionário
#del Dic
#print(Dic) # NameError: name 'Dic' is not defined

Dic = {"guarda-roupa" : 3, "televisão" : 2, "cadeira" : 4, "mesa" : 1}
# mostra todo conteudo "chave"
for chave in Dic:
    print(chave)
# mostra todo conteudo "valor"
for chave in Dic:
    print(Dic[chave])
# mostra todo conteudo "chave"
print(Dic.keys())
# mostra todo conteudo "valor"
print(Dic.values())
# mostra todo conteudo "chave" e "valor"
print(Dic.items())

# Itens em ordem - Dicionários
Dicio = {}

Dicio[2] = "a"
Dicio[1] = "d"
Dicio[3] = "r"

# na ordem q inseriu
print(Dicio) 

# Dicionario ordenado por "chave"
Lista_ordenada = dict(sorted(Dicio.items()))
print(Lista_ordenada) 

# Dicionário ordenado por "valor"
chave_ordenada = sorted(Dicio, key=Dicio.get)
dicio_ordenado = {}
print(chave_ordenada) 
for i in chave_ordenada:
    dicio_ordenado[i] = Dicio[i]
print(dicio_ordenado)

