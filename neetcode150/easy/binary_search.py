"""
Implement the binary search algorithm

https://en.wikipedia.org/wiki/Binary_search_algorithm
"""

from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Binary search algorithm
        # Find middle element in arr: Based on length of arr.
        # If target is less than middle, set right side to middle index and go to earlier step
        # Else go to earlier step with start to middle index to end of list
        left = 0
        right = len(nums) - 1

        while left <= right:
            middle_index = (left + right) // 2

            # If value is the same return
            if nums[middle_index] == target:
                return middle_index
            # If middle is greater than target, value is in the left half
            elif nums[middle_index] > target:
                right = middle_index - 1
            else:
                # Value is in the right half
                left = middle_index + 1
        return -1

