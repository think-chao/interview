#!/usr/bin/env python  
# -*- coding:utf-8 _*-  
""" 
@author:wchao118
@license: Apache Licence 
@file: bestTimeToSellStock.py 
@time: 2019/03/27
@contact: wchao118@gmail.com
@software: PyCharm 
"""

"""
Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete at most two transactions.

Input: [3,3,5,0,0,3,1,4]
Output: 6
Explanation: Buy on day 4 (price = 0) and sell on day 6 (price = 3), profit = 3-0 = 3.
             Then buy on day 7 (price = 1) and sell on day 8 (price = 4), profit = 4-1 = 3.

"""


class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        max_transaction = 2
        dp = [[0] * (len(prices) + 1) for _ in range(max_transaction + 1)]
        for k in range(1, max_transaction + 1):
            for i in range(1, len(prices) + 1):
                min_one_trade = prices[0]
                for j in range(1, i + 1):
                    min_one_trade = min(min_one_trade, prices[j - 1] - dp[k - 1][j - 1])
                dp[k][i] = max(dp[k][i - 1], prices[i - 1] - min_one_trade)
        print(dp)

    def maxProfit_one(self, prices):
        max_transaction = 2
        dp = [[0] * (len(prices) + 1) for _ in range(max_transaction + 1)]
        for k in range(1, max_transaction + 1):
            min_one_trade = prices[0]
            for i in range(1, len(prices) + 1):
                min_one_trade = min(min_one_trade, prices[i - 1] - dp[k - 1][i - 1])
                dp[k][i] = max(dp[k][i - 1], prices[i - 1] - min_one_trade)
        print(dp)


if __name__ == '__main__':
    so = Solution()
    so.maxProfit([3, 3, 5, 0, 0, 3, 1, 4])
    so.maxProfit_one([3, 3, 5, 0, 0, 3, 1, 4])
