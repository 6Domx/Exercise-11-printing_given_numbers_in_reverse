# Pseudocode
# 1. Ask the user to give us a number
# 2. Evaluate the number
# 3. Print the number in reverse order

given_number = input("Please give us a number: ")
if given_number.isdigit():
    given_number = int(given_number)
else:
    print("Invalid, input must be numbers.")

