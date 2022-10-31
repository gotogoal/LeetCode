#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     :       2022/10/31 14:57
# @Author   :       YH
# @FILE     :       103. ZigzagLevelOrder.py
# @Software :       PyCharm


class TreeNode():
    # 节点类
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution():
    # 树类
    def __init__(self):
        self.root = TreeNode()

    # 层次遍历核心代码
    def zigzagLevelOrder(self, root):
        if not root:
            return []

        queue = [root]
        res = []
        flag = 1

        while queue:
            var = []
            nxt = []
            for node in queue:
                var.append(node.val)
                if node.left:
                    nxt.append(node.left)
                if node.right:
                    nxt.append(node.right)
            if flag == 1:
                res.append(var)
                flag = 0
            else:
                res.append(var[::-1])
                flag = 1
            queue = nxt

        return res
