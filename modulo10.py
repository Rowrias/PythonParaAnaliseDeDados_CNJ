import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

petro_df = pd.read_csv("PETR3.SA.csv", delimiter=',', usecols=["Adj Close"])
petro_df.insert(0, "Index", range(0, len(petro_df)))

sns.regplot(data=petro_df, x="Index", y="Adj Close");
plt.show()