#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     :       2022/10/11 20:56
# @Author   :       YH
# @FILE     :       88_MergeSortedArray.py
# @Software :       PyCharm


class Solution(object):
    def __init__(self):
        pass

    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        while (m > 0 and n > 0):
            # 从后向前, 谁大谁放后面
            if nums1[m-1] >= nums2[n-1]:
                nums1[m+n-1] = nums1[m-1]
                m -= 1
            else:
                nums1[m+n-1] = nums2[n-1]
                n -= 1
        
        # 看谁先结束, n 先结束了, m就可以不用动了, m 结束了就把 n 剩下的转移给 nums1
        if n > 0:
            nums1[0:n] = nums2[0:n]
        
        return nums1


if __name__ == '__main__':
    solution = Solution()
    nums1 = [1, 2, 3, 0, 0, 0]
    m = 3
    nums2 = [2, 5, 6]
    n = 3
    print(solution.merge(nums1, m, nums2, n))