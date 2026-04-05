import lasio
import pandas as pd

las = lasio.read("A15")

print("Кривые в этой скважине:")
print(las.keys())

df = las.df()
print(df.head())

stats = df.describe()
print(stats)

sandstone_filter = df['GAMMA'] < 60

sands = df[sandstone_filter]

print(sands.describe())

good_rocks_filter = df ['GAMMA'] < 70
good_rocks = df[good_rocks_filter]

print(good_rocks.mean())