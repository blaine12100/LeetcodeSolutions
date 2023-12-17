def one_to_n(n, counter):
    if counter > n:
        return
    else:
        print(counter)
        one_to_n(n, counter + 1)

def one_to_n_base(n):
    if n == 0:
        return
    one_to_n_base(n-1)
    print(n)

################################################################################################################

def sum_digits_recursion(n):
    if n <= 0:
        return 0
    #print(n % 10)
    return n % 10 + sum_digits_recursion(n//10)

#################################################################################################################
def facto(j):
    if j<=0 or j==1:
        return 1
    return j*(facto(j-1))

def nCr(n,r):
    return facto(n) // (facto(n-r) * facto(r))
##############################################################################################################


def string_palindrome_recursion(temp_str, i=0):
    if len(temp_str) == 1 or len(temp_str) == 0:
        return True
    if temp_str[0] == temp_str[-1]:
        i += 1
        return string_palindrome_recursion(temp_str[i:len(temp_str)-i])
    else:
        return False

################################################################################################################

# Based on printing 1-n in loop. Same dynamic but n needs to be decremented by 1 as well because n is the
# length of the array


def printArrayRecursively(self, arr, n):
    # code here
    if n == 0:
        return
    self.printArrayRecursively(arr, n - 1)
    print(arr[n - 1], end=" ")

#one_to_n(4, 1)
#one_to_n_base(4)
#op = sum_digits_recursion(9)
#print(op)
#temp_op = string_palindrome_recursion('racecar')
#print(temp_op)


def sumExists(arr, N, sum):
    # Your code here
    temp_dict = {}
    for item in arr:
        if item not in temp_dict:
            temp_dict[item] = 1
        else:
            temp_dict[item] += 1

    for key, value in temp_dict.items():
        temp_diff = sum - key
        if temp_diff > 0 and temp_diff != key and temp_diff in temp_dict:
            return 1
    return 0

'''N = 7
arr = [61, 14, 75, 71, 36, 34, 12]
sum=68
sumExists(arr, N, sum)'''


def firstRepeated(arr, n):
    # arr : given array
    # n : size of the array

    temp_hash = {}
    min_arr = []

    # Alternate approach, if index is already found, check if new index is lesser than earlier index and store
    # that. No need to store the values as a list then.

    for index, item in enumerate(arr):
        if item in temp_hash:
            temp_hash[item].append(index+1)
        else:
            temp_hash[item] = [index+1]

    if all(len(value) == 1 for key, value in temp_hash.items()):
        return -1

    for key, value in temp_hash.items():
        if len(value) > 1:
            min_arr.extend(value)
    return min(min_arr)

#arr = [61, 14, 75, 71, 36, 34, 12]
#arr = [1, 5, 3, 4, 3, 5, 6]
#firstRepeated(arr, len(arr))


############################################################################################################

# Function to check if 2 strings are anagrams of each other. Naive solution is to do comparisions for each
# character in second string and the index at which it appears. If there are 2 characters in first but only 1 in the
# second, you know then it's not' an anagram. The efficient solution used a count array (Common in string questions.
# Read up once)
# https://practice.geeksforgeeks.org/batch/ds-with-python/track/string-basic-python/video/MjA4Nw%3D%3D

def check_anagram(s1, s2):

    temp_hash_1, temp_hash_2 = {}, {}

    for item in s1:
        temp_hash_1[item] = temp_hash_1.get(item, 0) + 1

    for other in s2:
        temp_hash_2[other] = temp_hash_2.get(other, 0) + 1

    return temp_hash_1 == temp_hash_2

print(check_anagram("listen", "silent"))
print(check_anagram("aacb", "acab"))
print(check_anagram("axb", "aby"))

###############################################################################################################

# Ghyston Interview Question

def balance_point(input):
    # Your code goes here

    balance_point_found = False
    balance_index = None

    for index in range(0, len(input)):
        # Task is to find balance point. One way to do this is to consider each index and compute the sum of preceeding array and next array.
        if sum(input[:index]) == sum(input[index+1:]):
            balance_point_found = True
            balance_index = index
            break
    if balance_point_found:
        return balance_index
    else:
        return -1

op = balance_point([ 2, 7, 4, 5, -3, 8, 9, -1 ])
print(op)

########################################################3

# Ghyston Interview Question

import string

def caesar_cipher(input, key):
    # Your code goes here

    new_string = ""

    for item in input:
        if item not in string.punctuation and item != " ":
            #shifted_input = chr(((ord(item) - key) % 26) + ord('a'))
            amount_to_shift = 65 if item.isupper() else 97
            shifted_input = chr((ord(item) - amount_to_shift + key) % 26 + amount_to_shift)
            new_string += shifted_input
        else:
            new_string += item
    return new_string

print(caesar_cipher("Zwddg ogjdv!", 8))

############################################

