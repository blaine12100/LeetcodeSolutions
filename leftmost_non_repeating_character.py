"""
I thought that hashmap solution for leftmost repeating might not work here. Thought efficient solution
will use 1 traversal only. This question can also be implemented by a hashmap as well. Much more intuitive and
does not use this "TRICK"
"""


def leftmost_non_repeating(s1):
    temp_count_arr = [0] * 256
    for item in s1:
        temp_count_arr[ord(item)] += 1

    # Check if first character with count of 1 is formed.
    for index in range(len(s1)):
        if temp_count_arr[ord(s1[index])] == 1:
            return index
    return -1


# op = leftmost_non_repeating("abbcc")
op = leftmost_non_repeating("geeksforgeeks")
# op = leftmost_non_repeating("abcd")
print(op)
