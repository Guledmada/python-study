# A for loop is used to perform a repetitive task over and over. 
# You can also loop through a list and get individual values as below:
# We first use range function to generate numbers. 
# It's always best to typecast the range in a a list or a tuple .
# Then we get individual values using a loop.

# nil = []
# for num in range(0, 10):
#     if num == 6:
#         pass
#     nil.append(num)
# print(nil)


# Write a program that displays a numbers 1 to 50 inside a list.
# From 1 above display the ones divisible by 7 or 5 inside a list.
# Find sum and average of values in the range between 10 to 40.
# Put in a list the first 10 odd numbers between 10 to 50. 
# write a program that takes a number as input and prints its multiplication table up to 10 using a for loop.
# write a program that counts and prints the number of even numbers between 1 and 50 using a for loop

# numbers = []
# for number in range(1, 51):
#     numbers.append(number)
# print(numbers)
# number = []
# for num in range (1, 51):
#     if num % 7 == 0 or num % 5 ==0:
#         number.append(num)
# print(number)

# sum = 0
# number = []
# for add in range(10, 41):
#     sum += add
#     number.append(add)
#     avg = sum / len(number)
# print(avg)

#Put in a list the first 10 odd numbers between 10 to 50. 
# num = []
# count = 0
# for odd in range(10, 51):
#     if odd % 2 != 0:
#         count += 1
#         num.append(odd)
#         if count == 15:
#             break
# print(num)

#write a program that takes a number as input and prints its multiplication table up to 10 using a for loop.
# num = int(input("enter a number "))
# for number in range(0, 11):
#     results = num * number
#     print(results)


#write a program that counts and prints the number of even numbers between 1 and 50 using a for loop
# num = []
# count = 0
# for even in range(1, 51):
#     if even % 2 ==0:
#         count += 1
#         num.append(even)
# print(count)
# print(num)

# def logical(x):
#     if x == 1:
#         return 1
#     else:
#         return(x + logical(x-1))
    
# result = logical(3)

# print(result)

for i in range(2):
    for j in range(3):
        print(i,j)