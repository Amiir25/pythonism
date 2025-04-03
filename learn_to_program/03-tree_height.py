'''
02-tree_size.py

Ask the user for a number and print a tree like shape using the
# sign by the size of the input. This an example out put for input 
value of 5.

		#
		###
			  #####
			 #######
			#########
			    #

'''

# Ask the user for a number and put it in a variable 'height'
height = int(input("How tall is the tree? : "))

# Create a variable 'space' and assign height - 1 to it
space = height - 1

# Create a variable 'hash' and give it a value 1
hash = 1

# Create a variable 'counter' and initialise it to 0
counter = 0

# while counter is less than 'height'
while (counter < height):

	# For i in a range from 0 to 'space', Print ' ' without a new line
	for i in range(space):
		print(' ', end = '')

	# For i in a range from 0 to 'hash', Print '#' without a new line
	for i in range(hash):
		print('#', end = '')

	# Print a new line after the end of each row
	print('')

	# Decrement 'space' by one
	space -= 1

	# Increment 'hash' by two
	hash += 2

	# Increment 'counter' by one
	counter += 1

# For i in a range from 0 to 'height' - 1, Print ' ' without a new line
for i in range(height - 1):
	print(' ', end = '')

# Print #
print('#')
