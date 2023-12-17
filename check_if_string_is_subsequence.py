"""
Check if string is a subsequence of the other string. One approach that I can think of is using string indexing.
Basically, if the preceding string index is less than the current one, the given string can be a subsequence
(Ascending order). As if you have string which have a character towards the end in the middle, it cannot be a subsequence

ABCDE
ADC (Not a subsequence as D appears before C)

ABDCDE
ADC (Here it's possible as D appears multiple times)

Actual Solution: Use indexing (points for that. Implementation of the idea was wrong. Pro Tip. DO NOT RUSH to the
solution. Maybe If I had waited a bit, this might have come to me too)
"""


def check_subsequence(s1, s2):

    # To make search easier
    """temp_hashmap = {}
    subsequence_check = True

    # Edge case when s2 is empty
    if s2 == "":
        return subsequence_check

    for index, item in enumerate(s1):
        if item not in temp_hashmap:
            temp_hashmap[item] = index

    for index, item in enumerate(s2):
        if item in temp_hashmap and (temp_hashmap[item] <= index or s2.index(item) == len(s2)-1):
            continue
        else:
            subsequence_check = False
            break
    return subsequence_check"""

    index_s1, index_s2 = 0, 0

    while index_s1 < len(s1) and index_s2 < len(s2):
        # Move both index if element is the same.
        if s1[index_s1] == s2[index_s2]:
            index_s2 += 1
        # Only move the upper string
        index_s1 += 1

    if index_s2 == len(s2):
        # If second string reached last index, that means that all characters were found
        return True
    else:
        return False

print(check_subsequence("ABCD", "AD"))
print(check_subsequence("ABCD", "AED"))
print(check_subsequence("ABDDE", "ADD"))