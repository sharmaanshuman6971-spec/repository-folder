# Part 2: Simple Contact Book (Dictionary)

# Step 1: Store contacts in a dictionary
contacts = {
    "Ravi": "9876543210",
    "Anita": "9123456780",
    "Suresh": "9988776655"
}

# Step 2: Print all contacts
print("All contacts:")
for name, number in contacts.items():
    print(name, ":", number)

# Step 3: Ask user for a name
search_name = input("Enter a name to search: ")

# Step 4: Lookup and display result
if search_name in contacts:
    print("Phone number of", search_name, "is:", contacts[search_name])
else:
    print("Contact not found")