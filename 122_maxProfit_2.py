#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     :       2022/1/13 19:54
# @Author   :       YH
# @FILE     :       122_maxProfit_2.py
# @Software :       PyCharm


# 策略是所有上涨交易日都买卖（赚到所有利润），所有下降交易日都不买卖（永不亏钱）
class Solution(object):
    
    def __init__(self):
        pass
    
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        max_profit = 0
        for i in range(1, len(prices)):
            profit = prices[i] - prices[i-1]
            if profit > 0:
                max_profit += profit
        
        return max_profit


if __name__ == '__main__':
    solution = Solution()
    prices = [7, 1, 5, 3, 6, 4]
    print(solution.maxProfit(prices))