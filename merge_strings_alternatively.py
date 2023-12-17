def temp(word1, word2):
    new_str = []
    for index in range(len(word1)):
        new_str.append(word1[index])
        if not index > len(word2)-1:
            new_str.append(word2[index])

    # Handled extra case when either input is not present
    if word1:
        if len(word1) > len(word2):
            new_str.append(word1[index+1:])
        else:
            new_str.append(word2[index+1:])
    else:
        return word2
    return ''.join(x for x in new_str)

print(temp('abcd', 'pq'))
print(temp('ab', 'pqrs'))
print(temp('abc', 'pqr'))
print(temp('abc', ''))
print(temp('', 'abc'))