"""
Implement pow(x, n), which calculates x raised to the power n (i.e., xn).

https://leetcode.com/problems/powx-n/description/

Solution 1: Implement separate power increment operation based on if n > 0 or < 0 (Works for 95% of cases)
Solution 2: Use fast exponentiation formula (If exponent is even, previous result can be used here. For odd
exponent, convert to even by adding + 1 to exponent)

https://en.wikipedia.org/wiki/Exponentiation_by_squaring
"""

# Solution 1

class Solution:
    def myPow(self, x: float, n: int) -> float:
        current_number = 1
        base_counter = 1

        if n > 0:
            while base_counter <= n:
                current_number *= x
                base_counter += 1
            return current_number
        else:
            base_counter = -1
            while base_counter >= n:
                current_number *= x
                base_counter -= 1
            return 1 / current_number


# Solution 2: Used the Fast exponentiation formula. Could not figure out the logic myself.


class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            return self.myPow(1/x, -n)
        elif n == 0:
            return 1
        elif n % 2 == 0:
            return self.myPow(x * x, n / 2)
        elif n %2 !=0:
            return x * self.myPow(x * x, (n - 1) / 2)