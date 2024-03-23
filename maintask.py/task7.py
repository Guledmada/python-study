scores = int(input("Enter your score "))
if scores >= 79:
    print("A")
elif scores >= 60 and scores <= 79:
    print("B")
elif scores >= 49 and scores <= 59:
    print("C")
elif scores >= 40 and scores <= 49:
    print("D")
elif scores < 40:
    print("E")
