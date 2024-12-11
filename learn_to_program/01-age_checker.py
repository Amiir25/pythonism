'''
age_checker.py

Ask the user for their age. For ages below 4, tell they're too early to go to school.
For ages 4 to 6 print go to kindergarten. For ages 7 to 18 tell to go to the grade 
level that is less than from their age by 6 (For age 10, tell to go to grade 4).
For ages above 18 tell'em to go to collage.
'''
# Ask the user for their age and put it in a variable
age = int(input("Enter your age: "))

# if the age is below 4, they're too early to go to school
if (age < 4 and age >= 0):
	print("Too early to go to school!")

# if the age is 4 to 6, they're going to kindergarten
elif (age >= 4 and age <= 6):
	print("Go to kindergarten!")

# if the age is 7 to 18, they're going to the grade level of their age - 6
elif (age >= 7 and age <= 18):
	grade = age - 6
	print("Go to grade {}!".format(grade))

# if the age is above 18, they're going to collage
elif (age > 18 and age <= 65):
	print("Go to collage!")

# if the age is above 65, tell'em to retire
elif (age > 65):
	print("You learned enough, time to teach and advise!")

# if the age is below 0, ignore it
elif (age < 0):
	print("Get born first!")
