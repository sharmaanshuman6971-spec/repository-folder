# Even or Odd Checker
def check_number(num):
    if num % 2 == 0:
        return "Number is Even"
    else:
        return "Number is Odd"

# Call the function and print result
print(check_number(10))   # Example: should print "Number is Even"
print(check_number(7))    # Example: should print "Number is Odd"