# %%
import lasio
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.patches import Patch
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, f1_score, classification_report

# %% Загрузка скважин
las10 = lasio.read('wells/A10')
df10 = las10.df().replace(-999.25, np.nan)

las15 = lasio.read('wells/A15')
df15 = las15.df().replace(-999.25, np.nan)

las16 = lasio.read('wells/A16')
df16 = las16.df().replace(-999.25, np.nan)

print('A10:', df10.shape)
print('A15:', df15.shape)
print('A16:', df16.shape)
print('Распределение LITH до очистки:')
print('A10')
print(df10['LITH'].value_counts(dropna=False).sort_index())
print('A15')
print(df15['LITH'].value_counts(dropna=False).sort_index())
print('A16')
print(df16['LITH'].value_counts(dropna=False).sort_index())

print('Пропуски до dropna:')
print('A10:', df10.isna().sum().sum(), 'из', len(df10))
print('A15:', df15.isna().sum().sum(), 'из', len(df15))
print('A16:', df16.isna().sum().sum(), 'из', len(df16))

df10 = df10.dropna()
df15 = df15.dropna()
df16 = df16.dropna()

# Рабочая геологическая интерпретация числовых классов
df10['LITH_GEO'] = df10['LITH'].map({1.0: 'clay', 2.0: 'siltstone', 3.0: 'sandstone'})
df15['LITH_GEO'] = df15['LITH'].map({0.0: 'clay', 1.0: 'siltstone', 2.0: 'siltstone', 3.0: 'sandstone'})
df16['LITH_GEO'] = df16['LITH'].map({1.0: 'siltstone', 2.0: 'clay', 3.0: 'sandstone'})

print('Рабочая геологическая разметка:')
for name, df in [('A10', df10), ('A15', df15), ('A16', df16)]:
    print(name)
    print(pd.crosstab(df['LITH'], df['LITH_GEO']))

print('Строки после dropna:')
print('A10:', len(df10))
print('A15:', len(df15))
print('A16:', len(df16))

# %% Статистика по литологии
columns = ['GAMMA', 'RESISTIVITY', 'PERM', 'POROSITY']

print('Статистика A10 по LITH_GEO:')
print(df10.groupby('LITH_GEO')[columns].describe())

print('Статистика A15 по LITH_GEO:')
print(df15.groupby('LITH_GEO')[columns].describe())

print('Статистика A16 по LITH_GEO:')
print(df16.groupby('LITH_GEO')[columns].describe())

# %% Выделение коллекторов
for df in [df10, df15, df16]:
    df['TYPE'] = 'неколлектор'
    df.loc[
        (df['GAMMA'] < 60) &
        (df['RESISTIVITY'] > 10) &
        (df['POROSITY'] > 0.0019),
        'TYPE',
    ] = 'коллектор'
    df.loc[
        (df['PERM'] > 0.003) &
        (df['POROSITY'] > 0.002),
        'TYPE',
    ] = 'другое'

for name, df in [('A10', df10), ('A15', df15), ('A16', df16)]:
    collector_rule = (
        (df['GAMMA'] < 60) &
        (df['RESISTIVITY'] > 10) &
        (df['POROSITY'] > 0.0019)
    )
    other_rule = (
        (df['PERM'] > 0.003) &
        (df['POROSITY'] > 0.002)
    )
    print(f'Пересечение правил TYPE {name}:', (collector_rule & other_rule).sum())

print('Типы интервалов A10:')
print(df10['TYPE'].value_counts())
print('Типы интервалов A15:')
print(df15['TYPE'].value_counts())
print('Типы интервалов A16:')
print(df16['TYPE'].value_counts())

# %% Признаки
X_train = pd.concat([
    df15[['GAMMA', 'RESISTIVITY', 'PERM', 'POROSITY']],
    df16[['GAMMA', 'RESISTIVITY', 'PERM', 'POROSITY']],
])
y_train = pd.concat([df15['LITH_GEO'], df16['LITH_GEO']])
X_test = df10[['GAMMA', 'RESISTIVITY', 'PERM', 'POROSITY']]
y_test = df10['LITH_GEO']

print('Train: A15 и A16')
print('Test: A10')
print(X_train.shape)
print(X_test.shape)
print(y_train.value_counts())

# %% Дерево решений
model = DecisionTreeClassifier(
    max_depth=6,
    class_weight='balanced',
    random_state=42,
)
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
print(f'Accuracy дерева: {accuracy_score(y_test, y_pred):.4f}')
print(f'Macro-F1 дерева: {f1_score(y_test, y_pred, average="macro"):.4f}')
print(classification_report(y_test, y_pred, zero_division=0))

# %% Случайный лес
model = RandomForestClassifier(
    n_estimators=100,
    class_weight='balanced',
    random_state=42,
)
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
print(f'Accuracy леса: {accuracy_score(y_test, y_pred):.4f}')
print(f'Macro-F1 леса: {f1_score(y_test, y_pred, average="macro"):.4f}')
print(classification_report(y_test, y_pred, zero_division=0))

# %% График
collector = (
    (df10['GAMMA'] < 60) &
    (df10['RESISTIVITY'] > 10) &
    (df10['POROSITY'] > 0.0019)
)
true_collector = df10['TYPE'] == 'коллектор'

fig, (ax1, ax2, ax3) = plt.subplots(
    1,
    3,
    sharey=True,
    figsize=(13, 10),
)

ax1.plot(df10['GAMMA'], df10.index, color='red', label='Гамма каротаж')
ax1.fill_betweenx(
    df10.index,
    0,
    df10['GAMMA'].max(),
    where=df10['GAMMA'] < 60,
    color='green',
    alpha=0.3,
)

ax2.plot(
    df10['RESISTIVITY'],
    df10.index,
    color='yellow',
    label='Сопротивление',
)
ax2.fill_betweenx(
    df10.index,
    0,
    df10['RESISTIVITY'].max(),
    where=df10['RESISTIVITY'] > 10,
    color='green',
    alpha=0.3,
)

ax3.plot(df10['POROSITY'], df10.index, color='black', label='Пористость')
ax3.fill_betweenx(
    df10.index,
    0,
    df10['POROSITY'].max(),
    where=df10['POROSITY'] > 0.0019,
    color='green',
    alpha=0.3,
)

for ax in [ax1, ax2, ax3]:
    ax.fill_betweenx(
        df10.index,
        ax.get_xlim()[0],
        ax.get_xlim()[1],
        where=collector,
        color='purple',
        alpha=0.4,
    )
    ax.fill_betweenx(
        df10.index,
        ax.get_xlim()[0],
        ax.get_xlim()[1],
        where=true_collector,
        color='orange',
        alpha=0.2,
        hatch='///',
    )
    ax.grid()

legend_handles = [
    Patch(facecolor='green', alpha=0.3, label='Условие этой кривой'),
    Patch(facecolor='purple', alpha=0.4, label='Совпали все условия'),
    Patch(facecolor='orange', alpha=0.2, hatch='///', label='Потенциально нефтенасыщенный интервал'),
]
ax1.legend(handles=legend_handles, loc='best')

ax1.invert_yaxis()
ax1.set(xlabel='Гамма каротаж, gAPI', ylabel='Глубина, м')
ax2.set(xlabel='Сопротивление, ohm.m')
ax3.set(xlabel='Пористость, m3/m3')
fig.suptitle('Планшет скважины A10')
plt.tight_layout()
plt.show()



