for x in range(1, 101):
    if x % 3 == 0 and x % 5 == 0:
        print("FizzBuzz")
    elif x % 3 == 0:
        print("Fizz")
    elif x % 5 == 0:
        print("Buzz")
    else:
        print(x)

# ^ This is good but it can be better like this

for x in range(1, 101):
    output = ""
    if x % 3 == 0:
        output += "Fizz"
    if x % 5 == 0:
        output += "Buzz"
    if x % 7 == 0:
        output += "Bazz"
    if output == "":
        output = x
    print(output)
