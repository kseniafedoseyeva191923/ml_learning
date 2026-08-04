#%% 
import pandas as pd
import numpy as np

A15 = pd.read_csv('A15', skiprows=32, sep=r'\s+', header=None,
    names=['DEPTH', 'GR', 'Perm', 'Porosity', 'Resistivity', 'LITH'])

A15 = A15.replace(-999.25, np.nan)
print(A15.shape)
print(A15.head())

# %% Разведка данных
print(A15.isnull().sum()) # Сколько пропусков в каждой колонке?
print("\nТипы литоглогии:")
print(A15['LITH'].value_counts())

# %% groupby - Группировка по литологии и расчет среднего ГК
grouped = A15.groupby('LITH').mean()
print(grouped)

print("\nСреднее ГК по типам породы:")
print(A15.groupby('LITH')['GR'].mean().round(1))

# %% Расчет средней пористости и сопротивления по группам
print("\nСредняя пористость по группам:")
print(A15.groupby('LITH')['Porosity'].mean().round(4))

print("\nСреднее сопротивление по группам:")
print(A15.groupby('LITH')['Resistivity'].mean().round(2))

# %%  Сводные таблиы
pivot = pd.pivot_table(A15,
                       values=['GR', 'Porosity', 'Resistivity'],
                       index='LITH',
                       aggfunc='mean').round(3)
print(pivot)
# %% Статистика за клик
print(A15.groupby('LITH').describe().round(2))

print("\nКоличество замеров по типам пород")
print(A15.groupby('LITH').size())

# %%
