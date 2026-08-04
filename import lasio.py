# %%
import lasio
import numpy as np
from scipy import stats


# Загружаем обе скважины
las15 = lasio.read('A15')
las16 = lasio.read('A16')
las10 = lasio.read('A10')

las15 = las15.df().replace(-999.25, np.nan).dropna()
las16 = las16.df().replace(-999.25, np.nan).dropna()
las10 = las10.df().replace(-999.25, np.nan).dropna()

por15 = las15['POROSITY']
por16 = las16['POROSITY']

t_stat, p_value = stats.ttest_ind(por15, por16)
print(f"t-статистика: {t_stat:.4f}")
print(f"p-value: {p_value:.6f}")
# %%
por10 = las10['POROSITY']

mean10 = por10.mean()
sem10 = stats.sem(por10)  # стандартная ошибка среднего

ci = stats.t.interval(0.95, len(por10)-1, loc=mean10, scale=sem10)
print(f"Средняя пористость A10: {mean10*100:.2f}%")
print(f"95% доверительный интервал: [{ci[0]*100:.2f}%, {ci[1]*100:.2f}%]")
# %%
res10 = las10['RESISTIVITY']
res15 = las15['RESISTIVITY']

t_stat, p_value = stats.ttest_ind(res10, res15)
print(f"t-статистика: {t_stat:.4f}")
print(f"p-value: {p_value:.6f}")
# %%
