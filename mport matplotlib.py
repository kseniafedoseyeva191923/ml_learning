import matplotlib.pyplot as plt

# 1. Создаем фигуру
plt.figure(figsize=(6, 10))

# 2. Рисуем основную кривую ГК (серым цветом)
plt.plot(df['GAMMA'], df['DEPTH'], color='gray', alpha=0.5, label='Исходный ГК')

# 3. Рисуем только песчаники (выделяем их ярким цветом, например, желтым)
plt.scatter(sands['GAMMA'], sands['DEPTH'], color='gold', s=10, label='Песчаник (< 60 API)')

# 4. Настройка графика
plt.gca().invert_yaxis()  # Глубина идет сверху вниз
plt.axvline(x=60, color='red', linestyle='--', label='Линия отсечки')
plt.xlabel('Gamma Ray (API)')
plt.ylabel('Depth (m)')
plt.title('Выделение песчаников по ГК')
plt.legend()
plt.grid(True, linestyle=':', alpha=0.6)

plt.show()