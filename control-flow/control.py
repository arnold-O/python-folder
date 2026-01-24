#Loops are repeating statements

# We have for loop and while loop

#statement can be repeated along the lens of truth or number times


#while loop
# Using count for while loop

#count = 0
#while count < 5:
#    print(count + 1, "Hello from the main page")
#    count += 1

count  = int(input("Enter a number "))


while count > 0:
    r = count % 10
    count = count // 10
    print(r)




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