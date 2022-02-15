#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     :       2022/2/10 13:19
# @Author   :       YH
# @FILE     :       32_LongestValidParentheses.py
# @Software :       PyCharm

class Solution:
    def __init__(self):
        pass
    
    def longestValidParentheses(self, s):
        """
        思路：边判断括号有效性，边统计最大长度

        利用栈来判断括号合理性
        遇到每个左括号，下标放入栈中，用于后续的匹配右括号
        遇到每个右括号，先弹出栈顶来匹配
            弹出后为空 -> 当前右括号没有被匹配，用其下标来更新栈底「最后一个没有被匹配的右括号的下标」，此时的栈顶就是栈底，因为是空栈
            弹出不为空 -> 当前右括号被匹配，当前下标-栈顶 为当前右括号为结尾的最大长度子串
        骚操作：保持栈底为「最后一个没有被匹配的右括号的下标」，用于边界处理，便于计算最大长度

        :param s: 
        :return: 
        """
        stack = [-1]
        res = 0
        
        for i, j in enumerate(s):
            if j == '(':
                stack.append(i)
            # 遇到 ), 就把最后一个 ( 下标出栈
            else:
                stack.pop()
                # 出栈后为空
                if not stack:
                    stack.append(i)
                else:
                    res = max(res, i-stack[-1])
        
        return res


if __name__ == '__main__':
    solution = Solution()
    s = ")()()())"
    print(solution.longestValidParentheses(s))
        