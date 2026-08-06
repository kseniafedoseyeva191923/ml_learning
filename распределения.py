# %%
import numpy as np 
import matplotlib.pyplot as plt 
import lasio 
from scipy.stats import binom
from scipy.stats import poisson
# %%
data = np.random.normal(loc=100, scale=15, size=1000)

plt.hist(data, bins=30)
plt.show()

print(f"Среднее: {data.mean():.2f}")
# %%
mean = data.mean()
std = data.std()

within_1std = ((data > mean - std) & (data < mean + std)).mean() * 100
within_2std = ((data > mean - 2*std) & (data < mean + 2*std)).mean() * 100

print(f"В пределах ±1 std: {within_1std:.1f}%")
print(f"В пределах ±2 std: {within_2std:.1f}%")
# %%
las = lasio.read('A15')
df = las.df().replace(-999.25, np.nan).dropna()
gamma = df['GAMMA'].values

plt.hist(gamma, bins = 30)
plt.show()

print(f"Среднее: {gamma.mean():.2f}")
print(f"Std: {gamma.std():.2f}")

# %%
mean = gamma.mean()
std = gamma.std()
within_std = ((data > mean - std) & (data < mean + std)).mean() * 100
print(f"В пределе 1std: {within_std:.2f} %")
# %%
n = 10
p = 0.5

x = np.arange(0, 11)
probabilities = binom.pmf(x, n, p)

plt.bar(x, probabilities)
plt.xlabel('Количество орлов')
plt.ylabel('Вероятность')
plt.show()
# %%
lam = 3

x1 = np.arange(0, 15)
probabilities1 = poisson.pmf(x1, lam)

plt.bar(x1, probabilities1)
plt.xlabel('Количество клиентов')
plt.ylabel('Вероятность')
plt.show()
# %%
las15 = lasio.read('A15')
df15= las15.df().replace(-999.25, np.nan).dropna()

las16 = lasio.read('A16')
df16 = las16.df().replace(-999.25, np.nan).dropna()

plt.hist(df15['GAMMA'], bins = 30, density = True, alpha = 0.5, label = 'A15')
plt.hist(df16['GAMMA'], bins = 30, density = True, alpha = 0.5, label = 'A16')
plt.legend()
plt.show()

# %%
