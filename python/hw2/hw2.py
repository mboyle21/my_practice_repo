# MARGARET MARY BOYLE
# I used CoPilot for a little bit of help on finding the correct constructors to use.

def middle_three(str):
    """
    Given a string with an odd length greater than or equal to 3, 
    return the middle three characters.
    If the string length is less than 3 or even, return an empty string.
    
    Example:
    middle_three("abcdefg") returns "cde"
    middle_three("12345") returns "234"
    middle_three("hi") returns ""
    """
    if len(str) < 3 or len(str) % 2 == 0:
        return ""
    
    middle = len(str) // 2

    return str[middle - 1: middle + 2]

  

def filter_long_words(words, length):
    """
    Given a list of strings, return a new list containing only the words
    that have a length greater than the specified `length` parameter.
    Important: Use list comprehensions.

    Example:
    filter_long_words(["apple", "bat", "car", "dolphin"], 3) returns ["apple", "dolphin"]
    filter_long_words(["a", "ab", "abc", "abcd"], 2) returns ["abc", "abcd"]
    """
    return [word for word in words if len(word) > length]
  

def unique_characters(word):
    """
    Implement a function that accepts a string and returns a set of 
    unique characters in the string.
    Important: this must be done in at most two lines of code.
    
    Example:
    unique_characters("hello") returns {"h", "e", "l", "o"}
    unique_characters("abc") returns {"a", "b", "c"}
    """
    return set(word)
  

def merge_dictionaries(dict1, dict2):
    """
    Given two dictionaries, merge them into one dictionary. 
    If the same key exists in both dictionaries,
    the value from `dict2` should overwrite the value from `dict1`.

    Example:
    merge_dictionaries({"a": 1, "b": 2}, {"b": 3, "c": 4}) returns {"a": 1, "b": 3, "c": 4}
    merge_dictionaries({}, {"x": 10}) returns {"x": 10}
    """
    return {**dict1, **dict2}
  

def character_frequency(strings):
    """
    The classic character frequency algorithm: given a list of strings, 
    return a dictionary with a key for each character and the value being 
    the number of times that character appears across all strings.

    Example:
    character_frequency(["abc", "ab", "c"]) returns {"a": 2, "b": 2, "c": 2}
    character_frequency(["hello", "world"]) returns {"h": 1, "e": 1, "l": 3, "o": 2, "w": 1, "r": 1, "d": 1}
    """
    frequency = {}

    for string in strings: 
        for character in string:
            if character in frequency:
                frequency[character] += 1
            else:
                frequency[character] = 1
    return frequency
  
def group_by_length(strings):
    """
    Write a function that takes a list of strings and groups them by their 
    lengths. Return a dictionary where keys are the lengths and values 
    are lists of words with that length.

    Example:
    group_by_length(["a", "bb", "ccc", "dd", "eee"]) returns {1: ["a"], 2: ["bb", "dd"], 3: ["ccc", "eee"]}
    group_by_length(["apple", "bat", "cat", "dolphin"]) returns {5: ["apple"], 3: ["bat", "cat"], 7: ["dolphin"]}
    """
    length_of_groups = {}

    for word in strings:
        length = len(word)
        if length not in length_of_groups:
            length_of_groups[length] = []
        length_of_groups[length].append(word)
    return length_of_groups

  

# Test functions
assert middle_three("abcdefg") == "cde", 'middle_three("abcdefg") expected "cde"'
print("correct")
assert middle_three("12345") == "234", 'middle_three("12345") expected "234"'
print("correct")
assert middle_three("hi") == "", 'middle_three("hi") expected ""'
print("correct")

assert filter_long_words(["apple", "bat", "car", "dolphin"], 3) == ["apple", "dolphin"], 'Expected ["apple", "dolphin"]'
print("correct")
assert filter_long_words(["a", "ab", "abc", "abcd"], 2) == ["abc", "abcd"], 'Expected ["abc", "abcd"]'
print("correct")

assert unique_characters("hello") == {"h", "e", "l", "o"}, 'unique_characters("hello") expected {"h", "e", "l", "o"}'
print("correct")
assert unique_characters("abc") == {"a", "b", "c"}, 'unique_characters("abc") expected {"a", "b", "c"}'
print("correct")

assert merge_dictionaries({"a": 1, "b": 2}, {"b": 3, "c": 4}) == {"a": 1, "b": 3, "c": 4}, 'Expected {"a": 1, "b": 3, "c": 4}'
print("correct")
assert merge_dictionaries({}, {"x": 10}) == {"x": 10}, 'Expected {"x": 10}'
print("correct")

assert character_frequency(["abc", "ab", "c"]) == {"a": 2, "b": 2, "c": 2}, 'Expected {"a": 2, "b": 2, "c": 2}'
print("correct")
assert character_frequency(["hello", "world"]) == {"h": 1, "e": 1, "l": 3, "o": 2, "w": 1, "r": 1, "d": 1}, 'Expected {"h": 1, "e": 1, "l": 3, "o": 2, "w": 1, "r": 1, "d": 1}'
print("correct")

assert group_by_length(["a", "bb", "ccc", "dd", "eee"]) == {1: ["a"], 2: ["bb", "dd"], 3: ["ccc", "eee"]}, 'Expected {1: ["a"], 2: ["bb", "dd"], 3: ["ccc", "eee"]}'
print("correct")
assert group_by_length(["apple", "bat", "cat", "dolphin"]) == {5: ["apple"], 3: ["bat", "cat"], 7: ["dolphin"]}, 'Expected {5: ["apple"], 3: ["bat", "cat"], 7: ["dolphin"]}'
print("correct")