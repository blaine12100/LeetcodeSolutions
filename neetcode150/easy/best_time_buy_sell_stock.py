"""
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/

Solution 1: Check each number and use 2 for loops to find the next smallest number to see if max profit can be
achieved.

Solution 2: Use strategy of buy low and sell high. Find min price in the entire arr and use that information to
find the max profit

Solution 3: Extension of the 2 pointer approach. I had to find the min price so far and not overall min price (Which
is why my earlier logic failed). Had to watch the solution video to understand this approach.

https://www.youtube.com/watch?v=1pkOgXD63yU
"""

from typing import List


# Solution 1
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        current_max = 0
        for index in range(len(prices)):
            for other in range(index + 1, len(prices)):
                if other <= len(prices) - 1:
                    # Buying > selling
                    if prices[index] > prices[other]:
                        continue
                    else:
                        difference = prices[other] - prices[index]
                        if difference > current_max:
                            current_max = difference
        return current_max

# Solution 2 (Works for 80% of cases. Not there)


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        current_max = 0
        min_price = 99999999999
        min_index = 0
        # find min element and it's index. Max profit can only be achieved from buy low and sell high.
        for index, item in enumerate(prices):
            if item < min_price:
                min_price = item
                min_index = index

        for other in range(min_index, len(prices)):
            curr_difference = prices[other] - min_price
            if curr_difference > current_max:
                current_max = curr_difference
        return current_max

# Solution 3 (Non recursive approach but logic was still there)

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        current_max = 0
        # Two pointer approach (Had to watch the solution video to understand it)
        buying_index = 0
        selling_index = 1

        while (selling_index < len(prices)):
            # Max profit canot be achieved
            if prices[buying_index] > prices[selling_index]:
                buying_index = selling_index
            else:
                difference = prices[selling_index] - prices[buying_index]
                if difference > current_max:
                    current_max = difference
            selling_index += 1
        return current_max
