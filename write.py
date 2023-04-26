#!/usr/bin/env python
# -*- coding: utf-8 -*-

def func(nums, k):
    low = 0
    high = len(nums) - 1
    target = k - 1
    while True:
        pos = partitions(nums, low, high)
        if pos == target:
            return nums[pos]
        elif pos > target:
            high = pos - 1
        else:
            low = pos + 1
        
    return -1
    
def partitions(nums, i, j):
    value = nums[i]
    
    while i < j:
        while i < j and nums[j] <= value:
            j -= 1
        nums[i] = nums[j]
        
        while i < j and nums[i] >= value:
            i += 1
        nums[j] = nums[i]
    
    nums[j] = value
    return j
    
            
        
    
            

if __name__ == '__main__':
    print(func('0', '0'))