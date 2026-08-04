#%% 
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

A15 = pd.read_csv('A15', skiprows=32, sep=r'\s+', header=None, names=['DEPTH', 'GR', 'Perm', 'Porosity', 'Resistivity', 'LITH'])
A15 = A15.replace(-999.25, np.nan)
fig, (ax1, ax2, ax3) = plt.subplots(1, 3, sharey=True)
ax1.plot(A15['GR'], A15['DEPTH'], color = 'red', label = 'Гамма-каротаж')
ax2.plot(A15['Resistivity'], A15['DEPTH'], color = 'yellow', label = 'Сопротивление')
ax3.plot(A15['Porosity'], A15 ['DEPTH'], color = 'green', label = 'Пористость')
ax1.invert_yaxis() 

fig.suptitle("Каротаж скважины A15")

ax1.set_xlabel("Гамма-каротаж, мкр/ч")
ax1.set_ylabel("Глубина, м")
ax1.grid()
ax1.legend()

ax2.set_xlabel("Сопротивление, Ом")
ax2.grid()
ax2.legend()

ax3.set_xlabel("Пористость, мкД")
ax3.grid()
ax3.legend()
plt.show()
# %%
