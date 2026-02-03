#List is a collect of object:: It an oredered colletion of objects and it allows duplicate
from numpy.ma.core import append

# List creation in two ways

#list1 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
#list3 = ["Hello", "world", "friends"]
#list2 = list(("eric", "garcia", "henry"))
#print(list3)

#List are mutable
#list1[0]  = 9

#print(list1)
#we can modify list with index or append()
#Chnage list size is costly.

#Operators that work in List Datatypes

#Index :: you can read and write using index.
#Index can be a little bit confusing because it uses the [start:end:step] approach
#print(list2[2])

#x= list1[-1:-11:-1]

#list1[0:3] = [10,23,50]
#It is possible to select less/more index when compare to new variables to fit into the list, example below.
#list1[0:3] = [10,20,89,90,34]   #This will be forced into that list as well, even though the index is less than the new element provided.
#print(list1)



####Concatenation
#Joining two list to form one list

#list5 = [1,2,3,4,5]
#list6 = [9,8,7,6]

#list7 = list5 + list6  #add list called concatenation :: you can add a number lik + 4 to a list, to do this the four must b in the square bracket notation [4]

#list7 = list7 + [4]

#print(list7)


##Extend

#list7.extend([50,60,70])

#print(list7)

# * this will repeat the list

#list11 = [1,2,3,4,5]
#list12 =list11*3
#print(list12)


## In and not in return boolean, used in conditional statements


#if 80 in list11:
#    print("80 is in list11")
#else:
#    print("80 is not in list11")


##Travesing or Visiting Element in a list

list1 = [6,6,7,8,9,1,10]

#for loop

#for x in list1:
#    print(x)


#For loop using Range

#for x in range(0, len(list1)):
#    print()
#    print(x+1, "==", list1[x])

#While loop



##REverse printing, using positive or negative indeces
#for x in range(len(list1)-1, -1, -1):
#   print(list1[x])

#While loop

#list22 = [2,22,3,33,4,44]

#count = 0

#while count < len(list22):
#   print(list22[count])
#   count += 1

#count = len(list22)-1

#while count > 0:
#     print(list22[count])
#     count -= 1

#List methods
## Append Insert Extend Copy
#append
#fruits = ["apple", "banana"]
#fruits.append("orange")

#print(fruits)

##insert()
#fruits = ["apple", "banana"]
#fruits.insert(1, "orange")   # insert at index 1



##extend

#fruits = ["apple", "banana"]
#more_fruits = ["orange", "grape"]

#fruits.extend(more_fruits)




##copy
fruits = ["apple", "banana"]
new_list = fruits.copy()

new_list.append("orange")