"""
Requirement: A palindrome is a string that is written the same way backward and forward.
Given a string, this function will return the longest palindromic substring in the string.
This may well be a single character in the string.
Implementation: We iterate through the array and at each character, check if that character
together with the characters to the left and right form a palindrome. We also check if there’s
a palindrome forming from between the current character and the previous one.
Complexity:O(n2) T  and O(n) S as we iterate through the array and at each character we check
either direction of the character to determine if it is a palindrome. We do this a second time
to determine if there’s a palindrome forming between the character and the previous character.
So there’s potentially two checks to n. We then could potentially hold the whole string length
if the string is one whole palindrome.
"""


def get_longest_palindrome(string, start, end):
    while start >= 0 and end < len(string):
        if string[start] != string[end]:
            break
        start -= 1
        end += 1
    return start + 1, end


def longest_palindromic_substring(string):
    index_current_longest = (0, 1)
    def length(indices): return abs(indices[1] - indices[0])
    for i in range(1, len(string)):
        odd = get_longest_palindrome(string, i - 1, i + 1)
        even = get_longest_palindrome(string, i-1, i)
        new_palindrome_length = odd if length(odd) > length(even) else even
        if length(new_palindrome_length) > length(index_current_longest):
            index_current_longest = new_palindrome_length
    return string[index_current_longest[0]:index_current_longest[1]]
