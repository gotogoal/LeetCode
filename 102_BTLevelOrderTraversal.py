#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     :       2022/9/6 11:23
# @Author   :       YH
# @FILE     :       102_BTLevelOrderTraversal.py
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
    def levelOrder(self, root):
        if not root:
            return []

        queue = [root]
        res = []

        while queue:
            var = []
            nxt = []
            for node in queue:
                var.append(node.val)
                if node.left:
                    nxt.append(node.left)
                if node.right:
                    nxt.append(node.right)
            res.append(var)
            queue = nxt
        
        return res
