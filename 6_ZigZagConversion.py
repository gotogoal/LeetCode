#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     :       2022/7/6 23:53
# @Author   :       YH
# @FILE     :       6_ZigZagConversion.py
# @Software :       PyCharm


class Solution():
    def __init__(self):
        pass
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows < 2:
            return s
        res = ["" for _ in range(numRows)]
        i, flag = 0, -1
        for c in s:
            res[i] += c
            if i == 0 or i == numRows - 1:
                flag = -flag
            i += flag
        return "".join(res)