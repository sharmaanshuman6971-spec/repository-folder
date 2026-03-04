# employee_pipeline.py

import pandas as pd
import numpy as np

# Step 1: Creating sample dataset
data = {
    "Employee": ["Anit", "Neha", "Rahul", "Sneha", "Vikram"],
    "Department": ["IT", "HR", "IT", "Finance", "HR"],
    "Salary": [600000, 500000, np.nan, 700000, 200000],
    "Temporary_Notes": ["On probation", "Contract", "Pending docs", "Verified", "Intern"]
}

df = pd.DataFrame(data)
print("Step 1: Sample DataFrame\n", df)

# Step 2: Detect missing values
print("\nStep 2: Missing Values\n", df.isnull().sum())

# Step 3: Fill missing Salary with mean (fixed style)
mean_salary = df["Salary"].mean()
df["Salary"] = df["Salary"].fillna(mean_salary)
print("\nStep 3: After Filling Missing Salary\n", df)

# Step 4: Drop Temporary_Notes column
df = df.drop(columns=["Temporary_Notes"])
print("\nStep 4: After Dropping Temporary_Notes\n", df)

# Step 5: Rename Salary column
df = df.rename(columns={"Salary": "Annual_Salary"})
print("\nStep 5: After Renaming Salary\n", df)

# Step 6: Group by Department (Mean Salary & Count)
summary = df.groupby("Department").agg(
    Mean_Salary=("Annual_Salary", "mean"),
    Employee_Count=("Employee", "count")
).reset_index()

print("\nStep 6: Final Summary Table\n", summary)