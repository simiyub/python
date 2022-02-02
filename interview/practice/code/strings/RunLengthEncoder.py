"""
This function takes a non-empty string and returns the run-length encoding of it.
The input string can contain special characters including numbers. As such long runs
are encoded in splits such that the count of any sequence of repeating characters
will be split into parts of a maximum of 9 at a time. So ‘ZZZZZZZZZZZZZZZZ’ will be 9Z6Z
rather than 15Z.
This function will run through the length of the string counting similar characters.
Each time there is a different character from the previous one, we add it to an
array of the encoded characters, prefixed by the count of characters found.
We do this also when we reach 9 for the  character count. We then return the encoded string.
O(n) T and O(n) S as we traverse through the whole string and need space to store the encoded string.

"""
def encode(string):
    encoded_values = []
    count = 1
    def previous(index): return string[index - 1]
    def current(index): return string[index]

    for i in range(1, len(string)):

        if previous(i) != current(i) or count == 9:
            encoded_values.append(str(count) + previous(i))
            count = 0
        count += 1
    encoded_values.append(str(count) + string[len(string)-1])

    return "".join(encoded_values)
