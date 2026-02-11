# Part 3: Employee Role Checker (Tuples + Sets)

# Step 1: Store employee details as a tuple
employee = (101, "Rahul", "IT")

# Step 2: Store employee roles in a set
roles = {"admin", "editor", "viewer"}

# Step 3: Print employee info from tuple
print("Employee ID:", employee[0])
print("Employee Name:", employee[1])
print("Department:", employee[2])

# Step 4: Check whether 'admin' exists in roles
if "admin" in roles:
    print("Admin Access: Yes")
else:
    print("Admin Access: No")