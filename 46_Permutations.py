#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     :       2022/11/14 20:08
# @Author   :       YH
# @FILE     :       46_Permutations.py
# @Software :       PyCharm


# 先考虑一位的情况，然后把递归地考虑去掉这一位数后的数组的全排列。
class Solution(object):
    
    def __init__(self):
        pass

    def permute(self, nums):
        res = []

        def dfs(tmp, nums):
            if not nums:
                res.append(tmp)
                return

            for i, x in enumerate(nums):
                dfs(tmp + [x], nums[:i] + nums[i+1:])

        dfs([], nums)

        return res


if __name__ == '__main__':
    solution = Solution()
    nums = [1, 2, 3]
    print(solution.permute(nums))