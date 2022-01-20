#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     :       2022/1/13 7:50
# @Author   :       YH
# @FILE     :       121_maxProfit.py
# @Software :       PyCharm

# 首先要保存历史最低价格 和 最大利润
# 当前股票价格 - 历史最低价 = 利润 > 历史最大利润时，更新 最大利润
# 更新历史最低价格
class Solution():
    
    def __init__(self):
        pass

    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        max_profit = 0
        min_price = prices[0]
        
        for i in range(1, len(prices)):
            stock_price = prices[i]
            profit = stock_price - min_price
            if profit > 0 and profit > max_profit:
                max_profit = profit
            if stock_price < min_price:
                min_price = stock_price
        return max_profit
    

if __name__ == '__main__':
    solution = Solution()
    prices = [7, 6, 4, 3, 1]
    print(solution.maxProfit(prices))