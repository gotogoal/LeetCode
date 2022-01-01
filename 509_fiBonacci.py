#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     :       2021/12/9 7:54
# @Author   :       YH
# @FILE     :       509_fibonacci.py
# @Software :       PyCharm

# F(0) = 0, F(1) = 1
# F(n) = F(n - 1) + F(n - 2), for n > 1.

class Solution:
    def __init__(self):
        pass
    
    def fib(self, n):
        if n < 0:
            return 0
        elif n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            a = 0
            b = 1
            for i in range(2, n+1):
                c = a + b
                a, b = b, c
            return c
        

if __name__ == '__main__':
    solution = Solution()
    print(solution.fib(10))