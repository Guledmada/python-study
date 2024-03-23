# Get user input for a phone number
user_input = input("Enter a phone number: ")


cleaned_number = ''.join(filter(str.isdigit, user_input))


if cleaned_number.startswith("07"):
    formatted_number = "+254" + cleaned_number[1:]
elif cleaned_number.startswith("71"):
    formatted_number = "+254" + cleaned_number
elif cleaned_number.startswith("254"):
    formatted_number = "+" + cleaned_number
elif cleaned_number.startswith("01"):
    formatted_number = "+254" + cleaned_number[1:]
else:
    print("Invalid phone number format")
    exit()


print(formatted_number)
