# Modulo 4 
# Matrizes

#Enquanto um array é uma estrutura para armazenar dados de 
#forma “linear”, uma matriz é um array bi-dimensional
#Um array bi-dimensional é um array dentro de outro array.
#Logo, a matriz e uma lista de listas.

Matriz = [ ["e00", "e01", "e02"], ["e10", "e11", "e12"] ]
print(Matriz)

Matriz = [[0, 1, 2], 
          [3, 4, 5]]

print(Matriz)
print(Matriz[0]) # imprime os elementos da linha 0
print(Matriz[1]) # imprime os elementos da linha 1
print(Matriz[1][1]) # elemento indexado pela “linha 1”, “coluna 1”

#Tipo de uma matriz:
print(type(Matriz))

#Inserção em matriz:
Matriz.append([6, 7, 8])
print(Matriz)

#Inserção posicional em Matriz
Matriz = [ [0, 1, 2], [3, 4, 5] ]
Matriz.insert(1, [6, 7, 8])
print(Matriz)

#Atualizando uma Matriz
Matriz = [ [0, 1, 2], [3, 4, 5] ]
Matriz[0] = [-3, -2, -1]
print(Matriz)
#Atualizando um elemento
Matriz[0][2] = -10
print(Matriz)

#removendo uma linha(apaga uma lista)
Matriz = [ [0, 1, 2], [3, 4, 5] ]
del(Matriz[1]) 
print(Matriz)

#Tamanho de uma Matriz
Matriz = [ [0, 1, 2], [3, 4, 5] ]
Tamanho = len(Matriz)
print(Tamanho)

#Mostra um pedaço
Matriz = [ [0, 1, 2], [3, 4, 5], [6, 7, 8], [9, 10, 11], [12, 13, 14] ]
Matriz2 = Matriz[1:4] #seleciona os varios pedaços 'entre'
print(Matriz2)

Matriz3 = Matriz[3:] # do 3 até o final
print(Matriz3)

Matriz4 = Matriz[:3] # do "2" até o começo
print(Matriz4)

print("Cópia de uma Matriz:")
print("Exemplo1")
M1 = [ [1, 1], [2, 2] ]
M2 = M1
M1[0] = [0, 0]
print(M1)
print(M2)
print("Exemplo2")
import copy
M1 = [ [1, 1], [2, 2] ]
M2 = copy.copy(M1)
M1[0] = [0, 0]
print(M1)
print(M2)
print("Exemplo3")
import copy
M1 = [ [1, 1], [2, 2] ]
M2 = copy.deepcopy(M1)
M1[0][0] = 0
print(M1)
print(M2)