"""
In this question, we need to check if 1 string is a rotation of the other string. To solve this, we can
either use the KMP algorithm, or the naive approach of rotating 1 string N times clockwise / counterclockwise and
checking. The latter method I had earlier disqualified as N can be arbitrarily large and slow. The efficient solution
is to append the first string to itself and then checking for sub pattern (since it's a rotation, it should be present)
"""


def check_rotation(s1, s2):
    # Obvious check
    if len(s1) != len(s2):
        return -1

    temp = s1 + s1

    # Check if second string is present in the appended string
    return temp.find(s2) != -1
