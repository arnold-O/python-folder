## Principles or concepts to understand here are Encapsulation, Abstraction Polymorphism, Inheritance

# Encapsulation is
# Abstraction is showing only required features while hiding internal details
# Polymorphism: One Name different Actions
# Inheritance


##FIRST EXAMPLE

# class cuboid:
#     def __init__(self, l, b, h):
#         print(id(self))
#         self.length = l
#         self.breadth = b
#         self.height = h
#
#     def lidarea(self):
#         return self.length * self.breadth
#
#     def volume(self):
#         print(id(self))
#         return self.length * self.breadth * self.height


# c1 = cuboid(1, 2, 3)
# c1.volume()

# print(id(c1))
# Self means reference to the current object

# print(id(c1))

## INSTANCE VARIABLE and METHOD

# The volume() and area() are instance method using the instance variables of the class

# creating instance variable ( 3 approaches)
# class Test:
#     def __init__(self):
#         self.a = 6
#     def funb(self):
#         self.b = 7
#
# r3 = Test()
# r3.funb()
# r3.c = 8
#
# print(dir(r3))

##  CLASS VARIABLE and CLASS METHOD

class Test1:
    count = 0
    def __init__(self, l, b, h):
        self.length = l
        self.breadth = b
        self.height = h
        Test1.count += 1

    def perimeter(self):
        return 2 * self.length + self.breadth + self.height
    def area(self):
        return (self.length * self.breadth) * self.height

    def classCount(cls):
        print(cls.count)

r1 = Test1(1,3,6)
r2 = Test1(3,5,6)
r3 = Test1(6,7,8)
r2.classCount()






