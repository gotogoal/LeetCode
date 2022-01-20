#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     :       2022/1/1 17:44
# @Author   :       YH
# @FILE     :       53_MaximumSubarray.py
# @Software :       PyCharm


class Solution:
    
    def __init__(self):
        pass
    
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 当前最大和
        sum_max = nums[0]
        # 记录目前连续数组和
        n = nums[0]
        for i in range(1, len(nums)):
            # 当前连续数组和还是正数，则不放弃，继续加当前数字 nums[i]
            if n > 0:
                n += nums[i]
            # 当前连续数组和已经 非正，则可以放弃了，重新开始计算连续数组
            else:
                n = nums[i]

            if sum_max < n:
                sum_max = n
        return sum_max


if __name__ == '__main__':
    solution = Solution()
    nums = [5, -3, 5]
    print(solution.maxSubArray(nums))