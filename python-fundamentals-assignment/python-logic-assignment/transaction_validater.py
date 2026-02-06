balance = int(input("Enter account balance: "))
withdrawal = int(input("Enter withdrawal amount: "))
verified = input("Are you verified? (True/False): ")

if verified.lower() == "true":
    verified = True
else:
    verified = False

if verified and withdrawal <= balance:
    print("Withdrawal successful")
else:
    print("Transaction denied")