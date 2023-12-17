"""
https://leetcode.com/problems/product-of-array-except-self/description/

Given an array of nums, return an array in which for ith index, the product is returned without the nums at nums[i]
th index.

Solution: Naive (Bruteforce): Use 2 loops. The first loop is to count the index and the second one is used to
create the products of numbers without the first loop index.

The other banned solution is to calculate the product of all numbers in the array and use the division operator
to divide the ith number with the completed product. This will give you the target answer

Actual Solution: In this, calculate the prefix products of the array. Calculate the suffix products of the array.
Combine the 2 to get the answer

For ones, who did not understand how prefix-postfix works, lets change 1, 2, 3, 4 positions to symbols like a, b, c, d, so multiplying will be:
prefix:
->
|       a       |   a*b   | a*b*c | a*b*c*d |
postfix:
<-
| a*b*c*d | b*c*d |   c*d   |      d        |

the result is a multiply without the symbol in own position (the left value from prefix and the right one from postfix):
|    b*c*d  | a*c*d | a*b*d |   a*b*c   |

I got the prefix part right. Didn't know that the suffix would be required and how to integrate the 2 of them
together
"""
from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        """Initial output array"""
        res = [1] * len(nums)
        prefix = 1
        postfix = 1

        # Compute the prefix array. In this, the ith index is assigned the current prefix value and it's updated
        # in the same iteration by using the current index's value
        for index in range(len(nums)):
            res[index] = prefix
            prefix *= nums[index]

        # For the postfix operation, update the existing prefix value by multiplying it with the current value
        # and then storing it so that it can be used further
        for index in range(len(nums) - 1, -1, -1):
            res[index] *= postfix
            postfix *= nums[index]

        return res

