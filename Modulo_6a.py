# NumPy
# (NUMerical PYthon)

# Biblioteca para Python para lidar com vetores e matrizes 
# “grandes” e de múltiplas dimensões
# Mitiga muitas das ineficiências computacionais do Python 
# quando lidando com esse tipo de dado.

# Algumas vantagens do NumPy
# ▸ Estrutura de dados eficiente para armazenar e operar em 
# arrays (vetores/matrizes)
# ▸ Funções matemáticas prontas para operar em arrays
# ▸ Funções para carga e descarga de dados de/para o disco
# ▸ Funções de álgebra, geração de números aleatórios, 
# transformadas, …

# instale via pip, depois de instalar basta importar.

import numpy as np

#criando a partir de uma lista
lista = [1,2,3]
array1 = np.array(lista)
print("Elemento em zero: ", array1[0])
for item in array1:
    print(item)

#criando diretamente
array2 = np.array([4,5,6])
for item in array2:
    print(item)

# É possível iterar nos itens da matriz, ou acessar diretamente via o operador []
print("via operador:")
import numpy as np

#criando diretamente
array = np.array([[4,5,6],[7,8,9]])
for linha in array:
    for coluna in linha:
        print(coluna, end=' ')
    print()
print("Item na linha 1, coluna 2: ", array[1][2])

# Arrays NumPy possuem algumas propriedades que podem ser acessadas
#dtype: qual o tipo dos dados do array
#shape: qual o formato (dimensões) do array
#size: tamanho total do array
#ndim: número de dimensões
print("Propriedade que podem ser acessado:")
import numpy as np
vetor = np.array([1.7,2,3,4])
matriz = np.array([[4,5,6],[7,8,9]])
print(vetor.ndim, vetor.shape, vetor.dtype, vetor.size)
print(matriz.ndim, matriz.shape, matriz.dtype, matriz.size)

# 2 - Inicialização de Arrays
# Vazio e uns

