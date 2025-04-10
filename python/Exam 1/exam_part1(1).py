# MARGARET MARY BOYLE

def repeat_start(s):
    """
    Given a string, return a new string where the first two characters 
    are repeated 
    three times. If the string is shorter than two characters, 
    return the string repeated three times.
    repeat_start("hello") returns "hehehe"
    repeat_start("a") returns "aaa"
    """
    return (s[:2]*3)
    


def shift_left(lst):
    """
    Given a list, rotate its elements to the left by one position. 
    The first element should become the last.
    shift_left([1, 2, 3, 4]) returns [2, 3, 4, 1]
    shift_left([5]) returns [5]
    """
    if len(lst) > 1:
        return lst[1:] + [lst[0]]
    return lst
    

def count_digits(s):
    """
    Use a comprehension to count the number of digits in a string.
    *** Important: your code must use comprehensions and should not be more than
    two lines of code including the return statement ***
    count_digits("The year is 2025!") returns 4
    The string function isdigit() returns True if the string is a digit.
    Eg. c='1' c.isdigit() returns True
    """
    return sum(1 for c in s if c.isdigit())
    

def swap(lst):
    """
    Given a list, find the minimum element in the list and swap it with the first
    element in the list. Return the list.
    swap([5,4,3,2,1]) returns [1, 4, 3, 2, 5]
    """
    if lst:
        minimum = lst.index(min(lst))
        lst[0], lst[minimum] = lst[minimum], lst[0]
    return lst
    

def build_grades_dict():
    '''
    Create a dictionary where the key is a student's name and the value is
    their grade stored as an integer. 
    Read in the file, grades.txt, store the student's first and last name as 
    the key (first and last name should have a space between them) 
    and their grade as the integer value.
    Your output should read:
     {'Alice Brown': 90, 'Bob Smith': 85, 'Charlie Johnson': 78, 
     'Daisy Lee': 92, 'Evelyn Taylor': 88}
    '''
    student_dictionary = {}
    with open("grades(1).txt") as file:
        for line in file:
            info = line.strip().split()
            key = info[0] + " " + info[1]
            grade = int(info[2])
            student_dictionary[key] = grade
    return student_dictionary
    

# Test Cases
print('repeat_start("hello") expected: hehehe')
print('repeat_start("hello") actual:', repeat_start("hello"))
#print('repeat_start("a") expected: aaa')
#print('repeat_start("a") actual:', repeat_start("a"))

print('shift_left([1, 2, 3, 4]) expected: [2, 3, 4, 1]')
print('shift_left([1, 2, 3, 4]) actual:', shift_left([1, 2, 3, 4]))
#print('shift_left([6, 7, 8, 9]) expected: [7, 8, 9, 6]')
#print('shift_left([6, 7, 8, 9]) actual:', shift_left([6, 7, 8, 9]))

print('count_digits("The year is 2025!") expected: 4')
print('count_digits("The year is 2025!") actual:', count_digits("The year is 2025!"))
#print('count_digits("The year is abc123!") expected: 3')
#print('count_digits("The year is abc123!") actual:', count_digits("The year is abc123!"))

print('swap([5,4,3,2,1]) expected: [1, 4, 3, 2, 5]')
print('swap([5,4,3,2,1]) actual:',swap([5,4,3,2,1]))
#print('swap([9,8,7,6,5]) expected: [5, 8, 7, 6, 9]')
#print('swap([9,8,7,6,5]) actual:',swap([9,8,7,6,5]))

print(build_grades_dict())
