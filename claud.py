import numpy as np

# Создаём массив замеров ГК (гамма-каротаж)
gk = np.array([45, 62, 78, 55, 90, 110, 48, 33, 75, 88])

print("Массив:", gk)
print("Тип:", type(gk))
print("Форма:", gk.shape)
print("Среднее ГК:", np.mean(gk))
print("Макс:", np.max(gk))
print("Мин:", np.min(gk))