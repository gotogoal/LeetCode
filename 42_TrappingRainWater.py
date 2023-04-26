#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     :       2023/4/24 20:47
# @Author   :       YH
# @FILE     :       42_TrappingRainWater.py
# @Software :       PyCharm


class Solution(object):

    def __init__(self):
        pass

    # 暴力解法，遍历
    # 这个解法很好理解，每个位置的储水量由它左边最大数和右边最大数-这两者的最小值决定，最小值减去自身高度
    def trap1(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        n = len(height)
        if 0 == n:
            return 0
        
        water = 0
        for index, value in enumerate(height):
            l_max = 0
            r_max = 0
            for i in range(index):
                l_max = max(l_max, height[i])
            
            for j in range(index+1, n):
                r_max = max(r_max, height[j])
            
            # 如果 min(l_max, r_max) - height[index] 值小于 0, 就不加了
            water = water + max((min(l_max, r_max) - height[index]), 0)
        
        return water

    # 在方法1中，每个点求其左边和右边的最大值的时候都要重新寻找一遍，这导致了重复的计算。
    # 方法2开了两个数组记录了每个点其左边和右边的最大值，减少了重复计算，降低了时间复杂度，但空间复杂度变为了O(n)。
    # 这个动态规划指的是在寻找最大值时候使用了动态规划，不是直接对储水量进行的动态规划。
    def trap2(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        # 边界条件，一定要判断，否则后面按照数组长度生成新数组的时候，如果为空，会产生溢出
        if not height: 
            return 0
        n = len(height)
        water = 0
        # 每个位置处，从左向右的最大值
        max_left = [0] * n
        # 每个位置处，从右向左的最大值
        max_right = [0] * n
        # 设置初始值
        max_left[0] = height[0]
        # 设置初始值
        max_right[n - 1] = height[n - 1]
        # 求从左向右的最大值
        for i in range(1, n):
            max_left[i] = max(max_left[i - 1], height[i])
        # 求从右向左的最大值
        for j in range(n - 2, -1, -1):
            max_right[j] = max(max_right[j + 1], height[j])
        # 每个位置处，都可以表中拿到左边最大值和右边最大值
        for i in range(n):
            if min(max_left[i], max_right[i]) > height[i]:
                water += min(max_left[i], max_right[i]) - height[i]
        return water


if __name__ == '__main__':
    height = [0,1,0,2,1,0,1,3,2,1,2,1]
    solution = Solution()
    print(solution.trap1(height))
            