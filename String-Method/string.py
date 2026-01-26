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

s4 = "Hello world"

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

s3 = "hello, who goes you"
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
print(s3.count("you"))