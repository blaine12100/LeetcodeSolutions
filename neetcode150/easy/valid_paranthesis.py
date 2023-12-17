'''
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.

Solution 1:

Use array as stack (Insert and delete from the top). Insert only the opening halves of the brackets. When closing
half is received, check if last element in the arr (top) is the same type. If yes, remove and increment the number
of operations performed + 1. At the end, check if 2 * the number of operations performed is equal to the len of the
string. This works as we are only counting the remove operations so the product should be equivalent to the len of the
string.
'''


class Solution:
    def isValid(self, s: str) -> bool:

        temp_arr = []
        number_of_operations = 0

        # Special case for  input length equal to 1
        if len(s) == 1:
            return False

        for item in s:
            if item in '{[(':
                temp_arr.append(item)
            else:
                # Check if last element currently inserted matches the corresponding closing bracket
                if temp_arr:
                    if temp_arr[-1] == '(' and item == ')':
                        number_of_operations += 1
                        del temp_arr[-1]
                    elif temp_arr[-1] == '{' and item == '}':
                        number_of_operations += 1
                        del temp_arr[-1]
                    elif temp_arr[-1] == '[' and item == ']':
                        number_of_operations += 1
                        del temp_arr[-1]
        # String re-construction (Since the number of operations are counted based on removing elements from the stack. If we multiply this with 2, it should equal the length of characters of the original input)
        if number_of_operations * 2 == len(s):
            return True
        else:
            return False