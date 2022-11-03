import numpy as np

#1
array = np.array([[4, 5, 6], [7, 8, 9]])
for linha in array:
    for coluna in linha:
        print(coluna, end=' ')
    print()

print("Item na linha 1, coluna 2: ", array[1][2])

#2
vetor = np.array([1,7,2,3,4])
matriz = np.array([[4,5,6],[7,8,9]])

print(vetor.ndim, vetor.shape, vetor.dtype, vetor.size)
print(matriz.ndim, matriz.shape, matriz.dtype, matriz.size)