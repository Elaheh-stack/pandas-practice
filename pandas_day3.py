import pandas as pd

df = pd.read_csv("airtravel.csv")

filtered = df[df['1958'] > 400]
print(filtered)
