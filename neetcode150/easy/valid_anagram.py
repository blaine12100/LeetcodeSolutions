"""
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the
original letters exactly once.

https://leetcode.com/problems/valid-anagram/

Approach 1: Use count array (Refer to geeksforgeeks for this. If both count array are the same, then it's
an anagram. Else it's not)

Approach 2: Use same concept but with hashmap

Appraoch 3: Use sorting. With sorting, they become the same string (similar concept to duplicate characters question)
"""

# Solution 1

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count_array_1 = [0] * 26
        count_array_2 = [0] * 26

        for character in s:
            char_position = ord(character) - 97
            count_array_1[char_position] += 1

        for other_character in t:
            other_char_position = ord(other_character) - 97
            count_array_2[other_char_position] += 1

        if count_array_1 == count_array_2:
            return True
        return False

# Solution 2

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)