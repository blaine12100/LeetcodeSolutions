"""
The problem is centered around finding the longest common subsequence in between 2 pairs of strings.

The base solution can be done in the following way.

1) Loop on the second string. IN each iteration take a ith slice of the string. In the second string,slice for
the entire string into i sized parts to check if they all have the same sequence. If yes, the solution is solved.
However, since the problem is about the longest common subsequence, we need to find all subsequences and then choose the
largest one. If no subsequences are common, return the blank string
"""


def gcdOfStrings(str1: str, str2: str) -> str:
    final_string = ""
    max_length = 0
    current_sequence_length = 1

    while current_sequence_length < len(str2)+1:
        initial_sequence = str2[0:current_sequence_length]
        j = current_sequence_length
        max_subsequence_found = True
        for initial in range(0, len(str1), current_sequence_length):
            j = (current_sequence_length + initial)
            if not str1[initial:j] == initial_sequence:
                max_subsequence_found = False
                break
        if max_subsequence_found:
            if j >= max_length:
                max_length = j
                final_string = initial_sequence
        current_sequence_length += 1
    return final_string


print(gcdOfStrings("TAUXXTAUXXTAUXXTAUXXTAUXX", "TAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXX"))
print(gcdOfStrings("ABABABAB", "ABAB"))
print(gcdOfStrings("LEET", "CODE"))
print(gcdOfStrings("ABABAB", "ABAB"))
print(gcdOfStrings("ABCABC", "ABC"))