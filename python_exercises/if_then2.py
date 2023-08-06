#prompts user to enter a certain number; checks if number is even or odd

user_input = input("Please enter an integer: ")
number = int(user_input)

if number % 2 == 0:
	print("Your number is even.")
else:
	print("Your number is odd.")
