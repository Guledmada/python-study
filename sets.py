# Remove friday and sunday from the set using methods.
# Add them back to the set

# days = {"monday","tuesday","wednesday","thursday",
#          "friday","saturday","sunday","sunday","sunday","sunday"}
# days.add("May")
# days.remove("friday")
# days.remove("sunday")
# days.add("Friday")
# days.add("Sunday")
# print(days)
numbers = {10, 20, 25, 45, 90, 120, 60}
numbers1 = {10, 20, 45, 55, 90, 100}
#union | combines elements from two sets excluding duplicates 
union_set = numbers|numbers1
print(union_set)
#intersections we use & operator. 
#it finds common element between two sets 
intersection_set = numbers & numbers1
print(intersection_set)
#difference we use - sign, and it is used 
#to find element present in first set but not second set
difference_set = numbers - numbers1
print(difference_set)
#symmetric difference we use the ^ sign 
#and finds elements present in either set but not similar numbers
symmetric_difference = numbers ^ numbers1
print(symmetric_difference)

