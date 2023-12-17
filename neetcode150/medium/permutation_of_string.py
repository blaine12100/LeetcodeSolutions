"""
Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.
In other words, return true if one of s1's permutations is the substring of s2.

While trying to solve this, I was using the index (2 pointer) approach here but ran into issues while trying to
https://leetcode.com/problems/permutation-in-string/description/
https://github.com/neetcode-gh/leetcode/blob/main/python%2F0567-permutation-in-string.py

Able to think a bit but my solution was quite far off from the actual one.
"""

# Solution 1: Using sliding windows (Too complicated to use as it is)


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        first_index_s1 = 0
        first_index_s2 = 0

        while True:

            if s1[first_index_s1] == s2[first_index_s2]:
                second_index_s1 = first_index_s1 + 1
                second_index_s2 = first_index_s2 + 1

                while True:
                    if second_index_s1 <= len(s1) - 1 and second_index_s2 <= len(s2) - 1:
                        if s1[second_index_s1] == s2[second_index_s2]:
                            second_index_s1 += 1
                            second_index_s2 += 1
                        else:
                            # No point in checking further
                            second_index_s1 += 1
                            break

                        if second_index_s1 >= len(s1):
                            # Subsequence has been found
                            return True
                    else:
                        # Since we are the last character of the first string and no subsequence has been found yet,
                        # It will never be found so we break the loop here
                        if second_index_s1 >= len(s1) - 1:
                            return False
            else:
                first_index_s2 += 1

            # Subsequence does not exist
            if first_index_s1 >= len(s1) - 1 and first_index_s2 >= len(s2) - 1:
                return False

            if first_index_s2 == len(s2) - 1:
                # Nth character does not exist in s2 and we have checked the entire string. Then we need to reset
                # first_index_s2 and increment s1
                first_index_s2 = 0
                first_index_s1 += 1


# Actual Solution: Using hashmaps and sliding window approach (A bit confusing).

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # If the length of s1 is greater than s2, it will have more characters and that makes it impossible
        # for the substring to exist
        if len(s1) > len(s2):
            return False

        s1Count, s2Count = [0] * 26, [0] * 26
        # Hashmap (count array) to count the character count for a particular value. The index refers to
        # the count of a character based on the english alphabet
        for i in range(len(s1)):
            s1Count[ord(s1[i]) - ord("a")] += 1
            s2Count[ord(s2[i]) - ord("a")] += 1

        matches = 0
        # 26 is used here as the problem specifies that
        for i in range(26):
            matches += 1 if s1Count[i] == s2Count[i] else 0

        l = 0

        for r in range(len(s1), len(s2)):
            # If all characters match (Existing or otherwise), the permutation exists
            if matches == 26:
                return True
            # Current value which we are checking
            index = ord(s2[r]) - ord("a")
            s2Count[index] += 1
            # If both characters match, increment the numbers of matched characters
            if s1Count[index] == s2Count[index]:
                matches += 1
            # In this, after incrementing the counter, if it becomes equal to s2 count, that means before
            # incrementing the sequences were already matched hence we need to decrement by 1 as well.
            elif s1Count[index] + 1 == s2Count[index]:
                matches -= 1
            # Same logic as above. We are using L to traverse the second count index map
            index = ord(s2[l]) - ord("a")
            s2Count[index] -= 1
            if s1Count[index] == s2Count[index]:
                matches += 1
            elif s1Count[index] - 1 == s2Count[index]:
                matches -= 1
            l += 1
        return matches == 26

temp_sol = Solution()
first_string = 'ab'
second_string = "eidooobasdlsadlsakdlskdlsabklbajdsajsad"

true_false = temp_sol.checkInclusion(first_string, second_string)
print(true_false)