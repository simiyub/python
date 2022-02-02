"""
This function takes an array of characters and a string to generate from the characters.
The function returns a boolean value, True
if the string can be created from the characters or False if not.
We traverse the array containing the characters available and store the count in a dictionary.
We then traverse the string that we want to create and if we find a character that is missing
from the dictionary of available characters we return false. Otherwise, we reduce the count of
the characters used from the dictionary until we run out of characters required. If we get to
the end of the characters in the string we are building successfully, we return true.

Complexity: O(n+m) T O(n) S for storage as we traverse both the string and characters available
to the end and store the characters available in a dict which in worst case would be unique
characters hence a maximum of x.
"""


def generate(characters, string):
    characters_available = {}
    def new_char_count(key): return characters_available.get(key, 0) + 1

    for char in characters:
        characters_available.update({char: new_char_count(char)})

    for char in string:
        if characters_available.get(char) is None or characters_available.get(char) <= 0:
            return False
        else:
            characters_available.update({char: characters_available.get(char) - 1})
    return True
