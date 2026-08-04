# %% Импорт, загрузка
import pandas as pd
import numpy as np

A15 = pd.read_csv('A15', skiprows=32, sep=r'\s+', header=None, names=['DEPTH', 'GR', 'Perm', 'Porosity', 'Resistivity', 'LITH'])
A15 = A15.replace(-999.25, np.nan)

print(A15.shape)
print(A15.isnull().sum())
# %% Дубликаты. Отсутствуют
print("Дубликатов:", A15.duplicated().sum())
print(A15[A15.duplicated()])
# %% Работа с пропусками
A15_dropped = A15.dropna()
print("После удаления строк с Nan:", A15_dropped.shape)

A15_filled = A15.fillna(A15.mean())
print("После заполнения средним:")
print(A15_filled.isnull().sum())

A15_ffill = A15.fillna(method= 'ffill')
print("После ffill:")
print(A15_ffill.isnull().sum())

A15_clean = A15.ffill().bfill()
print(A15_clean.isnull().sum())
# %% Выбросы
mean_gr = A15['GR'].mean()
std_gr = A15['GR'].std()

outliers = A15 [ 
    (A15['GR'] > mean_gr + 3 * std_gr) |
    (A15['GR'] < mean_gr - 3 * std_gr)
]
print(f"Среднее ГК: {mean_gr:.1f}")
print(f"Стандартное отклонение: {std_gr:.1f}")
print(f"Порог выброса: выше {mean_gr + 3 * std_gr:.1f} или ниже {mean_gr - 3 * std_gr:.1f}")
print(f"Выбросов найдено: {len(outliers)}")
print(outliers)

mean_r = A15['Resistivity'].mean()
std_r = A15['Resistivity'].std()

outliers_r = A15[
    (A15['Resistivity'] > mean_r + 3 * std_r) |
    (A15['Resistivity'] < mean_r - 3 * std_r)
]

print(f"Среднее сопротивления: {mean_r:.2f}")
print(f"Стд. отклонение: {std_r:.2f}")
print(f"Порог: выше {mean_r + 3*std_r:.2f}")
print(f"\nВыбросов найдено: {len(outliers_r)}")
print(outliers_r[['DEPTH', 'GR', 'Resistivity', 'LITH']])
# %%
