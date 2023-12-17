'''
Combined approach for finding divisors of a number for a given number. Used square root method but getting TLE for
it. https://practice.geeksforgeeks.org/batch/ds-with-python/track/mathematics-basics-python/problem/exactly-3-divisorss
'''

# {
# Driver Code Starts
# Initial Template for Python 3


import math


# } Driver Code Ends
# User function Template for python3

class Solution:
    def exactly3Divisors(self, N):
        exactly_3_divisors = 0
        for item in range(2, N):
            divisor_count = 0
            for other in range(1, (int)(math.sqrt(item)) + 1):
                if item % other == 0:
                    if item / other == other:
                        divisor_count = divisor_count + 1
                    else:  # Otherwise count both
                        divisor_count = divisor_count + 2
            if divisor_count == 3:
                exactly_3_divisors += 1
        return exactly_3_divisors


# {
# Driver Code Starts.
def main():
    T = int(input())

    while (T > 0):
        N = int(input())
        ob = Solution()
        print(ob.exactly3Divisors(N))

        T -= 1


if __name__ == "__main__":
    main()
# } Driver Code Ends