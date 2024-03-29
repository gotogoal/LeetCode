#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     :       2022/10/7 16:26
# @Author   :       YH
# @FILE     :       200_NumberOfIslands.py
# @Software :       PyCharm


'''

1.目标是找到矩阵中 “岛屿的数量” ，上下左右相连的 1 都被认为是连续岛屿
2.dfs方法： 设目前指针指向一个岛屿中的某一点 (i, j)，寻找包括此点的岛屿边界。
    从 (i, j) 向此点的上下左右 (i+1, j), (i-1,j), (i,j+1), (i,j-1) 做深度搜索
    终止条件：
        (i, j) 越过矩阵边界;
        grid[i][j] == 0，代表此分支已越过岛屿边界。
    搜索岛屿的同时，执行 grid[i][j] = '0'，即将岛屿所有节点删除，以免之后重复搜索相同岛屿。
3.主循环：
    遍历整个矩阵，当遇到 grid[i][j] == '1' 时，从此点开始做深度优先搜索 dfs，岛屿数 count + 1 且在深度优先搜索中删除此岛屿。
    最终返回岛屿数 count 即可。

'''
class Solution:
    def __init__(self):
        pass

    def numIslands(self, grid):
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    self.dfs(grid, i, j)
                    count += 1
        return count

    def dfs(self, grid, i, j):
        if not (0 <= i < len(grid)):
            return
        if not (0 <= j < len(grid[0])):
            return 
        if grid[i][j] == '0':
            return

        grid[i][j] = '0'
        self.dfs(grid, i + 1, j)
        self.dfs(grid, i - 1, j)
        self.dfs(grid, i, j + 1)
        self.dfs(grid, i, j - 1)