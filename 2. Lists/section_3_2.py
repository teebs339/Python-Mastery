# ------------------------------------------------------------------
# TOPIC 1 - LISTS

# letters = ["a", "b", "c"]  # list
# matrix = [[0, 1], [2, 3]]  # 2D list

# zeros = [0] * 5
# combined = zeros + letters  # combined list with lists

# numbers = list(range(20))

# chars = list("Hello World")

# print(len(chars))

# ------------------------------------------------------------------
# TOPIC 3 - UNPACKING LISTS

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 69]
# first = numbers[0]
# second = numbers[1]
# third = numbers[2]

# ^ looks like shit right?
# v here's the correct way of doing the same shit

# the pointer * next to the other var is the combination of all the remaining values in the list
# first, *other, last = numbers

# print(f"first: {first}, last: {last}, middle: {other}")


# def multiply(*numbers):
#     print(f"oi muppet this is from function: {numbers}")


# multiply(other, numbers)

# ------------------------------------------------------------------
# TOPIC 4 - LOOPING OVER LISTS

# letters = ["a", "b", "c"]
# # for letter in enumerate(letters):  # gives us a tuple -> TUPLE IS READ ONLY
# #     print(letter[0], letter[1])

# for index, letter in enumerate(letters):
#     print(index, letter)

# ------------------------------------------------------------------
# TOPIC 5 - ADDING/REMOVING ITEMS FROM LIST - ADD/APPEND

# Add
# letters = ["a", "b", "c", "b"]
# letters.append("69")
# letters.insert(1, "wtf")

# # Remove
# letters.pop(1)
# # letters.pop()
# letters.remove("b")
# del letters[0:3]
# letters.clear()

# print(letters)

# ------------------------------------------------------------------
# TOPIC 6 - FINDING ITEMS IN A LIST

# letters = ["a", "b", "c", "b"]
# # if the object dont exists, it will NOT return -1, it will throw error
# print(letters.index("b"))

# # notice how i used the '' inside the count instead of the usual ""
# print(f"count of the letter \"b\" in the list: {str(letters.count('b'))}")

# if "d" not in letters:
#     print('the letter "d" doesn\'t exist in the list')

# ------------------------------------------------------------------
# TOPIC 7 - SORTING LISTS

# List of normal numbers or letters whatever
# numbers = [1, 21, 69, 4, 42, 6, 65, 54, 9]
# numbers.sort(reverse=True)
# print(numbers)

# print(numbers.sort())
# print(sorted("numbers", reverse=True))

# List of complex shit like tuple/matrix
# items = [
#     ("Product1", 10),
#     ("Product3", 12),
#     ("Product2", 9),
# ]


# def sort_item(item):
#     return item[0]


# # this won't work cuz python is dumb af and you need to tell it how to sort a tuple
# items.sort(key=sort_item)
# print(items)

# ------------------------------------------------------------------
# TOPIC 8 - LAMBDA FUNCTION

# items = [
#     ("Product1", 10),
#     ("Product3", 12),
#     ("Product2", 9),
# ]

# # Lambda function syntax: parameters:expression
# # in this case we dont need the sort_item function anymore
# items.sort(key=lambda item: item[0])
# print(items)

# ------------------------------------------------------------------
# PRACTICE LAMBDA FUNCTION -> parameters:expression

# Lambda function doesn't have a name other than just lambda. its just lambda thats literally it. its functionality is to replace the small functions from your code giving it a "neater" and more "professional" look that the python nerds can appreciate. other than that it serves no purpose.

# Lets say we make a sum function:
# def sum_numbers(x, y):
#     return x + y
# print(sum_numbers(1, 2))

# Now we can do that same shit like this: NOTE that when "Format on save" setting is turned on from File > Preferences > Settings, it will automatically convert the lambda into a def function because according to pep8, lambda needs to die.

# add = lambda x, y: x+ y
# print(add(3, 5))

# ------------------------------------------------------------------
# TOPIC 9 - DEBUGGING -> IMP INFO: Make sure to create a json file by going in debugging > and creating a .vscode > launch.json file. i forgot how i did it, but i beleive in you. ALSO you can press F9 to quick add a breakpoint

# def multiply(*numbers):
#     total = 1
#     for x in numbers:
#         total *= x
#     return total


# print("Start")
# print(multiply(1, 2, 3))

# ------------------------------------------------------------------
# TOPIC 10 - MAP FUNCTION

# items = {
#     ("Product2", 10),
#     ("Product1", 9),
#     ("Product3", 12)
# }

# # prices = []
# # for x in items:
# #     prices.append(x[1])
# # ^ instead of this loop which looks ugly asf, we will use map function to achieve the same result

# prices = [item[1] for item in items]  # bonus tip instead of using lambda
# print(f"prices: {prices}")

# bruh = list(map(lambda item: item[1], items))
# print(bruh)  # prints out a list
# for item in bruh:
#     print(item)

# ------------------------------------------------------------------
# TOPIC 11 - FILTER FUNCTION

# items = [
#     ("Products1", 10),
#     ("Products2", 9),
#     ("Products3", 12)
# ]

# # x = filter(lambda item: item[1] >= 10, items) # this will return us with a list object. we can put a loop on it or map it to get the values from it

