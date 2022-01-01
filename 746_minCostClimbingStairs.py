#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     :       2021/12/21 7:48
# @Author   :       YH
# @FILE     :       746_minCostClimbingStairs.py
# @Software :       PyCharm

class Solution(object):
    def __init__(self):
        pass
    
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        到达当前台阶时判断下从前一个台阶过来省事，还是从前一个的前一个过来省事，一直累加到最后一个台阶完，最小值就是最省体力的。
        用p1和p2表示前两个和前一个台阶所耗费的体力
        """
        p1,p2 = 0, 0
        for i in range(2, len(cost)+1):
            p1, p2 = p2, min(p2 + cost[i-1], p1 + cost[i-2])
        return p2