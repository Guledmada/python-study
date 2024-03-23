#Functions are used to write a block of code for the purpose of reusing it later on.
# there are two types of functions , in built function and custom functions
# function are used to perform a certain task
#functions take in data, performs operation on that data and gives final output. 
#how to define functions -> start with the "def" key word followed by the name of that function, and then(parameters),
# then followed by a : 
#example of a function that says hello
#functions cannot be executed unless they are called by their names. 
#aparemeters are variables used only inside the function
#arguments are exact values passed into the function.
 
# def greetings (a):
#     print(f"Hello {a}")
    
# name = input("Whats your name ")
# greetings(name)

#area of a triangle

# def area_triangle (a, b):
#     area = a * b * 0.5
#     print(area)
    
# height = int(input("height "))
# base = int(input("base "))
# area_triangle(height, base)

# def area_rectangle(l, w):
#     area = l * w
#     print(area)
    
# lenght = int(input("lenght of a rectangle "))
# width = int(input("width of a rectangle "))
# area_rectangle(lenght, width)

# Prompt the user for a number either on a form input or the terminal. Depending on whether the number is even or odd, 
# display  either “odd” or “even” to the user.
#  Hint: how does an even / odd number react differently when divided by 2?

# def check_number(num):
#     if num % 2 ==0:
#         print("The number is even")
#     else:
#         print("The number is odd")
        
# number = int(input("enter a number "))
# check_number(number)

# Implement a program that takes 3 form inputs or from the terminal, and stores them in three variables.
# Return the largest of the three. Do this without using the the inbuilt max ()function!

# def largest_number (num1, num2, num3):
#     if num1 > num2 and num1 > num3:
#         results = f"{num1} is the largest number " 
#     elif num2 > num1 and num2 > num3:
#         results = f"{num2} is the largest number "
#     else:
#         results = f"{num3} is the largest number "
#     return(results)
        
# first_number = int(input("Enter a number "))
# second_number = int(input("Enter a number "))
# third_number = int(input("Enter a number "))

# value = largest_number(first_number, second_number, third_number)
# print(value)

# Write a python program that takes from a user 5 inputs (maths, eng, swa, sci, sos). 
# Create a function that calculates the total marks another the average marks ,then a functions that finds the grade
# according to the table below. 
# Use the value from total to get the average and average to find the grade.

# A > 79 , B - 60 to 79, C -  59 to 49, D - 40 to 49, E - less 40


# def subjects (maths, eng, swa, sci, sos):
#     total_marks = maths + eng + swa + sci + sos
#     return total_marks
# maths = int(input("Enter marks for math "))
# eng = int(input("Enter marks for eng "))
# swa = int(input("Enter marks for swa "))
# sci = int(input("Enter marks for sci "))
# sos = int(input("Enter marks for sos "))
# total_sum = subjects(maths, eng, swa, sci, sos)
# print(total_sum)

# def calc_average (total, subjects):
#     average = total / subjects
#     return average
# total_avg = calc_average(total_sum, 5)
# print(total_avg)

# def calc_grade(avg):
#     if avg > 79:
#         grade = "A"
#     elif avg > 60:
#         grade = "B"
#     elif avg > 59:
#         grade = "C"
#     elif avg > 49:
#         grade = "D"
#     else:
#         grade = "E"
#     return grade
# average = calc_grade(total_avg)
# print(average)

# Write a program that takes input of someone's basic salary and benefits, adds them to find the gross salary then uses
# the gross salary to find the NHIF.
