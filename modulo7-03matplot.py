import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0, 10, 1)
y2 = x**2 #f(x) = x^2
y3 = x**3

plt.plot(x,y2, 'b-.', label = "x^2")
plt.plot(x,y3, 'k:', label = "x^3")
plt.legend(loc='upper left')
plt.ylabel("Eixo Y")
plt.xlabel("Eixo X")
plt.show()