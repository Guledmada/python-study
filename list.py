# # TASK: Create a List of days of the Week. 
# #Print the day today using an index.
day_of_the_week = ["Sunday", "Monday", "Tuesday",
                    "Wednesday", "Thursday", "Friday", "Saturday", "Wednesday"]
# print(day_of_the_week[2::-1]) #reverses the list 
# # print(day_of_the_week[::-2])
# # print(day_of_the_week[2::2])

# print(day_of_the_week * 4)
# print ("Sunday" in day_of_the_week)
# del day_of_the_week[4]
# day_of_the_week.append("May") #adding values at the end of the list
# day_of_the_week.insert(5, "April")
# day_of_the_week.pop(0) #remove last value by default
# day_of_the_week.remove("Wednesday")
#day_of_the_week.clear() #use to clear entire list
# print(day_of_the_week.count("Wednesday")) checking the occurence of a value.
a = day_of_the_week.copy()
# print(a)
# day_of_the_week.extend(a)
# print(day_of_the_week)
# day_of_the_week.reverse() #reverses the list 
# print(day_of_the_week)
# day_of_the_week.sort() sort them alphabetically
# print(day_of_the_week)


# tasks Display 2 from the list.
# 2. Output James  from the list.
# 3. Using a method add 56 at the end of the list.
# 4. Using a method add the name Mike between James and Mary
# 5. Change the value of 2 to 8
# 6. Remove John and Mary from the list.
# 7. Using a function, determine the length of the list

# trainees = ["John", [2, ["James","Mary"]]]

# # print (trainees[1][0])
# # print(trainees[1][1][0])
# # trainees.append(56)
# # print(trainees)
# trainees[1][1].insert(1, "Mike")
# trainees[1][1].insert(3, "Adam")
# trainees.insert(1, 'kevin')
# trainees[2][0] = 8
# trainees[2][1].remove("Mary")
# trainees.remove("John")
# print(len(trainees))

L = ['a', 'b', ['cc', 'dd', ['eee', 'fff']], 'g', 'h']
print(L[2][2][1])