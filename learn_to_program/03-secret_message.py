'''
	03-secret_message.py

	Accept a string from the user. Convert the string in to
	its equivalent unicode and print it as a secret message.
	And convert the unicode back to its original message and
	print it as original message.

'''

# Accept a message from the user
while True:
    try:
        msg = str(input("Enter a message : ")).upper()
        break
    except ValueError:
        print('Error: You are entering a number!')

# Convert each character of the message into its equivalent ASCII code
secret_msg = ''
for i in msg:
    secret_msg += str(ord(i))

# Print the unicode
print(secret_msg)

# Convert the unicode back to the original message
original_msg = ''
for i in range(0, len(secret_msg) - 1, 2):
    code = secret_msg[i] + secret_msg[i + 1]
    original_msg += chr(int(code))

# Print the original message
print(original_msg)
