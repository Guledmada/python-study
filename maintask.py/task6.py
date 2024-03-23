# Correct password
correct_password = "admin@123"

# Number of attempts allowed
attempts_allowed = 4

# Loop for password attempts
for attempt in range(1, attempts_allowed + 1):
    # Get user input for the password
    user_password = input("Enter the password: ")

    # Check if the entered password is correct
    if user_password == correct_password:
        print("Access granted!")
        break
    else:
        remaining_attempts = attempts_allowed - attempt
        if remaining_attempts > 0:
            print(f"Incorrect password. {remaining_attempts} attempts remaining.")
        else:
            print("Account blocked. Too many incorrect attempts.")
