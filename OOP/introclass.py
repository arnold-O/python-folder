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

# class Test1:
#     count = 0
#     def __init__(self, l, b, h):
#         self.length = l
    #     self.breadth = b
    #     self.height = h
    #     Test1.count += 1
    #
    # def perimeter(self):
    #     return 2 * self.length + self.breadth + self.height
    # def area(self):
    #     return (self.length * self.breadth) * self.height
    #
    # @classmethod
    # def classCount(cls):
    #     print(cls.count)
    #
    # @staticmethod
    # def issquare(len , bre):
    #     return len == bre

# r1 = Test1(1,3,6)
# r2 = Test1(3,5,6)
# r3 = Test1(6,7,8)
# r2.classCount()

# You can call static method with object created or name of class

# r5 = Test1(8,9,10)
# print(r5.issquare(9,7))
# print(Test1.issquare(2,2))

#ACESSORS and MUTATORS
# class Test2:
#     def __init__(self, l, b, h):
#         self.length = l
#         self.breadth = b
#         self.height = h
#     def setLength(self, l):
#         self.length = l
#     def setBreadth(self, b):
#         self.breadth = b
#     def getlength(self):
#         return self.length
#     def getbreadth(self):
#         return self.breadth
#
# r4 = Test2(8,9,10)
#
# print(r4.getlength())


## Inheritance Examples

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Teacher(Student):
    def __init__(self,rank, name, age):
        self.rank = rank
        super().__init__(name, age)


    def print_name(self):
        return f"my name is {self.name}, i'm {self.age} years old and my rank is {self.rank}"
        


r3 = Teacher('R3', "Ugochukwu", 20)

print(r3.print_name())