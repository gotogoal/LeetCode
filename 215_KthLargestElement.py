#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     :       2022/8/21 15:11
# @Author   :       YH
# @FILE     :       215_KthLargestElement.py
# @Software :       PyCharm
from heapq import *


class Solution(object):
    def __init__(self):
        pass

    def findKthLargest_1(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        return sorted(nums, reverse=True)[k-1]

    def findKthLargest_2(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        
        heap = []
        # 将一个对象压入堆中
        heapify(heap)
        for num in nums:
            heappush(heap, num)
            if len(heap) > k:
                heappop(heap)
        return heap[0]

    def findKthLargest_3(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        low = 0
        high = len(nums) - 1
        target = k - 1
        while True:
            pos = self.partition(nums, low, high)
            if pos == target:
                return nums[pos]
            # 要往左找
            elif pos > target:
                high = pos - 1
            # 要往右找
            elif pos < target:
                low = pos + 1

    def partition(self, nums, i, j):
        # 倒序
        pivot = nums[i]
        while i < j:
            while i < j and nums[j] <= pivot:
                j -= 1
            nums[i] = nums[j]
            while i < j and nums[i] >= pivot:
                i += 1
            nums[j] = nums[i]
        nums[j] = pivot
        return j


if __name__ == '__main__':
    solution = Solution()
    nums = [3, 2, 1, 5, 6, 4]
    k = 2
    print(solution.findKthLargest_1(nums, k))
    print(solution.findKthLargest_2(nums, k))
    print(solution.findKthLargest_3(nums, k))