#Loops are repeating statements

# We have for loop and while loop

#statement can be repeated along the lens of truth or number times


#while loop
# Using count for while loop

#count = 0
#while count < 5:
#    print(count + 1, "Hello from the main page")
#    count += 1

#count  = int(input("Enter a number "))


#while count > 0:
#    r = count % 10
#    count = count // 10
#    print(r)


#Display a multiplication table for any given number

#no = int(input("Enter a number "))
#multiply = 1

#while  multiply <= 10:
#    r = no * multiply
#    print(no, "X", multiply, "=", r)
#    multiply = multiply + 1


######*************** STUDENT CHALLENGE************************

# i. counting the number of Digit in a number

#num = int(input("Enter a number "))
#count = 0
#while num > 0 :
#    num = num // 10
#    count += 1
#print("The number has", count, "digit")

# ii. find the sum of Digit in a number

#num = int(input("Enter a number "))
#original = 0

#while num > 0:
#    r = num % 10
#    num = num // 10
#    original = original + r
#print(original)

# iii. Reversing a number


#num = int(input("Enter a number "))
#original = 0

#while num > 0:
#    r = num % 10
#    num = num // 10
#   original = original * 10 + r
#print(original)



# iii. check if a number is palindrome

num = int(input("Enter a number "))
b = num
original = 0

while num > 0:
    r = num % 10
    num = num // 10
    original = original * 10 + r

print(original)
if original == b:
    print("This is a palindrome")
else:
    print("This is not a palindrome")

#for loop (iterate over something)

#for i in range(5):
#    print(i)
#    Common uses:

#    for char in "hello":
#        print(char)

#    for item in [1, 2, 3]:
#        print(item)


#while loop (repeat while condition is true)
#count = 0

#while count < 5:
#    print(count)
#    count += 1

#Loop control statements
#break – exit loop immediately
#for i in range(10):
#    if i == 5:
#        break

#continue – skip to next iteration
#for i in range(5):
#    if i == 2:
#        continue
#    print(i)

#Match-case (Python 3.10+)

#Like a switch statement.

#command = "start"

#match command:
#    case "start":
#        print("Starting")
#    case "stop":
#        print("Stopping")
#    case _:
#        print("Unknown command")

#Exception control flow (try / except)

#Handle errors gracefully.

#try:
#    x = int(input("Enter number: "))
#except ValueError:
#    print("Not a number")
#else:
#    print("Success")
#finally:
#    print("Done")