import pandas as pd

# Step 1: Create sample dataset
data = {
    "Name": ["Alice", "Bob", "Charlie", "David", "Eva"],
    "Score": [95, 92, 76, 88, 67],
    "Passed": [True, True, False, True, False],
    "Category": ["A", "A", "B", "B", "C"]
}

df = pd.DataFrame(data)
print("=== Original Dataset ===")
print(df)

# Step 2: Column Selection
print("\n=== Single Column - Name ===")
print(df["Name"])

print("\n=== Multiple Columns - Name and Score ===")
print(df[["Name", "Score"]])

# Step 3: Row Selection
print("\n=== First 3 rows using iloc ===")
print(df.iloc[:3])

df_indexed = df.set_index("Name")
print("\n=== Using loc with index 'Name' ===")
print(df_indexed.loc[["Alice", "David"]])

# Step 4: Filtering
print("\n=== Score > 85 ===")
print(df[df["Score"] > 85])

print("\n=== Score > 85 and Passed == True ===")
print(df[(df["Score"] > 85) & (df["Passed"] == True)])

# Step 5: Sorting
filtered_sorted = df[(df["Score"] > 85) & (df["Passed"] == True)].sort_values(by="Score", ascending=False)
print("\n=== Filtered and Sorted Result ===")
print(filtered_sorted)

# Step 6: Chaining
print("\n=== Chained Filtering and Sorting (Score > 85) ===")
print(df[df["Score"] > 85].sort_values(by="Score", ascending=False))