"""
Sliding Window Maximum

https://leetcode.com/problems/sliding-window-maximum/description/

You are given an array of integers nums, there is a sliding window of size k which is moving from the very left of the
array to the very right. You can only see the k numbers in the window.
Each time the sliding window moves right by one position. Return the max sliding window.

Current Approach:

Calculate the Initial Maximum number and it's index.

If we have the maximum number, check if the starting index is greater than the index of the maximum number. This is done so that we know when the current max number goes out the window and we need to re-calculate the maximum for the new window.

If not, check if the new number (referenced by start_index + k -1) is bigger than the current maximum. If so, update the relavant details.

If both cases are not applicable, it means we need to add the earlier max number to the list which is to be returned for the output.
"""
from typing import List


class Solution:

    def loop_mamx_calculate(self, start_index, end_index, nums):
        single_loop_max = nums[start_index]
        temp_max_index = start_index
        for item in range(start_index, end_index):
            if nums[item] > single_loop_max:
                single_loop_max = nums[item]
                temp_max_index = item
        return single_loop_max, temp_max_index

    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        start_index = 0
        end_index = start_index + k
        temp_list = []
        single_loop_max, temp_max_index = self.loop_mamx_calculate(start_index, end_index, nums)

        while start_index <= len(nums) - k:
            if single_loop_max:
                if start_index >= temp_max_index:
                    new_max, new_index = self.loop_mamx_calculate(start_index, end_index, nums)
                    single_loop_max = new_max
                    temp_max_index = new_index
                    temp_list.append(single_loop_max)
                else:
                    if nums[end_index-1] > single_loop_max:
                        new_max = nums[end_index-1]
                        single_loop_max = new_max
                        temp_max_index = end_index
                        temp_list.append(single_loop_max)
                    else:
                        temp_list.append(single_loop_max)
            start_index += 1
            end_index += 1

        return temp_list

temp_class = Solution()
#temp_list = [1, 3, -1, -3, 5, 3, 6, 7]
#temp_k = 3
#temp_list = [1]
#temp_k = 1
#temp_list = [1,3,-1,-3]
#temp_k = 1
#temp_list = [1,3,-1,-3, 2, 5, 10]
#temp_k = 2
temp_list = [-6,-10,-7,-1,-9,9,-8,-4,10,-5,2,9,0,-7,7,4,-2,-10,8,7]
temp_k = 7
new_op = temp_class.maxSlidingWindow(temp_list, temp_k)
print(new_op)



'''while start_index <= len(nums) - k:
            print(start_index, start_index + k, temp_list)
            if temp_max:
                new_number_to_check = nums[(start_index + k) - 1]
                if new_number_to_check > temp_max:
                    temp_max = new_number_to_check
                temp_list.append(temp_max)
            else:
                current_slice = nums[start_index:start_index + k]
                single_loop_max = current_slice[0]
                temp_max_index = 0
                for item in range(len(current_slice)):
                    if current_slice[item] > single_loop_max:
                        single_loop_max = current_slice[item]
                        temp_max_index = item
            # max_number = max(current_slice)
            temp_list.append(single_loop_max)
            temp_max = single_loop_max
        start_index += 1'''