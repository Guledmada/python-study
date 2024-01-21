#Clean up the following variable to give the clean version in 
#lower case.Using inbuilt methods in the str class 
#name = “  JOHn  .“ to “john”

name = "   JOHn  ."
name = name.replace(".", " ")
name = name.strip()
name = name.lower()
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
sentence_two = "Defeats for the Clinton forces, this was her moment of triumph"
#print(sentence_two.index("S"))
sentence_two = sentence_two[16:30]
print(sentence_two)
#Split the below sentence using a semicolon i.e ; And display length of the result. 
#“The lazy dog; ran so fast; it hit the wall.”
dog = "The lazy dog; ran so fast; it hit the wall"
dog = dog.split(";")
print(dog)
print (len(dog))
print(dog[2])