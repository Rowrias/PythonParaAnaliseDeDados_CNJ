import matplotlib.pyplot as plt
import numpy as np

x = np.array([2,1,1,4,5,3,3,4,4,5,5,5,6,7,7,7])

plt.hist(x, bins=7, edgecolor='white')
plt.show()