# Take three inputs from a user, separately. 
# Print the largest of the numbers.
# Hint: Determine what type of data is taken in as input
# Take as input from a user the temperature if the temperature is
# above 30°C display “The temperature is too high”, 
# otherwise display “Normal temperature”


# num1 = input("Enter first number ")
# num2 = input("Enter second numeber ")
# num3 = input("Enter third numeber ")
# largest_number = max(num1, num2, num3)
# print ("The largest number is :", largest_number)

# num1 = float(input("Enter first number "))
# num2 = float(input("Enter second numeber "))
# num3 = float(input("Enter third numeber "))

# if (num1 > num2 and num1 > num3):
#     print(num1, "is greatest")
# elif (num2 > num1 and num2 > num3):
#     print(num2, "2 is greatest")
# else: 
#     print(num3, "is greatest")

temp = float(input("Enter the temperature in celcius "))
if temp > 30:
    print("The Temperature is too high")
elif temp >15 and temp <30 :
    print("normal")
elif temp >0 and temp <15 :
    print("cold")
else:
    print("extremely cold")