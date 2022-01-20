#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     :       2022/1/2 22:14
# @Author   :       YH
# @FILE     :       152_MaximumProductSubarray.py
# @Software :       PyCharm

# 这题是求数组中子区间的最大乘积
# 对于乘法，我们需要注意，负数乘以负数，会变成正数，所以解这题的时候我们需要维护两个变量，当前的最大值，以及最小值，最小值可能为负数，但没准下一步乘以一个负数，当前的最大值就变成最小值，而最小值则变成最大值了。
# maxDP[i + 1] = max(maxDP[i] * A[i + 1], A[i + 1],minDP[i] * A[i + 1])
# minDP[i + 1] = min(minDP[i] * A[i + 1], A[i + 1],maxDP[i] * A[i + 1])
# dp[i + 1] = max(dp[i], maxDP[i + 1])
class Solution(object):
    
    def __init__(self):
        pass
    
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        elif len(nums) == 1:
            return nums[0]
        else:
            dp = nums[0]
            max_dp = nums[0]
            min_dp = nums[0]
            for i in range(1, len(nums)):
                t = max_dp
                max_dp = max(max(max_dp*nums[i], nums[i]), min_dp*nums[i])
                min_dp = min(min(t*nums[i], nums[i]), min_dp*nums[i])
                dp = max(max_dp, dp)
            
            return dp


if __name__ == '__main__':
    solution = Solution()
    nums = [-2,0,-1]
    print(solution.maxProduct(nums))