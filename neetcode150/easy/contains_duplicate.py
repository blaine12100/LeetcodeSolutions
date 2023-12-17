'''
Given an integer array nums, return true if any value appears at least twice in the array,
and return false if every element is distinct.

https://leetcode.com/problems/contains-duplicate/description/

Approach 1: Use set addition and search operations
Appraoch 2: Use sorting and comparision with adjacent elements
'''
from typing import List


# Approach 1

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        temp_set = set()

        for item in nums:
            if item in temp_set:
                return True
            else:
                temp_set.add(item)
        return False

# Approach 2 (Native Hashmap)

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        temp_hash = dict()

        for item in nums:
            if item not in temp_hash:
                temp_hash[item] = 1
            else:
                return True
        return False

#Approach 3

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        for index in range(len(nums)):
            if index + 1 <= len(nums)-1:
                if nums[index] == nums[index+1]:
                    return True
        return False