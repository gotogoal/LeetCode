#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     :       2022/7/13 7:53
# @Author   :       YH
# @FILE     :       28_ImplementStr.py
# @Software :       PyCharm


class Solution:
    def __init__(self):
        pass

    def strStr(self, haystack, needle):
        if not needle:
            return 0
        l1 = len(haystack)
        l2 = len(needle)
        for i in range(l1-l2+1):
            if needle==haystack[i:i+l2]:
                return i
        return -1


if __name__ == '__main__':
    solution = Solution()
    haystack = 'hello'
    needle = 'll'
    print(solution.strStr(haystack, needle))