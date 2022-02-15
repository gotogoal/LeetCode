#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     :       2022/2/5 11:57
# @Author   :       YH
# @FILE     :       22_GenerateParentheses.py
# @Software :       PyCharm


class Solution:
    def __init__(self):
        pass

    def generateParenthesis(self, n):
        if n <= 0:
            return []
        res = []

        def dfs(paths, left, right):
            if left > n or right > left:
                return
            if len(paths) == n * 2:  # 因为括号都是成对出现的
                res.append(paths)
                return

            dfs(paths + '(', left + 1, right)  # 生成一个就加一个
            dfs(paths + ')', left, right + 1)

        dfs('', 0, 0)
        return res


    def generateParenthesisStepOne(self, n):
        """
        第一步:先递归所有的括号序列
        :param n: 
        :return: 
        """
        if n == 0:
            return []

        res = []
        def dfs(path):
            # 序列长度为 2n 时可以输出
            if len(path) == n * 2:
                res.append(path)
                return
            # 否则就加上左括号和右括号
            dfs(path + '(')
            dfs(path + ')')

        dfs('')
        return res

    def generateParenthesisStepTwo(self, n):
        """
        改善第一步:有效序列需要增加限制
        我们发现有一些结果是我们不需要的，比如((((，比如))))
        观察不需要的括号特点，((((实际上已经超过n了，我们生成同一方向的括号只需要n个即可，在生成的时候我们要限制住左括号与右括号生成的数量
        这时我增加了left与right参数，分别代表左括号与右括号的数量，每生成一个我就增加一个。
        那结束DFS的条件首先就需要把不符合的给过滤掉，
        :param n: 
        :return: 
        """
        if n == 0:
            return []
        res = []
        def dfs(path, left, right):
            if left > n or right > n or right > left:
                return
            if len(path) == n * 2:
                res.append(path)
                return
            dfs(path + '(', left+1, right)
            dfs(path + ')', left, right+1)

        dfs('', 0, 0)
        return res
    
    
if __name__ == '__main__':
    solution = Solution()
    print(solution.generateParenthesis(2))
    print(solution.generateParenthesisStepOne(2))
    print(solution.generateParenthesisStepTwo(2))