#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Solution:
    def __init__(self):
        pass
    
    def quick_sort(self, nums, low, high):
        if low < high:
            pos = self.partition(nums, low, high)
            self.quick_sort(nums, low, pos-1)
            self.quick_sort(nums, pos+1, high)
        return nums
        
    def partition(self, nums, i, j):
        value = nums[i]
        while(i<j):
            while i < j and nums[j] >= value:
                j -= 1
            nums[i] = nums[j]
            while i < j and nums[i] <= value:
                i += 1
            nums[j] = nums[i]
        nums[j] = value
        return j
        
            


if __name__ == '__main__':
    solution = Solution()
    print(solution.longest('abcdecmncdighlmnopm'))