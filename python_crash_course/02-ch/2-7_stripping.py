"""
2-7. Stripping Names

Use a variable to represent a person's name, and include some 
whitespace characters at the beginning and end of the name.
Make sure you use each character combination, "\t" and "\n",
at least once. Print the name once, so the whitespace around
the name is displayed. Then print the name using each of the
three stripping functions, lstrip(), rstrip(), and strip().
"""

# create a variable for the person's name and add white spaces
name = "\tAmir Sadik \n"

# print the name with white spaces
print(name)

# print the name using lstrip() method
print(name.lstrip())

# print the name with rstrip() method
print(name.rstrip())

# print the name wiht strip() method
print(name.strip())
