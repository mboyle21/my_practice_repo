# Margaret Mary Boyle

# Function #1
def function_one(lst): # Calling it function_one to know what it is compared to the directions
    return len(lst) # Using the len() function to return an integer of the length of the list



# Function #2 ... goal is to flip the first and last letter of the word
def function_two(string):

    if " " in string:
        return "Error: Input must be a single word with no spaces." # Only dealing with one word strings...so this accounts for if the string is more than one word
    
    if len(string) <= 1: # Accounts for words that are too small to flip first and last letter AKA one letter words
        return "Error: Input is too small."
    
    return string[-1] + string[1 : -1] + string[0] # Takes the last letter at the beginning, the first letter at the end, and keeps the letters in between first and last letter in their same order



# Test calls for Function #1
print("Function #1 Test Calls:")
print(function_one([1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3]))
print(function_one([13, 77, 84]))
print(function_one([]))

# Test calls for Function #2
print("Function #2 Test Calls")
print(function_two("two words"))
print(function_two("villanova"))
print(function_two("racecar"))
print(function_two("I"))