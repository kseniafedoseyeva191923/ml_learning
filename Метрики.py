# %%
import lasio
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import matplotlib.pyplot as plt

# %%
las = lasio.read('A15')
df = las.df()
df = df.replace(-999.25, np.nan)
df = df.dropna()

y = df['POROSITY']

X1 = df[['GAMMA']]
X1_train, X1_test, y_train, y_test = train_test_split(X1, y, test_size = 0.2, random_state=42)


model1 = LinearRegression()
model1.fit(X1_train, y_train)
y_pred1 = model1.predict(X1_test)


mae = mean_absolute_error(y_test, y_pred1)
r2 = r2_score(y_test, y_pred1)
mse = mean_squared_error(y_test, y_pred1)
rmse = np.sqrt(mse)

print(f"MAE: {mae:.8f}")
print(f"R2: {r2:.8f}")
print(f"MSE: {mse:.8f}")
print(f"RMSE: {rmse:.8f}")
# %%
X2 = df[['GAMMA', 'RESISTIVITY', 'PERM']]
X2_train, X2_test, y_train, y_test = train_test_split(X2, y, test_size = 0.2, random_state=42)

model2 = LinearRegression()
model2.fit(X2_train, y_train)
y_pred2 = model2.predict(X2_test)


mae2 = mean_absolute_error(y_test, y_pred2)
r22 = r2_score(y_test, y_pred2)
mse2 = mean_squared_error(y_test, y_pred2)
rmse2 = np.sqrt(mse2)

print(f"MAE: {mae2:.8f}")
print(f"R2: {r22:.8f}")
print(f"MSE: {mse2:.8f}")
print(f"RMSE: {rmse2:.8f}")

# %%
plt.figure(figsize=(8, 6))

# Точки: x = реальное, y = предсказанное
plt.scatter(y_test, y_pred2, alpha=0.5, color='blue')

# Красная линия = идеальное предсказание
plt.plot([y_test.min(), y_test.max()],
        [y_test.min(), y_test.max()],
        color='red', linewidth=2, label='Идеал')

plt.xlabel('Реальные значения POROSITY')
plt.ylabel('Предсказанные значения POROSITY')
plt.title('Реальные vs Предсказанные — модель 2')
plt.legend()
plt.grid(True)
plt.show()
# %%
