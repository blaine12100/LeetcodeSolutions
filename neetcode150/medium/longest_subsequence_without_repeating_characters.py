"""
Given a string s, find the length of the longest substring without repeating characters. Substring is a continuous
sequence of characters
https://leetcode.com/problems/longest-substring-without-repeating-characters/

Solution: Using a set as the data structure of choice by using the logic of sliding window, we can solve this problem.
The sliding window concept builds on top of the 2 pointer approach. For this problem, we need to consider 2 pointers:
the first pointer set to index 0 and the next one set to first+1. Then, we keep on adding the elements to the set if a
duplicate element is not encountered. After adding the element, increment the second index by 1.
If we get a duplicate element, it means that the sequence length is equal to the current elements in the set.
Now, we need to increment the first index to start the next sequence. This continues till the second index is equal
to the last element in the list.
"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s:
            temp_set = set(s[0])
            first_index = 0
            second_index = first_index + 1
            final_max_length = len(temp_set)

            while second_index <= len(s) - 1:
                if s[second_index] not in temp_set:
                    temp_set.add(s[second_index])
                    second_index += 1
                else:
                    # Comparison with the global max length
                    max_length = len(temp_set)
                    if max_length > final_max_length:
                        final_max_length = max_length
                    first_index += 1
                    second_index = first_index + 1
                    temp_set = set(s[first_index])
            # Second check as we were getting cases where the last element was reached but the max length was not
            # updated
            max_length = len(temp_set)
            if max_length > final_max_length:
                final_max_length = max_length
            return final_max_length
        else:
            return 0

# Solution 2 https://www.youtube.com/watch?v=wiGpQwVHdE0

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        l = 0
        charSet = set()

        # In this case, we are reducing the sliding window from the left till we eliminate all the duplicate
        # characters. I found the logic that I have used to be more intuitive. This logic is more concise tbh. The use
        # of incrementing l is to allow us to explore the unexplored parts of the string (Similar to my 2 pointer appro
        # ach above)

        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
            charSet.add(s[r])
            res = max(res, r-l + 1)
        return res


temp_class = Solution()

#new_str = "dvdf"
#new_str = "abcabcbb"
#new_str = "ahsladjalsjdlasjdquoqwu"
new_str = "anviaj"

op = temp_class.lengthOfLongestSubstring(new_str)
print(op)