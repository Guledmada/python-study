 #Find wednesday using an index
#2. Using a function a find the length of the tuple.
#3. Replace Thursday with Thur

days = ("monday","tuesday","wednesday","thursday", 
        "friday","saturday","sunday")
print(days[2])
print(len(days))
days = list(days)
days[3] = "Thur"
days = tuple(days)
days = list(days)
days[2] = "Wed"
days = tuple(days)
print(days)
