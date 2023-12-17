def leftmost_repeating(s1):

    temp_hashmap = {}
    leftmost_occurence = 999999999999999999999999999999999999999

    for index, item in enumerate(s1):
        if item not in temp_hashmap:
            # Assign it to temp hashmap
            temp_hashmap[item] = index
        else:
            # Check if existing index is less than leftmost. If yes, assign it
            if temp_hashmap[item] < leftmost_occurence:
                leftmost_occurence = temp_hashmap[item]

    if leftmost_occurence == 999999999999999999999999999999999999999:
        return -1
    else:
        return leftmost_occurence

#op = leftmost_repeating("abbcc")
#op = leftmost_repeating("geeksforgeeks")
op = leftmost_repeating("abcd")
print(op)