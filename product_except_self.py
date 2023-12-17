from typing import List
from functools import reduce
from itertools import combinations


'''def temp_function(a, b):
    return a * b


def productExceptSelf(nums: List[int]) -> List[int]:
    temp_set = []
    for index, item in enumerate(nums):
        new_array = [x for x in nums if x != item]
        if new_array:
            temp_set.append(reduce(temp_function, new_array))
    # Set subtraction operation
    #temp_set = temp_set - set(nums)
    return temp_set


temp_ip = [1, 2, 3, 4]
#temp_ip = [-1,1,0,-3,3]
temp_ip = [1, 2, 3]
temp_ip = [0,0]
print(productExceptSelf(temp_ip))
'''

temp_set = []
for index, item in enumerate(nums):
    new_array = []
    #new_array = [x for x in nums if x != nums[index]]
    for other in range(0, len(nums)):
        if other != index:
            new_array.append(nums[other])
    if new_array:
        temp_set.append(reduce(temp_function, new_array))
# For same input case
#if all(item == nums[0] for index, item in enumerate(nums)):
#    return nums
return temp_set