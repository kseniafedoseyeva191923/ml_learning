# %%
import numpy as np
import matplotlib.pyplot as plt
import lasio

np.random.seed(42)
coin_flips = (np.random.choice([0, 1], size = 10000))
summ = np.cumsum(coin_flips)
print(summ)
# %%
counts = np.arange(1, 10001)
running_mean = summ / counts

plt.plot(running_mean)
plt.axhline(0.5, color='red', linestyle='--', label='Истинная вероятность 0.5')
plt.xlabel('Количество подбрасываний')
plt.ylabel('Среднее (доля орлов)')
plt.legend()
plt.show()

# %%
means = []
for i in range(1000):
    kubik = np.random.choice([1, 2, 3, 4, 5, 6], size = 30)
    mean_kubik = kubik.mean()
    means.append(mean_kubik)
    
print(means)
# %%
plt.hist(means, bins = 30)
plt.xlabel('Среднее значение 30 бросков')
plt.ylabel('Количество')
plt.title('Распределение средних (ЦПТ)')
plt.show()

# %%
las = lasio.read('A15')
df = las.df().replace(-999.25, np.nan).dropna()

gamma = df['GAMMA']

means_gamma = []
for i in range(1000):
    gamma_random = np.random.choice(gamma, size = 30)
    mean_gamma_random = gamma_random.mean()
    means_gamma.append(mean_gamma_random)
    
plt.hist(means_gamma, bins = 30)
plt.xlabel('Среднее значение 30')
plt.ylabel('Количество')
plt.title('Распределение средних (ЦПТ)')
plt.show()
# %%
spisok = [45, 62, 130, 78, 55, 200, 61]
for i in spisok:
    if i > 100:
        print(spisok.index(i))
        break
    elif i < 100:
        pass
    else :
        print("-1")

# %%
poristost = {"A15": 0.18, "A16": 0.22, "A10": 0.15, "A12": 0.25, "A14": 0.19}
max_key = None
max_value = -float("inf")
for key, value in poristost.items():
    if value > max_value:
        max_value = value
        max_key = key
        
print(max_key)
        
# %%
gamma = {
    "interval_1": 85,
    "interval_2": 42,
    "interval_3": 120,
    "interval_4": 38,
    "interval_5": 95}

def find_min_key(gamma):
    min_key = None
    min_value = float("inf")
    for key, value in gamma.items():
        if value < min_value:
            min_value = value
            min_key = key
    return min_key

print(find_min_key(gamma))
# %%
resistivity = [12, 8, 45, 3, 67, 21, 9, 88, 15]

def count_above_threshold(values, threshold):
    counter = 0
    for value in values:
        if value > threshold:
            counter += 1
    return counter

print(count_above_threshold(resistivity, 20))
# %%
values = [15, 22, 15, 8, 22, 30, 8, 15]
def count_unique(values):
    unikals = set(values)
    kolvo = len(unikals)
    return kolvo
print(count_unique(values))
# %%
spisok = [3, 7, 2, 9, 4, 1, 8]
def second_largest(values):
    max_int = -float("inf")
    vtor_int = -float("inf")
    for value in values:
        if value > max_int:
            vtor_int = max_int
            max_int = value
        elif value < max_int and value > vtor_int:
            vtor_int = value
    return max_int, vtor_int
print(second_largest(spisok))
# %%
depths = [120, None, 135, 140, None, None, 150]
def count_missing(values):
    propusk = 0
    for value in values:
        if value is None:
            propusk += 1
    return propusk
print(count_missing(depths))
# %%
name = "  a15 Well   "
def clean_well_nane(name):
    result = name.strip().upper().split()[0]
    return result
print(clean_well_nane(name))
# %%
wells = ["  a15", "A16 ", " a10", "A12", "  a14  "]
def clean_all_wells(wells):
    clean_name_wells = []
    for well in wells:
        ideal = well.strip().upper()
        clean_name_wells.append(ideal)
    return clean_name_wells
print(clean_all_wells(wells))
# %%
wells = ["A15", "A16", "A15", "A10", "A16", "A15", "A12"]
def find_duplicates(wells):
    counts = {}
    for well in wells:
        if well in counts:
            counts[well] += 1
        else:
            counts[well] = 1
    itog = []
    for welle in counts:
        if counts[welle] > 1:
            itog.append(welle)
    return itog

print(find_duplicates(wells))
# %%
values = [0.10, 0.14, 0.18, 0.22, 0.25, 0.31]
def find_pair_sum(values, target):
    left = 0
    rigth = len(values)-1
    while left < rigth:
        total = values[left] + values[rigth]
        if abs(total - target) < 1e-9:
            return (values[left], values[rigth])
        elif total > target:
            rigth -= 1
        elif total < target:
            left += 1
    return None

print(find_pair_sum(values, 0.24))
# %%
