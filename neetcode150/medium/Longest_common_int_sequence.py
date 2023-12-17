"""
Longest Consecutive Sequence

Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.
You must write an algorithm that runs in O(n) time. Definitely a Hard question

Approach with Sorting using Radix sort (Works in O(N) time for large inputs. Does not work for our case as
it does not work with negative numbers

# Solution 3: Use set and find operation to solve this problem. For this approach, we focus on the problem
# of finding the starting index of a sequence. If that number exists, it cannot be the start. Once we find
# the number for which the previous number (item-1) does not exist, we then use a while loop to keep on
# incrementing from this number till we keep on finding the next big number. If we do, keep on incrementing
# the length of the numbers.
"""

from typing import List

# Approach with Sorting using Radix sort
"""class Solution:
    # Using counting sort to sort the elements in the basis of significant places
    def countingSort(self, array, place):
        size = len(array)
        output = [0] * size
        count = [0] * 10

        # Calculate count of elements
        for i in range(0, size):
            index = array[i] // place
            count[index % 10] += 1

        # Calculate cumulative count
        for i in range(1, 10):
            count[i] += count[i - 1]

        # Place the elements in sorted order
        i = size - 1
        while i >= 0:
            index = array[i] // place
            output[count[index % 10] - 1] = array[i]
            count[index % 10] -= 1
            i -= 1

        for i in range(0, size):
            array[i] = output[i]

    # Main function to implement radix sort
    def radixSort(self, array):
        # Get maximum element
        max_element = max(array)

        # Apply counting sort to sort elements based on place value.
        place = 1
        while max_element // place > 0:
            self.countingSort(array, place)
            place *= 10

    def longestConsecutive(self, nums: List[int]) -> int:
        if nums:
            self.radixSort(nums)
            current_max_len = 0
            temp_max = 0
            print(nums)

            if len(nums) == 1:
                return 1

            for item in range(len(nums)):
                if item + 1 < len(nums):
                    print(item, item + 1)
                    # Difference of 1
                    if nums[item + 1] - nums[item] == 1:
                        temp_max += 1
                    elif nums[item + 1] == nums[item]:
                        continue
                    else:
                        # Check if current length is greater than max
                        if temp_max > current_max_len:
                            # Extra incrementing since in initial case only 1 part is counted
                            current_max_len = temp_max + 1
                            temp_max = 0
            # Case where the main loop continues till the end so the code will no go in the else case.
            if temp_max > current_max_len:
                # Extra incrementing since in initial case only 1 part is counted
                current_max_len = temp_max + 1
                temp_max = 0
            elif temp_max == current_max_len:
                return len(set(nums))
            return current_max_len
        else:
            return 0
"""

# Solution 2 with set and normal sorting (Passing for 95% cases. FOr last 5 case not passing. Something is
# wrong with the approach

"""class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if nums:
            current_max_len = 0
            temp_max = 0
            temp_set = set(nums)
            if len(nums) == 1:
                return 1
            set_sorted = sorted(temp_set)
            print(set_sorted)
            for item in range(len(set_sorted)):
                if item + 1 < len(set_sorted):
                    print(item, item + 1, set_sorted[item], set_sorted[item+1])
                    # Difference of 1
                    if set_sorted[item + 1] - set_sorted[item] == 1:
                        temp_max += 1
                    elif set_sorted[item + 1] == set_sorted[item]:
                        continue
                    else:
                        # Check if current length is greater than max
                        if temp_max >= current_max_len:
                            if temp_max == 0 and current_max_len == 0:
                                continue
                            else:
                                # Extra incrementing since in initial case only 1 part is counted
                                current_max_len = temp_max + 1
                        temp_max = 0
            # Case where the main loop continues till the end so the code will no go in the else case.
            if temp_max > current_max_len:
                # Extra incrementing since in initial case only 1 part is counted
                current_max_len = temp_max + 1
            elif temp_max == current_max_len:
                return len(set_sorted)
            return current_max_len
        else:
            return 0

temp_obj = Solution()
final_ans = temp_obj.longestConsecutive([-8,-4,9,9,4,6,1,-4,-1,6,8])
print(final_ans)
"""

# Solution 3 using sets

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        temp_set = set(nums)
        current_max = 0
        for item in temp_set:
            # Check if left neighbour exists
            if (item - 1) not in temp_set:
                temp_max = 0
                while (item + temp_max) in temp_set:
                    temp_max += 1
                current_max = max(temp_max, current_max)
        return current_max
