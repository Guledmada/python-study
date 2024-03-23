# Write a program which gets a phone number from a form input or terminal
# Validates the phone number by checking if it starts with
# +254.. or 07.. or 71… or 254.. or 01... Convert the number to start 
# with +254… 
# e.g if a user enters “0712345678”, the program should display “+254712345678”
# e.g if a user enters “0112345678”, the program should display “+254112345678”
# e.g if a user enters “712345678”, the program should display “+254712345678”


phone_number = input("Enter the phone number ")
if phone_number[0:4] == "+254" and len(phone_number) == 13:
    valid_num = "This is correct format" 
elif phone_number[0:2] == "07" and len(phone_number) == 10:
    valid_num = "+254" + phone_number[1:] + " is a valid number"
elif phone_number[0:1] == "7" and len(phone_number) == 9:
    valid_num = "+254" + phone_number 
elif phone_number[0:3] == "254" and len(phone_number) == 12:
    valid_num = "+" + phone_number
elif phone_number[0:2] == "01" and len(phone_number) == 10:
    valid_num = "+254" + phone_number[1:]
print(valid_num + "is a valid number ")