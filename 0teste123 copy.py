import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

dados = pd.read_csv("dados.csv",delimiter=';')

sns.relplot(data=dados, size="Dado2", hue="Dado3", style="Dado3", col="Dado4", x="Dado1", y="Dado2")
plt.show()