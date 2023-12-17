"""
Check if the given string is a palindrome or not.

Solution 1: Reverse the string and check directly (Use [::-1])
Solution 2: Use 2 pointer approach. Start 1 pointer from the start of the string and the other one from the end. If the
corresponding characters are the same, increment the starting index and decrement the ending index. Continue doing this
till start <= end.
"""

import string

# Solution 2


class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Convert uppercase to lowercase
        s = s.lower()
        # Remove punctuation
        test_str = s.translate(str.maketrans('', '', string.punctuation))
        # Remove spaces
        test_str = ''.join(x for x in test_str.split() if x != " ")

        # Edge case for empty or single length string.
        if len(test_str) == 0 or len(test_str) == 1:
            return True

        starting_index = 0
        end_index = len(test_str) - 1

        while starting_index <= end_index:
            if test_str[starting_index] == test_str[end_index]:
                starting_index += 1
                end_index -= 1
            else:
                return False
        return True
