correct_pin = "1334"
attempts = 3
for i in range(1,4):
    pin = input("Enter pin number ")
    if pin == correct_pin:
        print("access granted ")
        break
    else:
        rem_att = attempts - 1
        if rem_att > 0:
            print("Login successful ")
        else:
            print("Blocked")
    