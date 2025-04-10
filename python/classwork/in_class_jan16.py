# Exercise 1: Printing Numbers
    # Write a for loop to print all numbers from 1 to 20 that are divisible by 3
for i in range(1, 21):
    if i % 3 == 0:
        print(i)
print()

# Exercise 2: Sum of Even numbers
    # Write a while loop that calculates the sum of all even numbers between 1 and 50 (inclusive). Print the result.
count = 1
sum = 0
while count <= 50:
    if count % 2 == 0:
        sum += count
    count += 1
print(sum)
print()

# Exercise 3: List Manipulation
    # You are given a list of numbers: numbers=[5, 8, 2, 15, 10, 3, 7]
        # 1. Use a for loop to print the numbers greater than 5.
numbers = [5, 8, 2, 15, 10, 3, 7]
for numbers in numbers: 
    if numbers > 5:
        print(numbers)
print()

# Challenge from board
lst = [1, 2, 3, 4, 5]
lst2 = []
lst.append(lst[1])

for i in range(1, len(lst)):
    lst2.append(lst2[i-1]+lst[i])
print(lst2)
print()

# Functions
    # Exercise 1: Swap elements
            # Write a function called swap that takes a list of elements and swaps teh first and last elements. For example,
            # if the in put to the function is [0, 3, 8, 4, 5] the swapped list would be [5, 3, 8, 4, 0]. You do not need
            # to return the list. Test the function like this:

def swap(lst):
    tmp = lst[0]
    lst[0] = lst[len(lst)-1]
    lst[len(lst)-1] = tmp
lst = [0, 3, 8, 4, 5]
swap(lst)
print(lst)