name = input("Please enter your name.")
print("Hello,", name)

try:
    num = int(input("Enter a number."))
    print(num)
    double = num*2
    print(double)
except:
    print("You didn't enter a number.")

# read in files
with open("movies.txt") as file:
    for line in file:
        print(line.strip()) # the .strip gets rid of the double line between printing the titles

with open("heights.txt") as file:
    for line in file:
        info = line.strip().split()
        print(info)
        info[2] = int(info[2])
        print(info)

file_name = input("Enter a file name:")
with open(file_name) as file:
    count = 1
    for line in file:
        print(str(count) + ". " + line.strip())
        count += 1