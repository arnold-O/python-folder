# Normally statements in python execute one after the other but conditional statement helps with the flow control ,
# for them not to execute just one line after another but for each lin to execute due to a certain reason/criteria me


#operators used are either relational or logical


#relational
# < less than
# > greater thn
# <= less than or equal to
# >= greater than or equal to
# =! not equal to
# == equal to

#logical operators
# or = OR
# and = AND
# not = NOT

#the above are the relational and logical operators

# These operators resolve to boolean , that is true or false

# examples

b = 12
a =  5

if a<=b:
     print("a is less than b")
else:
     print("b is less than a")


#c = int(input("Enter a number: "))
#if c<15:
#    print("less than 15")
#else:
#    print("greater than 15")


#Exmples
# Find the numbers between 2 numbers

#d = int(input("enter first number "))
#e = int(input("enter Second number "))

#if d - e > 0:
#    print(d - e)
#else:
#    print(e - d)

# Check a number is ODD or EVEN
#n = int(input("Enter a number "))

#if n%2 == 0:
#    print("This is even Number")
#else:
#    print("This is an Odd number")

# Check if a citizen can cast a vote if his age is greater or equal to 18

age = int(input("Kindly input your age "))


if age >= 18:
    print("you are eligible to vote, kindly exercise your civic right")
else:
    print("Please note that you cannot vote, see you when you are 18")

