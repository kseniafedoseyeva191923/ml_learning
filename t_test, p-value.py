# %%
import lasio
import numpy as np
from scipy import stats 

# %%
las15 = lasio.read('A15')
df15 = las15.df().replace(-999.25, np.nan).dropna()

las16 = lasio.read('A16')
df16 = las16.df().replace(-999.25, np.nan).dropna()

las10 = lasio.read('A10')
df10 = las10.df().replace(-999.25, np.nan).dropna()

res15 = df15['RESISTIVITY']
res16 = df16['RESISTIVITY']

por15 = df15['POROSITY']
por10 = df10['POROSITY']

perm15 = df15['PERM']
perm16 = df16['PERM']

t_stat, p_value = stats.ttest_ind(perm15, perm16)

print(f"t_статистика: {t_stat:.4f}")
print(f"p_value: {p_value:.4f}")

# %%
