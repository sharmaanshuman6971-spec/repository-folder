# Part 4: User Data Processing System

# Step 1: Store multiple users in a list of dictionaries
users = [
    {
        "name": "Alice",
        "scores": [80, 85, 90],
        "roles": {"admin", "editor"}
    },
    {
        "name": "Bob",
        "scores": [70, 75, 78],
        "roles": {"viewer"}
    },
    {
        "name": "Charlie",
        "scores": [88, 92, 84],
        "roles": {"editor", "viewer"}
    }
]

# Step 2: Function to calculate average score
def calculate_average(users):
    averages = {}
    for user in users:
        avg = sum(user["scores"]) / len(user["scores"])
        averages[user["name"]] = avg
    return averages

# Step 3: Function to check admin access
def has_admin_access(roles):
    return "admin" in roles

# Step 4: Main function
def main():
    averages = calculate_average(users)
    for user in users:
        print("Name:", user["name"])
        print("Average Score:", round(averages[user["name"]], 2))
        print("Admin Access:", has_admin_access(user["roles"]))
        print("-" * 30)

# Run the program
main()