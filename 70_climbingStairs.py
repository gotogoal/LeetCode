# -*- coding: utf-8 -*-
# @Time     :       2021/12/11 11:11
# @Author   :       YH
# @FILE     :       70_climbingStairs.py
# @Software :       PyCharm

# 设 f(n) 表示爬 n 阶楼梯需要的跳法。
# 倒推一下，假设当前位于第 n 阶，那么上一步可能在第 n-1 或者第 n-2 阶，分别需要爬 1 级台阶和 2 级台阶。
# 那么，f(n) = f(n-1) + f(n-2)，有这个式子我们就可以dfs暴力了
class Solution:
    def __init__(self):
        pass

    def climbStairs(self, n):
        if n <= 0:
            return 0
        if n == 1:
            return 1
        if n == 2:
            return 2
        else:
            a, b = 1, 2
            for i in range(3, n+1):
                c = a + b
                a, b = b, c
            return c
        
        
if __name__ == '__main__':
    solution = Solution()
    n = 10
    print(solution.climbStairs(n))