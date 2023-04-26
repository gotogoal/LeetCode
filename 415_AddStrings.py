#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     :       2023/4/5 15:37
# @Author   :       YH
# @FILE     :       415_AddStrings.py
# @Software :       PyCharm


class Solution(object):
    def __init__(self):
        pass

    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        n1 = len(num1)
        n2 = len(num2)
        p = n1 - 1
        q = n2 - 1
        res = ''
        flag = 0
        while p>=0 or q>=0 or flag:
            
            p_value = int(num1[p]) if p >= 0 else 0
            q_value = int(num2[q]) if q >= 0 else 0
            sum_value = p_value + q_value + flag
            if sum_value >= 10:
                flag = 1
                sum_value -= 10
            else:
                flag = 0
            res = str(sum_value) + res
            p -= 1
            q -= 1
        
        return res


if __name__ == '__main__':
    num1 = '456'
    num2 = '77'
    solution = Solution()
    print(solution.addStrings(num1, num2))