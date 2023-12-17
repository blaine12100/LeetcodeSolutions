# User function Template for python3

class Solution:
    def factorial(self, N):

        temp_op = 1

        while N !=0:

            temp_op = temp_op * N
            N-=1

        return temp_op

    def digitsInFactorial(self, N):
        # code here
        number_of_digits = 0

        factorial_number = self.factorial(N)

        while factorial_number > 0:
            factorial_number = factorial_number // 10
            number_of_digits += 1

        return number_of_digits


# {
# Driver Code Starts
# Initial Template for Python 3

import math


def main():
    T = int(input())

    while (T > 0):
        N = int(input())
        ob = Solution()
        print(ob.digitsInFactorial(N))

        T -= 1


if __name__ == "__main__":
    main()

'''
Used Property of Logarithms (Without this cannot solve it)
https://www.geeksforgeeks.org/count-digits-in-a-factorial-using-logarithm/

if (N < 0):
            return 0
 
        # base case
        if (N <= 1):
            return 1
     
        # else iterate through n and
        # calculate the value
        digits = 0
        for i in range(2, N + 1):
            digits += math.log10(i)
     
        return math.floor(digits) + 1
            
'''