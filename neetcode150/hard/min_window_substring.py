"""

"""


'''class Solution:
    def minWindow(self, s: str, t: str) -> str:
        temp_hash = {}
        t_hash = {}
        current_min_length = 999999
        current_subsequence_string = ""

        for item in t:
            t_hash[item] = t_hash.get(item, 0) + 1

        if len(s) == 1 and len(t) == 1:
            if s in t:
                return s
            else:
                return ""

        first_pointer = 0
        second_pointer = first_pointer + 1

        # Length check as below this length, it is not possible for the sequence to exist

        while first_pointer < len(s) - 1:
            # Case when hash items are not the same but we have finished searching the entire string. Then, we need to reset the pointer
            # print(first_pointer, second_pointer)
            first_char = s[first_pointer]
            second_char = s[second_pointer]

            if not temp_hash:
                temp_hash[first_char] = 1

            if second_char in temp_hash:
                temp_hash[second_char] += 1
            else:
                temp_hash[second_char] = 1

            # Check if t_hash is a subset of temp_hash. This means that the characters
            # and the number of times they are present is the same

            if t_hash.items() <= temp_hash.items():
                # sum values from temp_hash and compare with current min length
                current_min = sum(temp_hash.values())
                if current_min < current_min_length:
                    current_min_length = current_min
                    # End index is not included
                    current_subsequence_string = s[first_pointer:second_pointer+1] if second_char in t_hash else s[first_pointer:second_pointer]
                temp_hash = {}
                # Increment the first pointer so that we can start the search from the next character onwards. (Will not be used)
                #first_pointer = second_pointer + 1
                first_pointer += 1
                second_pointer = first_pointer + 1
                continue
            second_pointer += 1
            if second_pointer == len(s):
                first_pointer += 1
                second_pointer = first_pointer + 1
                temp_hash = {}
        return current_subsequence_string
'''


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        """The task is to find a substring in which every character in t is present in the subsequence of length t.
        The max size of the subsequence can be the entire string of len s. So the subsequence can be of length t till
        len s. This is the space in which our code will run. We will initially initialize the pointers to 0 and len(t)-1
        . Then, we will measure the length and go in our while loop and increment this till the length of the sequence
        satisfies the above condition. Once it does, we know that we have checked all possible combinations. In this time,
        we will keep on incrementing the starting and ending indexes till we complete one pass of the loop. We will
        check if the current hash of characters satisfies the condition. If it does, count the sum of values in the
        hash and compare it with the minimum obtained so far. Another approach to minimize the sum operation is to check
        the character that is going outside the current window and -1 it's quantity from the current hash and increment
        the total by +1 (This can be done later)
        """
        # Case where t is smaller. This means that sequence finding is impossible
        if len(t) > len(s):
            return ""

        extra_character = 0
        starting_pointer = 0
        second_pointer = starting_pointer+len(t) + extra_character
        second_hash = {}
        current_min = 9999999999999999
        for item in t:
            second_hash[item] = second_hash.get(item, 0) + 1
        initial_sequence = s[starting_pointer:second_pointer]
        best_so_far = ""
        # Potential case when len of both is same but output is not coming. In this case, need to add a condition
        # to check finally and exit if the condition is not matching. Else infinite loop
        while len(initial_sequence) <= len(s):
            temp_hash = {}

            for char in initial_sequence:
                temp_hash[char] = temp_hash.get(char, 0) + 1

            # This condition does not work. Only way is to do nested looping
            if second_hash.items() <= temp_hash.items():
                current_key_sum = sum(temp_hash.values())

                if current_key_sum < current_min:
                    current_min = current_key_sum
                    best_so_far = initial_sequence

            starting_pointer += 1
            second_pointer = starting_pointer + len(t) + extra_character
            # We have reached the end of examining all windows ith given size. Time to extend the window size
            if starting_pointer > len(s) - 1:
                extra_character += 1
                starting_pointer = 0
                second_pointer = starting_pointer + len(t) + extra_character

            initial_sequence = s[starting_pointer:second_pointer]

            # Condition to check if absolute min has been achieved. Could be a case when it's minimum but not the best
            # not sure (Adding 1000 to length is a hack. Does not work)
            if (len(initial_sequence) == len(s) and best_so_far and len(best_so_far) <= len(initial_sequence)) or starting_pointer > len(s):
                break

        return best_so_far

temp_sol = Solution()
#s = "ADOBECODEBANC"
#t = "ABC"
#s = "a"
#t = "a"
#s = "a"
#t = "aa"
#s = "ab"
#t = "b"
#s = "aa"
#t = "aa"
#s = "abc"
#t = "ac"
#s = "a"
#t = "b"
s = "aaaaaaaaaaaabbbbbcdd"
t = "abcdd"

temp_op = temp_sol.minWindow(s, t)
print(temp_op)