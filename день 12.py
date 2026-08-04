# %% 
import sys
!{sys.executable} -m pip install seaborn
import seaborn as sns
import pandas as pd
import lasio
import matplotlib.pyplot as plt
# %%
las = lasio.read('A15')
df = las.df()
df = df.reset_index()
sns.scatterplot(data = df, x = 'GAMMA', y = 'DEPT', hue = 'LITH')
plt.show()
sns.scatterplot(data = df, x = 'GAMMA', y = 'POROSITY', hue = 'LITH')
# %%
correlation_matrix = df.corr()
sns.heatmap(data = correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f')
plt.show()

sns.pairplot(df[['GAMMA', 'POROSITY', 'RESISTIVITY', 'LITH']], hue='LITH')
plt.show()
# %%
