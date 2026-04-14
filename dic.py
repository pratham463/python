import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df = pd.read_csv("Untitled spreadsheet - Sheet1.csv")
print (df.head(10))
print(df.info())
print(df.describe())
print(df.columns)
sns.pairplot(df.select_dtypes(include=[np.number]))
sns.heatmap(df.select_dtypes(include=[np.number]).corr(),annot=True)
plt.show()