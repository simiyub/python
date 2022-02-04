"""
Requirement: This function takes two strings and determines the minimum number of edit
operations required in the first string to match the second string. An edit can be
inserting a character, substituting or deleting.
Implementation:
If orig[row-1] == edit[col-1] then edit[row][col] = edit[row-1][col-1]
Else edit[row][col] = 1 + min(edit[row][col-1], edit[r-1][col], edit[row-1][col-1]
Complexity:
O(nm) T as we walk through the source string and the edit string to determine
the count of edits.
O(min(m,n) as We build an array of the edit array as we walk through the array
"""


def minimum_edits_to_match(string1, string2):
    small = string1 if len(string1) < len(string2) else string2
    big = string1 if len(string1) >= len(string2) else string2

    even_dits = [_ for _ in range(len(small) + 1)]
    odd_edits = [None for _ in range(len(small) + 1)]

    for i in range(1, len(big) + 1):
        if i % 2 == 1:
            current = odd_edits
            previous = even_dits
        else:
            current = even_dits
            previous = odd_edits
        current[0] = i
        for j in range(1, len(small) + 1):
            if big[i - 1] == small[j - 1]:
                current[j] = previous[j-1]
            else:
                current[j] = 1 + min(previous[j-1], previous[j], current[j-1])

    return even_dits[-1] if len(big) % 2 == 0 else odd_edits[-1]
