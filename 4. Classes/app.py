# ------------------------------------------------------------------
# TOPIC 2: CLASS

# class Point:
#     def draw(self):
#         print("draw")


# point = Point()
# print(type(point))
# print(isinstance(point, Point))  # check to see the instance of the class

# ------------------------------------------------------------------
# TOPIC 3: CONSTRUCTOR

# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

#     def draw(self):
#         print(f"Point ({self.x}, {self.y})")


# point = Point(1, 2)
# point.draw()

# ------------------------------------------------------------------
# TOPIC 4: CLASS VS INSTANCE ATTRIBUTE

class Point:
    default_color = "red"

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self):
        print(f"Point ({self.x}, {self.y})")


point = Point(1, 2)
print(point.default_color)
print(Point.default_color)
point.x = 69
point.draw()

Point.default_color = "yellow"

another = Point(3, 4)
print(another.default_color)
another.draw()
