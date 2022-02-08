"""
Requirement: Given a string, this function returns the first non repeating character.
Implementation: We iterate through the array of characters in the string and store the
frequency in a dictionary. Once we finish, we iterate through the dictionary to identify
the first element with a count of 1 character.
We return the first unique element that found or None if we run through the array and none is unique.
Complexity: O(n) T and O(1) S as we iterate through the array to store the value count into the
dictionary and the dictionary will store a maximum of 26 characters. Given that 26 is a constant,
the space complexity will be O(1).
"""


def first_non_repeating_character(string):
    character_count = {}
    for i in string:
        character_count.update({i: character_count.get(i, 0) + 1})
    for index in range(len(string)):
        if character_count[string[index]] == 1:
            return string[index]
    return None
