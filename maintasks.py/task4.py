# Write a program which accepts email as form input or from terminal.
# Validate the email by checking if it's a valid email. 
# Hint: Check if it contains an “@” symbol and “.” symbol.
email = input("Enter your email address ")
# if "@" and "." in email:
#     print("valid email")
# else:
    # print("invalid email")
if email.count("@") == 0 and email.count(".") ==0:
    print("invalid email")
else:
    print("valid email")