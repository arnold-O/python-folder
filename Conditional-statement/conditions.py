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

#age = int(input("Kindly input your age "))


#if age >= 18:
#    print("you are eligible to vote, kindly exercise your civic right")
#else:
#    print("Please note that you cannot vote, see you when you are 18")

##***************************Second Exercise**********************

#check if a student has passed or failed. by taking marks in 3 subjects

#phy = int(input("enter your physics score "))
#math = int(input("enter your math score "))
#chem = int(input("enter your chemistry score "))

#if phy >= 45 and math >= 45 and chem >= 45:
#    print("You Passed")
#else:
#    print("you failed")

#Check if a person or user has Admin Access


#username = input("Enter your user name please ")

#if username == "john" or username == "smith":
#    print("welcome, Here are dashboard for Admin User access")
#else:
##    print("You do not have admin access, kindly proceed with ordinary user duties")


#Check if a given case character is vowel or consonant

#vowels = "aeiou"
#sod = input("Enter a character in the alphabet to check whether is a vowel or consonant ")

#if sod in vowels:
#    print("Letter is among the vowel Letters")
#else:
#    print("Letter is a consonant")


#************************* Third Exercise***********************

#check who is eldest between 3 friends

#user1 = float(input("Kindly enter your age user 1 "))
#user2 = float(input("Kindly enter your age user 2 "))
#user3 = float(input("Kindly enter your age user 3 "))

#if user1 > user2 and user1 > user3:
#    print("User 1 is the eldest")
#elif user2 > user3:
#    print("User 2 is the eldest")
#else:
#    print ("User 3 is eldest")


# Discounted Amount

#am = int(input("Enter the Amount "))

#if am <= 1000 :
#    discount = am * (10/100)
#elif  1000 < am <= 5000 :
#    discount = am * (20/100)
#elif  5000 < am <= 10000 :
#    discount = am * (30/100)
#else:
#    discount = am * (50/100)

#discounted_amount = am - discount
#print(discounted_amount)


