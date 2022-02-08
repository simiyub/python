"""
Requirement: Given a string, this function will reverse every word in the string.
Words are a sequence of characters separated by whitespaces - potentially more than one white space.
 The string could also potentially be empty. We will not use python built in reverse or
 other helper methods except the join method.
Implementation: We start off by obtaining the characters in the string and reversing them.
We then iterate through the characters to determine individual words and reverse them back
in the right direction, and then we have the whole string reversed.
Complexity:Requires O(n) T O(n) S We will need to traverse the full length of the array to
find the words to be reversed, and we will need space equivalent to the length of the string
to store the reversed array of words to be returned.
"""


def reverse_list(words):
    start, end = 0, len(words) - 1
    while start < end:
        words[start], words[end] = words[end], words[start]
        start += 1
        end -= 1


def reverse1(string):
    words = []
    start = 0
    for index in range(len(string)):
        char = string[index]
        if char == " ":
            words.append(string[start:index])
            start = index
        elif string[start] == " ":
            words.append(" ")
            start = index
    words.append(string[start:])
    reverse_list(words)
    return "".join(words)


def reverse_array_range(characters, start, end):
    while start < end:
        characters[start], characters[end] = characters[end], characters[start]
        start += 1
        end -= 1


def reverse2(string):
    characters = [char for char in string]
    reverse_array_range(characters, 0, len(characters) - 1)
    start_of_word = 0
    while start_of_word < len(characters):
        end_of_word = start_of_word
        while end_of_word < len(characters) and characters[end_of_word] != " ":
            end_of_word += 1

        reverse_array_range(characters, start_of_word, end_of_word - 1)
        start_of_word = end_of_word + 1
    return "".join(characters)
