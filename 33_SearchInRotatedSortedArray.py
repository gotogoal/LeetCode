#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     :       2022/10/3 12:01
# @Author   :       YH
# @FILE     :       33_SearchInRotatedSortedArray.py
# @Software :       PyCharm


class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        n = len(nums)
        if n == 0:
            return -1
        
        start = 0
        end = n - 1
        while (start <=  end):
            mid = (start + end) // 2
            if nums[mid] == target:
                return mid
            # 说明旋转下标在 mid下标 后，因为从 start 到 mid 还是升序的
            elif nums[mid] >= nums[start]:
                if nums[start] <= target and target < nums[mid]:
                    end = mid - 1
                else:
                    start = mid + 1
            # 旋转点在 mid 之前
            else:
                if nums[mid] < target and target <= nums[end]:
                    start = mid + 1
                else:
                    end = mid - 1
        
        return -1


if __name__ == '__main__':
    solution = Solution()
    nums = [5, 1, 3]
    target = 5
    print(solution.search(nums, target))
                    
        
        