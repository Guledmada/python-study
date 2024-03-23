# Example: person = {“name” : “John Doe”, “age”:30, “location”: “Nairobi”,
# “email” :”johndoe@mail.com”}
# Accessing a dictionary: print(person[“name”])

person = {"name" : "John Doe", "age" :30,
           "location": "Nairobi", "email" :"johndoe@mail.com"}
# print(person["email"])
# person["City"] = "Mombasa" #adding value
# print(person)
# person["age"] = 40 #updating age
# person["location"] = "Kisumu" #updating location
# del person["name"] #deleting a key and a value 
# print(person)
# print(person.items()) #displays a list of tuples of key and value
# print(person.keys()) #displays a list of keys 
# print(person.values()) #displays a list of values 
print("city" in person) #check if a key exists in a dic. gives you boolean
