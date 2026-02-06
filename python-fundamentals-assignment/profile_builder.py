name = input("Enter your name: ")
age = int(input("Enter your age: "))
active_status = input("Are you an active user? (True/False): ")

if active_status.lower() == "true":
    active_status = True
else:
    active_status = False

print(f"User {name} is {age} years old. Active status: {active_status}")