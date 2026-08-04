# %% Импорт библиотек
import numpy as np
import pandas as pd

# %% Создание таблицы
data = {
    'Глубина': [1000, 1010, 1020, 1030, 1040],
    'ГК' : [45, 78, 110, 55, 33],
    'Пористость': [0.25, 0.18, 0.08, 0.22, 0.28]
}

df = pd.DataFrame(data)

print(df)
print("\nФорма таблицы:", df.shape)
print("\nТипы колонок:")
print(df.dtypes)
print("\nБыстрая статистика:")
print(df.describe())

# %% Булевая фильтрация
print(df['ГК'])
print(df[['Глубина', 'Пористость']])

глина = df[df['ГК'] > 70]
print("\nВозможно глина:")
print(глина)

песчаник = df[(df['ГК'] < 60) & (df['Пористость'] > 0.20)]
print("\nВозможно песчаник:")
print(песчаник)
# %% Загрузка реального CSV файла
df.to_csv('скважина_1.csv', index=False)
df2 = pd.read_csv('скважина_1.csv')
print(df2)
print("\nФайл загружен")

# %% Домашка
A15 = pd.read_csv('A15', skiprows=32, sep=r'\s+', header=None,
    names=['DEPTH', 'GR', 'Perm', 'Porosity', 'Resistivity', 'LITH'])

# Заменяем -999.25 на NaN
A15 = A15.replace(-999.25, np.nan)

print(A15.head())
print(A15.columns.tolist())

# %%
