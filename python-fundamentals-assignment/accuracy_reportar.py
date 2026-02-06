accuracy = input("Enter model accuracy: ")

try:
    accuracy_value = float(accuracy)
    print(f"Model accuracy is {accuracy_value}")
except ValueError:
    print("Invalid input! Please enter a number.")