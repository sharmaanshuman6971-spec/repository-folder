age = int(input("Enter your age: "))
has_id = input("Do you have an ID card? (True/False): ")

if has_id.lower() == "true":
    has_id = True
else:
    has_id = False

if age >= 18 and has_id:
    print("Entry allowed")
else:
    print("Entry denied")