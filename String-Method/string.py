#string

#s1 = "hello"
#print(s1)

#print(type(s1))

# find the length of a string using len()

#print(len(s1))

# Getting the letters of a string using either index method dor loop

#print(s1[2])
#print(s1[2:4])

#for x in s1:
#    print(x)
#String inside single quote and double quote '' , "" as well as multiline using multi-quotes

#s2 = """ Hello
#        Amadi"""
#print(s2)


# working with String Operators, concatenation, not in, in indexing Repetition, slicing

#Concatenation
#s1 = "hello"
#s2 = " friend"
#s3 = s1 + s2
#print(s3)

#Repetition multiply with integer values e.g * 3

#s1 = "new" * 2

#print(s1)

#Indexing

#s4 = "Hello world"

#print(s4[6])
#can also use loop and range in loop to get out the string values

#for x in range(0, len(s4)):
#    print(s4[x])

#for y in range(len(s4)-1, -1, -1):
#     print(s4[y])

# For String we can mention str[start:end:step]

#s5 = "We are here again"

#print(s5[3:7:1])
#REVERSE
#print(s5[-1:-len(s5)-1:-1])


# IN and NOT IN
#If a giving string is in a set of character , they resolve to boolean
#s6 = "fatty mama"
#print("ay" in  s6)  == false
#print("tty" in  s6)  == true


#Relation Operators , used for comparing strings [ ==, >=, <=, >, < != ]
#a1 = "abcde"
#b1 = "abcdf"
#print(a1 == b1)
#print (b1 > a1)


# STRING METHODS

#s3 = "hello, who goes you"
#help(s3.upper)
#s3.find("o")
#print(s3.find("o")) #it returns the index
#print(s3.find("z"))  #it gives -1 because it is not in the string

#print(s3.find("o", 5)) # sice there is multiple "o" specify the start of the find
#print(s3.find("o", 5, 7)) # since there is multiple "o" specify the start of the find, as well as end
#print(s3.rfind("o", 0, 16))  #this start from the right hand side, here the index is still from 0 to whatever number , but the find start from the right hand

#print(s3.count("o"))  # This gives the number times "o" occurs

#print(s3.index("o"))  # This gives the number times "o" occurs # index throws exception when it does not find the substring
#print(s3.rindex("o"))  # This gives the number times "o" occurs # rindex throws exception when it does not find the substring
#rint(s3.count("you"))


#Stiil on String Methods  [ Joining and Splitting Methods ]

#Replace str.replace(old, new [ , count])

#str_one = 'a-b-c-d-b-e'
#str_two = str_one.replace('-', ",")
#str_three = str_one.replace('-', ",", 3)

#str_four ="arnold@gmail.com"
#str_five = str_four.replace(".com", ".edu")


#Join str.join(iterable)

#sx = 'xyz'
#sy = "abc"

#print(sx.join(sy))

#join is trick if you don't understand the separator part

#s1 = ["Chris", "kene", "Arnold"]

#s2 = ","

#s6 = s2.join(s1)
#print(s6)

#Join str.split[sep [, max split]]

#s1 = "Chris kene Arnold"
#s3 = s1.split(" ")
#s4 = "Chris,kene,Arnold"
#s6 = s4.split(',')
#s6 = s4.split(',', 1)
#print(s6)

#5 = "hellofromusall"

#3 = []
#or x in s5:
#   s3.append(x)
#rint(s3)

#There is splitting from the right hand side called rsplit

#Exercise

#tr1 = "afdjoke"
#tr2 =sorted(str1) #sorted function gives us a list
# = "".join(str2)

#Displaying Data exercise


#first_fruit = input("Enter the food/fruit you want ")
#fruit_cost = (input("Enter the price "))

#total_length = len(fruit_cost) + len(first_fruit)
#print(total_length)
#dots = "." * (25 - total_length)

#try1 = first_fruit + dots + fruit_cost
#print(try1)


#Confirming of two password it is safe; idea of password and confirm password

#pass1 = input("please enter your password ")
#pass2 = input("please enter your password again ")

#while pass1 != pass2:
#    print("Incorrect password, try again")
#    pass1 = input("please enter your password ")
#    pass2 = input("please enter your password again ")

#else:
#    print("Password is correct , Welcome ovioba ")

#Display a credit card number
# from 1237648902355678
#  to  *************345

#credit1 = (input("Enter your 16 digit Credit input "))
#value1 = credit1[12:]
#four2 = "*" * 4 + " "
#show_details = four2 * 3 + value1
#print(show_details)

#Yourname and domain name from email address

#address1 = input("Enter you address ")

#address2 = address1.split("@")
#value1 = address2[0]
#value2 = address2[1]

#print("This is the usernameof the address", value1)
#print("This is the domain name of the address", value2)

#checking as string is a palindrome

#
#s2 = input("Enter a string ")
#
#
# revers = s2[::-1]
# print(revers)
#
# if s2 == revers:
#     print("This is a palindrome")
# else:
#     print("This is not a palindrome")

#From a giving string you can form a palindrome even though the string is not a palindrome


#Find day, month and year from a giving date

#sdate = input("Enter  date ")

#sdate1 = sdate.split("/")
#print("the day of the month is:", sdate1[0], "The month is:", sdate1[1], "And the year is:", sdate1[2])

#Anagram


s1 = input("Enter a string ")
s2 = input("Enter a second String ")

if len(s1) != len(s2):
    print("Not  Anagram")
else:
    for x in s1:
        if x not in s2:
            print("not Anagram")
    else:
        print("Anagram")