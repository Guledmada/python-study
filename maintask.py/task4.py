import re

# Function to validate email format
def is_valid_email(email):
    # Regular expression for a simple email validation
    email_pattern = re.compile(r"[^@]+@[^\.]+\..+")

    # Check if the email matches the pattern
    return bool(re.match(email_pattern, email))

# Get user input for an email address
user_input = input("Enter an email address: ")

# Validate the email
if is_valid_email(user_input):
    print("Valid email address")
else:
    print("Invalid email address")
