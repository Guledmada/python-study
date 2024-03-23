# Implement a program that takes 3 form inputs or from the terminal, 
# and stores them in three variables.Return the largest of the three.
# Do this without using the the inbuilt max () function!

number = input("Enter first number ")
number2 =input("Enter second number ")
number3 = input("Enter third number ")
if number >= number2 and number >= number3:
    new_number = f"{number} is the Largest number "
elif number2 >= number and number2 >= number3:
    new_number = f"{number2} is the Largest number "
else:
    new_number = f"{number3} is the largest number "
print(new_number)