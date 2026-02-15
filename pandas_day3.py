import pandas as pd

df = pd.read_csv("airtravel.csv")

# فیلتر برای مقادیر بالای 400 در 1958
filtered = df[df['1958'] > 400]

# خلاصه آماری
summary = filtered.describe()

print("Filtered Data:")
print(filtered)
print("\nSummary Statistics:")
print(summary)
