'''
In this, we are supposed to find the trailing zeroes in a number. The logic for this follows from the problem
of counting digits. We need to keep a count of digits where the previous number and current number are both zero.
If they are, then we can increment the count of zeroes till we encounter a number which breaks this rule.
Additional cases are required here when we have to take care of cases during incrementing the count of zero since
we are comparing both previous and current numbers i they are zero, +1 needs to be done at the end to account for
this. Also, consider the case when the last number is zero but the one previous is not. In this case, the main loop
will break but the count needs to be incremented by 1 before returning.
'''


def count_trailing_zero(number):

    count_zero = 0
    previous_number = None
    current_number = None

    while(number > 0):
        previous_number = current_number
        current_number = number % 10
        if current_number != 0:
            break
        if previous_number == current_number and previous_number == 0 and current_number == 0:
            count_zero += 1
        number = number // 10

    if count_zero:
        # Case when both ending numbers are zero but due to our check of both numbers, we increment only once. Hence
        # we have added the extra increment here.
        count_zero += 1
        return count_zero
    else:
        # Single case when next number is not a zero but last number was a zero. Only found in first trailing zero case
        if previous_number == 0:
            count_zero += 1
            return count_zero
        return 0


sample_input = 36288000000000000
print(count_trailing_zero(sample_input))