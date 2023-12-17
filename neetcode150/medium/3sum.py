"""
3sum

Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k,
and nums[i] + nums[j] + nums[k] == 0. Notice that the solution set must not contain duplicate triplets.

Brute Force: Use 3 loops and consider all possible combinations. This makes the solution O(N^3)

Solution 2: Use the property that a number subtracted from the target should exist in the array. Only then can a solution
be found. To do this, I had sorted the array and tried to find the answer. After this, the problem
becomes like the 2 sum problem(input is sorted. Which I was able to solve). Use the 2 pointer approach. Initialise the
first pointer to the starting index. The second index is at the end of the list. If the target is greater than the sum
of both, it means that the last index number is larger. Similarly, if the number is less than the target, it means
that the initial number is smaller. If the sum of both is equal, we have found the 2 numbers. Since 2 loops are involved
+ sorting, the solution is O(N^2)
"""
from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        temp_set = []
        nums.sort()

        for index, item in enumerate(nums):
            # If same items are found, skip as we would have already considered an iteration of this item beforehand
            if index > 0 and item == nums[index-1]:
                continue
            # 2 pointer approach (Similar to 2 sum: input is sorted)
            left, right = index + 1, len(nums) - 1
            while left < right:
                final_sum = item + nums[left] + nums[right]
                if final_sum > 0:
                    # Right is too big, decrement
                    right -= 1
                elif final_sum < 0:
                    # Left is too small, increment
                    left += 1
                else:
                    temp_set.append([nums[left], nums[right], item])
                    left += 1
                    # Condition to skip left pointer across all duplicates. With a fixed number, only 1 solution
                    # will exist
                    while nums[left] == nums[left-1] and left < right:
                        left += 1
        return temp_set
