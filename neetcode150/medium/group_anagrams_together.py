"""
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase,
typically using all the original letters exactly once.

https://leetcode.com/problems/group-anagrams/description/

Solution 1: Use the sorting trick from comparing anagrams question. Once the strings are sorted, create the respective
 original, sorted version tuple and iterate through them and check if the sorted string is in the hash. If no, create
 the key with the sorted string and the unsorted version as the value. Once this is done, return the values from
 the dictionary.
"""

from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        # For the first condition
        if len(strs) == 1:
            return [strs[0]] if strs[0] != "" else [[""]]
        else:
            # Create the key value pair for original string and it's sorted version. Helpful in the second stage of
            # the problem.
            new_str = [(x, ''.join(sorted(x))) for x in strs]
            temp_hash = {}
            print(new_str)

            # Hash comparison to check if the sorted key is in hash. If yes, add the unsorted string to it's values
            for item in new_str:
                if item[1] in temp_hash:
                    temp_hash[item[1]].append(item[0])
                else:
                    temp_hash[item[1]] = [item[0]]

            return temp_hash.values()