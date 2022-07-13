#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     :       2022/7/8 7:57
# @Author   :       YH
# @FILE     :       26._RemoveDuplicates.py
# @Software :       PyCharm


class Solution():
    def __init__(self):
        pass
    
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 2:
            return len(nums)
        slow = 0
        n = len(nums)
        fast = 1
        while fast < n:
            if(nums[slow] != nums[fast]):
                nums[slow+1] = nums[fast]
                slow += 1
                fast += 1
            else:
                fast += 1
        return slow + 1
                


if __name__ == '__main__':
    solution = Solution()
    print(solution.removeDuplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]))
                