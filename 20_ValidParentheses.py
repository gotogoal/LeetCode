#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     :       2022/10/10 13:52
# @Author   :       YH
# @FILE     :       20_ValidParentheses.py
# @Software :       PyCharm


class Solution(object):
    def __init__(self):
        pass

    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        dict_match = {'(':')', '{':'}', '[':']'}
        for _ in s:
            if _ in dict_match:
                stack.append(_)
                continue
            else:
                if stack and dict_match.get(stack[-1], '') == _:
                    stack.pop()
                else:
                    return False

        if stack:
            return False
        else:
            return True


if __name__ == '__main__':
    solution = Solution()
    s = "()[]{}"
    print(solution.isValid(s))
        
            