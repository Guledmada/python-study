#Write a program that displays a numbers 1 to 50 inside a list.
# numbers = list(range(1, 51))
# # print(numbers)
# #From 1 above display the ones divisible by 7 or 5 inside a list.
# divisible_by_7_or_5 = []

# for number in range(1, 51):
#     if number % 7==0 or number %5==0:
#         divisible_by_7_or_5.append(number)
 
# print(divisible_by_7_or_5)

#Find sum and average of values in the range between 10 to 40.

# sum = 0
# average = []

# for i in range(10, 41):
#     sum = sum + i 
#     average.append(i)
#     avg = sum/len(average)


# print(sum)
# print(avg)


#Put in a list the first 10 odd numbers between 10 to 50. 

oddnum = []
for num in range(10,51):
    if num % 2 != 0:
        oddnum.append(num)
results = oddnum[0:10] #slicing 
print(results)

# #5 write a program that takes a number as input and prints its 
# #multiplication table up to 10 using a for loop.

# # Get a number as input from the user
# num = int(input("Enter a number: "))

# # Print multiplication table up to 10 for the input number
# print(f"Multiplication table for {num}:")

# for i in range(1, 11):
#     result = num * i
#     print(f"{num} x {i} = {result}")


#6 write a program that counts and prints the number of even 
    #numbers between 1 and 50 using a for loop

# Count and print the number of even numbers between 1 and 50 using a for loop

# Initialize a variable to count even numbers
# even_count = 0


# for number in range(1, 51):
#     if number % 2 == 0:
#         even_count += 1


# print(f"Number of even numbers between 1 and 50: {even_count}")
