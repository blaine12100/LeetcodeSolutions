'''
In this, the task is to reverse vowels present in a string. The vowels can either be uppercase or lowercase.
To solve this, we can use the two pointer approach. In this, one pointer is at the start of the array and the
other one is at the end. If the vowel is found at the start, we then decrement the end till we get a vowel. Once
a vowel is found, we swap and this process continues till first is less than last and first and last don't refer
to the same vowel (only 1 vowel in the string)
'''


def reverseVowels(s: str) -> str:
    forward_ptr = 0
    backward_ptr = len(s) - 1
    vowel_string = 'aeiouAEIOU'
    temp_string = list(s)

    while forward_ptr < backward_ptr:
        if temp_string[forward_ptr] in vowel_string:
            # Vowel found, check from end
            if temp_string[backward_ptr] in vowel_string:
                temp_string[forward_ptr], temp_string[backward_ptr] = temp_string[backward_ptr], temp_string[
                    forward_ptr]
                forward_ptr += 1
                backward_ptr -= 1
            else:
                backward_ptr -= 1
        else:
            forward_ptr += 1
    return ''.join(x for x in temp_string)

sample_input = 'leetcode'
sample_input = 'hello'
sample_input = 'hell'
sample_input = 'aeabcdod'
print(reverseVowels(sample_input))