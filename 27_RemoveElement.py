#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     :       2022/7/11 8:33
# @Author   :       YH
# @FILE     :       27_RemoveElement.py
# @Software :       PyCharm


class Solution(object):
    def __init__(self):
        pass

    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        slow = 0
        fast = 0
        while fast < len(nums):
            if nums[fast] != val:
                nums[slow] = nums[fast]
                slow += 1
            fast += 1
        return slow


if __name__ == '__main__':
    solution = Solution()
    print(solution.removeElement([0, 1, 2, 2, 3, 0, 4, 2], 2))