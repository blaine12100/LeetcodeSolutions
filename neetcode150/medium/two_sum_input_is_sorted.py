"""
Given a list of numbers and targets, find 2 numbers which add upto target. One more condition this question has
is the index cannot be changed. In this case, the input list is sorted in ascending order

Approach 1: Do 2 for loops and do repeated addition with current numbers and consider all numbers other than the
current number

Solution 2: Use the property that a number subtracted from the target should exist in the array. Only then can a solution
be found. Since the input is sorted, use the 2 pointer approach. Initialise the first pointer to the starting index. The
second index is at the end of the list. If the target is greater than the sum of both, it means that the last index
number is larger. Similarly, if the number is less than the target, it means that the initial number is smaller. If the
sum of both is equal, we have found the 2 numbers.
"""
from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        solution_index_1, solution_index_2 = 0, len(numbers) - 1

        while solution_index_1 < solution_index_2:
            if numbers[solution_index_1] + numbers[solution_index_2] > target:
                solution_index_2 -= 1
            elif numbers[solution_index_1] + numbers[solution_index_2] < target:
                solution_index_1 += 1
            elif numbers[solution_index_1] + numbers[solution_index_2] == target:
                return [solution_index_1 + 1, solution_index_2 + 1]