# filtered = list(filter(lambda item: item[1] >= 10, items))

# print(filtered)


# ------------------------------------------------------------------
# TOPIC 12 - LIST COMPREHENSIONS

# items = [
#     ("Products1", 10),
#     ("Products2", 9),
#     ("Products3", 12)
# ]

# prices = list(map(lambda item: item[1], items))  # same as below
# prices = [item[1] for item in items]  # much better than lambda bullshit

# filtered = list(filter(lambda item: item[1] >= 10, items))
# filtered1 = [item for item in items if item[1] >= 10]
# print(filtered1)

# ------------------------------------------------------------------
# EXERCISE -> FIZZBUZZ

# If input is divisible by 3, it returns fizz. If the input is divisible by 5, it returns buzz. If the input is division by both 3 & 5, then return FizzBuzz. If its divisible by neither, return the number itself


# while True:
#     def fizz_buzz(input):
#         if input % 3 == 0 and input % 5 == 0:
#             return "FizzBuzz"
#         elif input % 5 == 0:
#             return "Buzz"
#         elif input % 3 == 0:
#             return "Fizz"
#         else:
#             return input

#     x = input(">")
#     if x.lower == "quit":
#         break
#     else:
#         print(fizz_buzz(int(x)))

# ------------------------------------------------------------------
# TOPIC 12 - ZIP FUNCTION

# list1 = [1, 2, 3]
# list2 = [10, 20, 30]

# print(list(zip(list1, list2)))

# ------------------------------------------------------------------
# TOPIC 13 - STACK -> LIFO -> Last In First Out

# browsing_sessions = []
# browsing_sessions.append(1)
# browsing_sessions.append(2)
# browsing_sessions.append(3)

# print(browsing_sessions)

# browsing_sessions.pop()
# browsing_sessions.pop()
# browsing_sessions.pop()
# print(browsing_sessions)

# if not browsing_sessions:
#     print("Disable back button")
# else:
#     print("redirect", browsing_sessions[-1])

# ------------------------------------------------------------------
# TOPIC 14 - QUEUE -> FIFO -> First In First Out

# from collections import deque
# queue = deque([])
# queue.append(1)
# queue.append(2)
# queue.append(3)
# print(queue)
# queue.popleft()
# queue.popleft()
# queue.popleft()
# print(queue)
# if not queue:
#     print("Empty")

# ------------------------------------------------------------------
# TOPIC 15 - TUPLE

# to define a tuple, we use parentheses instead of large brackets. Tuple are READ ONLY
# point = (1, 2, 3)
# print(point[0:2])
# print(type(point))
# x, y, z = point
# print(x, y, z)
# if 10 in point:
#     print("exists")

# ------------------------------------------------------------------
# TOPIC 16 - SWAPPING VARIABLES

# x = 69
# y = 9432223128

# print("Before swap:", x, y)

# x = x + y
# y = x - y
# x = x - y

# print("After swap:", x, y)

# OR YOU CAN DO THIS SHIT IN PYTHON
# print(x, y)
# x, y = y, x  # this is basically tuple swapping
# print(x, y)

# ------------------------------------------------------------------
# TOPIC 17 - SETS -> collection with no duplicates

# numbers = [1, 2, 1, 3, 4]
# unique = set(numbers)
# second = {1, 4}
# second.add(5)
# second.remove(1)
# print(len(second))
# print(unique)

# numbers = [1, 2, 1, 3, 4, 5, 5]
# first = set(numbers)
# second = {1, 5}

# print(first | second)  # UNION
# print(first & second)  # INTERSECTION
# print(first - second)
# print(first ^ second)

# ------------------------------------------------------------------
# TOPIC 18 - ARRAYS

# from array import array

# numbers = array("i", [1, 2, 3])
# numbers.append(69)
# print(numbers)

# ------------------------------------------------------------------
# TOPIC 19 - DICTIONARY -> use it to map out key, value pairs

# point = {"x": 1, "y": 2}  # string for key and int for value / can be any type
# v or do the same shit
# point = dict(x=1, y=2)
# point["x"] = 69
# point["z"] = 420
# print(point)

# if "a" in point:
#     print(point("a"))
# # v or do this shit returns None when key doesnt exist, or u can give anything in the next param
# print(point.get("a", -1))
# del point["x"]  # DELETE SHIT
# print(point)

# for key, value in point.items():
#     print(key, value)

# ------------------------------------------------------------------
# TOPIC 20 - UNPACKING OPERATOR

# numbers = [1, 2, 3]
# print(*numbers)  # the * is the unpacking shit


# values = list(range(5))

# v or do this shit instead, its called unpacking motherfucker

# values = [*range(5), *"Hello"]
# print(values)

# first = [1, 2]
# second = [3]
# values = [*first, *second, *"Hello"]
# print(values)

# first = {"x": 1}
# second = {"x": 10, "y": 2}
# combined = {**first, **second, "z": 1} # * unpacking again

# print(combined)

# ------------------------------------------------------------------
# TOPIC 21 - DICTIONARY COMPREHENSIONS

# values = []
# for x in range(5):
#     values.append(x*2)

# INSTEAD DO THIS SHIT

# values = {x: x * 2 for x in range(5)}
# print(values)
