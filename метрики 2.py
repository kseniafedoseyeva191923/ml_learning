#%%
import lasio
import numpy as np 
# %%
las = lasio.read('A15')
df = las.df().replace(-999.25, np.nan).dropna()

x = df['GAMMA'].values
y = df['POROSITY'].values

a = -0.000421
b = 0.001554

x = (x-x.mean()) / x.std()

pred = a * x + b

mae = np.mean(np.abs(y - pred))
mse = np.mean((y - pred)**2)
rmse = np.sqrt(mse)

ss_res = np.sum((y - pred)**2)
ss_tot = np.sum((y - y.mean())**2)
r2 = 1 - ss_res/ss_tot

print(f"MAE: {mae:.8f}")
print(f"MSE: {mse:.8f}")
print(f"RMSE: {rmse:.8f}")
print(f"R²: {r2:.4f}")
# %%
