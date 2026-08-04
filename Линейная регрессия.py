# %%
import lasio
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score
import matplotlib.pyplot as plt
# %%
las = lasio.read('A15')
df = las.df()
df = df.replace(-999.25, np.nan)
df = df.dropna()
X = df[['GAMMA', 'RESISTIVITY']]
y = df['POROSITY']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state=42)
print(f"Количество X_train: {len(X_train)}")
print(f"Количество X_test: {len(X_test)}")
print(f"Количество y_train: {len(y_train)}")
print(f"Количество y_test: {len(y_test)}")
# %%
model = LinearRegression()
model.fit(X_train, y_train)
# %%
print(f"Коэффициент GAMMA: {model.coef_[0]:.6f}")
print(f"Коэффициент RESISTIVITY: {model.coef_[1]:.6f}")
print(f"Свободный член b: {model.intercept_:.6f}")
# %%
y_pred = model.predict(X_test)
print(y_pred[:5])
print(y_test.values[:5])
# %%
mae = mean_absolute_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f"MAE: {mae:.6f}")
print(f"R²: {r2:.4f}")
# %%
plt.scatter(X_test['GAMMA'], y_test, color='blue', label='Реальные', alpha=0.5)
plt.scatter(X_test['GAMMA'], y_pred, color='red', label='Модель', alpha=0.5)
plt.xlabel('GAMMA')
plt.ylabel('POROSITY')
plt.legend()
plt.show()
# %%
