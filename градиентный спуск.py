#%%
import lasio
import numpy as np 
import matplotlib.pyplot as plt
#%% 
las = lasio.read('A15')
df = las.df().replace(-999.25, np.nan).dropna()

x = df['GAMMA'].values
y = df['POROSITY'].values

x = (x-x.mean()) / x.std()
print(x[:5])
print(x.mean(), x.std())
# %%
a = 0
b = 0
learning_rate= 0.01
epochs = 1000
n = len(x)
history_MSE = []

for epoch in range(epochs):
    pred = a * x + b
    
    grad_a = (-2/n) * np.sum(x * (y - pred))
    grad_b = (-2/n) * np.sum(y - pred)
    a = a - learning_rate * grad_a
    b = b - learning_rate * grad_b
    
    history_MSE.append(np.mean((y-pred)**2))
    
    if epoch % 200 == 0:
        mse = np.mean((y-pred)**2)
        print((f"Эпоха {epoch}: a={a:.6f}, b={b:.6f}, MSE={mse:.8f}"))

print(f"\nФинальные коэффициенты: a={a:.6f}, b={b:.6f}")

plt.plot(history_MSE)
plt.xlabel('Эпоха')
plt.ylabel('MSE')
plt.title('Как ошибка уменьшается во время обучения')
plt.show




# %%
