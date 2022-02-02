"""
This function will receive a non-empty string of lower case letters and an integer
representing a key and returns a new string created from shifting every character
in the string by positions equivalent to the key provided. Letters will wrap around the alphabet.
Here are two examples, of two strings shifted by a key of 3. One is wrapped and the other not:
“mno” becomes “pqr” - No wrapping.
 “xyz” becomes “abc” - Wrapping.
In this function, we use unicode values to determine the shifted value of each character in the string.
We then wrap if required and return a string made up of the resulting characters joined.
O(n) T as we have to iterate through the string once and a space complexity of O(n)
"""


def encrypt(string, shift_key):
    result_letters = []
    key = shift_key % 26
    def wrapped_value(value): return chr((96 + value) % 122)
    for letter in string:
        new_letter_unicode = ord(letter) + key
        result_letters.append(chr(new_letter_unicode)
                              if new_letter_unicode <= 122
                              else wrapped_value(new_letter_unicode))

    return "".join(result_letters)
