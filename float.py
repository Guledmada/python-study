#Convert a float to an integer with an inbuilt function in Python
#temp = 56.8926 to 57

# temp = 56.8926
# temp1 = int(temp)
# temp2 = round(temp)
# temp3 = round(temp, 2)
# print(temp2)

#Convert the float below to give the results as follows
#temp=56.8926 to 8.926 
temp = 56.8926 
temp = str(temp)
print(type(temp))
temp = temp[3:]
temp = int(temp)
temp = temp / 1000
print(temp)

