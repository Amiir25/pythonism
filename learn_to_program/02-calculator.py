'''
calculator.py

Write a python code that performs math operation 
with two numbers. Both the numbers and the operator should
be entered by the user.
'''

# Ask the user to enter two numbers and an operator & assign them for variables
num1, operator, num2 = input("Perform a calculation: ").split()

# convert the two numbers to integer
num1, num2 = int(num1), int(num2)

# check the operator
match operator:

	# if it is addition, print the sum
	case '+':
		print("{} + {} = {}".format(num1, num2, num1 + num2))

	# if it is subtraction, print the difference
	case '-':
		print("{} - {} = {}".format(num1, num2, num1 - num2))

	# if it is multiplication, print the product
	case '*':
		print("{} * {} = {}".format(num1, num2, num1 * num2))

	# if it is division, check if the second number is not 0
	case '/':

		# if true, print the quotient
		if (num2 != 0):
			print("{} /{} = {}".format(num1, num2, num1 / num2))

		# else print error message
		else:
			print("Invalid denominator!")

	# if it is modulo, check if the second number is not from 0
	case '%':

		# if true, print the remainder
		if (num2 != 0):
			print("{} % {} = {}".format(num1, num2, num1 % num2))

		# else print error message
		else:
			print("Invalid denominator")

	# else print error mesasge
	case _:
		print("Invalid operator!")
