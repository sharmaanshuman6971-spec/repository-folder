import pandas as pd

# Step 1: Create sample dataset and save to CSV
data = {
    "Name": ["Alice", "Bob", "Charlie", "David", "Eva"],
    "Age": [23, 25, 22, 24, 21],
    "Score": [95, 82, 76, 88, 67],
    "Label": ["A", "B", "B", "A", "C"]
}
df = pd.DataFrame(data)
df.to_csv("sample_dataset.csv", index=False)

# Step 2: Load dataset
df = pd.read_csv("sample_dataset.csv")
print("=== Loaded Dataset ===")
print(df)

# Step 3: Dataset attributes
print("\n=== First 5 rows ===")
print(df.head())

print("\n=== Last 5 rows ===")
print(df.tail())

print("\n=== Dataset Info ===")
print(df.info())

print("\n=== Summary Statistics ===")
print(df.describe())

# Step 4: Column selection
print("\n=== Single Column - Score ===")
print(df["Score"])

print("\n=== Multiple Columns - Name and Score ===")
print(df[["Name", "Score"]])

# Step 5: Filtering
print("\n=== Filtered Rows (Score > 80) ===")
print(df[df["Score"] > 80])