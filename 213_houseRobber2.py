#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     :       2021/12/27 8:03
# @Author   :       YH
# @FILE     :       213_houseRobber2.py
# @Software :       PyCharm


# nums第一个和最后一个不能同时被偷，所以执行俩次：nums[0:-1], nums[1:]
class Solution(object):
    def __init__(self):
        pass
    
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        elif len(nums) == 1:
            return nums[0]
        return max(self.basic(nums[0:-1]), self.basic(nums[1:]))

    
    def basic(self, nums):
        if len(nums) == 0:
            return 0
        elif len(nums) == 1:
            return nums[0]
        elif len(nums) == 2:
            return max(nums[0], nums[1])
        else:
            a = nums[0]
            b = max(nums[0], nums[1])
            for i in range(2, len(nums)):
                a, b = b, max(a+nums[i], b)
            return b