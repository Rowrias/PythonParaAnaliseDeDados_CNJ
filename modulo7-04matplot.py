import matplotlib.pyplot as plt
from datetime import datetime
import numpy as np

dataPetr = np.genfromtxt('PETR3.SA.csv', delimiter=',', skip_header = 1, usecols = (0,5), converters={0: lambda x: datetime.strptime(x.decode('ascii'), "%Y-%m-%d")})
dias = np.empty((dataPetr.shape[0]), dtype=datetime)
valores = np.empty((dataPetr.shape[0]), dtype=np.float64)

i = 0
for d in dataPetr:
    dias[i] = d[0]
    valores[i] = d[1]
    i += 1

plt.plot(dias, valores, "b-.", label = "PETR3")
plt.legend(loc="upper left")
plt.ylabel("Preço (R$)")
plt.xlabel("Data")
plt.show()