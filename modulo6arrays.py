import numpy as np

vetor_zeros = np.zeros(4)
matriz_zeros = np.zeros((3,2))
matriz_uns = np.ones((5,5), dtype=np.intc)
matriz_full= np.full((5,5),6,dtype=np.intc)

print(vetor_zeros)
print(matriz_zeros)
print(matriz_uns)
print(matriz_full)

vetor1 = np.arange(10, 20, 2)
print(vetor1)

vetor2 = np.linspace(10, 20, 5)
print(vetor2)
