'''
calculator.py

Write a python code that performs math operation 
with two numbers. Both the numbers and the operator should
be entered by the user.
'''

# Ask the user to enter two numbers with an operator & assign them for variables
num1, operator, num2 = input("Perform a calculation: ").split()

# convert the two numbers to integer
num1, num2 = int(num1), int(num2)

# check the operator entered by the user
match operator:

	# for addition, print the sum
	case '+':
		print("{} + {} = {}".format(num1, num2, num1 + num2))

	# for subtraction, print the difference
	case '-':
		print("{} - {} = {}".format(num1, num2, num1 - num2))

	# for multiplication, print the product
	case '*':
		print("{} * {} = {}".format(num1, num2, num1 * num2))

	# for division, check the second number
	case '/':

		# if it is not 0, print the quotient
		if (num2 != 0):
			print("{} /{} = {}".format(num1, num2, num1 / num2))

		# otherwise, print error message
		else:
			print("Invalid denominator!")

	# for modulo, check the second number
	case '%':

		# if it is not 0, print the remainder
		if (num2 != 0):
			print("{} % {} = {}".format(num1, num2, num1 % num2))

		# otherwise, print error message
		else:
			print("Invalid denominator")

	# for empty or not operator sign, print error mesasge
	case _:
		print("Invalid operator!")
