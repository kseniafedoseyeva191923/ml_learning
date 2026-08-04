# %%
import lasio
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# %%
las = lasio.read('A15')
df = las.df()
df = df.replace(-999.25, np.nan)

collector = (
    (df['GAMMA'] < 60) &
    (df['RESISTIVITY'] > 10) &
    (df['POROSITY'] > 0.0019)
)

fig, (ax1, ax2, ax3) = plt.subplots(1, 3, sharey = True, figsize=(12, 10))

ax1.plot(df['GAMMA'], df.index, color = 'red', label = 'Гамма каротаж')
ax1.fill_betweenx(df.index, 0, df['GAMMA'].max(),
                where=(df['GAMMA'] < 60),
                color='green',alpha=0.3)
ax2.plot(df['RESISTIVITY'], df.index, color = 'yellow', label = 'Сопротивление')
ax2.fill_betweenx(df.index, 0, df['RESISTIVITY'].max(),
                where=(df['RESISTIVITY'] > 10),
                color = 'green',alpha=0.3)
ax3.plot(df['POROSITY'], df.index, color = 'green', label = 'Пористость')
ax3.fill_betweenx(df.index, 0, df['POROSITY'].max(),
                where = (df['POROSITY'] > 0.0019), 
                color = 'green', alpha = 0.3)
ax1.invert_yaxis()
fig.suptitle('Каротаж скважины А15')

ax1.set(xlabel = 'Гамма каротаж, мкр/ч', ylabel = 'Глубина, м')
ax1.grid()
ax1.legend()

ax2.set(xlabel = 'Сопротивление, Ом')
ax2.grid()
ax2.legend()

ax3.set(xlabel = 'Пористость, мкрД')
ax3.grid()
ax3.legend()

plt.draw() 

for ax in [ax1, ax2, ax3]:
    ax.fill_betweenx(df.index, 
                    ax.get_xlim()[0], ax.get_xlim()[1],
                    where=collector,
                    color='purple', alpha=0.4,
                    label='Коллектор')

plt.tight_layout()
plt.show()
# %%
