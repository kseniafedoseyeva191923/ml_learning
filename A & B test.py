# %%
from statsmodels.stats.proportion import proportions_ztest
from statsmodels.stats.power import NormalIndPower
from statsmodels.stats.proportion import proportion_effectsize

successes = [45, 58]      # купили: старая, новая версия
totals = [500, 520]       # всего посетителей: старая, новая версия

z_stat, p_value = proportions_ztest(successes, totals)

print(f"Z-статистика: {z_stat:.4f}")
print(f"p-value: {p_value:.4f}")

# %%
from scipy.stats import chi2_contingency

table = [
    [120, 380],
    [150, 350],
    [90, 410]
]

chi2, p_value, dof, expected = chi2_contingency(table)

print(f"Chi2: {chi2:.4f}")
print(f"p-value: {p_value:.4f}")
# %%
