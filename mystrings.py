first_name = "      Guled       "
last_name = "Adam"
x= last_name.endswith("Adam")
email = "guledezra@gmail.com"

first_name = first_name.title().strip()
last_name = last_name.title().strip()
email = email.lower().strip()
full_name = first_name + " " + last_name
print(full_name, email)
print (email[-8:-4])
print(email[-8:15])
print(email[11:-4])
print(len(first_name))
#indexing- to get a single character from a string 