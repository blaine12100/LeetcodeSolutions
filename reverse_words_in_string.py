def reverse(s):
    # Strip leadning and trailing spaces
    s = s.strip()
    # Convert string to list for reversing
    temp_list = s
    #print(temp_list)

    current_word = ""
    final_word = []

    for item in s:
        if item != " ":
            current_word += item
        else:
            final_word.insert(0, current_word)
            current_word = ""
            continue
    final_word.insert(0, current_word)
    #print(final_word)
    #final_word.remove(" ")
    #print(final_word)
    #return final_word
    return ' '.join(x for x in final_word if x != "")

print(reverse("a good   example"))
print(reverse("  hello world  "))
print(reverse("the sky is blue"))
print(reverse("        a          good               example          "))