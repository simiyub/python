"""
This function takes a non-empty string and returns true if the string is a palindrome
or false if it isn’t

"""


def is_palindrome(string):
    start = 0
    end = len(string) - 1

    while start <= end:
        if string[start] != string[end]:
            return False
        start += 1
        end -= 1
    return True
