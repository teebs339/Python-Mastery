# TOPIC 1 - ASCII numbers
# Inverse of chr() function which returns a character/string based on the number provided

# print(ord("A"))
# print(chr(65))

# ------------------------------------------------------------------
# TOPIC 2 - IF ELSE

# temp = 35
# if (temp > 69):
#     print("cuh")
# else:
#     print("wtf")

# temperature = 35
# if (temperature > 69):
#     print("ayo cuh")
# elif (temperature < 69):
#     print("ayo wtf")
# else:
#     print("fk u")

# ------------------------------------------------------------------
# TOPIC 3 - TERNARY OPERATORS

# This look like dogshit right?
# age = 22
# if age >= 18:
#     message = "Eligible"
# else:
#     message = "Not eligible"
# print(message)

# Do it this way you mumpty
# age = 22
# message = "Eligible" if age >= 18 else "Not Eligible"
# print(message)

# ------------------------------------------------------------------
# TOPIC 4 - LOGICAL OPERATORS (and, or & not)

# high_income = True
# good_credit = False
# student = False


# if high_income and good_credit:  # AND OPERATOR - dont do this high_income == True | that is shite
#     print("Eligible for visa")
# else:
#     print("If in doubt, kick it out")

# if high_income or good_credit:  # OR OPERATOR
#     print("Eligible for visa")
# else:
#     print("If in doubt, kick it out")

# if (high_income or good_credit) and not student:  # NOT OPERATOR
#     print("Eligible")
# else:
#     print("Not Eligible")

# ------------------------------------------------------------------
# TOPIC 5 - SHORT CIRCUIT EVALUATION - for example if there are 3 conditions in the if statement and the first condition is true, it won't look at the rest of the conditions simply because it doesn't need to. which is why these conditions are called short-circuited

# high_income = False
# good_credit = True
# student = False

# print("Eligible" if high_income and good_credit
#       and not student else "Not Eligible")

# ------------------------------------------------------------------
# TOPIC 6 - CHAINED COMPARISON OPERATORS

# age should be between 22 and 65

# age = 69
# if 22 <= age < 65:
#     print("Eligible")
# else:
#     print("Not Eligible")

# ------------------------------------------------------------------
# QUIZ

# if 10 == "10":
#     print("a")
# elif "bbd" > "bb": # Here the first character is compared based on their ascii values
#     print("b")
# else:
#     print("c")

# ------------------------------------------------------------------
# TOPIC 7 - FOR LOOP

# for number in range(0, 10, 2):  # no.1 = start idx | no.2 = end idx | no.3 = idx stepping
#     print("Attempt", number + 1, (number + 1) * ".")

# ------------------------------------------------------------------
# TOPIC 8 - FOR ELSE LOOP | CONTINUE/BREAK

# successful = False

# for number in range(3):
#     print("Attempt")
#     if successful:
#         print("Successful")
#         break
# else:
#     print("Attempted 3 times and failed")

# ------------------------------------------------------------------
# EXTRA ACTIVITY

# idx = 0
# while True:
#     print(idx + 1)
#     idx += 1
#     if idx == 5:
#         break


# ------------------------------------------------------------------
# TOPIC 9 - NESTED LOOP

# for x in range(5):
#     for y in range(3):
#         # print(x, ".", y, sep="")
#         print(f"({x + 1}.{y + 1})")

# ------------------------------------------------------------------
# TOPIC 10 - ITERABLES

# print(type(range))  # TYPE
# print(type(range(5)))  # RANGE
# print(type([1, 2, 3, 4, 5, 6]))  # LIST

# x = "ateeb69"
# for y in x:
#     print(y)

# for x in [1, 2, 3, 4, 5, 6]:
#     print(x)

# ------------------------------------------------------------------
# TOPIC 11 - WHILE LOOP

# number = 100
# while number > 0:
#     print(number)
#     # number //= 2
#     number = number // 2

# command = ""
# while command.lower() != "quit":  # MOO
#     command = input(">")

# ------------------------------------------------------------------
# TOPIC 12 - INFINITE LOOP

# msg = "again "
# idx = 0
# while True:
#     command = input(">")
#     if command.lower() == "fk u":
#         print("aww :(")
#         break
#     else:
#         print(f"fk u {msg * idx}", sep="")
#         idx += 1

# ------------------------------------------------------------------
# EXERCISE

# Q. Display even numbers from 1 to 10 and at the end display how many even numbers there were found

# count = 0
# for x in range(1, 10):
#     if x % 2 == 0:
#         print(x)
#         count += 1
# print(f"We have {count} even numbers")
