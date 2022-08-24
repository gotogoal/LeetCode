#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     :       2022/7/14 8:23
# @Author   :       YH
# @FILE     :       11_ContainerWithMostWater.py
# @Software :       PyCharm


class Solution(object):
    def __init__(self):
        pass

    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        max_volume = 0
        i = 0
        j = len(height) - 1
        while i < j:
            if height[i] < height[j]:
                max_volume = max(max_volume, (j-i)*height[i])
                i += 1
            else:
                max_volume = max(max_volume, (j-i)*height[j])
                j -= 1
        return max_volume


if __name__ == '__main__':
    solution = Solution()
    height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    print(solution.maxArea(height))