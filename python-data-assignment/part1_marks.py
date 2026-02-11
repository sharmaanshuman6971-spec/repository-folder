# Student Marks Analyzer (Lists + Slicing)

# Step 1: Store marks of at least 8 students in a list
marks = [78, 85, 90, 65, 72, 88, 92, 80]

# Step 2: Print the full list
print("All student marks:", marks)

# Print the first 3 marks using slicing
print("First 3 marks:", marks[:3])

# Print the last 3 marks using slicing
print("Last 3 marks:", marks[-3:])

# Step 3: Calculate and print highest, lowest, and average marks
highest = max(marks)
lowest = min(marks)
average = sum(marks) / len(marks)

print("Highest mark:", highest)
print("Lowest mark:", lowest)
print("Average mark:", round(average, 2))