# %%
import sys
!{sys.executable} -m pip install lasio
import lasio
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#%%
A15 = lasio.read('A15')
print(A15)
print(f"\nМетаданные скважины: {A15.well}")
print(f"\nКривые скважины: {A15.curves}")
df = A15.df()
print(df.head())
print(df.shape)
# %%
A15_csv = pd.read_csv('A15', skiprows=32, sep=r'\s+', header=None,
    names=['DEPTH', 'GR', 'Perm', 'Porosity', 'Resistivity', 'LITH'])
print(A15_csv.columns.tolist())

A15 = lasio.read('A15')
df = A15.df()
print(df.columns.tolist())
# %%

las = lasio.read('A15')
df = las.df()
df = df.replace(-999.25, np.nan)

fig, (ax1, ax2, ax3) = plt.subplots(1, 3, sharey = True)

ax1.plot(df['GAMMA'], df.index, color = 'red', label = 'Гамма каротаж')
ax2.plot(df['RESISTIVITY'], df.index, color = 'yellow', label = 'Сопротивление')
ax3.plot(df['POROSITY'], df.index, color = 'green', label = 'Пористость')

ax1.invert_yaxis()
fig.suptitle('Каротаж скважины А15')

ax1.set(xlabel = 'Гамма-каротаж, мкр/ч', ylabel = 'Глубина, м')
ax1.grid()
ax1.legend()

ax2.set(xlabel = 'Сопротивление')
ax2.grid()
ax2.legend()

ax3.set(xlabel = 'Пористость')
ax3.grid()
ax3.legend()
# %%
