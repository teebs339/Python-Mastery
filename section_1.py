# Helping material
# Ctrl + / - instanly add a comment
# Ctrl + r - run python code
# Ctrl + d - debug python code

# ------------------------------------------------------------------

# TOPIC 1 - basic print in console
# print("Hello World 👌")
# print("*" * 69)  # will print * 10 times in the console

# ------------------------------------------------------------------

# TOPIC 2 - LINTING
# Problems section -> Ctrl + Shift + M -> error & debugging in all files
# Command Pallete -> Ctrl + Shift + P -> change linter, python version, etc, .

# ------------------------------------------------------------------

# TOPIC 3 - Python PEP8 styling
# Format document from command pallete autopep 8
# Format On Save - setting turned on from file > preferences
# x = 1
# y = 2
# unit_price = 3
# print(x + y + unit_price)

# ------------------------------------------------------------------

# TOPIC 4 - Variables
# students_count = 1000
# rating = 4.99
# is_published = False
# course_name = "Python Programming"

# ------------------------------------------------------------------

# TOPIC 5 - Strings & Longer strings
# IMP FINDINGS - python in console will add a space after ":" in this example even if you haven't which is retarded. but its only in console. in real code, it not have added it. so view it the same as in console as the code, add the (sep="") into it
# course = "Python Programming"
# message = """Hi John,
# whats cooking good looking"""
# bruh = "Length of the course:" + str(len(course))
# print(bruh)

# # substring function for only one letter
# print("Last character/letter of the course var:", course[-1], sep="")

# # substring function to get a combination of letters
# print("First word inside the course var:", course[0:3])
# print("First word inside the course var:", course[0:])
# print("First word inside the course var:", course[:3])
# print("First word inside the course var:", course[:])

# ------------------------------------------------------------------

# TOPIC 6 - ESCAPE SEQUENCES
# course = "Python \n \"Programming"

# print(course)

# ------------------------------------------------------------------

# TOPIC 7 - FORMATTED STRINGS
# first_name = "Ateeb"
# last_shahid = "Shahid"
# full_name = f"{len(first_name)}-{69 + 1}"

# print(full_name)

# ------------------------------------------------------------------

# TOPIC 8 - STRING METHODS
# len()
# course = "   python programming     "
# print(course.upper)  # returns the address of the method
# print(course.upper())  # is not the same as above. returns the uppercase value
# print(course.title())
# print(course.strip())  # trim method in VB.NET
# print(course.lstrip())  # Left trim method in VB.NET
# print(course.rstrip())  # Right trim method in VB.NET

# # gives out the index of the characters or combination of characters
# print(course.find("hon"))
# print(course.replace("p", "j"))

# # expression. NOT a method | .exists() in VB.NET
# print("pro" in course)
# print("pro" not in course)

# ------------------------------------------------------------------

# TOPIC 9 - NUMBERS

# print(10 / 3)  # gives out floating value
# print(10 // 3)  # gives out int value
# print(10 % 3)  # MOD function in VB.NET
# print(2 ** 2)  # 2 to the power of 2 = 4

# x = 10
# x += 3
# print(x)

# ------------------------------------------------------------------

# TOPIC 10 - WORKING WITH NUMBERS (BUILT-IN FUNCTIONS)

# import math

# print(round(2.6))
# print(abs(-2.9))  # absolute value of a number

# print(math.ceil(2.2))  # returns 3

# # you dont need the math library in this case
# print(f"max number b/w the two: {max(42069, 69)}")
# print(f"min number b/w the two: {min(42069, 69)}")

# ------------------------------------------------------------------

# TOPIC 11 - TYPE CASTING/CONVERSION

# x = input("x: ")  # takes an input from the user in the console
# print(type(x))
# y = int(x) + 69
# print(y)
