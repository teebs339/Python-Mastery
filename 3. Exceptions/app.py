# ------------------------------------------------------------------
# TOPIC 3: TRY/CATCH -> skipping topic 1 & 2 cuz its all just syntax

# try:
#     age = int(input("Age: "))
#     xfactor = 10 / age
# except (ValueError, ZeroDivisionError):
#     print("You didn't enter a valid age idiot")
# else:
#     print(f"your age: {age}")

# ------------------------------------------------------------------
# TOPIC 4: CLEANING UP

# try:
#     file = open("app.py")
#     print(file.ite)
#     age = int(input("Age: "))
#     xfactor = 10 / age
# except (ValueError, ZeroDivisionError):
#     print("You didn't enter a valie age stupo")
# else:
#     print(f"No exceptions were throw. Also ur age: {age}")
# finally:
#     file.close()


# ------------------------------------------------------------------
# TOPIC 5: WITH STATEMENT -> auto release external sources

# try:
#     with open("app.py") as file, open("yo.txt") as target:
#         print("File opened")
#     age = int(input("Age: "))
#     xfactor = 10 / age
# except (ValueError, ZeroDivisionError):
#     print("You didn't enter a valie age stupo")
# else:
#     print(f"No exceptions were throw. Also ur age: {age}")

# ------------------------------------------------------------------
# TOPIC 6: THROW/RETHROW
# learn more about exceptions and shit from here: https://docs.python.org/3/library/exceptions.html

# def calculate_xfactor(age):
#     if age <= 10:
#         raise ValueError("Age cannot be 0 or less")  # throwing error
#     return 10/age


# try:
#     print(calculate_xfactor(int(input("Age: "))))
# except ValueError as error:  # catching error
#     print(error)

# ------------------------------------------------------------------
# TOPIC 7: THROW/RETHROW -> better way


from timeit import timeit

code1 = """
def calculate_xfactor(age):
    if age <= 10:
        raise ValueError("Age cannot be 0 or less")  # throwing error
    return 10/age


try:
    print(calculate_xfactor(69))
except ValueError as error:  # catching error
    pass
"""

code2 = """
def calculate_xfactor(age):
    if age <= 10:
        return None
    return 10/age

xfactor = calculate_xfactor(-1)
if xfactor == None:
    pass
"""

# execute it 10,000 times
print("First code:", timeit(code1, number=100000))
print("Second code:", timeit(code2, number=100000))
