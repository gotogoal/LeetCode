#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     :       2022/1/20 19:43
# @Author   :       YH
# @FILE     :       64_MinimumPathSum.py
# @Software :       PyCharm


class Solution:
    def __init__(self):
        pass
    
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])
        dp = [ [0]*n for i in range(m) ]
        
        # 初始化边上的值
        dp[0][0] = grid[0][0]
        for i in range(1, m):
            dp[i][0] = grid[i][0] + dp[i-1][0]
        for j in range(1, n):
            dp[0][j] = grid[0][j] + dp[0][j-1]
        
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = min(dp[i-1][j] + grid[i][j], dp[i][j-1] + grid[i][j])

        return dp[-1][-1]
        

if __name__ == '__main__':
    solution = Solution()
    grid = [[1,3,1],[1,5,1],[4,2,1]]
    print(solution.minPathSum(grid))
                