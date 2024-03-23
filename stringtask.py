#Clean up the following variable to give the clean version in 
#lower case.Using inbuilt methods in the str class 
#name = “  JOHn  .“ to “john”

# name = "   JOHn  ."
# name = name.replace(".", " ")
# name = name.strip()
# name = name.lower()
# print(name)

# Slice the below string to get you the resulting sentence:
# sentence_one = “The Dog Breed is German Shepherd” 
# only display “Breed is German”
# sentence_two = “Defeats for the Clinton forces, this was her moment
 #of triumph” only display “Clinton forces”

# sentence_one = "The Dog Breed is German Shepherd"
# #print(sentence_one.index("n"))
# sentence_one = sentence_one[8:23]
# print(sentence_one)

# sentence_two = "Defeats for the Clinton forces, this was her moment of triumph"
#print(sentence_two.index("S"))
# sentence_two = sentence_two[16:30]
# print(sentence_two)

# #Split the below sentence using a semicolon i.e ; And display length of the result. 
# #“The lazy dog; ran so fast; it hit the wall.”
# dog = "The lazy dog; ran so fast; it hit the wall"
# dog = dog.split(";")
# print(dog)
# print (len(dog))

#first_name="  Joh.n"  last_name=
#"   Do,e" Clean up and display Full name i.e John Doe
# first_name = "  Joh.n"
# last_name = "   Do,e"
# first_name = first_name.replace(".", "")
# first_name = first_name.strip()
# last_name = last_name.replace(",", "")
# last_name = last_name.strip()
# print (first_name + " " + last_name)

#Having the string r = '["E","W","C"]' #Manipulate it to display EWC
# r = '["E", "W", "C"]'
# #method1
# # r = eval(r)
# # r = "".join(r)

# #method 2
# r = "".join(filter(str.isalpha, r))
# print(r)


