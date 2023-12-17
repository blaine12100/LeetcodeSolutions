"""
Given a list of numbers and targets, find 2 numbers which add upto target. One more condition this question has
is the index cannot be changed (I figured this out after trying sorting methods)

Approach 1: Do 2 for loops and do repeated addition with current numbers and consider all numbers other than the
current number

Solution 2: Use the property that a number subtracted from the target should exist in the array. Only then can a solution
be found. To do this, I had sorted the array and tried to find the answer. After this, use the 2 pointer
approach. Initialise the first pointer to the starting index. The second index is at the end of the list. If the target
is greater than the sum of both, it means that the last index number is larger. Similarly, if the number is less than
the target, it means that the initial number is smaller. If the sum of both is equal, we have found the 2 numbers.
"""

from typing import List

# Solution 1

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for index, item in enumerate(nums):
            for other in range(index + 1, len(nums)):
                if item + nums[other] == target:
                    return [index, other]


# Solution 2

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        temp_hash = {}

        for index, item in enumerate(nums):
            if item not in temp_hash:
                temp_hash[item] = [index]
            else:
                temp_hash[item].append(index)

        for index, item in enumerate(nums):
            temp = target - item
            if temp == item:
                if len(temp_hash[item]) > 1:
                    return temp_hash[item]
                else:
                    continue
            else:
                if temp in temp_hash:
                    return [temp_hash[item][0], temp_hash[temp][0]]
                else:
                    continue

# Solution 3 (Only add elements to hashmap if number - target is in hashmap

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        temp_hash = {}

        for index, item in enumerate(nums):
            if target - item in temp_hash:
                return [temp_hash[target - item], index]
            else:
                temp_hash[item] = index