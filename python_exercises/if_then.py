#we're are checking if a string is atleast 6 char long


input = input("Please enter a test string: ")

if len(input) < 6:
	print("Your string is too short.")
	print("Please enter a string with 6 characters.")
else:
	print("Strong password.")
