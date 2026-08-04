# %%
import seaborn as sns
import lasio
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler, StandardScaler
# %%
las = lasio.read('A15')
df = las.df()
df = df.replace(-999.25, np.nan)
# %%
scaler = MinMaxScaler()
cols = ['GAMMA', 'RESISTIVITY', 'POROSITY']
df_scaled = df[cols].copy()
df_scaled[cols] = scaler.fit_transform(df[cols])

print("До нормализации:")
print(df[cols].head())
print("\nПосле нормализации:")
print(df_scaled.head())
# %%
standard = StandardScaler()
cols1 = ['GAMMA', 'RESISTIVITY', 'POROSITY']
df_standart = df[cols1].copy()
df_standart[cols1] = standard.fit_transform(df[cols1])

print("До нормализации:")
print(df[cols1].head())
print("\nПосле нормализации:")
print(df_standart.head())

fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize = (15,5))
sns.histplot(data=df_standart, x= 'GAMMA',   bins=30, ax=ax1)
sns.histplot(data=df_standart, x='RESISTIVITY', bins=30, ax=ax2)
sns.histplot(data=df_standart, x='POROSITY', bins=30, ax=ax3)

plt.tight_layout()
plt.show()

fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(15, 5))

sns.boxplot(data=df, y='GAMMA', ax=ax1)
sns.boxplot(data=df, y='RESISTIVITY', ax=ax2)
sns.boxplot(data=df, y='POROSITY', ax=ax3)

plt.tight_layout()
plt.show()

for col in ['GAMMA', 'RESISTIVITY', 'POROSITY']:
    mean = df[col].mean()
    median = df[col].median()
    print(f"{col}: среднее={mean:.3f}, медиана={median:.3f}, разница={abs(mean-median):.3f}")
# %%
fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(15, 5))

sns.histplot(data=df_scaled, x= 'GAMMA',   bins=30, ax=ax1)
sns.histplot(data=df_scaled, x='RESISTIVITY', bins=30, ax=ax2)
sns.histplot(data=df_scaled, x='POROSITY', bins=30, ax=ax3)

plt.tight_layout()
plt.show()

fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(15, 5))

sns.boxplot(data=df, y='GAMMA', ax=ax1)
sns.boxplot(data=df, y='RESISTIVITY', ax=ax2)
sns.boxplot(data=df, y='POROSITY', ax=ax3)

plt.tight_layout()
plt.show()

for col in ['GAMMA', 'RESISTIVITY', 'POROSITY']:
    mean = df[col].mean()
    median = df[col].median()
    print(f"{col}: среднее={mean:.3f}, медиана={median:.3f}, разница={abs(mean-median):.3f}")
# %%
