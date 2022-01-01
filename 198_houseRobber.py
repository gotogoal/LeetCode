#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     :       2021/12/23 9:23
# @Author   :       YH
# @FILE     :       198_houseRobber.py
# @Software :       PyCharm


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
        elif len(nums) == 2:
            return max(nums[0], nums[1])
        else:
            a = nums[0]
            b = max(nums[0], nums[1])
            for i in range(2, len(nums)):
                a, b = b, max(a+nums[i], b)
            return b