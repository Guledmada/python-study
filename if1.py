#conditional statements in python
#they are used to make decisions in the code bsed on certain conditions
#in python most common used conditional statements are:
#1. if statement is used to execute a block 
     #of code if a given condition is true 
#example :
a= 10
b = 15

if (a > b) :
    print("a is greater than b")
else:
    print("You are right")

#take a users input for marks(input function)
    #write a program that checks if marks is above 50
    #display pass
    #otherwise display fail

#if-else executes a block of code if the condition is false
#elif is used when you have mu;tiple conditions to check
    #take a users input on points
    #write a program that checks on the grade  based on the following conditions 
    #80 to 100 A
    #70 to 79 B
    #60 to 69 C
    #50 to 59 D
    #40 to 49 E
#otherwise "Invalid marks"
    

# marks = int(input("Enter marks "))
# if marks > 50:
#     print("Pass")
# else:
#     print("Fail")


# if marks > 50:
#     print("Pass")
# elif(marks > 40) and (marks < 50):
#     print("Average")
# else:
#     print("Fail")




# grade = int(input("Enter a grade "))
# if grade >80 <100:
#     print("A")
# elif grade >70 <79:
#     print("B")
# elif grade >60 <69:
#     print("C")
# elif grade >50 <59:
#     print("D")
# elif grade >40 <49:
#     print("E")
# else:
#     print("Invalid Marks")



#checking if a numebr is even
    
number = float(input("enter number "))
if (number % 2==0):
    print("even")
else:
    print("odd")



#write a program that cehcks if a number is a prime number


# cars = ["audi", "bmw", "toyota", "subaru"]
# for car in cars:
#     if  car == "bmw":
#         print(car.upper())
#     else:
#         print(car.title())

# for car in cars:
#     if  car == "mazda":
#         print(car.upper())
#     else:
#         print("nothing".title())
    

    