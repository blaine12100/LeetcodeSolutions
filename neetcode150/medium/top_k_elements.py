"""
Given an integer array nums and an integer k, return the k most frequent elements.
You may return the answer in any order.

https://leetcode.com/problems/top-k-frequent-elements/description/

Solution 1: # Naive solution: Use a count array or hashmap and create a sorted copy of values in ascending /
descending order. Then, return the top k keys after sorting the hash based on keys.

Solution 2: Using Bucket Sort (count array) with a modification: each index stores the times that count of input
appears and the value is a list of inputs which fall in that category.
"""

from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Naive solution: Use a count array or hashmap and create a sorted copy of values in ascending / descending order. Then, return the top k keys after sorting the hash based on keys.

        '''temp_hash = {}

        for item in nums:
            temp_hash[item] = temp_hash.get(item, 0) + 1

        sorted_value_by_key = sorted(temp_hash.items(), key=lambda x:x[1], reverse=True)

        temp_sorted = [item[0] for item in sorted_value_by_key]
        return temp_sorted[:k]'''

        # Second Solution: Using Bucket Sort (count array) with a modification:
        # each index stores the times that count of input appears and the value is
        # a list of inputs which fall in that category.

        temp_hash = {}

        for item in nums:
            temp_hash[item] = temp_hash.get(item, 0) + 1

        bucket_sort_list = [[] for item in range(len(nums) + 1)]

        for key, value in temp_hash.items():
            bucket_sort_list[value].append(key)
        res = []

        for index in range(len(bucket_sort_list) - 1, 0, -1):
            for item in bucket_sort_list[index]:
                res.append(item)
                if len(res) == k:
                    return res