# Prompt the user to enter the base and height of a triangle
# base = float(input("Enter the base of the triangle: "))
# height = float(input("Enter the height of the triangle: "))

# # Calculate the area of the triangle
# area = 0.5 * base * height

# Print the result
#print(f"The area of the triangle with base {base} and height {height} is: {area}")

#task 2
#Prompt the user for a number either on a form input or the terminal. 
# Depending on whether the number is even or odd, display  either “odd”
# or “even” to the user.
#  Hint: how does an even / odd number react differently when divided
#  by 2?
# Once you learn functions,revisit this and write this code inside
#  a function.
# Extras:
# If the number is a multiple of 4, print out “divisible by 4”.

# Prompt the user for a number
user_number = int(input("Enter a number: "))

# Check if the number is even or odd
if user_number % 2 == 0:
    print("The number is even.")
else:
    print("The number is odd.")

# Check if the number is a multiple of 4
if user_number % 4 == 0:
    print("The number is divisible by 4.")
