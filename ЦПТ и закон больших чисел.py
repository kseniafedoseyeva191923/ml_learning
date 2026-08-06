# %%
import numpy as np
import matplotlib.pyplot as plt
import lasio

np.random.seed(42)
coin_flips = (np.random.choice([0, 1], size = 10000))
summ = np.cumsum(coin_flips)
print(summ)
# %%
counts = np.arange(1, 10001)
running_mean = summ / counts

plt.plot(running_mean)
plt.axhline(0.5, color='red', linestyle='--', label='Истинная вероятность 0.5')
plt.xlabel('Количество подбрасываний')
plt.ylabel('Среднее (доля орлов)')
plt.legend()
plt.show()

# %%
means = []
for i in range(1000):
    kubik = np.random.choice([1, 2, 3, 4, 5, 6], size = 30)
    mean_kubik = kubik.mean()
    means.append(mean_kubik)
    
print(means)
# %%
plt.hist(means, bins = 30)
plt.xlabel('Среднее значение 30 бросков')
plt.ylabel('Количество')
plt.title('Распределение средних (ЦПТ)')
plt.show()

# %%
las = lasio.read('A15')
df = las.df().replace(-999.25, np.nan).dropna()

gamma = df['GAMMA']

means_gamma = []
for i in range(1000):
    gamma_random = np.random.choice(gamma, size = 30)
    mean_gamma_random = gamma_random.mean()
    means_gamma.append(mean_gamma_random)
    
plt.hist(means_gamma, bins = 30)
plt.xlabel('Среднее значение 30')
plt.ylabel('Количество')
plt.title('Распределение средних (ЦПТ)')
plt.show()
# %%
