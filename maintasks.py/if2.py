# marks = int(input("Enter the grade ")) 
# if marks >= 0 and marks <=100: #the program will run only if it is true
#     if marks >= 90:
#         grade = "A"
#     elif marks >= 80 and marks < 90:
#         grade = "B"
#     elif marks >= 70 and marks < 80:
#         grade = "C"
#     elif marks >= 60 and marks < 70:
#         grade = "D"
#     else:
#         grade = "E"

# else:  #the program will only run if the statement is false
#     grade = "failed"
# print(grade)





# numbers = int(input("Check a number "))
# if numbers % 2 == 0:
#     print("the number is even")
# else:
#     print("the number is odd ")

#check if the numebr entered is divisble by 7 and 5
# if numbers % 7 == 0 and numbers % 5== 0:
#     results = "Divisible "
#     if numbers % 2 == 0:
#       results = "the number is even " 
#     else:
#        results = "the number is odd " 
# else:
#     results = "Not divisible "
# print(results)


# average_marks= 60
# if average_marks  >= 70:
#  		 print("A")
# elif average_marks  >= 60 and average_marks  < 70:
#  	 print("B")
# elif average_marks  >= 50 and average_marks  < 60:
#    		print("C")
# elif average_marks  >= 40 and average_marks  < 50:
#    		print("D")
# else:
#    print("E")

# Take three inputs from a user, separately. Print the largest of the numbers.
#     Hint: Determine what type of data is taken in as input
# Take as input from a user the temperature if the temperature is above 
# 30°C display “The temperature is too high”, otherwise display “Normal temperature”

# num = input("enter first number ")
# num2 = input("enter second number ")
# num3 = input("enter third number ")
# if num > num2 and num > num3:
#     large_num = f"{num} is the largest num"
# elif num2> num and num2 > num3:
#     large_num = f"{num2} is the largest num"
# else:
#     large_num = f" {num3} is the largest num"
# print(large_num)

# temp = float(input("Enter the temperature "))
# if temp > 30:
#     temperature = "The temperature is too high "
# elif temp > 15 and temp <= 30:
#     temperature = "Normal temperature"
# else:
#     temperature = "Too cold "
# print(temperature)



prods =[["omo", "30 ksh", "300"], ["milk", "50 ksh", '200'], ["bread", "45ksh", "359",]["coffee", "5 ksh", "79"]["tea", "100 ksh", "1000"]]
total_stock = 0
for prod in prods:
    print(prod[2])
stock = int(prod[-1])
total_stock += stock
print("Total stock in the company:", total_stock)