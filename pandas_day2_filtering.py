import pandas as pd

# Read CSV file
df = pd.read_csv("airtravel.csv")

# Filter rows where 1958 value is greater than 400
filtered = df[df["1958"] > 400]

# Show result in terminal
print(filtered)

# Save filtered result to a new CSV file
filtered.to_csv("filtered_report.csv", index=False)

print("Filtered report created successfully.")
